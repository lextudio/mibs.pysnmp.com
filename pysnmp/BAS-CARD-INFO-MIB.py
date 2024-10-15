# SNMP MIB module (BAS-CARD-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-CARD-INFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:19 2024
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

(BasCardClass,
 BasChassisId,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 basCardInfo) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasCardClass",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basCardInfo")

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
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

basCardInfoMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasCardObjects_ObjectIdentity = ObjectIdentity
basCardObjects = _BasCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1)
)
_BasCardInfoTable_Object = MibTable
basCardInfoTable = _BasCardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    basCardInfoTable.setStatus("current")
_BasCardInfoEntry_Object = MibTableRow
basCardInfoEntry = _BasCardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1)
)
basCardInfoEntry.setIndexNames(
    (0, "BAS-CARD-INFO-MIB", "basCardInfoChassis"),
    (0, "BAS-CARD-INFO-MIB", "basCardInfoSlot"),
    (0, "BAS-CARD-INFO-MIB", "basCardInfoIf"),
    (0, "BAS-CARD-INFO-MIB", "basCardInfoLPort"),
)
if mibBuilder.loadTexts:
    basCardInfoEntry.setStatus("current")
_BasCardInfoChassis_Type = BasChassisId
_BasCardInfoChassis_Object = MibTableColumn
basCardInfoChassis = _BasCardInfoChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 1),
    _BasCardInfoChassis_Type()
)
basCardInfoChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCardInfoChassis.setStatus("current")
_BasCardInfoSlot_Type = BasSlotId
_BasCardInfoSlot_Object = MibTableColumn
basCardInfoSlot = _BasCardInfoSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 2),
    _BasCardInfoSlot_Type()
)
basCardInfoSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCardInfoSlot.setStatus("current")
_BasCardInfoIf_Type = BasInterfaceId
_BasCardInfoIf_Object = MibTableColumn
basCardInfoIf = _BasCardInfoIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 3),
    _BasCardInfoIf_Type()
)
basCardInfoIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCardInfoIf.setStatus("current")
_BasCardInfoLPort_Type = BasLogicalPortId
_BasCardInfoLPort_Object = MibTableColumn
basCardInfoLPort = _BasCardInfoLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 4),
    _BasCardInfoLPort_Type()
)
basCardInfoLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCardInfoLPort.setStatus("current")
_BasCardInfoChassisNumber_Type = Integer32
_BasCardInfoChassisNumber_Object = MibTableColumn
basCardInfoChassisNumber = _BasCardInfoChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 5),
    _BasCardInfoChassisNumber_Type()
)
basCardInfoChassisNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCardInfoChassisNumber.setStatus("current")
_BasCardInfoClass_Type = BasCardClass
_BasCardInfoClass_Object = MibTableColumn
basCardInfoClass = _BasCardInfoClass_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 6),
    _BasCardInfoClass_Type()
)
basCardInfoClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCardInfoClass.setStatus("current")


class _BasAgentConfigSave_Type(Integer32):
    """Custom type basAgentConfigSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("save", 2),
          ("saving", 3))
    )


_BasAgentConfigSave_Type.__name__ = "Integer32"
_BasAgentConfigSave_Object = MibTableColumn
basAgentConfigSave = _BasAgentConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 7),
    _BasAgentConfigSave_Type()
)
basAgentConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basAgentConfigSave.setStatus("current")


class _BasAgentConfigSaveStatus_Type(Integer32):
    """Custom type basAgentConfigSaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("none", 1),
          ("passed", 2))
    )


_BasAgentConfigSaveStatus_Type.__name__ = "Integer32"
_BasAgentConfigSaveStatus_Object = MibTableColumn
basAgentConfigSaveStatus = _BasAgentConfigSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 8),
    _BasAgentConfigSaveStatus_Type()
)
basAgentConfigSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basAgentConfigSaveStatus.setStatus("current")
_BasBcmIpAddress_Type = IpAddress
_BasBcmIpAddress_Object = MibTableColumn
basBcmIpAddress = _BasBcmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 9),
    _BasBcmIpAddress_Type()
)
basBcmIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basBcmIpAddress.setStatus("current")


