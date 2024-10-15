# SNMP MIB module (PANDATEL-FXG-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANDATEL-FXG-MODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:48 2024
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

_Fxg_ObjectIdentity = ObjectIdentity
fxg = _Fxg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 506)
)
_FxgModemTable_Object = MibTable
fxgModemTable = _FxgModemTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 506, 1)
)
if mibBuilder.loadTexts:
    fxgModemTable.setStatus("mandatory")
_FxgTableEntry_Object = MibTableRow
fxgTableEntry = _FxgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 506, 1, 1)
)
fxgTableEntry.setIndexNames(
    (0, "PANDATEL-FXG-MODEM-MIB", "mdmRack"),
    (0, "PANDATEL-FXG-MODEM-MIB", "mdmModem"),
    (0, "PANDATEL-FXG-MODEM-MIB", "mdmPosition"),
)
if mibBuilder.loadTexts:
    fxgTableEntry.setStatus("mandatory")
_MdmRack_Type = Integer32
_MdmRack_Object = MibTableColumn
mdmRack = _MdmRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 506, 1, 1, 1),
    _MdmRack_Type()
)
mdmRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRack.setStatus("mandatory")
_MdmModem_Type = Integer32
_MdmModem_Object = MibTableColumn
mdmModem = _MdmModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 506, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 506, 1, 1, 3),
    _MdmPosition_Type()
)
mdmPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPosition.setStatus("mandatory")
_MdmModemName_Type = DisplayString
_MdmModemName_Object = MibTableColumn
mdmModemName = _MdmModemName_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 506, 1, 1, 5),
    _MdmModemName_Type()
)
mdmModemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmModemName.setStatus("mandatory")


class _MdmAlarm_Type(Integer32):
    """Custom type mdmAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("other", 1))
    )


_MdmAlarm_Type.__name__ = "Integer32"
_MdmAlarm_Object = MibTableColumn
mdmAlarm = _MdmAlarm_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 506, 1, 1, 15),
    _MdmAlarm_Type()
)
mdmAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmAlarm.setStatus("mandatory")


class _MdmRemoteAccessMode_Type(Integer32):
    """Custom type mdmRemoteAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disable-local", 8),
          ("disable-local-and-remote", 9),
          ("enable", 5),
          ("other", 1))
    )


_MdmRemoteAccessMode_Type.__name__ = "Integer32"
_MdmRemoteAccessMode_Object = MibTableColumn
mdmRemoteAccessMode = _MdmRemoteAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 506, 1, 1, 64),
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
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 506, 1, 1, 65),
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
              6,
              7,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("fibre-Channel-1062", 7),
          ("gigabit-Ethernet-1250", 6),
          ("not-available", 100),
          ("other", 1))
    )


_MdmClockRecovery_Type.__name__ = "Integer32"
_MdmClockRecovery_Object = MibTableColumn
mdmClockRecovery = _MdmClockRecovery_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 506, 1, 1, 70),
    _MdmClockRecovery_Type()
)
mdmClockRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmClockRecovery.setStatus("mandatory")


class _MdmOperationMode_Type(Integer32):
    """Custom type mdmOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("converter-mode", 3),
          ("modem-mode", 2),
          ("other", 1))
    )


_MdmOperationMode_Type.__name__ = "Integer32"
_MdmOperationMode_Object = MibTableColumn
mdmOperationMode = _MdmOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 506, 1, 1, 72),
    _MdmOperationMode_Type()
)
mdmOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmOperationMode.setStatus("mandatory")


class _MdmInterfaceAlarmCondition_Type(Integer32):
    """Custom type mdmInterfaceAlarmCondition based on Integer32"""
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
          ("no-link-signal", 3),
          ("not-available", 100),
          ("other", 1))
    )


_MdmInterfaceAlarmCondition_Type.__name__ = "Integer32"
_MdmInterfaceAlarmCondition_Object = MibTableColumn
mdmInterfaceAlarmCondition = _MdmInterfaceAlarmCondition_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 506, 1, 1, 98),
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("no-link-signal", 3),
          ("not-available", 100),
          ("other", 1))
    )


_MdmLineAlarmCondition_Type.__name__ = "Integer32"
_MdmLineAlarmCondition_Object = MibTableColumn
mdmLineAlarmCondition = _MdmLineAlarmCondition_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 506, 1, 1, 99),
    _MdmLineAlarmCondition_Type()
)
mdmLineAlarmCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLineAlarmCondition.setStatus("mandatory")
_Fxg_modem_ObjectIdentity = ObjectIdentity
fxg_modem = _Fxg_modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 506)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANDATEL-FXG-MODEM-MIB",
    **{"fxg": fxg,
       "fxgModemTable": fxgModemTable,
       "fxgTableEntry": fxgTableEntry,
       "mdmRack": mdmRack,
       "mdmModem": mdmModem,
       "mdmPosition": mdmPosition,
       "mdmModemName": mdmModemName,
       "mdmAlarm": mdmAlarm,
       "mdmRemoteAccessMode": mdmRemoteAccessMode,
       "mdmForcedRemoteAccess": mdmForcedRemoteAccess,
       "mdmClockRecovery": mdmClockRecovery,
       "mdmOperationMode": mdmOperationMode,
       "mdmInterfaceAlarmCondition": mdmInterfaceAlarmCondition,
       "mdmLineAlarmCondition": mdmLineAlarmCondition,
       "fxg-modem": fxg_modem}
)
