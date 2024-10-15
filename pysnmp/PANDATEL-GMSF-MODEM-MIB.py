# SNMP MIB module (PANDATEL-GMSF-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANDATEL-GMSF-MODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:53 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(device_id,
 mdmSpecifics) = mibBuilder.importSymbols(
    "PANDATEL-MODEM-MIB",
    "device-id",
    "mdmSpecifics")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gmsf_ObjectIdentity = ObjectIdentity
gmsf = _Gmsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205)
)
_GmsfModemTable_Object = MibTable
gmsfModemTable = _GmsfModemTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1)
)
if mibBuilder.loadTexts:
    gmsfModemTable.setStatus("mandatory")
_GmsfTableEntry_Object = MibTableRow
gmsfTableEntry = _GmsfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1)
)
gmsfTableEntry.setIndexNames(
    (0, "PANDATEL-GMSF-MODEM-MIB", "mdmRack"),
    (0, "PANDATEL-GMSF-MODEM-MIB", "mdmModem"),
    (0, "PANDATEL-GMSF-MODEM-MIB", "mdmPosition"),
)
if mibBuilder.loadTexts:
    gmsfTableEntry.setStatus("mandatory")
_MdmRack_Type = Integer32
_MdmRack_Object = MibTableColumn
mdmRack = _MdmRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 1),
    _MdmRack_Type()
)
mdmRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRack.setStatus("mandatory")
_MdmModem_Type = Integer32
_MdmModem_Object = MibTableColumn
mdmModem = _MdmModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 2),
    _MdmModem_Type()
)
mdmModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmModem.setStatus("mandatory")


class _MdmPosition_Type(Integer32):
    """Custom type mdmPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_MdmPosition_Type.__name__ = "Integer32"
_MdmPosition_Object = MibTableColumn
mdmPosition = _MdmPosition_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 3),
    _MdmPosition_Type()
)
mdmPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPosition.setStatus("mandatory")
_MdmModemName_Type = DisplayString
_MdmModemName_Object = MibTableColumn
mdmModemName = _MdmModemName_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 5),
    _MdmModemName_Type()
)
mdmModemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmModemName.setStatus("mandatory")


class _MdmInterfaceEmulationMode_Type(Integer32):
    """Custom type mdmInterfaceEmulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dce", 3),
          ("dte", 2),
          ("nt", 5),
          ("other", 1),
          ("te", 4),
          ("unknown", 99))
    )


_MdmInterfaceEmulationMode_Type.__name__ = "Integer32"
_MdmInterfaceEmulationMode_Object = MibTableColumn
mdmInterfaceEmulationMode = _MdmInterfaceEmulationMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 6),
    _MdmInterfaceEmulationMode_Type()
)
mdmInterfaceEmulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmInterfaceEmulationMode.setStatus("mandatory")


class _MdmModemProperty_Type(Integer32):
    """Custom type mdmModemProperty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("other", 1),
          ("t1", 3),
          ("unknown", 99))
    )


_MdmModemProperty_Type.__name__ = "Integer32"
_MdmModemProperty_Object = MibTableColumn
mdmModemProperty = _MdmModemProperty_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 7),
    _MdmModemProperty_Type()
)
mdmModemProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmModemProperty.setStatus("mandatory")


class _MdmHDSLUnit_Type(Integer32):
    """Custom type mdmHDSLUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ltu", 3),
          ("ntu", 2),
          ("other", 1))
    )


_MdmHDSLUnit_Type.__name__ = "Integer32"
_MdmHDSLUnit_Object = MibTableColumn
mdmHDSLUnit = _MdmHDSLUnit_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 10),
    _MdmHDSLUnit_Type()
)
mdmHDSLUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmHDSLUnit.setStatus("mandatory")


class _MdmClockSystem_Type(Integer32):
    """Custom type mdmClockSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dual", 2),
          ("other", 1),
          ("single", 3))
    )


_MdmClockSystem_Type.__name__ = "Integer32"
_MdmClockSystem_Object = MibTableColumn
mdmClockSystem = _MdmClockSystem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 23),
    _MdmClockSystem_Type()
)
mdmClockSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmClockSystem.setStatus("mandatory")


class _MdmClockSource_Type(Integer32):
    """Custom type mdmClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("external", 4),
          ("internal", 2),
          ("other", 1),
          ("remote", 3))
    )


