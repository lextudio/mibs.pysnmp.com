# SNMP MIB module (BAS-HACKED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-HACKED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:25 2024
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
 basHackedInfo) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasCardClass",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basHackedInfo")

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

basHackedInfoMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasHackedObjects_ObjectIdentity = ObjectIdentity
basHackedObjects = _BasHackedObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1)
)
_BasHackedInfoTable_Object = MibTable
basHackedInfoTable = _BasHackedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1, 1)
)
if mibBuilder.loadTexts:
    basHackedInfoTable.setStatus("current")
_BasHackedInfoEntry_Object = MibTableRow
basHackedInfoEntry = _BasHackedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1, 1, 1)
)
basHackedInfoEntry.setIndexNames(
    (0, "BAS-HACKED-MIB", "basHackedCardInfoChassis"),
    (0, "BAS-HACKED-MIB", "basHackedCardInfoSlot"),
    (0, "BAS-HACKED-MIB", "basHackedCardInfoIf"),
    (0, "BAS-HACKED-MIB", "basHackedCardInfoLPort"),
)
if mibBuilder.loadTexts:
    basHackedInfoEntry.setStatus("current")
_BasHackedCardInfoChassis_Type = BasChassisId
_BasHackedCardInfoChassis_Object = MibTableColumn
basHackedCardInfoChassis = _BasHackedCardInfoChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1, 1, 1, 1),
    _BasHackedCardInfoChassis_Type()
)
basHackedCardInfoChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basHackedCardInfoChassis.setStatus("current")
_BasHackedCardInfoSlot_Type = BasSlotId
_BasHackedCardInfoSlot_Object = MibTableColumn
basHackedCardInfoSlot = _BasHackedCardInfoSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1, 1, 1, 2),
    _BasHackedCardInfoSlot_Type()
)
basHackedCardInfoSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basHackedCardInfoSlot.setStatus("current")
_BasHackedCardInfoIf_Type = BasInterfaceId
_BasHackedCardInfoIf_Object = MibTableColumn
basHackedCardInfoIf = _BasHackedCardInfoIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1, 1, 1, 3),
    _BasHackedCardInfoIf_Type()
)
basHackedCardInfoIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basHackedCardInfoIf.setStatus("current")
_BasHackedCardInfoLPort_Type = BasLogicalPortId
_BasHackedCardInfoLPort_Object = MibTableColumn
basHackedCardInfoLPort = _BasHackedCardInfoLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1, 1, 1, 4),
    _BasHackedCardInfoLPort_Type()
)
basHackedCardInfoLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basHackedCardInfoLPort.setStatus("current")
_BasHackedCardInfoChassisNumber_Type = Integer32
_BasHackedCardInfoChassisNumber_Object = MibTableColumn
basHackedCardInfoChassisNumber = _BasHackedCardInfoChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1, 1, 1, 5),
    _BasHackedCardInfoChassisNumber_Type()
)
basHackedCardInfoChassisNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basHackedCardInfoChassisNumber.setStatus("current")
_BasHackedCardInfoClass_Type = BasCardClass
_BasHackedCardInfoClass_Object = MibTableColumn
basHackedCardInfoClass = _BasHackedCardInfoClass_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1, 1, 1, 6),
    _BasHackedCardInfoClass_Type()
)
basHackedCardInfoClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basHackedCardInfoClass.setStatus("current")


class _BasHackedAgentConfigSave_Type(Integer32):
    """Custom type basHackedAgentConfigSave based on Integer32"""
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


_BasHackedAgentConfigSave_Type.__name__ = "Integer32"
_BasHackedAgentConfigSave_Object = MibTableColumn
basHackedAgentConfigSave = _BasHackedAgentConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1, 1, 1, 7),
    _BasHackedAgentConfigSave_Type()
)
basHackedAgentConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basHackedAgentConfigSave.setStatus("current")


class _BasHackedAgentConfigSaveStatus_Type(Integer32):
    """Custom type basHackedAgentConfigSaveStatus based on Integer32"""
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


