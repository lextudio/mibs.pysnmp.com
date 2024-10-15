# SNMP MIB module (PANDATEL-BMZ-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANDATEL-BMZ-MODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:41 2024
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

_Bmz_ObjectIdentity = ObjectIdentity
bmz = _Bmz_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 302)
)
_BmzModemTable_Object = MibTable
bmzModemTable = _BmzModemTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 302, 1)
)
if mibBuilder.loadTexts:
    bmzModemTable.setStatus("mandatory")
_BmzTableEntry_Object = MibTableRow
bmzTableEntry = _BmzTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 302, 1, 1)
)
bmzTableEntry.setIndexNames(
    (0, "PANDATEL-BMZ-MODEM-MIB", "mdmRack"),
    (0, "PANDATEL-BMZ-MODEM-MIB", "mdmModem"),
    (0, "PANDATEL-BMZ-MODEM-MIB", "mdmPosition"),
)
if mibBuilder.loadTexts:
    bmzTableEntry.setStatus("mandatory")
_MdmRack_Type = Integer32
_MdmRack_Object = MibTableColumn
mdmRack = _MdmRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 302, 1, 1, 1),
    _MdmRack_Type()
)
mdmRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRack.setStatus("mandatory")
_MdmModem_Type = Integer32
_MdmModem_Object = MibTableColumn
mdmModem = _MdmModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 302, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 302, 1, 1, 3),
    _MdmPosition_Type()
)
mdmPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPosition.setStatus("mandatory")
_MdmModemName_Type = DisplayString
_MdmModemName_Object = MibTableColumn
mdmModemName = _MdmModemName_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 302, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 302, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 302, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 302, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 302, 1, 1, 23),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 302, 1, 1, 24),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 302, 1, 1, 25),
    _MdmDataRate_Type()
)
mdmDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDataRate.setStatus("mandatory")


class _MdmRemoteAccessMode_Type(Integer32):
    """Custom type mdmRemoteAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("other", 1),
          ("via-hdsl-channel", 7))
    )


_MdmRemoteAccessMode_Type.__name__ = "Integer32"
_MdmRemoteAccessMode_Object = MibTableColumn
mdmRemoteAccessMode = _MdmRemoteAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 302, 1, 1, 64),
    _MdmRemoteAccessMode_Type()
)
mdmRemoteAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRemoteAccessMode.setStatus("mandatory")
_Bmz_modem_ObjectIdentity = ObjectIdentity
bmz_modem = _Bmz_modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 302)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANDATEL-BMZ-MODEM-MIB",
    **{"bmz": bmz,
       "bmzModemTable": bmzModemTable,
       "bmzTableEntry": bmzTableEntry,
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
       "mdmRemoteAccessMode": mdmRemoteAccessMode,
       "bmz-modem": bmz_modem}
)