_MdmClockSource_Type.__name__ = "Integer32"
_MdmClockSource_Object = MibTableColumn
mdmClockSource = _MdmClockSource_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 24),
    _MdmClockSource_Type()
)
mdmClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmClockSource.setStatus("mandatory")


class _MdmDataRate_Type(Integer32):
    """Custom type mdmDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("other", 1)
    )


_MdmDataRate_Type.__name__ = "Integer32"
_MdmDataRate_Object = MibTableColumn
mdmDataRate = _MdmDataRate_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 25),
    _MdmDataRate_Type()
)
mdmDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDataRate.setStatus("mandatory")


class _MdmStartTimeslot_Type(Integer32):
    """Custom type mdmStartTimeslot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("other", 99),
          ("timeslot-1", 1),
          ("timeslot-10", 10),
          ("timeslot-11", 11),
          ("timeslot-12", 12),
          ("timeslot-13", 13),
          ("timeslot-14", 14),
          ("timeslot-15", 15),
          ("timeslot-16", 16),
          ("timeslot-17", 17),
          ("timeslot-18", 18),
          ("timeslot-19", 19),
          ("timeslot-2", 2),
          ("timeslot-20", 20),
          ("timeslot-21", 21),
          ("timeslot-22", 22),
          ("timeslot-23", 23),
          ("timeslot-24", 24),
          ("timeslot-25", 25),
          ("timeslot-26", 26),
          ("timeslot-27", 27),
          ("timeslot-28", 28),
          ("timeslot-29", 29),
          ("timeslot-3", 3),
          ("timeslot-30", 30),
          ("timeslot-31", 31),
          ("timeslot-4", 4),
          ("timeslot-5", 5),
          ("timeslot-6", 6),
          ("timeslot-7", 7),
          ("timeslot-8", 8),
          ("timeslot-9", 9),
          ("unframed", 98))
    )


_MdmStartTimeslot_Type.__name__ = "Integer32"
_MdmStartTimeslot_Object = MibTableColumn
mdmStartTimeslot = _MdmStartTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 26),
    _MdmStartTimeslot_Type()
)
mdmStartTimeslot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmStartTimeslot.setStatus("mandatory")


class _MdmTimeslotSize_Type(Integer32):
    """Custom type mdmTimeslotSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("nx56k", 3),
          ("nx64k", 2),
          ("other", 1))
    )


_MdmTimeslotSize_Type.__name__ = "Integer32"
_MdmTimeslotSize_Object = MibTableColumn
mdmTimeslotSize = _MdmTimeslotSize_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 27),
    _MdmTimeslotSize_Type()
)
mdmTimeslotSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTimeslotSize.setStatus("mandatory")


class _MdmTimeslot16_Type(Integer32):
    """Custom type mdmTimeslot16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("not-available", 100),
          ("other", 1))
    )


_MdmTimeslot16_Type.__name__ = "Integer32"
_MdmTimeslot16_Object = MibTableColumn
mdmTimeslot16 = _MdmTimeslot16_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 40),
    _MdmTimeslot16_Type()
)
mdmTimeslot16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTimeslot16.setStatus("mandatory")


class _MdmCRC4Generation_Type(Integer32):
    """Custom type mdmCRC4Generation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("not-available", 100),
          ("other", 1))
    )


_MdmCRC4Generation_Type.__name__ = "Integer32"
_MdmCRC4Generation_Object = MibTableColumn
mdmCRC4Generation = _MdmCRC4Generation_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 41),
    _MdmCRC4Generation_Type()
)
mdmCRC4Generation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCRC4Generation.setStatus("mandatory")


class _MdmFramingMode_Type(Integer32):
    """Custom type mdmFramingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("d4", 2),
          ("esf", 3),
          ("not-available", 100),
          ("other", 1))
    )