class _BasCardReset_Type(Integer32):
    """Custom type basCardReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_BasCardReset_Type.__name__ = "Integer32"
_BasCardReset_Object = MibTableColumn
basCardReset = _BasCardReset_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 10),
    _BasCardReset_Type()
)
basCardReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCardReset.setStatus("current")


class _BasAgentSharedKey_Type(OctetString):
    """Custom type basAgentSharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_BasAgentSharedKey_Type.__name__ = "OctetString"
_BasAgentSharedKey_Object = MibTableColumn
basAgentSharedKey = _BasAgentSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 11),
    _BasAgentSharedKey_Type()
)
basAgentSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basAgentSharedKey.setStatus("current")


class _BasAgentUdpPort_Type(Integer32):
    """Custom type basAgentUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BasAgentUdpPort_Type.__name__ = "Integer32"
_BasAgentUdpPort_Object = MibTableColumn
basAgentUdpPort = _BasAgentUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 12),
    _BasAgentUdpPort_Type()
)
basAgentUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basAgentUdpPort.setStatus("current")


class _BasAgentTcpPort_Type(Integer32):
    """Custom type basAgentTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BasAgentTcpPort_Type.__name__ = "Integer32"
_BasAgentTcpPort_Object = MibTableColumn
basAgentTcpPort = _BasAgentTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 13),
    _BasAgentTcpPort_Type()
)
basAgentTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basAgentTcpPort.setStatus("current")


class _BasCardInfoAdminStatus_Type(Integer32):
    """Custom type basCardInfoAdminStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("agentxstarted", 9),
          ("agentxstarting", 8),
          ("down", 2),
          ("loaded", 5),
          ("loading", 4),
          ("registered", 7),
          ("registering", 6),
          ("testing", 3),
          ("up", 1))
    )


_BasCardInfoAdminStatus_Type.__name__ = "Integer32"
_BasCardInfoAdminStatus_Object = MibTableColumn
basCardInfoAdminStatus = _BasCardInfoAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 14),
    _BasCardInfoAdminStatus_Type()
)
basCardInfoAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basCardInfoAdminStatus.setStatus("current")


class _BasCardResetState_Type(Integer32):
    """Custom type basCardResetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_BasCardResetState_Type.__name__ = "Integer32"
_BasCardResetState_Object = MibTableColumn
basCardResetState = _BasCardResetState_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 15),
    _BasCardResetState_Type()
)
basCardResetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCardResetState.setStatus("current")


class _BasCardWatchdogTimer_Type(Integer32):
    """Custom type basCardWatchdogTimer based on Integer32"""
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
          ("enable", 1),
          ("notSupported", 3))
    )


_BasCardWatchdogTimer_Type.__name__ = "Integer32"
_BasCardWatchdogTimer_Object = MibTableColumn
basCardWatchdogTimer = _BasCardWatchdogTimer_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 16),
    _BasCardWatchdogTimer_Type()
)
basCardWatchdogTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCardWatchdogTimer.setStatus("current")
_BasCardRSTable_Object = MibTable
basCardRSTable = _BasCardRSTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    basCardRSTable.setStatus("current")
_BasCardRSEntry_Object = MibTableRow
basCardRSEntry = _BasCardRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1)
)
basCardRSEntry.setIndexNames(
    (0, "BAS-CARD-INFO-MIB", "basCardChassis"),
    (0, "BAS-CARD-INFO-MIB", "basCardSlot"),
    (0, "BAS-CARD-INFO-MIB", "basCardIf"),
    (0, "BAS-CARD-INFO-MIB", "basCardLPort"),
    (0, "BAS-CARD-INFO-MIB", "basCardRSChassis"),
    (0, "BAS-CARD-INFO-MIB", "basCardRSSlot"),
    (0, "BAS-CARD-INFO-MIB", "basCardRSIf"),
    (0, "BAS-CARD-INFO-MIB", "basCardRSLPort"),
)
if mibBuilder.loadTexts:
    basCardRSEntry.setStatus("current")
