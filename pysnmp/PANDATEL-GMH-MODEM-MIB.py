# SNMP MIB module (PANDATEL-GMH-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANDATEL-GMH-MODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:51 2024
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

_Gmh_ObjectIdentity = ObjectIdentity
gmh = _Gmh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 201)
)
_GmhModemTable_Object = MibTable
gmhModemTable = _GmhModemTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 201, 1)
)
if mibBuilder.loadTexts:
    gmhModemTable.setStatus("mandatory")
_GmhTableEntry_Object = MibTableRow
gmhTableEntry = _GmhTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 201, 1, 1)
)
gmhTableEntry.setIndexNames(
    (0, "PANDATEL-GMH-MODEM-MIB", "mdmRack"),
    (0, "PANDATEL-GMH-MODEM-MIB", "mdmModem"),
    (0, "PANDATEL-GMH-MODEM-MIB", "mdmPosition"),
)
if mibBuilder.loadTexts:
    gmhTableEntry.setStatus("mandatory")
_MdmRack_Type = Integer32
_MdmRack_Object = MibTableColumn
mdmRack = _MdmRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 201, 1, 1, 1),
    _MdmRack_Type()
)
mdmRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRack.setStatus("mandatory")
_MdmModem_Type = Integer32
_MdmModem_Object = MibTableColumn
mdmModem = _MdmModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 201, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 201, 1, 1, 3),
    _MdmPosition_Type()
)
mdmPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPosition.setStatus("mandatory")
_MdmModemName_Type = DisplayString
_MdmModemName_Object = MibTableColumn
mdmModemName = _MdmModemName_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 201, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 201, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 201, 1, 1, 7),
    _MdmModemProperty_Type()
)
mdmModemProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmModemProperty.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 201, 1, 1, 23),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 201, 1, 1, 24),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 201, 1, 1, 25),
    _MdmDataRate_Type()
)
mdmDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDataRate.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 201, 1, 1, 63),
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
              5)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 5),
          ("other", 1))
    )


_MdmRemoteAccessMode_Type.__name__ = "Integer32"
_MdmRemoteAccessMode_Object = MibTableColumn
mdmRemoteAccessMode = _MdmRemoteAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 201, 1, 1, 64),
    _MdmRemoteAccessMode_Type()
)
mdmRemoteAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmRemoteAccessMode.setStatus("mandatory")


class _MdmForcedRemoteAccess_Type(Integer32):
    """Custom type mdmForcedRemoteAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_MdmForcedRemoteAccess_Type.__name__ = "Integer32"
_MdmForcedRemoteAccess_Object = MibTableColumn
mdmForcedRemoteAccess = _MdmForcedRemoteAccess_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 201, 1, 1, 65),
    _MdmForcedRemoteAccess_Type()
)
mdmForcedRemoteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmForcedRemoteAccess.setStatus("mandatory")
_Gmh_modem_ObjectIdentity = ObjectIdentity
gmh_modem = _Gmh_modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 201)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANDATEL-GMH-MODEM-MIB",
    **{"gmh": gmh,
       "gmhModemTable": gmhModemTable,
       "gmhTableEntry": gmhTableEntry,
       "mdmRack": mdmRack,
       "mdmModem": mdmModem,
       "mdmPosition": mdmPosition,
       "mdmModemName": mdmModemName,
       "mdmDataEquipmentEmulation": mdmDataEquipmentEmulation,
       "mdmModemProperty": mdmModemProperty,
       "mdmClockSystem": mdmClockSystem,
       "mdmClockSource": mdmClockSource,
       "mdmDataRate": mdmDataRate,
       "mdmScrambler": mdmScrambler,
       "mdmRemoteAccessMode": mdmRemoteAccessMode,
       "mdmForcedRemoteAccess": mdmForcedRemoteAccess,
       "gmh-modem": gmh_modem}
)