_MdmFramingMode_Type.__name__ = "Integer32"
_MdmFramingMode_Object = MibTableColumn
mdmFramingMode = _MdmFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 50),
    _MdmFramingMode_Type()
)
mdmFramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmFramingMode.setStatus("mandatory")


class _MdmScrambler_Type(Integer32):
    """Custom type mdmScrambler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_MdmScrambler_Type.__name__ = "Integer32"
_MdmScrambler_Object = MibTableColumn
mdmScrambler = _MdmScrambler_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 63),
    _MdmScrambler_Type()
)
mdmScrambler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScrambler.setStatus("mandatory")


class _MdmRemoteAccessMode_Type(Integer32):
    """Custom type mdmRemoteAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("other", 1),
          ("via-hdsl-channel", 7),
          ("via-next-free-timeslot", 3),
          ("via-timeslot-0-Sa4-bit", 4))
    )


_MdmRemoteAccessMode_Type.__name__ = "Integer32"
_MdmRemoteAccessMode_Object = MibTableColumn
mdmRemoteAccessMode = _MdmRemoteAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 64),
    _MdmRemoteAccessMode_Type()
)
mdmRemoteAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmRemoteAccessMode.setStatus("mandatory")


class _MdmCRC6Test_Type(Integer32):
    """Custom type mdmCRC6Test based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("other", 1),
          ("start", 3),
          ("stop", 4))
    )


_MdmCRC6Test_Type.__name__ = "Integer32"
_MdmCRC6Test_Object = MibTableColumn
mdmCRC6Test = _MdmCRC6Test_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 100),
    _MdmCRC6Test_Type()
)
mdmCRC6Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCRC6Test.setStatus("mandatory")


class _MdmCRC6Status_Type(Integer32):
    """Custom type mdmCRC6Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              7,
              100)
        )
    )
    namedValues = NamedValues(
        *(("never-started", 2),
          ("not-available", 100),
          ("other", 1),
          ("running", 5),
          ("start-failed", 7),
          ("stopped", 6))
    )


_MdmCRC6Status_Type.__name__ = "Integer32"
_MdmCRC6Status_Object = MibTableColumn
mdmCRC6Status = _MdmCRC6Status_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 101),
    _MdmCRC6Status_Type()
)
mdmCRC6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCRC6Status.setStatus("mandatory")
_MdmCRC6Error_Type = Gauge32
_MdmCRC6Error_Object = MibTableColumn
mdmCRC6Error = _MdmCRC6Error_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 102),
    _MdmCRC6Error_Type()
)
mdmCRC6Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCRC6Error.setStatus("mandatory")
_Gmsf_modem_ObjectIdentity = ObjectIdentity
gmsf_modem = _Gmsf_modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 205)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANDATEL-GMSF-MODEM-MIB",
    **{"gmsf": gmsf,
       "gmsfModemTable": gmsfModemTable,
       "gmsfTableEntry": gmsfTableEntry,
       "mdmRack": mdmRack,
       "mdmModem": mdmModem,
       "mdmPosition": mdmPosition,
       "mdmModemName": mdmModemName,
       "mdmInterfaceEmulationMode": mdmInterfaceEmulationMode,
       "mdmModemProperty": mdmModemProperty,
       "mdmHDSLUnit": mdmHDSLUnit,
       "mdmClockSystem": mdmClockSystem,
       "mdmClockSource": mdmClockSource,
       "mdmDataRate": mdmDataRate,
       "mdmStartTimeslot": mdmStartTimeslot,
       "mdmTimeslotSize": mdmTimeslotSize,
       "mdmTimeslot16": mdmTimeslot16,
       "mdmCRC4Generation": mdmCRC4Generation,
       "mdmFramingMode": mdmFramingMode,
       "mdmScrambler": mdmScrambler,
       "mdmRemoteAccessMode": mdmRemoteAccessMode,
       "mdmCRC6Test": mdmCRC6Test,
       "mdmCRC6Status": mdmCRC6Status,
       "mdmCRC6Error": mdmCRC6Error,
       "gmsf-modem": gmsf_modem}
)
