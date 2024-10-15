# SNMP MIB module (PANDATEL-GMD-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANDATEL-GMD-MODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:49 2024
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

_Gmd_ObjectIdentity = ObjectIdentity
gmd = _Gmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203)
)
_GmdModemTable_Object = MibTable
gmdModemTable = _GmdModemTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1)
)
if mibBuilder.loadTexts:
    gmdModemTable.setStatus("mandatory")
_GmdTableEntry_Object = MibTableRow
gmdTableEntry = _GmdTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1)
)
gmdTableEntry.setIndexNames(
    (0, "PANDATEL-GMD-MODEM-MIB", "mdmRack"),
    (0, "PANDATEL-GMD-MODEM-MIB", "mdmModem"),
    (0, "PANDATEL-GMD-MODEM-MIB", "mdmPosition"),
)
if mibBuilder.loadTexts:
    gmdTableEntry.setStatus("mandatory")
_MdmRack_Type = Integer32
_MdmRack_Object = MibTableColumn
mdmRack = _MdmRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 1),
    _MdmRack_Type()
)
mdmRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRack.setStatus("mandatory")
_MdmModem_Type = Integer32
_MdmModem_Object = MibTableColumn
mdmModem = _MdmModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 3),
    _MdmPosition_Type()
)
mdmPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPosition.setStatus("mandatory")
_MdmModemName_Type = DisplayString
_MdmModemName_Object = MibTableColumn
mdmModemName = _MdmModemName_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 5),
    _MdmModemName_Type()
)
mdmModemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmModemName.setStatus("mandatory")


class _MdmDataEquipmentEmulation_Type(Integer32):
    """Custom type mdmDataEquipmentEmulation based on Integer32"""
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
        *(("dce", 3),
          ("dte", 2),
          ("other", 1),
          ("unknown", 99))
    )


_MdmDataEquipmentEmulation_Type.__name__ = "Integer32"
_MdmDataEquipmentEmulation_Object = MibTableColumn
mdmDataEquipmentEmulation = _MdmDataEquipmentEmulation_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 6),
    _MdmDataEquipmentEmulation_Type()
)
mdmDataEquipmentEmulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDataEquipmentEmulation.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 10),
    _MdmHDSLUnit_Type()
)
mdmHDSLUnit.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 23),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 24),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 25),
    _MdmDataRate_Type()
)
mdmDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDataRate.setStatus("mandatory")


class _MdmStartChannel_Type(Integer32):
    """Custom type mdmStartChannel based on Integer32"""
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
        *(("channel-1", 1),
          ("channel-10", 10),
          ("channel-11", 11),
          ("channel-12", 12),
          ("channel-13", 13),
          ("channel-14", 14),
          ("channel-15", 15),
          ("channel-16", 16),
          ("channel-17", 17),
          ("channel-18", 18),
          ("channel-19", 19),
          ("channel-2", 2),
          ("channel-20", 20),
          ("channel-21", 21),
          ("channel-22", 22),
          ("channel-23", 23),
          ("channel-24", 24),
          ("channel-25", 25),
          ("channel-26", 26),
          ("channel-27", 27),
          ("channel-28", 28),
          ("channel-29", 29),
          ("channel-3", 3),
          ("channel-30", 30),
          ("channel-31", 31),
          ("channel-4", 4),
          ("channel-5", 5),
          ("channel-6", 6),
          ("channel-7", 7),
          ("channel-8", 8),
          ("channel-9", 9),
          ("not-available", 100),
          ("other", 99),
          ("unframed", 98))
    )


_MdmStartChannel_Type.__name__ = "Integer32"
_MdmStartChannel_Object = MibTableColumn
mdmStartChannel = _MdmStartChannel_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 26),
    _MdmStartChannel_Type()
)
mdmStartChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmStartChannel.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 40),
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_MdmCRC4Generation_Type.__name__ = "Integer32"
_MdmCRC4Generation_Object = MibTableColumn
mdmCRC4Generation = _MdmCRC4Generation_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 41),
    _MdmCRC4Generation_Type()
)
mdmCRC4Generation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCRC4Generation.setStatus("mandatory")


class _MdmHDSLFramer_Type(Integer32):
    """Custom type mdmHDSLFramer based on Integer32"""
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


