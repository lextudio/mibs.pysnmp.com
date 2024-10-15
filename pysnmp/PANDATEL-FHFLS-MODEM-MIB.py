# SNMP MIB module (PANDATEL-FHFLS-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANDATEL-FHFLS-MODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:45 2024
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

_Fhfls_ObjectIdentity = ObjectIdentity
fhfls = _Fhfls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103)
)
_FhflsModemTable_Object = MibTable
fhflsModemTable = _FhflsModemTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103, 1)
)
if mibBuilder.loadTexts:
    fhflsModemTable.setStatus("mandatory")
_FhflsTableEntry_Object = MibTableRow
fhflsTableEntry = _FhflsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103, 1, 1)
)
fhflsTableEntry.setIndexNames(
    (0, "PANDATEL-FHFLS-MODEM-MIB", "mdmRack"),
    (0, "PANDATEL-FHFLS-MODEM-MIB", "mdmModem"),
    (0, "PANDATEL-FHFLS-MODEM-MIB", "mdmPosition"),
)
if mibBuilder.loadTexts:
    fhflsTableEntry.setStatus("mandatory")
_MdmRack_Type = Integer32
_MdmRack_Object = MibTableColumn
mdmRack = _MdmRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103, 1, 1, 1),
    _MdmRack_Type()
)
mdmRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRack.setStatus("mandatory")
_MdmModem_Type = Integer32
_MdmModem_Object = MibTableColumn
mdmModem = _MdmModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103, 1, 1, 3),
    _MdmPosition_Type()
)
mdmPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPosition.setStatus("mandatory")
_MdmModemName_Type = DisplayString
_MdmModemName_Object = MibTableColumn
mdmModemName = _MdmModemName_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103, 1, 1, 5),
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
              4,
              5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 100),
          ("nt", 5),
          ("other", 1),
          ("te", 4))
    )


_MdmInterfaceEmulationMode_Type.__name__ = "Integer32"
_MdmInterfaceEmulationMode_Object = MibTableColumn
mdmInterfaceEmulationMode = _MdmInterfaceEmulationMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103, 1, 1, 6),
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
              14,
              15,
              99)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("stm1-oc3-coax", 14),
          ("sts3-oc3", 15),
          ("unknown", 99))
    )


_MdmModemProperty_Type.__name__ = "Integer32"
_MdmModemProperty_Object = MibTableColumn
mdmModemProperty = _MdmModemProperty_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103, 1, 1, 23),
    _MdmClockSystem_Type()
)
mdmClockSystem.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103, 1, 1, 24),
    _MdmClockSource_Type()
)
mdmClockSource.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103, 1, 1, 25),
    _MdmDataRate_Type()
)
mdmDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDataRate.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103, 1, 1, 64),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103, 1, 1, 65),
    _MdmForcedRemoteAccess_Type()
)
mdmForcedRemoteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmForcedRemoteAccess.setStatus("mandatory")


class _MdmClockRecovery_Type(Integer32):
    """Custom type mdmClockRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("not-available", 100),
          ("other", 1),
          ("stm1-oc3-155mbps", 3),
          ("stm4-oc12-622mbps", 4))
    )


_MdmClockRecovery_Type.__name__ = "Integer32"
_MdmClockRecovery_Object = MibTableColumn
mdmClockRecovery = _MdmClockRecovery_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103, 1, 1, 70),
    _MdmClockRecovery_Type()
)
mdmClockRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmClockRecovery.setStatus("mandatory")


class _MdmInterfaceAlarmCondition_Type(Integer32):
    """Custom type mdmInterfaceAlarmCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("no-clock-signal", 6),
          ("no-clock-signal-or-no-link-signal", 7),
          ("no-link-signal", 3),
          ("not-available", 100),
          ("other", 1))
    )


_MdmInterfaceAlarmCondition_Type.__name__ = "Integer32"
_MdmInterfaceAlarmCondition_Object = MibTableColumn
mdmInterfaceAlarmCondition = _MdmInterfaceAlarmCondition_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103, 1, 1, 98),
    _MdmInterfaceAlarmCondition_Type()
)
mdmInterfaceAlarmCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmInterfaceAlarmCondition.setStatus("mandatory")


class _MdmLineAlarmCondition_Type(Integer32):
    """Custom type mdmLineAlarmCondition based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("all", 9),
          ("disable", 2),
          ("laser-fail", 4),
          ("no-clock-signal", 6),
          ("no-clock-signal-or-laser-fail", 8),
          ("no-clock-signal-or-no-link-signal", 7),
          ("no-link-signal", 3),
          ("no-link-signal-or-laser-fail", 5),
          ("not-available", 100),
          ("other", 1))
    )


_MdmLineAlarmCondition_Type.__name__ = "Integer32"
_MdmLineAlarmCondition_Object = MibTableColumn
mdmLineAlarmCondition = _MdmLineAlarmCondition_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 103, 1, 1, 99),
    _MdmLineAlarmCondition_Type()
)
mdmLineAlarmCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLineAlarmCondition.setStatus("mandatory")
_Fhfls_modem_ObjectIdentity = ObjectIdentity
fhfls_modem = _Fhfls_modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 103)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANDATEL-FHFLS-MODEM-MIB",
    **{"fhfls": fhfls,
       "fhflsModemTable": fhflsModemTable,
       "fhflsTableEntry": fhflsTableEntry,
       "mdmRack": mdmRack,
       "mdmModem": mdmModem,
       "mdmPosition": mdmPosition,
       "mdmModemName": mdmModemName,
       "mdmInterfaceEmulationMode": mdmInterfaceEmulationMode,
       "mdmModemProperty": mdmModemProperty,
       "mdmClockSystem": mdmClockSystem,
       "mdmClockSource": mdmClockSource,
       "mdmDataRate": mdmDataRate,
       "mdmRemoteAccessMode": mdmRemoteAccessMode,
       "mdmForcedRemoteAccess": mdmForcedRemoteAccess,
       "mdmClockRecovery": mdmClockRecovery,
       "mdmInterfaceAlarmCondition": mdmInterfaceAlarmCondition,
       "mdmLineAlarmCondition": mdmLineAlarmCondition,
       "fhfls-modem": fhfls_modem}
)
