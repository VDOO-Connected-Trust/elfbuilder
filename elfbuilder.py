from makeelf.elf import ELF, EM, ELFDATA
import easyargs
import pickle


def output_elf(sections, fname):
    # TODO: architecture support
    elf = ELF(e_machine=EM.EM_ARM, e_data=ELFDATA.ELFDATA2LSB)
    for section_name, section_data, section_offset, section_permissions in sections:
        sec_index = elf._append_section(
            section_name, section_data, section_offset, section_permissions
        )
        elf.append_segment(sec_index)

    with open(fname, "wb") as elf_file:
        elf_file.write(bytes(elf))


@easyargs
def main(elf_data_pickle, output_elf_file):
    with open(elf_data_pickle, 'rb') as data_pickle:
        sections = pickle.load(data_pickle)
        output_elf(sections, output_elf_file)


if __name__ == "__main__":
    main()