_BasCardChassis_Type = BasChassisId
_BasCardChassis_Object = MibTableColumn
basCardChassis = _BasCardChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 1),
    _BasCardChassis_Type()
)
basCardChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCardChassis.setStatus("current")
_BasCardSlot_Type = BasSlotId
_BasCardSlot_Object = MibTableColumn
basCardSlot = _BasCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 2),
    _BasCardSlot_Type()
)
basCardSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCardSlot.setStatus("current")
_BasCardIf_Type = BasInterfaceId
_BasCardIf_Object = MibTableColumn
basCardIf = _BasCardIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 3),
    _BasCardIf_Type()
)
basCardIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCardIf.setStatus("current")
_BasCardLPort_Type = BasLogicalPortId
_BasCardLPort_Object = MibTableColumn
basCardLPort = _BasCardLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 4),
    _BasCardLPort_Type()
)
basCardLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCardLPort.setStatus("current")
_BasCardRSChassis_Type = BasChassisId
_BasCardRSChassis_Object = MibTableColumn
basCardRSChassis = _BasCardRSChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 5),
    _BasCardRSChassis_Type()
)
basCardRSChassis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basCardRSChassis.setStatus("current")
_BasCardRSSlot_Type = BasSlotId
_BasCardRSSlot_Object = MibTableColumn
basCardRSSlot = _BasCardRSSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 6),
    _BasCardRSSlot_Type()
)
basCardRSSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basCardRSSlot.setStatus("current")
_BasCardRSIf_Type = BasInterfaceId
_BasCardRSIf_Object = MibTableColumn
basCardRSIf = _BasCardRSIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 7),
    _BasCardRSIf_Type()
)
basCardRSIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basCardRSIf.setStatus("current")
_BasCardRSLPort_Type = BasLogicalPortId
_BasCardRSLPort_Object = MibTableColumn
basCardRSLPort = _BasCardRSLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 8),
    _BasCardRSLPort_Type()
)
basCardRSLPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basCardRSLPort.setStatus("current")
_BasCardRSStatus_Type = RowStatus
_BasCardRSStatus_Object = MibTableColumn
basCardRSStatus = _BasCardRSStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 9),
    _BasCardRSStatus_Type()
)
basCardRSStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basCardRSStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-CARD-INFO-MIB",
    **{"basCardInfoMib": basCardInfoMib,
       "basCardObjects": basCardObjects,
       "basCardInfoTable": basCardInfoTable,
       "basCardInfoEntry": basCardInfoEntry,
       "basCardInfoChassis": basCardInfoChassis,
       "basCardInfoSlot": basCardInfoSlot,
       "basCardInfoIf": basCardInfoIf,
       "basCardInfoLPort": basCardInfoLPort,
       "basCardInfoChassisNumber": basCardInfoChassisNumber,
       "basCardInfoClass": basCardInfoClass,
       "basAgentConfigSave": basAgentConfigSave,
       "basAgentConfigSaveStatus": basAgentConfigSaveStatus,
       "basBcmIpAddress": basBcmIpAddress,
       "basCardReset": basCardReset,
       "basAgentSharedKey": basAgentSharedKey,
       "basAgentUdpPort": basAgentUdpPort,
       "basAgentTcpPort": basAgentTcpPort,
       "basCardInfoAdminStatus": basCardInfoAdminStatus,
       "basCardResetState": basCardResetState,
       "basCardWatchdogTimer": basCardWatchdogTimer,
       "basCardRSTable": basCardRSTable,
       "basCardRSEntry": basCardRSEntry,
       "basCardChassis": basCardChassis,
       "basCardSlot": basCardSlot,
       "basCardIf": basCardIf,
       "basCardLPort": basCardLPort,
       "basCardRSChassis": basCardRSChassis,
       "basCardRSSlot": basCardRSSlot,
       "basCardRSIf": basCardRSIf,
       "basCardRSLPort": basCardRSLPort,
       "basCardRSStatus": basCardRSStatus}
)