_BasHackedAgentConfigSaveStatus_Type.__name__ = "Integer32"
_BasHackedAgentConfigSaveStatus_Object = MibTableColumn
basHackedAgentConfigSaveStatus = _BasHackedAgentConfigSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1, 1, 1, 8),
    _BasHackedAgentConfigSaveStatus_Type()
)
basHackedAgentConfigSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basHackedAgentConfigSaveStatus.setStatus("current")
_BasHackedBcmIpAddress_Type = IpAddress
_BasHackedBcmIpAddress_Object = MibTableColumn
basHackedBcmIpAddress = _BasHackedBcmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1, 1, 1, 9),
    _BasHackedBcmIpAddress_Type()
)
basHackedBcmIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basHackedBcmIpAddress.setStatus("current")


class _BasHackedCardReset_Type(Integer32):
    """Custom type basHackedCardReset based on Integer32"""
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


_BasHackedCardReset_Type.__name__ = "Integer32"
_BasHackedCardReset_Object = MibTableColumn
basHackedCardReset = _BasHackedCardReset_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1, 1, 1, 10),
    _BasHackedCardReset_Type()
)
basHackedCardReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basHackedCardReset.setStatus("current")


class _BasHackedAgentSharedKey_Type(OctetString):
    """Custom type basHackedAgentSharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_BasHackedAgentSharedKey_Type.__name__ = "OctetString"
_BasHackedAgentSharedKey_Object = MibTableColumn
basHackedAgentSharedKey = _BasHackedAgentSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1, 1, 1, 11),
    _BasHackedAgentSharedKey_Type()
)
basHackedAgentSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basHackedAgentSharedKey.setStatus("current")


class _BasHackedAgentUdpPort_Type(Integer32):
    """Custom type basHackedAgentUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BasHackedAgentUdpPort_Type.__name__ = "Integer32"
_BasHackedAgentUdpPort_Object = MibTableColumn
basHackedAgentUdpPort = _BasHackedAgentUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1, 1, 1, 12),
    _BasHackedAgentUdpPort_Type()
)
basHackedAgentUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basHackedAgentUdpPort.setStatus("current")


class _BasHackedAgentTcpPort_Type(Integer32):
    """Custom type basHackedAgentTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BasHackedAgentTcpPort_Type.__name__ = "Integer32"
_BasHackedAgentTcpPort_Object = MibTableColumn
basHackedAgentTcpPort = _BasHackedAgentTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1, 1, 1, 13),
    _BasHackedAgentTcpPort_Type()
)
basHackedAgentTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basHackedAgentTcpPort.setStatus("current")


class _BasHackedCardResetState_Type(Integer32):
    """Custom type basHackedCardResetState based on Integer32"""
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


_BasHackedCardResetState_Type.__name__ = "Integer32"
_BasHackedCardResetState_Object = MibTableColumn
basHackedCardResetState = _BasHackedCardResetState_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000, 1, 1, 1, 1, 14),
    _BasHackedCardResetState_Type()
)
basHackedCardResetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basHackedCardResetState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-HACKED-MIB",
    **{"basHackedInfoMib": basHackedInfoMib,
       "basHackedObjects": basHackedObjects,
       "basHackedInfoTable": basHackedInfoTable,
       "basHackedInfoEntry": basHackedInfoEntry,
       "basHackedCardInfoChassis": basHackedCardInfoChassis,
       "basHackedCardInfoSlot": basHackedCardInfoSlot,
       "basHackedCardInfoIf": basHackedCardInfoIf,
       "basHackedCardInfoLPort": basHackedCardInfoLPort,
       "basHackedCardInfoChassisNumber": basHackedCardInfoChassisNumber,
       "basHackedCardInfoClass": basHackedCardInfoClass,
       "basHackedAgentConfigSave": basHackedAgentConfigSave,
       "basHackedAgentConfigSaveStatus": basHackedAgentConfigSaveStatus,
       "basHackedBcmIpAddress": basHackedBcmIpAddress,
       "basHackedCardReset": basHackedCardReset,
       "basHackedAgentSharedKey": basHackedAgentSharedKey,
       "basHackedAgentUdpPort": basHackedAgentUdpPort,
       "basHackedAgentTcpPort": basHackedAgentTcpPort,
       "basHackedCardResetState": basHackedCardResetState}
)