_MdmHDSLFramer_Type.__name__ = "Integer32"
_MdmHDSLFramer_Object = MibTableColumn
mdmHDSLFramer = _MdmHDSLFramer_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 62),
    _MdmHDSLFramer_Type()
)
mdmHDSLFramer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmHDSLFramer.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 100),
    _MdmCRC6Test_Type()
)
mdmCRC6Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCRC6Test.setStatus("mandatory")


class _MdmPair1CRC6Status_Type(Integer32):
    """Custom type mdmPair1CRC6Status based on Integer32"""
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


_MdmPair1CRC6Status_Type.__name__ = "Integer32"
_MdmPair1CRC6Status_Object = MibTableColumn
mdmPair1CRC6Status = _MdmPair1CRC6Status_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 101),
    _MdmPair1CRC6Status_Type()
)
mdmPair1CRC6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPair1CRC6Status.setStatus("mandatory")
_MdmPair1CRC6Error_Type = Gauge32
_MdmPair1CRC6Error_Object = MibTableColumn
mdmPair1CRC6Error = _MdmPair1CRC6Error_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 102),
    _MdmPair1CRC6Error_Type()
)
mdmPair1CRC6Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPair1CRC6Error.setStatus("mandatory")


class _MdmPair2CRC6Status_Type(Integer32):
    """Custom type mdmPair2CRC6Status based on Integer32"""
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


_MdmPair2CRC6Status_Type.__name__ = "Integer32"
_MdmPair2CRC6Status_Object = MibTableColumn
mdmPair2CRC6Status = _MdmPair2CRC6Status_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 103),
    _MdmPair2CRC6Status_Type()
)
mdmPair2CRC6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPair2CRC6Status.setStatus("mandatory")
_MdmPair2CRC6Error_Type = Gauge32
_MdmPair2CRC6Error_Object = MibTableColumn
mdmPair2CRC6Error = _MdmPair2CRC6Error_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 104),
    _MdmPair2CRC6Error_Type()
)
mdmPair2CRC6Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPair2CRC6Error.setStatus("mandatory")


class _MdmPair3CRC6Status_Type(Integer32):
    """Custom type mdmPair3CRC6Status based on Integer32"""
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


_MdmPair3CRC6Status_Type.__name__ = "Integer32"
_MdmPair3CRC6Status_Object = MibTableColumn
mdmPair3CRC6Status = _MdmPair3CRC6Status_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 105),
    _MdmPair3CRC6Status_Type()
)
mdmPair3CRC6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPair3CRC6Status.setStatus("mandatory")
_MdmPair3CRC6Error_Type = Gauge32
_MdmPair3CRC6Error_Object = MibTableColumn
mdmPair3CRC6Error = _MdmPair3CRC6Error_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 203, 1, 1, 106),
    _MdmPair3CRC6Error_Type()
)
mdmPair3CRC6Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPair3CRC6Error.setStatus("mandatory")
_Gmd_modem_ObjectIdentity = ObjectIdentity
gmd_modem = _Gmd_modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 203)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANDATEL-GMD-MODEM-MIB",
    **{"gmd": gmd,
       "gmdModemTable": gmdModemTable,
       "gmdTableEntry": gmdTableEntry,
       "mdmRack": mdmRack,
       "mdmModem": mdmModem,
       "mdmPosition": mdmPosition,
       "mdmModemName": mdmModemName,
       "mdmDataEquipmentEmulation": mdmDataEquipmentEmulation,
       "mdmModemProperty": mdmModemProperty,
       "mdmHDSLUnit": mdmHDSLUnit,
       "mdmClockSystem": mdmClockSystem,
       "mdmClockSource": mdmClockSource,
       "mdmDataRate": mdmDataRate,
       "mdmStartChannel": mdmStartChannel,
       "mdmTimeslot16": mdmTimeslot16,
       "mdmCRC4Generation": mdmCRC4Generation,
       "mdmHDSLFramer": mdmHDSLFramer,
       "mdmCRC6Test": mdmCRC6Test,
       "mdmPair1CRC6Status": mdmPair1CRC6Status,
       "mdmPair1CRC6Error": mdmPair1CRC6Error,
       "mdmPair2CRC6Status": mdmPair2CRC6Status,
       "mdmPair2CRC6Error": mdmPair2CRC6Error,
       "mdmPair3CRC6Status": mdmPair3CRC6Status,
       "mdmPair3CRC6Error": mdmPair3CRC6Error,
       "gmd-modem": gmd_modem}
)
