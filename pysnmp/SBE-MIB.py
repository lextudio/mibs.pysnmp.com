# SNMP MIB module (SBE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SBE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:46 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "RFC1230-MIB",
    "MacAddress")

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
 NotificationType,
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
    "NotificationType",
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

_Sbe_ObjectIdentity = ObjectIdentity
sbe = _Sbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 1)
)


class _SyDateTime_Type(OctetString):
    """Custom type syDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SyDateTime_Type.__name__ = "OctetString"
_SyDateTime_Object = MibScalar
syDateTime = _SyDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1055, 1, 1),
    _SyDateTime_Type()
)
syDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syDateTime.setStatus("mandatory")


class _SyRAMConfigurationChangedFlag_Type(Integer32):
    """Custom type syRAMConfigurationChangedFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("different", 2),
          ("same", 1))
    )


_SyRAMConfigurationChangedFlag_Type.__name__ = "Integer32"
_SyRAMConfigurationChangedFlag_Object = MibScalar
syRAMConfigurationChangedFlag = _SyRAMConfigurationChangedFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 1, 3),
    _SyRAMConfigurationChangedFlag_Type()
)
syRAMConfigurationChangedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syRAMConfigurationChangedFlag.setStatus("mandatory")


class _SyConfigurationLockFlag_Type(Integer32):
    """Custom type syConfigurationLockFlag based on Integer32"""
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


_SyConfigurationLockFlag_Type.__name__ = "Integer32"
_SyConfigurationLockFlag_Object = MibScalar
syConfigurationLockFlag = _SyConfigurationLockFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 1, 5),
    _SyConfigurationLockFlag_Type()
)
syConfigurationLockFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syConfigurationLockFlag.setStatus("mandatory")


class _SyModel_Type(DisplayString):
    """Custom type syModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SyModel_Type.__name__ = "DisplayString"
_SyModel_Object = MibScalar
syModel = _SyModel_Object(
    (1, 3, 6, 1, 4, 1, 1055, 1, 7),
    _SyModel_Type()
)
syModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syModel.setStatus("mandatory")


class _SyBootInfo_Type(Integer32):
    """Custom type syBootInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              33280)
        )
    )
    namedValues = NamedValues(
        *(("base-board-flash-corrupt", 2),
          ("daughter-board-flash-corrupt", 8),
          ("missing-base-board-kernel-module", 4),
          ("missing-daughter-board-kernel-module", 16),
          ("normal-boot-from-LAN", 1),
          ("system-type-Central", 64),
          ("system-type-ROUTEMAN", 256),
          ("system-type-ROUTEMANXL", 512),
          ("system-type-ROUTEMANXLl", 33280),
          ("system-type-SoHo", 32),
          ("system-type-torte", 128))
    )


_SyBootInfo_Type.__name__ = "Integer32"
_SyBootInfo_Object = MibScalar
syBootInfo = _SyBootInfo_Object(
    (1, 3, 6, 1, 4, 1, 1055, 1, 10),
    _SyBootInfo_Type()
)
syBootInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syBootInfo.setStatus("deprecated")


class _SyActivatedLevel_Type(DisplayString):
    """Custom type syActivatedLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SyActivatedLevel_Type.__name__ = "DisplayString"
_SyActivatedLevel_Object = MibScalar
syActivatedLevel = _SyActivatedLevel_Object(
    (1, 3, 6, 1, 4, 1, 1055, 1, 11),
    _SyActivatedLevel_Type()
)
syActivatedLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syActivatedLevel.setStatus("mandatory")


class _SySerialNumber_Type(OctetString):
    """Custom type sySerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SySerialNumber_Type.__name__ = "OctetString"
_SySerialNumber_Object = MibScalar
sySerialNumber = _SySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1055, 1, 12),
    _SySerialNumber_Type()
)
sySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sySerialNumber.setStatus("mandatory")


class _SyBaseActivationLevel_Type(Integer32):
    """Custom type syBaseActivationLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              11,
              12,
              13,
              14,
              15,
              16,
              18,
              20,
              21,
              23,
              25,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("central20Base", 4),
          ("central21Base", 18),
          ("central30Dormant", 25),
          ("centralTest", 12),
          ("rOUTEMAN20Base", 1),
          ("rOUTEMAN21Base", 20),
          ("rOUTEMAN30Dormant", 27),
          ("rOUTEMANTest", 13),
          ("rOUTEMANX30Dormant", 28),
          ("rOUTEMANXL201Base", 15),
          ("rOUTEMANXL20Base", 6),
          ("rOUTEMANXL21Base", 21),
          ("rOUTEMANXLTest", 14),
          ("soHo20Base", 2),
          ("soHo21Base", 16),
          ("soHo30Dormant", 23),
          ("soHoTest", 11))
    )


_SyBaseActivationLevel_Type.__name__ = "Integer32"
_SyBaseActivationLevel_Object = MibScalar
syBaseActivationLevel = _SyBaseActivationLevel_Object(
    (1, 3, 6, 1, 4, 1, 1055, 1, 13),
    _SyBaseActivationLevel_Type()
)
syBaseActivationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syBaseActivationLevel.setStatus("mandatory")
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 2)
)
_Routsys_ObjectIdentity = ObjectIdentity
routsys = _Routsys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 2, 1)
)


class _SyBootOrder_Type(OctetString):
    """Custom type syBootOrder based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SyBootOrder_Type.__name__ = "OctetString"
_SyBootOrder_Object = MibScalar
syBootOrder = _SyBootOrder_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 1, 1),
    _SyBootOrder_Type()
)
syBootOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syBootOrder.setStatus("mandatory")


class _SyMtuMru_Type(Integer32):
    """Custom type syMtuMru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_SyMtuMru_Type.__name__ = "Integer32"
_SyMtuMru_Object = MibScalar
syMtuMru = _SyMtuMru_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 1, 2),
    _SyMtuMru_Type()
)
syMtuMru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syMtuMru.setStatus("mandatory")


class _SyEventToLogThreshold_Type(Integer32):
    """Custom type syEventToLogThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SyEventToLogThreshold_Type.__name__ = "Integer32"
_SyEventToLogThreshold_Object = MibScalar
syEventToLogThreshold = _SyEventToLogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 1, 3),
    _SyEventToLogThreshold_Type()
)
syEventToLogThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syEventToLogThreshold.setStatus("mandatory")


class _SyEventToTrapThreshold_Type(Integer32):
    """Custom type syEventToTrapThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SyEventToTrapThreshold_Type.__name__ = "Integer32"
_SyEventToTrapThreshold_Object = MibScalar
syEventToTrapThreshold = _SyEventToTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 1, 5),
    _SyEventToTrapThreshold_Type()
)
syEventToTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syEventToTrapThreshold.setStatus("mandatory")


class _SyControlOperation_Type(Integer32):
    """Custom type syControlOperation based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("boot-override", 14),
          ("change-password", 10),
          ("clear-SNMP-statistics", 3),
          ("crash", 9),
          ("dialout", 4),
          ("disable-port", 7),
          ("disable-port-after-call", 8),
          ("display-IP-Routes", 15),
          ("display-IPX-Networks", 16),
          ("display-IPX-Servers", 17),
          ("enable-port", 6),
          ("hangup", 5),
          ("none", 1),
          ("ram-to-Flash", 11),
          ("reboot", 2),
          ("reboot-file-transfer", 18),
          ("reset-port", 13),
          ("start-tftp-download", 12))
    )


_SyControlOperation_Type.__name__ = "Integer32"
_SyControlOperation_Object = MibScalar
syControlOperation = _SyControlOperation_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 1, 7),
    _SyControlOperation_Type()
)
syControlOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syControlOperation.setStatus("mandatory")


class _SyControlVariableStringOne_Type(OctetString):
    """Custom type syControlVariableStringOne based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SyControlVariableStringOne_Type.__name__ = "OctetString"
_SyControlVariableStringOne_Object = MibScalar
syControlVariableStringOne = _SyControlVariableStringOne_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 1, 8),
    _SyControlVariableStringOne_Type()
)
syControlVariableStringOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syControlVariableStringOne.setStatus("mandatory")


class _SyControlVariableIntegerOne_Type(Integer32):
    """Custom type syControlVariableIntegerOne based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SyControlVariableIntegerOne_Type.__name__ = "Integer32"
_SyControlVariableIntegerOne_Object = MibScalar
syControlVariableIntegerOne = _SyControlVariableIntegerOne_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 1, 9),
    _SyControlVariableIntegerOne_Type()
)
syControlVariableIntegerOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syControlVariableIntegerOne.setStatus("mandatory")


class _SyDialinAuthentication_Type(Integer32):
    """Custom type syDialinAuthentication based on Integer32"""
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
        *(("chap", 3),
          ("none", 1),
          ("pap", 2),
          ("paporchap", 4))
    )


_SyDialinAuthentication_Type.__name__ = "Integer32"
_SyDialinAuthentication_Object = MibScalar
syDialinAuthentication = _SyDialinAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 1, 10),
    _SyDialinAuthentication_Type()
)
syDialinAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syDialinAuthentication.setStatus("mandatory")


class _SyEventToSpeakThreshold_Type(Integer32):
    """Custom type syEventToSpeakThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SyEventToSpeakThreshold_Type.__name__ = "Integer32"
_SyEventToSpeakThreshold_Object = MibScalar
syEventToSpeakThreshold = _SyEventToSpeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 1, 11),
    _SyEventToSpeakThreshold_Type()
)
syEventToSpeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syEventToSpeakThreshold.setStatus("mandatory")


class _SyNumberOfTimesToSpeak_Type(Integer32):
    """Custom type syNumberOfTimesToSpeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SyNumberOfTimesToSpeak_Type.__name__ = "Integer32"
_SyNumberOfTimesToSpeak_Object = MibScalar
syNumberOfTimesToSpeak = _SyNumberOfTimesToSpeak_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 1, 12),
    _SyNumberOfTimesToSpeak_Type()
)
syNumberOfTimesToSpeak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syNumberOfTimesToSpeak.setStatus("mandatory")


class _SySaveRamToFlashState_Type(Integer32):
    """Custom type sySaveRamToFlashState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 2),
          ("updating", 1))
    )


_SySaveRamToFlashState_Type.__name__ = "Integer32"
_SySaveRamToFlashState_Object = MibScalar
sySaveRamToFlashState = _SySaveRamToFlashState_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 1, 13),
    _SySaveRamToFlashState_Type()
)
sySaveRamToFlashState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sySaveRamToFlashState.setStatus("mandatory")


class _SyDialbackRetryInterval_Type(Integer32):
    """Custom type syDialbackRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_SyDialbackRetryInterval_Type.__name__ = "Integer32"
_SyDialbackRetryInterval_Object = MibScalar
syDialbackRetryInterval = _SyDialbackRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 1, 14),
    _SyDialbackRetryInterval_Type()
)
syDialbackRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syDialbackRetryInterval.setStatus("mandatory")


class _SyDialbackRetryLimit_Type(Integer32):
    """Custom type syDialbackRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SyDialbackRetryLimit_Type.__name__ = "Integer32"
_SyDialbackRetryLimit_Object = MibScalar
syDialbackRetryLimit = _SyDialbackRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 1, 15),
    _SyDialbackRetryLimit_Type()
)
syDialbackRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syDialbackRetryLimit.setStatus("mandatory")


class _SyReverseCallbackTimeout_Type(Integer32):
    """Custom type syReverseCallbackTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_SyReverseCallbackTimeout_Type.__name__ = "Integer32"
_SyReverseCallbackTimeout_Object = MibScalar
syReverseCallbackTimeout = _SyReverseCallbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 1, 16),
    _SyReverseCallbackTimeout_Type()
)
syReverseCallbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syReverseCallbackTimeout.setStatus("mandatory")
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 2, 2)
)


class _SyBridgeConfiguredFlag_Type(Integer32):
    """Custom type syBridgeConfiguredFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SyBridgeConfiguredFlag_Type.__name__ = "Integer32"
_SyBridgeConfiguredFlag_Object = MibScalar
syBridgeConfiguredFlag = _SyBridgeConfiguredFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 2, 1),
    _SyBridgeConfiguredFlag_Type()
)
syBridgeConfiguredFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syBridgeConfiguredFlag.setStatus("mandatory")


class _SyBridgeFilterFlag_Type(Integer32):
    """Custom type syBridgeFilterFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("all", 8),
          ("exclude", 4),
          ("include", 2),
          ("other", 1))
    )


_SyBridgeFilterFlag_Type.__name__ = "Integer32"
_SyBridgeFilterFlag_Object = MibScalar
syBridgeFilterFlag = _SyBridgeFilterFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 2, 2),
    _SyBridgeFilterFlag_Type()
)
syBridgeFilterFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syBridgeFilterFlag.setStatus("mandatory")


class _SyBridgePriority_Type(Integer32):
    """Custom type syBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SyBridgePriority_Type.__name__ = "Integer32"
_SyBridgePriority_Object = MibScalar
syBridgePriority = _SyBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 2, 3),
    _SyBridgePriority_Type()
)
syBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syBridgePriority.setStatus("mandatory")
_SyBridgeTable_Object = MibTable
syBridgeTable = _SyBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 2, 4)
)
if mibBuilder.loadTexts:
    syBridgeTable.setStatus("mandatory")
_SyBridgeEntry_Object = MibTableRow
syBridgeEntry = _SyBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 2, 4, 1)
)
syBridgeEntry.setIndexNames(
    (0, "SBE-MIB", "syBridgeProtocol"),
)
if mibBuilder.loadTexts:
    syBridgeEntry.setStatus("mandatory")


class _SyBridgeStatus_Type(Integer32):
    """Custom type syBridgeStatus based on Integer32"""
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
        *(("create-request", 2),
          ("invalid", 4),
          ("under-creation", 3),
          ("valid", 1))
    )


_SyBridgeStatus_Type.__name__ = "Integer32"
_SyBridgeStatus_Object = MibTableColumn
syBridgeStatus = _SyBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 2, 4, 1, 1),
    _SyBridgeStatus_Type()
)
syBridgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syBridgeStatus.setStatus("mandatory")
_SyBridgeProtocol_Type = Integer32
_SyBridgeProtocol_Object = MibTableColumn
syBridgeProtocol = _SyBridgeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 2, 4, 1, 2),
    _SyBridgeProtocol_Type()
)
syBridgeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syBridgeProtocol.setStatus("mandatory")
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3)
)


class _IpConfiguredFlag_Type(Integer32):
    """Custom type ipConfiguredFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpConfiguredFlag_Type.__name__ = "Integer32"
_IpConfiguredFlag_Object = MibScalar
ipConfiguredFlag = _IpConfiguredFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 1),
    _IpConfiguredFlag_Type()
)
ipConfiguredFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfiguredFlag.setStatus("mandatory")
_IpLANAddress_Type = IpAddress
_IpLANAddress_Object = MibScalar
ipLANAddress = _IpLANAddress_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 2),
    _IpLANAddress_Type()
)
ipLANAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLANAddress.setStatus("mandatory")
_IpLANSubnetMask_Type = IpAddress
_IpLANSubnetMask_Object = MibScalar
ipLANSubnetMask = _IpLANSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 3),
    _IpLANSubnetMask_Type()
)
ipLANSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLANSubnetMask.setStatus("mandatory")
_IpBroadcastAddress_Type = IpAddress
_IpBroadcastAddress_Object = MibScalar
ipBroadcastAddress = _IpBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 4),
    _IpBroadcastAddress_Type()
)
ipBroadcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipBroadcastAddress.setStatus("mandatory")
_IpDefaultGateway_Type = IpAddress
_IpDefaultGateway_Object = MibScalar
ipDefaultGateway = _IpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 5),
    _IpDefaultGateway_Type()
)
ipDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDefaultGateway.setStatus("mandatory")


class _IpRipReceiveAdvertisementFlag_Type(Integer32):
    """Custom type ipRipReceiveAdvertisementFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpRipReceiveAdvertisementFlag_Type.__name__ = "Integer32"
_IpRipReceiveAdvertisementFlag_Object = MibScalar
ipRipReceiveAdvertisementFlag = _IpRipReceiveAdvertisementFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 6),
    _IpRipReceiveAdvertisementFlag_Type()
)
ipRipReceiveAdvertisementFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRipReceiveAdvertisementFlag.setStatus("mandatory")


class _IpRipSendInterval_Type(Integer32):
    """Custom type ipRipSendInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpRipSendInterval_Type.__name__ = "Integer32"
_IpRipSendInterval_Object = MibScalar
ipRipSendInterval = _IpRipSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 7),
    _IpRipSendInterval_Type()
)
ipRipSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRipSendInterval.setStatus("mandatory")


class _IpDefaultGatewayType_Type(Integer32):
    """Custom type ipDefaultGatewayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan", 1),
          ("none", 0),
          ("wan", 2))
    )


_IpDefaultGatewayType_Type.__name__ = "Integer32"
_IpDefaultGatewayType_Object = MibScalar
ipDefaultGatewayType = _IpDefaultGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 8),
    _IpDefaultGatewayType_Type()
)
ipDefaultGatewayType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDefaultGatewayType.setStatus("mandatory")


class _IpWanDestinationName_Type(DisplayString):
    """Custom type ipWanDestinationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpWanDestinationName_Type.__name__ = "DisplayString"
_IpWanDestinationName_Object = MibScalar
ipWanDestinationName = _IpWanDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 9),
    _IpWanDestinationName_Type()
)
ipWanDestinationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipWanDestinationName.setStatus("mandatory")


class _IpWanUserName_Type(DisplayString):
    """Custom type ipWanUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpWanUserName_Type.__name__ = "DisplayString"
_IpWanUserName_Object = MibScalar
ipWanUserName = _IpWanUserName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 10),
    _IpWanUserName_Type()
)
ipWanUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipWanUserName.setStatus("mandatory")
_IpStaticRouteMaxEntry_Type = Integer32
_IpStaticRouteMaxEntry_Object = MibScalar
ipStaticRouteMaxEntry = _IpStaticRouteMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 11),
    _IpStaticRouteMaxEntry_Type()
)
ipStaticRouteMaxEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStaticRouteMaxEntry.setStatus("mandatory")
_IpStaticRouteTable_Object = MibTable
ipStaticRouteTable = _IpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 12)
)
if mibBuilder.loadTexts:
    ipStaticRouteTable.setStatus("mandatory")
_IpStaticRouteEntry_Object = MibTableRow
ipStaticRouteEntry = _IpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 12, 1)
)
ipStaticRouteEntry.setIndexNames(
    (0, "SBE-MIB", "ipStaticRouteDestinationAddress"),
)
if mibBuilder.loadTexts:
    ipStaticRouteEntry.setStatus("mandatory")


class _IpStaticRouteStatus_Type(Integer32):
    """Custom type ipStaticRouteStatus based on Integer32"""
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
        *(("create-request", 2),
          ("invalid", 4),
          ("under-creation", 3),
          ("valid", 1))
    )


_IpStaticRouteStatus_Type.__name__ = "Integer32"
_IpStaticRouteStatus_Object = MibTableColumn
ipStaticRouteStatus = _IpStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 12, 1, 1),
    _IpStaticRouteStatus_Type()
)
ipStaticRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStaticRouteStatus.setStatus("mandatory")
_IpStaticRouteDestinationAddress_Type = IpAddress
_IpStaticRouteDestinationAddress_Object = MibTableColumn
ipStaticRouteDestinationAddress = _IpStaticRouteDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 12, 1, 2),
    _IpStaticRouteDestinationAddress_Type()
)
ipStaticRouteDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStaticRouteDestinationAddress.setStatus("mandatory")
_IpStaticRouteDestinationSubnetMask_Type = IpAddress
_IpStaticRouteDestinationSubnetMask_Object = MibTableColumn
ipStaticRouteDestinationSubnetMask = _IpStaticRouteDestinationSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 12, 1, 3),
    _IpStaticRouteDestinationSubnetMask_Type()
)
ipStaticRouteDestinationSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStaticRouteDestinationSubnetMask.setStatus("mandatory")


class _IpStaticRouteDestinationHopCount_Type(Integer32):
    """Custom type ipStaticRouteDestinationHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IpStaticRouteDestinationHopCount_Type.__name__ = "Integer32"
_IpStaticRouteDestinationHopCount_Object = MibTableColumn
ipStaticRouteDestinationHopCount = _IpStaticRouteDestinationHopCount_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 12, 1, 4),
    _IpStaticRouteDestinationHopCount_Type()
)
ipStaticRouteDestinationHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStaticRouteDestinationHopCount.setStatus("mandatory")


class _IpStaticRouteDestinationName_Type(DisplayString):
    """Custom type ipStaticRouteDestinationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpStaticRouteDestinationName_Type.__name__ = "DisplayString"
_IpStaticRouteDestinationName_Object = MibTableColumn
ipStaticRouteDestinationName = _IpStaticRouteDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 12, 1, 5),
    _IpStaticRouteDestinationName_Type()
)
ipStaticRouteDestinationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStaticRouteDestinationName.setStatus("mandatory")


class _IpStaticRouteNetworkInterface_Type(Integer32):
    """Custom type ipStaticRouteNetworkInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan", 1),
          ("wan", 2))
    )


_IpStaticRouteNetworkInterface_Type.__name__ = "Integer32"
_IpStaticRouteNetworkInterface_Object = MibTableColumn
ipStaticRouteNetworkInterface = _IpStaticRouteNetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 12, 1, 6),
    _IpStaticRouteNetworkInterface_Type()
)
ipStaticRouteNetworkInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStaticRouteNetworkInterface.setStatus("mandatory")


class _IpStaticRouteUserName_Type(DisplayString):
    """Custom type ipStaticRouteUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpStaticRouteUserName_Type.__name__ = "DisplayString"
_IpStaticRouteUserName_Object = MibTableColumn
ipStaticRouteUserName = _IpStaticRouteUserName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 12, 1, 7),
    _IpStaticRouteUserName_Type()
)
ipStaticRouteUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStaticRouteUserName.setStatus("mandatory")
_IpStaticRouteGateway_Type = IpAddress
_IpStaticRouteGateway_Object = MibTableColumn
ipStaticRouteGateway = _IpStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 12, 1, 8),
    _IpStaticRouteGateway_Type()
)
ipStaticRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStaticRouteGateway.setStatus("mandatory")


class _IpDefaultGatewayIfType_Type(Integer32):
    """Custom type ipDefaultGatewayIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lan", 1),
          ("none", 3),
          ("wan", 2))
    )


_IpDefaultGatewayIfType_Type.__name__ = "Integer32"
_IpDefaultGatewayIfType_Object = MibScalar
ipDefaultGatewayIfType = _IpDefaultGatewayIfType_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 13),
    _IpDefaultGatewayIfType_Type()
)
ipDefaultGatewayIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDefaultGatewayIfType.setStatus("mandatory")


class _IpBroadcastForwardTypes_Type(Integer32):
    """Custom type ipBroadcastForwardTypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_IpBroadcastForwardTypes_Type.__name__ = "Integer32"
_IpBroadcastForwardTypes_Object = MibScalar
ipBroadcastForwardTypes = _IpBroadcastForwardTypes_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 3, 14),
    _IpBroadcastForwardTypes_Type()
)
ipBroadcastForwardTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipBroadcastForwardTypes.setStatus("mandatory")
_Ipx_ObjectIdentity = ObjectIdentity
ipx = _Ipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 2, 4)
)


class _IpxConfiguredFlag_Type(Integer32):
    """Custom type ipxConfiguredFlag based on Integer32"""
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
        *(("ipx-and-auto-learn-both-off", 1),
          ("ipx-and-auto-learn-both-on", 4),
          ("ipx-off-and-auto-learn-on", 2),
          ("ipx-on-and-auto-learn-off", 3))
    )


_IpxConfiguredFlag_Type.__name__ = "Integer32"
_IpxConfiguredFlag_Object = MibScalar
ipxConfiguredFlag = _IpxConfiguredFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 4, 1),
    _IpxConfiguredFlag_Type()
)
ipxConfiguredFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxConfiguredFlag.setStatus("mandatory")


class _IpxNetbios_Type(Integer32):
    """Custom type ipxNetbios based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxNetbios_Type.__name__ = "Integer32"
_IpxNetbios_Object = MibScalar
ipxNetbios = _IpxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 4, 8),
    _IpxNetbios_Type()
)
ipxNetbios.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxNetbios.setStatus("mandatory")
_IpxMultiFrameTable_Object = MibTable
ipxMultiFrameTable = _IpxMultiFrameTable_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 4, 9)
)
if mibBuilder.loadTexts:
    ipxMultiFrameTable.setStatus("mandatory")
_IpxMultiFrameEntry_Object = MibTableRow
ipxMultiFrameEntry = _IpxMultiFrameEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 4, 9, 1)
)
ipxMultiFrameEntry.setIndexNames(
    (0, "SBE-MIB", "ipxMultiFrameType"),
)
if mibBuilder.loadTexts:
    ipxMultiFrameEntry.setStatus("mandatory")


class _IpxMultiFrameStatus_Type(Integer32):
    """Custom type ipxMultiFrameStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("create-request", 2),
          ("invalid", 4),
          ("modify", 5),
          ("under-creation", 3),
          ("valid", 1))
    )


_IpxMultiFrameStatus_Type.__name__ = "Integer32"
_IpxMultiFrameStatus_Object = MibTableColumn
ipxMultiFrameStatus = _IpxMultiFrameStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 4, 9, 1, 1),
    _IpxMultiFrameStatus_Type()
)
ipxMultiFrameStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxMultiFrameStatus.setStatus("mandatory")


class _IpxMultiFrameType_Type(Integer32):
    """Custom type ipxMultiFrameType based on Integer32"""
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
        *(("ethernet-II", 4),
          ("ieee-8022", 1),
          ("ieee-8022-SNAP", 3),
          ("ieee-8023-raw", 2))
    )


_IpxMultiFrameType_Type.__name__ = "Integer32"
_IpxMultiFrameType_Object = MibTableColumn
ipxMultiFrameType = _IpxMultiFrameType_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 4, 9, 1, 2),
    _IpxMultiFrameType_Type()
)
ipxMultiFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxMultiFrameType.setStatus("mandatory")


class _IpxMultiFrameSelectFlag_Type(Integer32):
    """Custom type ipxMultiFrameSelectFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxMultiFrameSelectFlag_Type.__name__ = "Integer32"
_IpxMultiFrameSelectFlag_Object = MibTableColumn
ipxMultiFrameSelectFlag = _IpxMultiFrameSelectFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 4, 9, 1, 3),
    _IpxMultiFrameSelectFlag_Type()
)
ipxMultiFrameSelectFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxMultiFrameSelectFlag.setStatus("mandatory")


class _IpxMultiFrameNetworkAddress_Type(OctetString):
    """Custom type ipxMultiFrameNetworkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxMultiFrameNetworkAddress_Type.__name__ = "OctetString"
_IpxMultiFrameNetworkAddress_Object = MibTableColumn
ipxMultiFrameNetworkAddress = _IpxMultiFrameNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 4, 9, 1, 4),
    _IpxMultiFrameNetworkAddress_Type()
)
ipxMultiFrameNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxMultiFrameNetworkAddress.setStatus("mandatory")


class _IpxNetAddressAutoLearnStateCounter_Type(Integer32):
    """Custom type ipxNetAddressAutoLearnStateCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70),
    )


_IpxNetAddressAutoLearnStateCounter_Type.__name__ = "Integer32"
_IpxNetAddressAutoLearnStateCounter_Object = MibScalar
ipxNetAddressAutoLearnStateCounter = _IpxNetAddressAutoLearnStateCounter_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 4, 11),
    _IpxNetAddressAutoLearnStateCounter_Type()
)
ipxNetAddressAutoLearnStateCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxNetAddressAutoLearnStateCounter.setStatus("mandatory")
_Wan_ObjectIdentity = ObjectIdentity
wan = _Wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5)
)
_WanPortTable_Object = MibTable
wanPortTable = _WanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1)
)
if mibBuilder.loadTexts:
    wanPortTable.setStatus("mandatory")
_WanPortEntry_Object = MibTableRow
wanPortEntry = _WanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2)
)
wanPortEntry.setIndexNames(
    (0, "SBE-MIB", "wanPortNumber"),
)
if mibBuilder.loadTexts:
    wanPortEntry.setStatus("mandatory")


class _WanPortEntryStatus_Type(Integer32):
    """Custom type wanPortEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("create-request", 2),
          ("invalid", 4),
          ("modify", 5),
          ("under-creation", 3),
          ("valid", 1))
    )


_WanPortEntryStatus_Type.__name__ = "Integer32"
_WanPortEntryStatus_Object = MibTableColumn
wanPortEntryStatus = _WanPortEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 1),
    _WanPortEntryStatus_Type()
)
wanPortEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanPortEntryStatus.setStatus("mandatory")


class _WanPortNumber_Type(Integer32):
    """Custom type wanPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_WanPortNumber_Type.__name__ = "Integer32"
_WanPortNumber_Object = MibTableColumn
wanPortNumber = _WanPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 2),
    _WanPortNumber_Type()
)
wanPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPortNumber.setStatus("mandatory")


class _WanPortEnabled_Type(Integer32):
    """Custom type wanPortEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WanPortEnabled_Type.__name__ = "Integer32"
_WanPortEnabled_Object = MibTableColumn
wanPortEnabled = _WanPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 3),
    _WanPortEnabled_Type()
)
wanPortEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPortEnabled.setStatus("mandatory")
_WanDefaultDialinIPAddress_Type = IpAddress
_WanDefaultDialinIPAddress_Object = MibTableColumn
wanDefaultDialinIPAddress = _WanDefaultDialinIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 4),
    _WanDefaultDialinIPAddress_Type()
)
wanDefaultDialinIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDefaultDialinIPAddress.setStatus("mandatory")
_WanDefaultDialinSubnetMask_Type = IpAddress
_WanDefaultDialinSubnetMask_Object = MibTableColumn
wanDefaultDialinSubnetMask = _WanDefaultDialinSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 5),
    _WanDefaultDialinSubnetMask_Type()
)
wanDefaultDialinSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDefaultDialinSubnetMask.setStatus("mandatory")


class _WanDefaultIPXNetworkAddress_Type(OctetString):
    """Custom type wanDefaultIPXNetworkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WanDefaultIPXNetworkAddress_Type.__name__ = "OctetString"
_WanDefaultIPXNetworkAddress_Object = MibTableColumn
wanDefaultIPXNetworkAddress = _WanDefaultIPXNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 6),
    _WanDefaultIPXNetworkAddress_Type()
)
wanDefaultIPXNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDefaultIPXNetworkAddress.setStatus("mandatory")


class _WanDefaultDialinIPXNodeAddress_Type(OctetString):
    """Custom type wanDefaultDialinIPXNodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WanDefaultDialinIPXNodeAddress_Type.__name__ = "OctetString"
_WanDefaultDialinIPXNodeAddress_Object = MibTableColumn
wanDefaultDialinIPXNodeAddress = _WanDefaultDialinIPXNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 7),
    _WanDefaultDialinIPXNodeAddress_Type()
)
wanDefaultDialinIPXNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDefaultDialinIPXNodeAddress.setStatus("mandatory")


class _WanDialinAllowedFlag_Type(Integer32):
    """Custom type wanDialinAllowedFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_WanDialinAllowedFlag_Type.__name__ = "Integer32"
_WanDialinAllowedFlag_Object = MibTableColumn
wanDialinAllowedFlag = _WanDialinAllowedFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 8),
    _WanDialinAllowedFlag_Type()
)
wanDialinAllowedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDialinAllowedFlag.setStatus("mandatory")


class _WanDialoutAllowedFlag_Type(Integer32):
    """Custom type wanDialoutAllowedFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_WanDialoutAllowedFlag_Type.__name__ = "Integer32"
_WanDialoutAllowedFlag_Object = MibTableColumn
wanDialoutAllowedFlag = _WanDialoutAllowedFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 9),
    _WanDialoutAllowedFlag_Type()
)
wanDialoutAllowedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDialoutAllowedFlag.setStatus("mandatory")


class _WanLinkLayerType_Type(Integer32):
    """Custom type wanLinkLayerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("async", 1),
          ("autosync", 3),
          ("sync", 2))
    )


_WanLinkLayerType_Type.__name__ = "Integer32"
_WanLinkLayerType_Object = MibTableColumn
wanLinkLayerType = _WanLinkLayerType_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 10),
    _WanLinkLayerType_Type()
)
wanLinkLayerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanLinkLayerType.setStatus("mandatory")


class _WanLinkLayerNRZFlag_Type(Integer32):
    """Custom type wanLinkLayerNRZFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 1),
          ("nrzi", 2))
    )


_WanLinkLayerNRZFlag_Type.__name__ = "Integer32"
_WanLinkLayerNRZFlag_Object = MibTableColumn
wanLinkLayerNRZFlag = _WanLinkLayerNRZFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 11),
    _WanLinkLayerNRZFlag_Type()
)
wanLinkLayerNRZFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanLinkLayerNRZFlag.setStatus("mandatory")


class _WanLinkLayerProtocolType_Type(Integer32):
    """Custom type wanLinkLayerProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("framerelaydce", 6),
          ("framerelaydte", 5),
          ("isdn", 3),
          ("none", 1),
          ("ppp", 2),
          ("x25", 4))
    )


_WanLinkLayerProtocolType_Type.__name__ = "Integer32"
_WanLinkLayerProtocolType_Object = MibTableColumn
wanLinkLayerProtocolType = _WanLinkLayerProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 12),
    _WanLinkLayerProtocolType_Type()
)
wanLinkLayerProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanLinkLayerProtocolType.setStatus("mandatory")


class _WanLinkDialupFlag_Type(Integer32):
    """Custom type wanLinkDialupFlag based on Integer32"""
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
        *(("dedicated", 2),
          ("dialup", 1),
          ("dtr-dial", 3),
          ("isdn-dialup", 4))
    )


_WanLinkDialupFlag_Type.__name__ = "Integer32"
_WanLinkDialupFlag_Object = MibTableColumn
wanLinkDialupFlag = _WanLinkDialupFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 13),
    _WanLinkDialupFlag_Type()
)
wanLinkDialupFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanLinkDialupFlag.setStatus("mandatory")


class _WanModemName_Type(DisplayString):
    """Custom type wanModemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_WanModemName_Type.__name__ = "DisplayString"
_WanModemName_Object = MibTableColumn
wanModemName = _WanModemName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 14),
    _WanModemName_Type()
)
wanModemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanModemName.setStatus("mandatory")


class _WanModemSpeed_Type(Integer32):
    """Custom type wanModemSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1200,
              2400,
              4800,
              9600,
              19200,
              38400,
              57600,
              115200)
        )
    )
    namedValues = NamedValues(
        *(("fiftysevensix", 57600),
          ("fortyeighthundred", 4800),
          ("nineteentwelve", 19200),
          ("ninetysixhundred", 9600),
          ("onefifteentwo", 115200),
          ("thirtyeigthfour", 38400),
          ("twelvehundred", 1200),
          ("twentyfourhundred", 2400))
    )


_WanModemSpeed_Type.__name__ = "Integer32"
_WanModemSpeed_Object = MibTableColumn
wanModemSpeed = _WanModemSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 15),
    _WanModemSpeed_Type()
)
wanModemSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanModemSpeed.setStatus("mandatory")


class _WanModemInitializationString_Type(DisplayString):
    """Custom type wanModemInitializationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 59),
    )


_WanModemInitializationString_Type.__name__ = "DisplayString"
_WanModemInitializationString_Object = MibTableColumn
wanModemInitializationString = _WanModemInitializationString_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 16),
    _WanModemInitializationString_Type()
)
wanModemInitializationString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanModemInitializationString.setStatus("mandatory")


class _WanModemDialPrefix_Type(DisplayString):
    """Custom type wanModemDialPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_WanModemDialPrefix_Type.__name__ = "DisplayString"
_WanModemDialPrefix_Object = MibTableColumn
wanModemDialPrefix = _WanModemDialPrefix_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 17),
    _WanModemDialPrefix_Type()
)
wanModemDialPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanModemDialPrefix.setStatus("mandatory")


class _WanPortType_Type(Integer32):
    """Custom type wanPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("pcmcia", 1),
          ("rs232", 2),
          ("v35", 4))
    )


_WanPortType_Type.__name__ = "Integer32"
_WanPortType_Object = MibTableColumn
wanPortType = _WanPortType_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 18),
    _WanPortType_Type()
)
wanPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPortType.setStatus("mandatory")


class _WanPCMCIACardName_Type(DisplayString):
    """Custom type wanPCMCIACardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_WanPCMCIACardName_Type.__name__ = "DisplayString"
_WanPCMCIACardName_Object = MibTableColumn
wanPCMCIACardName = _WanPCMCIACardName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 19),
    _WanPCMCIACardName_Type()
)
wanPCMCIACardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPCMCIACardName.setStatus("mandatory")


class _WanIpRipReceiveAdvertisementFlag_Type(Integer32):
    """Custom type wanIpRipReceiveAdvertisementFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_WanIpRipReceiveAdvertisementFlag_Type.__name__ = "Integer32"
_WanIpRipReceiveAdvertisementFlag_Object = MibTableColumn
wanIpRipReceiveAdvertisementFlag = _WanIpRipReceiveAdvertisementFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 20),
    _WanIpRipReceiveAdvertisementFlag_Type()
)
wanIpRipReceiveAdvertisementFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanIpRipReceiveAdvertisementFlag.setStatus("mandatory")


class _WanIpRipSendInterval_Type(Integer32):
    """Custom type wanIpRipSendInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WanIpRipSendInterval_Type.__name__ = "Integer32"
_WanIpRipSendInterval_Object = MibTableColumn
wanIpRipSendInterval = _WanIpRipSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 21),
    _WanIpRipSendInterval_Type()
)
wanIpRipSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanIpRipSendInterval.setStatus("mandatory")


class _WanIpxRipReceiveBroadcastFlag_Type(Integer32):
    """Custom type wanIpxRipReceiveBroadcastFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_WanIpxRipReceiveBroadcastFlag_Type.__name__ = "Integer32"
_WanIpxRipReceiveBroadcastFlag_Object = MibTableColumn
wanIpxRipReceiveBroadcastFlag = _WanIpxRipReceiveBroadcastFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 22),
    _WanIpxRipReceiveBroadcastFlag_Type()
)
wanIpxRipReceiveBroadcastFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanIpxRipReceiveBroadcastFlag.setStatus("mandatory")


class _WanIpxRipSendInterval_Type(Integer32):
    """Custom type wanIpxRipSendInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WanIpxRipSendInterval_Type.__name__ = "Integer32"
_WanIpxRipSendInterval_Object = MibTableColumn
wanIpxRipSendInterval = _WanIpxRipSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 23),
    _WanIpxRipSendInterval_Type()
)
wanIpxRipSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanIpxRipSendInterval.setStatus("mandatory")


class _WanIpxSapReceiveAdvertisementFlag_Type(Integer32):
    """Custom type wanIpxSapReceiveAdvertisementFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_WanIpxSapReceiveAdvertisementFlag_Type.__name__ = "Integer32"
_WanIpxSapReceiveAdvertisementFlag_Object = MibTableColumn
wanIpxSapReceiveAdvertisementFlag = _WanIpxSapReceiveAdvertisementFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 24),
    _WanIpxSapReceiveAdvertisementFlag_Type()
)
wanIpxSapReceiveAdvertisementFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanIpxSapReceiveAdvertisementFlag.setStatus("mandatory")


class _WanIpxSapSendInterval_Type(Integer32):
    """Custom type wanIpxSapSendInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WanIpxSapSendInterval_Type.__name__ = "Integer32"
_WanIpxSapSendInterval_Object = MibTableColumn
wanIpxSapSendInterval = _WanIpxSapSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 25),
    _WanIpxSapSendInterval_Type()
)
wanIpxSapSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanIpxSapSendInterval.setStatus("mandatory")


class _WanIpxNetbios_Type(Integer32):
    """Custom type wanIpxNetbios based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_WanIpxNetbios_Type.__name__ = "Integer32"
_WanIpxNetbios_Object = MibTableColumn
wanIpxNetbios = _WanIpxNetbios_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 26),
    _WanIpxNetbios_Type()
)
wanIpxNetbios.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanIpxNetbios.setStatus("mandatory")


class _WanISDNSwitchType_Type(Integer32):
    """Custom type wanISDNSwitchType based on Integer32"""
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("btnr", 4),
          ("cornet", 19),
          ("dass2", 5),
          ("dms100", 8),
          ("dss1", 2),
          ("ess4", 6),
          ("ess5", 7),
          ("etsi", 3),
          ("ins64", 17),
          ("itr6", 18),
          ("kdd", 16),
          ("leased64s", 24),
          ("leasedE1", 29),
          ("leasedH0", 27),
          ("leasedS01", 25),
          ("leasedS02", 26),
          ("leasedT1", 28),
          ("ni1", 9),
          ("ni2", 10),
          ("ni3", 11),
          ("other", 1),
          ("tad2", 20),
          ("tad30", 21),
          ("ts013", 22),
          ("ts014", 23),
          ("vn2", 12),
          ("vn3", 13),
          ("vn4", 14),
          ("vn6", 15))
    )


_WanISDNSwitchType_Type.__name__ = "Integer32"
_WanISDNSwitchType_Object = MibTableColumn
wanISDNSwitchType = _WanISDNSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 27),
    _WanISDNSwitchType_Type()
)
wanISDNSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanISDNSwitchType.setStatus("mandatory")


class _WanISDNCallingPhoneNoB1_Type(DisplayString):
    """Custom type wanISDNCallingPhoneNoB1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WanISDNCallingPhoneNoB1_Type.__name__ = "DisplayString"
_WanISDNCallingPhoneNoB1_Object = MibTableColumn
wanISDNCallingPhoneNoB1 = _WanISDNCallingPhoneNoB1_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 28),
    _WanISDNCallingPhoneNoB1_Type()
)
wanISDNCallingPhoneNoB1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanISDNCallingPhoneNoB1.setStatus("mandatory")


class _WanISDNCallingPhoneNoB2_Type(DisplayString):
    """Custom type wanISDNCallingPhoneNoB2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WanISDNCallingPhoneNoB2_Type.__name__ = "DisplayString"
_WanISDNCallingPhoneNoB2_Object = MibTableColumn
wanISDNCallingPhoneNoB2 = _WanISDNCallingPhoneNoB2_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 29),
    _WanISDNCallingPhoneNoB2_Type()
)
wanISDNCallingPhoneNoB2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanISDNCallingPhoneNoB2.setStatus("mandatory")


class _WanISDNSPID1_Type(DisplayString):
    """Custom type wanISDNSPID1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WanISDNSPID1_Type.__name__ = "DisplayString"
_WanISDNSPID1_Object = MibTableColumn
wanISDNSPID1 = _WanISDNSPID1_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 30),
    _WanISDNSPID1_Type()
)
wanISDNSPID1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanISDNSPID1.setStatus("mandatory")


class _WanISDNSPID2_Type(DisplayString):
    """Custom type wanISDNSPID2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WanISDNSPID2_Type.__name__ = "DisplayString"
_WanISDNSPID2_Object = MibTableColumn
wanISDNSPID2 = _WanISDNSPID2_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 31),
    _WanISDNSPID2_Type()
)
wanISDNSPID2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanISDNSPID2.setStatus("mandatory")


class _WanPortGroup_Type(Integer32):
    """Custom type wanPortGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("group", 1),
          ("non-group", 2))
    )


_WanPortGroup_Type.__name__ = "Integer32"
_WanPortGroup_Object = MibTableColumn
wanPortGroup = _WanPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 32),
    _WanPortGroup_Type()
)
wanPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanPortGroup.setStatus("mandatory")


class _WanISDNSubAddress1_Type(DisplayString):
    """Custom type wanISDNSubAddress1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WanISDNSubAddress1_Type.__name__ = "DisplayString"
_WanISDNSubAddress1_Object = MibTableColumn
wanISDNSubAddress1 = _WanISDNSubAddress1_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 33),
    _WanISDNSubAddress1_Type()
)
wanISDNSubAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanISDNSubAddress1.setStatus("mandatory")


class _WanISDNSubAddress2_Type(DisplayString):
    """Custom type wanISDNSubAddress2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WanISDNSubAddress2_Type.__name__ = "DisplayString"
_WanISDNSubAddress2_Object = MibTableColumn
wanISDNSubAddress2 = _WanISDNSubAddress2_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 34),
    _WanISDNSubAddress2_Type()
)
wanISDNSubAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanISDNSubAddress2.setStatus("mandatory")


class _WanISDNNTTCard_Type(Integer32):
    """Custom type wanISDNNTTCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_WanISDNNTTCard_Type.__name__ = "Integer32"
_WanISDNNTTCard_Object = MibTableColumn
wanISDNNTTCard = _WanISDNNTTCard_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 35),
    _WanISDNNTTCard_Type()
)
wanISDNNTTCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanISDNNTTCard.setStatus("mandatory")


class _WanISDNChannels_Type(Integer32):
    """Custom type wanISDNChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneb", 1),
          ("twob", 2))
    )


_WanISDNChannels_Type.__name__ = "Integer32"
_WanISDNChannels_Object = MibTableColumn
wanISDNChannels = _WanISDNChannels_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 36),
    _WanISDNChannels_Type()
)
wanISDNChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanISDNChannels.setStatus("mandatory")


class _WanEnableDataCompression_Type(Integer32):
    """Custom type wanEnableDataCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_WanEnableDataCompression_Type.__name__ = "Integer32"
_WanEnableDataCompression_Object = MibTableColumn
wanEnableDataCompression = _WanEnableDataCompression_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 37),
    _WanEnableDataCompression_Type()
)
wanEnableDataCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanEnableDataCompression.setStatus("mandatory")


class _WanISDNChannelSpeed_Type(Integer32):
    """Custom type wanISDNChannelSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cs56", 1),
          ("cs64", 2))
    )


_WanISDNChannelSpeed_Type.__name__ = "Integer32"
_WanISDNChannelSpeed_Object = MibTableColumn
wanISDNChannelSpeed = _WanISDNChannelSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 38),
    _WanISDNChannelSpeed_Type()
)
wanISDNChannelSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanISDNChannelSpeed.setStatus("mandatory")


class _WanUsageMode_Type(Integer32):
    """Custom type wanUsageMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modempool", 2),
          ("routing", 1),
          ("share", 3))
    )


_WanUsageMode_Type.__name__ = "Integer32"
_WanUsageMode_Object = MibTableColumn
wanUsageMode = _WanUsageMode_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 39),
    _WanUsageMode_Type()
)
wanUsageMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanUsageMode.setStatus("mandatory")


class _WanModemPoolGSN_Type(DisplayString):
    """Custom type wanModemPoolGSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_WanModemPoolGSN_Type.__name__ = "DisplayString"
_WanModemPoolGSN_Object = MibTableColumn
wanModemPoolGSN = _WanModemPoolGSN_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 40),
    _WanModemPoolGSN_Type()
)
wanModemPoolGSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanModemPoolGSN.setStatus("mandatory")


class _WanModemPoolSSN_Type(DisplayString):
    """Custom type wanModemPoolSSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_WanModemPoolSSN_Type.__name__ = "DisplayString"
_WanModemPoolSSN_Object = MibTableColumn
wanModemPoolSSN = _WanModemPoolSSN_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 1, 2, 41),
    _WanModemPoolSSN_Type()
)
wanModemPoolSSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanModemPoolSSN.setStatus("mandatory")
_WanIPAddressTable_Object = MibTable
wanIPAddressTable = _WanIPAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 2)
)
if mibBuilder.loadTexts:
    wanIPAddressTable.setStatus("mandatory")
_WanIPAddressEntry_Object = MibTableRow
wanIPAddressEntry = _WanIPAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 2, 1)
)
wanIPAddressEntry.setIndexNames(
    (0, "SBE-MIB", "wanIPAddress"),
)
if mibBuilder.loadTexts:
    wanIPAddressEntry.setStatus("mandatory")


class _WanIPAddressStatus_Type(Integer32):
    """Custom type wanIPAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("create-request", 2),
          ("invalid", 4),
          ("modify", 5),
          ("under-creation", 3),
          ("valid", 1))
    )


_WanIPAddressStatus_Type.__name__ = "Integer32"
_WanIPAddressStatus_Object = MibTableColumn
wanIPAddressStatus = _WanIPAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 2, 1, 1),
    _WanIPAddressStatus_Type()
)
wanIPAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanIPAddressStatus.setStatus("mandatory")
_WanIPAddress_Type = IpAddress
_WanIPAddress_Object = MibTableColumn
wanIPAddress = _WanIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 2, 1, 2),
    _WanIPAddress_Type()
)
wanIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIPAddress.setStatus("mandatory")
_WanStatPortTable_Object = MibTable
wanStatPortTable = _WanStatPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3)
)
if mibBuilder.loadTexts:
    wanStatPortTable.setStatus("mandatory")
_WanStatPortEntry_Object = MibTableRow
wanStatPortEntry = _WanStatPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1)
)
wanStatPortEntry.setIndexNames(
    (0, "SBE-MIB", "wanStatPortNumber"),
)
if mibBuilder.loadTexts:
    wanStatPortEntry.setStatus("mandatory")


class _WanStatPortEntryStatus_Type(Integer32):
    """Custom type wanStatPortEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("create-request", 2),
          ("invalid", 4),
          ("modify", 5),
          ("under-creation", 3),
          ("valid", 1))
    )


_WanStatPortEntryStatus_Type.__name__ = "Integer32"
_WanStatPortEntryStatus_Object = MibTableColumn
wanStatPortEntryStatus = _WanStatPortEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 1),
    _WanStatPortEntryStatus_Type()
)
wanStatPortEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanStatPortEntryStatus.setStatus("mandatory")


class _WanStatPortNumber_Type(Integer32):
    """Custom type wanStatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_WanStatPortNumber_Type.__name__ = "Integer32"
_WanStatPortNumber_Object = MibTableColumn
wanStatPortNumber = _WanStatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 2),
    _WanStatPortNumber_Type()
)
wanStatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanStatPortNumber.setStatus("mandatory")


class _WanStatPortState_Type(Integer32):
    """Custom type wanStatPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("disconnected", 1))
    )


_WanStatPortState_Type.__name__ = "Integer32"
_WanStatPortState_Object = MibTableColumn
wanStatPortState = _WanStatPortState_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 3),
    _WanStatPortState_Type()
)
wanStatPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanStatPortState.setStatus("mandatory")


class _WanStatPortUserName_Type(DisplayString):
    """Custom type wanStatPortUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WanStatPortUserName_Type.__name__ = "DisplayString"
_WanStatPortUserName_Object = MibTableColumn
wanStatPortUserName = _WanStatPortUserName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 4),
    _WanStatPortUserName_Type()
)
wanStatPortUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanStatPortUserName.setStatus("mandatory")
_WanStatPortFrameTransmitted_Type = Integer32
_WanStatPortFrameTransmitted_Object = MibTableColumn
wanStatPortFrameTransmitted = _WanStatPortFrameTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 5),
    _WanStatPortFrameTransmitted_Type()
)
wanStatPortFrameTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanStatPortFrameTransmitted.setStatus("mandatory")
_WanStatPortFrameReceived_Type = Integer32
_WanStatPortFrameReceived_Object = MibTableColumn
wanStatPortFrameReceived = _WanStatPortFrameReceived_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 6),
    _WanStatPortFrameReceived_Type()
)
wanStatPortFrameReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanStatPortFrameReceived.setStatus("mandatory")
_WanStatPortTransmitError_Type = Integer32
_WanStatPortTransmitError_Object = MibTableColumn
wanStatPortTransmitError = _WanStatPortTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 7),
    _WanStatPortTransmitError_Type()
)
wanStatPortTransmitError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanStatPortTransmitError.setStatus("mandatory")
_WanStatPortReceiveError_Type = Integer32
_WanStatPortReceiveError_Object = MibTableColumn
wanStatPortReceiveError = _WanStatPortReceiveError_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 8),
    _WanStatPortReceiveError_Type()
)
wanStatPortReceiveError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanStatPortReceiveError.setStatus("mandatory")
_WanStatPortTransmitQueueFull_Type = Integer32
_WanStatPortTransmitQueueFull_Object = MibTableColumn
wanStatPortTransmitQueueFull = _WanStatPortTransmitQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 9),
    _WanStatPortTransmitQueueFull_Type()
)
wanStatPortTransmitQueueFull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanStatPortTransmitQueueFull.setStatus("mandatory")
_WanStatPortCallOriginated_Type = Integer32
_WanStatPortCallOriginated_Object = MibTableColumn
wanStatPortCallOriginated = _WanStatPortCallOriginated_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 10),
    _WanStatPortCallOriginated_Type()
)
wanStatPortCallOriginated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanStatPortCallOriginated.setStatus("mandatory")
_WanStatPortCallAnswered_Type = Integer32
_WanStatPortCallAnswered_Object = MibTableColumn
wanStatPortCallAnswered = _WanStatPortCallAnswered_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 11),
    _WanStatPortCallAnswered_Type()
)
wanStatPortCallAnswered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanStatPortCallAnswered.setStatus("mandatory")
_WanStatPortNoDialTone_Type = Integer32
_WanStatPortNoDialTone_Object = MibTableColumn
wanStatPortNoDialTone = _WanStatPortNoDialTone_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 12),
    _WanStatPortNoDialTone_Type()
)
wanStatPortNoDialTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanStatPortNoDialTone.setStatus("mandatory")
_WanStatPortNoAnswer_Type = Integer32
_WanStatPortNoAnswer_Object = MibTableColumn
wanStatPortNoAnswer = _WanStatPortNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 13),
    _WanStatPortNoAnswer_Type()
)
wanStatPortNoAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanStatPortNoAnswer.setStatus("mandatory")
_WanStatPortBusyDetected_Type = Integer32
_WanStatPortBusyDetected_Object = MibTableColumn
wanStatPortBusyDetected = _WanStatPortBusyDetected_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 14),
    _WanStatPortBusyDetected_Type()
)
wanStatPortBusyDetected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanStatPortBusyDetected.setStatus("mandatory")
_WanStatPortNoCarrier_Type = Integer32
_WanStatPortNoCarrier_Object = MibTableColumn
wanStatPortNoCarrier = _WanStatPortNoCarrier_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 15),
    _WanStatPortNoCarrier_Type()
)
wanStatPortNoCarrier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanStatPortNoCarrier.setStatus("mandatory")
_WanStatPortModemSignal_Type = Integer32
_WanStatPortModemSignal_Object = MibTableColumn
wanStatPortModemSignal = _WanStatPortModemSignal_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 16),
    _WanStatPortModemSignal_Type()
)
wanStatPortModemSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanStatPortModemSignal.setStatus("mandatory")


class _WanStatPortConnDirection_Type(Integer32):
    """Custom type wanStatPortConnDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 3),
          ("dialin", 1),
          ("dialout", 2))
    )


_WanStatPortConnDirection_Type.__name__ = "Integer32"
_WanStatPortConnDirection_Object = MibTableColumn
wanStatPortConnDirection = _WanStatPortConnDirection_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 17),
    _WanStatPortConnDirection_Type()
)
wanStatPortConnDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanStatPortConnDirection.setStatus("mandatory")
_WanStatPortProtoUp_Type = Integer32
_WanStatPortProtoUp_Object = MibTableColumn
wanStatPortProtoUp = _WanStatPortProtoUp_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 3, 1, 18),
    _WanStatPortProtoUp_Type()
)
wanStatPortProtoUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanStatPortProtoUp.setStatus("mandatory")
_WanIPAddressMaxEntry_Type = Integer32
_WanIPAddressMaxEntry_Object = MibScalar
wanIPAddressMaxEntry = _WanIPAddressMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 5, 4),
    _WanIPAddressMaxEntry_Type()
)
wanIPAddressMaxEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIPAddressMaxEntry.setStatus("mandatory")
_Destination_ObjectIdentity = ObjectIdentity
destination = _Destination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6)
)
_DestTable_Object = MibTable
destTable = _DestTable_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1)
)
if mibBuilder.loadTexts:
    destTable.setStatus("mandatory")
_DestEntry_Object = MibTableRow
destEntry = _DestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1)
)
destEntry.setIndexNames(
    (0, "SBE-MIB", "destName"),
)
if mibBuilder.loadTexts:
    destEntry.setStatus("mandatory")


class _DestStatus_Type(Integer32):
    """Custom type destStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("create-request", 2),
          ("invalid", 4),
          ("modify", 5),
          ("under-creation", 3),
          ("valid", 1))
    )


_DestStatus_Type.__name__ = "Integer32"
_DestStatus_Object = MibTableColumn
destStatus = _DestStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 1),
    _DestStatus_Type()
)
destStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destStatus.setStatus("mandatory")


class _DestName_Type(DisplayString):
    """Custom type destName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DestName_Type.__name__ = "DisplayString"
_DestName_Object = MibTableColumn
destName = _DestName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 2),
    _DestName_Type()
)
destName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destName.setStatus("mandatory")


class _DestType_Type(Integer32):
    """Custom type destType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("lan-to-lan", 1)
    )


_DestType_Type.__name__ = "Integer32"
_DestType_Object = MibTableColumn
destType = _DestType_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 3),
    _DestType_Type()
)
destType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destType.setStatus("mandatory")


class _DestDialoutPhoneNumber_Type(DisplayString):
    """Custom type destDialoutPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DestDialoutPhoneNumber_Type.__name__ = "DisplayString"
_DestDialoutPhoneNumber_Object = MibTableColumn
destDialoutPhoneNumber = _DestDialoutPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 4),
    _DestDialoutPhoneNumber_Type()
)
destDialoutPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destDialoutPhoneNumber.setStatus("mandatory")


class _DestDialoutProtoSupport_Type(Integer32):
    """Custom type destDialoutProtoSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DestDialoutProtoSupport_Type.__name__ = "Integer32"
_DestDialoutProtoSupport_Object = MibTableColumn
destDialoutProtoSupport = _DestDialoutProtoSupport_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 5),
    _DestDialoutProtoSupport_Type()
)
destDialoutProtoSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destDialoutProtoSupport.setStatus("mandatory")


class _DestDialoutIpxSupport_Type(Integer32):
    """Custom type destDialoutIpxSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DestDialoutIpxSupport_Type.__name__ = "Integer32"
_DestDialoutIpxSupport_Object = MibTableColumn
destDialoutIpxSupport = _DestDialoutIpxSupport_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 6),
    _DestDialoutIpxSupport_Type()
)
destDialoutIpxSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destDialoutIpxSupport.setStatus("mandatory")


class _DestDialoutModemSpeed_Type(Integer32):
    """Custom type destDialoutModemSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1200,
              2400,
              4800,
              9600,
              19200,
              38400,
              57600,
              115200)
        )
    )
    namedValues = NamedValues(
        *(("fiftysevensix", 57600),
          ("fortyeighthundred", 4800),
          ("nineteentwelve", 19200),
          ("ninetysixhundred", 9600),
          ("onefifteentwo", 115200),
          ("thirtyeigthfour", 38400),
          ("twelvehundred", 1200),
          ("twentyfourhundred", 2400))
    )


_DestDialoutModemSpeed_Type.__name__ = "Integer32"
_DestDialoutModemSpeed_Object = MibTableColumn
destDialoutModemSpeed = _DestDialoutModemSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 7),
    _DestDialoutModemSpeed_Type()
)
destDialoutModemSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destDialoutModemSpeed.setStatus("mandatory")


class _DestPppMtuMru_Type(Integer32):
    """Custom type destPppMtuMru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_DestPppMtuMru_Type.__name__ = "Integer32"
_DestPppMtuMru_Object = MibTableColumn
destPppMtuMru = _DestPppMtuMru_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 8),
    _DestPppMtuMru_Type()
)
destPppMtuMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destPppMtuMru.setStatus("mandatory")


class _DestDialoutHandshake_Type(Integer32):
    """Custom type destDialoutHandshake based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 3),
          ("none", 1),
          ("pap", 2))
    )


_DestDialoutHandshake_Type.__name__ = "Integer32"
_DestDialoutHandshake_Object = MibTableColumn
destDialoutHandshake = _DestDialoutHandshake_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 9),
    _DestDialoutHandshake_Type()
)
destDialoutHandshake.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destDialoutHandshake.setStatus("mandatory")


class _DestDialoutUserName_Type(DisplayString):
    """Custom type destDialoutUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DestDialoutUserName_Type.__name__ = "DisplayString"
_DestDialoutUserName_Object = MibTableColumn
destDialoutUserName = _DestDialoutUserName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 10),
    _DestDialoutUserName_Type()
)
destDialoutUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destDialoutUserName.setStatus("mandatory")


class _DestDialoutPassword_Type(DisplayString):
    """Custom type destDialoutPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DestDialoutPassword_Type.__name__ = "DisplayString"
_DestDialoutPassword_Object = MibTableColumn
destDialoutPassword = _DestDialoutPassword_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 11),
    _DestDialoutPassword_Type()
)
destDialoutPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destDialoutPassword.setStatus("mandatory")


class _DestPorts_Type(Integer32):
    """Custom type destPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_DestPorts_Type.__name__ = "Integer32"
_DestPorts_Object = MibTableColumn
destPorts = _DestPorts_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 12),
    _DestPorts_Type()
)
destPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destPorts.setStatus("mandatory")


class _DestMaximumDialoutConnectTime_Type(Integer32):
    """Custom type destMaximumDialoutConnectTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DestMaximumDialoutConnectTime_Type.__name__ = "Integer32"
_DestMaximumDialoutConnectTime_Object = MibTableColumn
destMaximumDialoutConnectTime = _DestMaximumDialoutConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 13),
    _DestMaximumDialoutConnectTime_Type()
)
destMaximumDialoutConnectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destMaximumDialoutConnectTime.setStatus("mandatory")


class _DestDialoutStatus_Type(Integer32):
    """Custom type destDialoutStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("connected", 3),
          ("connection-failed", 4),
          ("dialing", 2),
          ("disconnected", 5),
          ("none", 1))
    )


_DestDialoutStatus_Type.__name__ = "Integer32"
_DestDialoutStatus_Object = MibTableColumn
destDialoutStatus = _DestDialoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 14),
    _DestDialoutStatus_Type()
)
destDialoutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destDialoutStatus.setStatus("mandatory")


class _DestDialoutSchedule_Type(OctetString):
    """Custom type destDialoutSchedule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(96, 96),
    )


_DestDialoutSchedule_Type.__name__ = "OctetString"
_DestDialoutSchedule_Object = MibTableColumn
destDialoutSchedule = _DestDialoutSchedule_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 15),
    _DestDialoutSchedule_Type()
)
destDialoutSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destDialoutSchedule.setStatus("mandatory")


class _DestHolidaySchedule_Type(Integer32):
    """Custom type destHolidaySchedule based on Integer32"""
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
        *(("friday", 8),
          ("monday", 4),
          ("nodialout", 2),
          ("normal", 1),
          ("saturday", 9),
          ("sunday", 3),
          ("thursday", 7),
          ("tuesday", 5),
          ("wednesday", 6))
    )


_DestHolidaySchedule_Type.__name__ = "Integer32"
_DestHolidaySchedule_Object = MibTableColumn
destHolidaySchedule = _DestHolidaySchedule_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 16),
    _DestHolidaySchedule_Type()
)
destHolidaySchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destHolidaySchedule.setStatus("mandatory")


class _DestLinkLayerNRZFlag_Type(Integer32):
    """Custom type destLinkLayerNRZFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 1),
          ("nrzi", 2))
    )


_DestLinkLayerNRZFlag_Type.__name__ = "Integer32"
_DestLinkLayerNRZFlag_Object = MibTableColumn
destLinkLayerNRZFlag = _DestLinkLayerNRZFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 17),
    _DestLinkLayerNRZFlag_Type()
)
destLinkLayerNRZFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destLinkLayerNRZFlag.setStatus("mandatory")


class _DestLinkLayerProtocolType_Type(Integer32):
    """Custom type destLinkLayerProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("framerelaydce", 6),
          ("framerelaydte", 5),
          ("isdn", 3),
          ("none", 1),
          ("ppp", 2),
          ("x25", 4))
    )


_DestLinkLayerProtocolType_Type.__name__ = "Integer32"
_DestLinkLayerProtocolType_Object = MibTableColumn
destLinkLayerProtocolType = _DestLinkLayerProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 18),
    _DestLinkLayerProtocolType_Type()
)
destLinkLayerProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destLinkLayerProtocolType.setStatus("mandatory")


class _DestLinkDialupFlag_Type(Integer32):
    """Custom type destLinkDialupFlag based on Integer32"""
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
        *(("dedicated", 2),
          ("dialup", 1),
          ("dtr-dial", 3),
          ("isdn-dialup", 4))
    )


_DestLinkDialupFlag_Type.__name__ = "Integer32"
_DestLinkDialupFlag_Object = MibTableColumn
destLinkDialupFlag = _DestLinkDialupFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 19),
    _DestLinkDialupFlag_Type()
)
destLinkDialupFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destLinkDialupFlag.setStatus("mandatory")


class _DestPortType_Type(Integer32):
    """Custom type destPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("pcmcia", 1),
          ("rs232", 2),
          ("v35", 4))
    )


_DestPortType_Type.__name__ = "Integer32"
_DestPortType_Object = MibTableColumn
destPortType = _DestPortType_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 20),
    _DestPortType_Type()
)
destPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destPortType.setStatus("mandatory")


class _DestLinkLayerType_Type(Integer32):
    """Custom type destLinkLayerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("async", 1),
          ("autosync", 3),
          ("sync", 2))
    )


_DestLinkLayerType_Type.__name__ = "Integer32"
_DestLinkLayerType_Object = MibTableColumn
destLinkLayerType = _DestLinkLayerType_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 21),
    _DestLinkLayerType_Type()
)
destLinkLayerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destLinkLayerType.setStatus("mandatory")


class _DestDialoutStatusData_Type(OctetString):
    """Custom type destDialoutStatusData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DestDialoutStatusData_Type.__name__ = "OctetString"
_DestDialoutStatusData_Object = MibTableColumn
destDialoutStatusData = _DestDialoutStatusData_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 22),
    _DestDialoutStatusData_Type()
)
destDialoutStatusData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destDialoutStatusData.setStatus("mandatory")


class _DestDialoutScheduleFlag_Type(Integer32):
    """Custom type destDialoutScheduleFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_DestDialoutScheduleFlag_Type.__name__ = "Integer32"
_DestDialoutScheduleFlag_Object = MibTableColumn
destDialoutScheduleFlag = _DestDialoutScheduleFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 23),
    _DestDialoutScheduleFlag_Type()
)
destDialoutScheduleFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destDialoutScheduleFlag.setStatus("mandatory")


class _DestDialinUserName_Type(DisplayString):
    """Custom type destDialinUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DestDialinUserName_Type.__name__ = "DisplayString"
_DestDialinUserName_Object = MibTableColumn
destDialinUserName = _DestDialinUserName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 24),
    _DestDialinUserName_Type()
)
destDialinUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destDialinUserName.setStatus("mandatory")


class _DestDialinPassword_Type(DisplayString):
    """Custom type destDialinPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DestDialinPassword_Type.__name__ = "DisplayString"
_DestDialinPassword_Object = MibTableColumn
destDialinPassword = _DestDialinPassword_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 25),
    _DestDialinPassword_Type()
)
destDialinPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destDialinPassword.setStatus("mandatory")


class _DestMaximumDialinConnectTime_Type(Integer32):
    """Custom type destMaximumDialinConnectTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DestMaximumDialinConnectTime_Type.__name__ = "Integer32"
_DestMaximumDialinConnectTime_Object = MibTableColumn
destMaximumDialinConnectTime = _DestMaximumDialinConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 26),
    _DestMaximumDialinConnectTime_Type()
)
destMaximumDialinConnectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destMaximumDialinConnectTime.setStatus("mandatory")


class _DestTSDFlag_Type(Integer32):
    """Custom type destTSDFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-tsd", 2),
          ("tsd", 1))
    )


_DestTSDFlag_Type.__name__ = "Integer32"
_DestTSDFlag_Object = MibTableColumn
destTSDFlag = _DestTSDFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 27),
    _DestTSDFlag_Type()
)
destTSDFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destTSDFlag.setStatus("mandatory")


class _DestTSDInactivityTime_Type(Integer32):
    """Custom type destTSDInactivityTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DestTSDInactivityTime_Type.__name__ = "Integer32"
_DestTSDInactivityTime_Object = MibTableColumn
destTSDInactivityTime = _DestTSDInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 28),
    _DestTSDInactivityTime_Type()
)
destTSDInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destTSDInactivityTime.setStatus("mandatory")


class _DestTSDMaxDownTime_Type(Integer32):
    """Custom type destTSDMaxDownTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DestTSDMaxDownTime_Type.__name__ = "Integer32"
_DestTSDMaxDownTime_Object = MibTableColumn
destTSDMaxDownTime = _DestTSDMaxDownTime_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 29),
    _DestTSDMaxDownTime_Type()
)
destTSDMaxDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destTSDMaxDownTime.setStatus("mandatory")


class _DestTSDPortGroup_Type(Integer32):
    """Custom type destTSDPortGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_DestTSDPortGroup_Type.__name__ = "Integer32"
_DestTSDPortGroup_Object = MibTableColumn
destTSDPortGroup = _DestTSDPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 30),
    _DestTSDPortGroup_Type()
)
destTSDPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destTSDPortGroup.setStatus("mandatory")


class _DestManualDialCallback_Type(Integer32):
    """Custom type destManualDialCallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DestManualDialCallback_Type.__name__ = "Integer32"
_DestManualDialCallback_Object = MibTableColumn
destManualDialCallback = _DestManualDialCallback_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 31),
    _DestManualDialCallback_Type()
)
destManualDialCallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destManualDialCallback.setStatus("mandatory")


class _DestAllowDynamicIPAddr_Type(Integer32):
    """Custom type destAllowDynamicIPAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DestAllowDynamicIPAddr_Type.__name__ = "Integer32"
_DestAllowDynamicIPAddr_Object = MibTableColumn
destAllowDynamicIPAddr = _DestAllowDynamicIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 32),
    _DestAllowDynamicIPAddr_Type()
)
destAllowDynamicIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destAllowDynamicIPAddr.setStatus("mandatory")


class _DestISDNChannels_Type(Integer32):
    """Custom type destISDNChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneb", 1),
          ("twob", 2))
    )


_DestISDNChannels_Type.__name__ = "Integer32"
_DestISDNChannels_Object = MibTableColumn
destISDNChannels = _DestISDNChannels_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 33),
    _DestISDNChannels_Type()
)
destISDNChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destISDNChannels.setStatus("mandatory")


class _DestDialoutPhoneNumber2_Type(DisplayString):
    """Custom type destDialoutPhoneNumber2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DestDialoutPhoneNumber2_Type.__name__ = "DisplayString"
_DestDialoutPhoneNumber2_Object = MibTableColumn
destDialoutPhoneNumber2 = _DestDialoutPhoneNumber2_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 34),
    _DestDialoutPhoneNumber2_Type()
)
destDialoutPhoneNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destDialoutPhoneNumber2.setStatus("mandatory")


class _DestTSDExpectCallback_Type(Integer32):
    """Custom type destTSDExpectCallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DestTSDExpectCallback_Type.__name__ = "Integer32"
_DestTSDExpectCallback_Object = MibTableColumn
destTSDExpectCallback = _DestTSDExpectCallback_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 1, 1, 35),
    _DestTSDExpectCallback_Type()
)
destTSDExpectCallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destTSDExpectCallback.setStatus("mandatory")
_DestMaxEntry_Type = Integer32
_DestMaxEntry_Object = MibScalar
destMaxEntry = _DestMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 2),
    _DestMaxEntry_Type()
)
destMaxEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destMaxEntry.setStatus("mandatory")
_DestScriptTable_Object = MibTable
destScriptTable = _DestScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 3)
)
if mibBuilder.loadTexts:
    destScriptTable.setStatus("mandatory")
_DestScriptEntry_Object = MibTableRow
destScriptEntry = _DestScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 3, 2)
)
destScriptEntry.setIndexNames(
    (0, "SBE-MIB", "destinationName"),
)
if mibBuilder.loadTexts:
    destScriptEntry.setStatus("mandatory")


class _DestScriptEntryStatus_Type(Integer32):
    """Custom type destScriptEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("create-request", 2),
          ("invalid", 4),
          ("modify", 5),
          ("under-creation", 3),
          ("valid", 1))
    )


_DestScriptEntryStatus_Type.__name__ = "Integer32"
_DestScriptEntryStatus_Object = MibTableColumn
destScriptEntryStatus = _DestScriptEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 3, 2, 1),
    _DestScriptEntryStatus_Type()
)
destScriptEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destScriptEntryStatus.setStatus("mandatory")


class _DestinationName_Type(DisplayString):
    """Custom type destinationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DestinationName_Type.__name__ = "DisplayString"
_DestinationName_Object = MibTableColumn
destinationName = _DestinationName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 3, 2, 2),
    _DestinationName_Type()
)
destinationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destinationName.setStatus("mandatory")


class _DestScriptUseFlag_Type(Integer32):
    """Custom type destScriptUseFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_DestScriptUseFlag_Type.__name__ = "Integer32"
_DestScriptUseFlag_Object = MibTableColumn
destScriptUseFlag = _DestScriptUseFlag_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 3, 2, 3),
    _DestScriptUseFlag_Type()
)
destScriptUseFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destScriptUseFlag.setStatus("mandatory")


class _DestScriptTimeout_Type(Integer32):
    """Custom type destScriptTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DestScriptTimeout_Type.__name__ = "Integer32"
_DestScriptTimeout_Object = MibTableColumn
destScriptTimeout = _DestScriptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 3, 2, 4),
    _DestScriptTimeout_Type()
)
destScriptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destScriptTimeout.setStatus("mandatory")


class _DestScriptName_Type(DisplayString):
    """Custom type destScriptName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DestScriptName_Type.__name__ = "DisplayString"
_DestScriptName_Object = MibTableColumn
destScriptName = _DestScriptName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 3, 2, 5),
    _DestScriptName_Type()
)
destScriptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destScriptName.setStatus("mandatory")


class _DestScript_Type(DisplayString):
    """Custom type destScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DestScript_Type.__name__ = "DisplayString"
_DestScript_Object = MibTableColumn
destScript = _DestScript_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 3, 2, 6),
    _DestScript_Type()
)
destScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destScript.setStatus("mandatory")


class _DestScriptStartupCmd_Type(DisplayString):
    """Custom type destScriptStartupCmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DestScriptStartupCmd_Type.__name__ = "DisplayString"
_DestScriptStartupCmd_Object = MibTableColumn
destScriptStartupCmd = _DestScriptStartupCmd_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 6, 3, 2, 7),
    _DestScriptStartupCmd_Type()
)
destScriptStartupCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destScriptStartupCmd.setStatus("mandatory")
_User_ObjectIdentity = ObjectIdentity
user = _User_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 2, 7)
)
_UserMaxEntries_Type = Integer32
_UserMaxEntries_Object = MibScalar
userMaxEntries = _UserMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 7, 1),
    _UserMaxEntries_Type()
)
userMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userMaxEntries.setStatus("mandatory")
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 7, 2)
)
if mibBuilder.loadTexts:
    userTable.setStatus("mandatory")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 7, 2, 1)
)
userEntry.setIndexNames(
    (0, "SBE-MIB", "userName"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("mandatory")


class _UserStatus_Type(Integer32):
    """Custom type userStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("create-request", 2),
          ("invalid", 4),
          ("modify", 5),
          ("under-creation", 3),
          ("valid", 1))
    )


_UserStatus_Type.__name__ = "Integer32"
_UserStatus_Object = MibTableColumn
userStatus = _UserStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 7, 2, 1, 2),
    _UserStatus_Type()
)
userStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userStatus.setStatus("mandatory")


class _UserName_Type(DisplayString):
    """Custom type userName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UserName_Type.__name__ = "DisplayString"
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 7, 2, 1, 3),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("mandatory")


class _UserPassword_Type(DisplayString):
    """Custom type userPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UserPassword_Type.__name__ = "DisplayString"
_UserPassword_Object = MibTableColumn
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 7, 2, 1, 4),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPassword.setStatus("mandatory")


class _UserPermissions_Type(Integer32):
    """Custom type userPermissions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dial-in", 2),
          ("dial-out", 4),
          ("none", 1))
    )


_UserPermissions_Type.__name__ = "Integer32"
_UserPermissions_Object = MibTableColumn
userPermissions = _UserPermissions_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 7, 2, 1, 5),
    _UserPermissions_Type()
)
userPermissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPermissions.setStatus("mandatory")


class _UserCallbackType_Type(Integer32):
    """Custom type userCallbackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("none", 1))
    )


_UserCallbackType_Type.__name__ = "Integer32"
_UserCallbackType_Object = MibTableColumn
userCallbackType = _UserCallbackType_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 7, 2, 1, 6),
    _UserCallbackType_Type()
)
userCallbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userCallbackType.setStatus("mandatory")


class _UserPhoneNo_Type(DisplayString):
    """Custom type userPhoneNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UserPhoneNo_Type.__name__ = "DisplayString"
_UserPhoneNo_Object = MibTableColumn
userPhoneNo = _UserPhoneNo_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 7, 2, 1, 7),
    _UserPhoneNo_Type()
)
userPhoneNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPhoneNo.setStatus("mandatory")


class _UserDialInMax_Type(Integer32):
    """Custom type userDialInMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UserDialInMax_Type.__name__ = "Integer32"
_UserDialInMax_Object = MibTableColumn
userDialInMax = _UserDialInMax_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 7, 2, 1, 8),
    _UserDialInMax_Type()
)
userDialInMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userDialInMax.setStatus("mandatory")
_UserIpAddress_Type = IpAddress
_UserIpAddress_Object = MibTableColumn
userIpAddress = _UserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 7, 2, 1, 10),
    _UserIpAddress_Type()
)
userIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userIpAddress.setStatus("mandatory")
_Manager_ObjectIdentity = ObjectIdentity
manager = _Manager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 2, 8)
)


class _MgrTimeoutForMACProtocolResponses_Type(Integer32):
    """Custom type mgrTimeoutForMACProtocolResponses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_MgrTimeoutForMACProtocolResponses_Type.__name__ = "Integer32"
_MgrTimeoutForMACProtocolResponses_Object = MibScalar
mgrTimeoutForMACProtocolResponses = _MgrTimeoutForMACProtocolResponses_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 8, 1),
    _MgrTimeoutForMACProtocolResponses_Type()
)
mgrTimeoutForMACProtocolResponses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgrTimeoutForMACProtocolResponses.setStatus("mandatory")


class _MgrNumberOfRetriesForMACProtocolResponses_Type(Integer32):
    """Custom type mgrNumberOfRetriesForMACProtocolResponses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MgrNumberOfRetriesForMACProtocolResponses_Type.__name__ = "Integer32"
_MgrNumberOfRetriesForMACProtocolResponses_Object = MibScalar
mgrNumberOfRetriesForMACProtocolResponses = _MgrNumberOfRetriesForMACProtocolResponses_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 8, 2),
    _MgrNumberOfRetriesForMACProtocolResponses_Type()
)
mgrNumberOfRetriesForMACProtocolResponses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgrNumberOfRetriesForMACProtocolResponses.setStatus("mandatory")


class _MgrEventPollingInterval_Type(Integer32):
    """Custom type mgrEventPollingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MgrEventPollingInterval_Type.__name__ = "Integer32"
_MgrEventPollingInterval_Object = MibScalar
mgrEventPollingInterval = _MgrEventPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 8, 3),
    _MgrEventPollingInterval_Type()
)
mgrEventPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgrEventPollingInterval.setStatus("mandatory")
_Holiday_ObjectIdentity = ObjectIdentity
holiday = _Holiday_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 2, 9)
)
_HolidayMaxEntries_Type = Integer32
_HolidayMaxEntries_Object = MibScalar
holidayMaxEntries = _HolidayMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 9, 1),
    _HolidayMaxEntries_Type()
)
holidayMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    holidayMaxEntries.setStatus("mandatory")
_HolidayTable_Object = MibTable
holidayTable = _HolidayTable_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 9, 2)
)
if mibBuilder.loadTexts:
    holidayTable.setStatus("mandatory")
_HolidayEntry_Object = MibTableRow
holidayEntry = _HolidayEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 9, 2, 1)
)
holidayEntry.setIndexNames(
    (0, "SBE-MIB", "holidayDate"),
)
if mibBuilder.loadTexts:
    holidayEntry.setStatus("mandatory")


class _HolidayStatus_Type(Integer32):
    """Custom type holidayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("create-request", 2),
          ("invalid", 4),
          ("modify", 5),
          ("under-creation", 3),
          ("valid", 1))
    )


_HolidayStatus_Type.__name__ = "Integer32"
_HolidayStatus_Object = MibTableColumn
holidayStatus = _HolidayStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 9, 2, 1, 1),
    _HolidayStatus_Type()
)
holidayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    holidayStatus.setStatus("mandatory")


class _HolidayDate_Type(DisplayString):
    """Custom type holidayDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HolidayDate_Type.__name__ = "DisplayString"
_HolidayDate_Object = MibTableColumn
holidayDate = _HolidayDate_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 9, 2, 1, 2),
    _HolidayDate_Type()
)
holidayDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    holidayDate.setStatus("mandatory")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 2, 10)
)
_SnmpCommunityNameTable_Object = MibTable
snmpCommunityNameTable = _SnmpCommunityNameTable_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 10, 1)
)
if mibBuilder.loadTexts:
    snmpCommunityNameTable.setStatus("mandatory")
_SnmpCommunityNameEntry_Object = MibTableRow
snmpCommunityNameEntry = _SnmpCommunityNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 10, 1, 1)
)
snmpCommunityNameEntry.setIndexNames(
    (0, "SBE-MIB", "snmpCommunityName"),
)
if mibBuilder.loadTexts:
    snmpCommunityNameEntry.setStatus("mandatory")


class _SnmpCommunityNameStatus_Type(Integer32):
    """Custom type snmpCommunityNameStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("create-request", 2),
          ("invalid", 4),
          ("modify", 5),
          ("under-creation", 3),
          ("valid", 1))
    )


_SnmpCommunityNameStatus_Type.__name__ = "Integer32"
_SnmpCommunityNameStatus_Object = MibTableColumn
snmpCommunityNameStatus = _SnmpCommunityNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 10, 1, 1, 1),
    _SnmpCommunityNameStatus_Type()
)
snmpCommunityNameStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityNameStatus.setStatus("mandatory")


class _SnmpCommunityName_Type(DisplayString):
    """Custom type snmpCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SnmpCommunityName_Type.__name__ = "DisplayString"
_SnmpCommunityName_Object = MibTableColumn
snmpCommunityName = _SnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 10, 1, 1, 2),
    _SnmpCommunityName_Type()
)
snmpCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommunityName.setStatus("mandatory")


class _SnmpCommunityPermission_Type(Integer32):
    """Custom type snmpCommunityPermission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lanuser", 3),
          ("readonly", 1),
          ("readwrite", 2))
    )


_SnmpCommunityPermission_Type.__name__ = "Integer32"
_SnmpCommunityPermission_Object = MibTableColumn
snmpCommunityPermission = _SnmpCommunityPermission_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 10, 1, 1, 3),
    _SnmpCommunityPermission_Type()
)
snmpCommunityPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityPermission.setStatus("mandatory")
_SnmpMacServerTable_Object = MibTable
snmpMacServerTable = _SnmpMacServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 10, 2)
)
if mibBuilder.loadTexts:
    snmpMacServerTable.setStatus("mandatory")
_SnmpMacServerEntry_Object = MibTableRow
snmpMacServerEntry = _SnmpMacServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 10, 2, 1)
)
snmpMacServerEntry.setIndexNames(
    (0, "SBE-MIB", "snmpMacServerAddress"),
)
if mibBuilder.loadTexts:
    snmpMacServerEntry.setStatus("mandatory")


class _SnmpMacServerStatus_Type(Integer32):
    """Custom type snmpMacServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("create-request", 2),
          ("invalid", 4),
          ("modify", 5),
          ("under-creation", 3),
          ("valid", 1))
    )


_SnmpMacServerStatus_Type.__name__ = "Integer32"
_SnmpMacServerStatus_Object = MibTableColumn
snmpMacServerStatus = _SnmpMacServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 10, 2, 1, 1),
    _SnmpMacServerStatus_Type()
)
snmpMacServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpMacServerStatus.setStatus("mandatory")


class _SnmpMacServerAddress_Type(OctetString):
    """Custom type snmpMacServerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_SnmpMacServerAddress_Type.__name__ = "OctetString"
_SnmpMacServerAddress_Object = MibTableColumn
snmpMacServerAddress = _SnmpMacServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 10, 2, 1, 2),
    _SnmpMacServerAddress_Type()
)
snmpMacServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpMacServerAddress.setStatus("mandatory")
_SnmpIpServerTable_Object = MibTable
snmpIpServerTable = _SnmpIpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 10, 3)
)
if mibBuilder.loadTexts:
    snmpIpServerTable.setStatus("mandatory")
_SnmpIpServerEntry_Object = MibTableRow
snmpIpServerEntry = _SnmpIpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 10, 3, 1)
)
snmpIpServerEntry.setIndexNames(
    (0, "SBE-MIB", "snmpIpServerAddress"),
)
if mibBuilder.loadTexts:
    snmpIpServerEntry.setStatus("mandatory")


class _SnmpIpServerStatus_Type(Integer32):
    """Custom type snmpIpServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("create-request", 2),
          ("invalid", 4),
          ("modify", 5),
          ("under-creation", 3),
          ("valid", 1))
    )


_SnmpIpServerStatus_Type.__name__ = "Integer32"
_SnmpIpServerStatus_Object = MibTableColumn
snmpIpServerStatus = _SnmpIpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 10, 3, 1, 1),
    _SnmpIpServerStatus_Type()
)
snmpIpServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpIpServerStatus.setStatus("mandatory")
_SnmpIpServerAddress_Type = IpAddress
_SnmpIpServerAddress_Object = MibTableColumn
snmpIpServerAddress = _SnmpIpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 10, 3, 1, 2),
    _SnmpIpServerAddress_Type()
)
snmpIpServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpIpServerAddress.setStatus("mandatory")
_SnmpCommunityNameMaxEntry_Type = Integer32
_SnmpCommunityNameMaxEntry_Object = MibScalar
snmpCommunityNameMaxEntry = _SnmpCommunityNameMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 10, 4),
    _SnmpCommunityNameMaxEntry_Type()
)
snmpCommunityNameMaxEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommunityNameMaxEntry.setStatus("mandatory")
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 2, 11)
)
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 11, 1)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("mandatory")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 11, 1, 1)
)
eventEntry.setIndexNames(
    (0, "SBE-MIB", "eventGroupIndex"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("mandatory")


class _EventGroupIndex_Type(Integer32):
    """Custom type eventGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EventGroupIndex_Type.__name__ = "Integer32"
_EventGroupIndex_Object = MibTableColumn
eventGroupIndex = _EventGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 11, 1, 1, 1),
    _EventGroupIndex_Type()
)
eventGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventGroupIndex.setStatus("mandatory")


class _EventData_Type(OctetString):
    """Custom type eventData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_EventData_Type.__name__ = "OctetString"
_EventData_Object = MibTableColumn
eventData = _EventData_Object(
    (1, 3, 6, 1, 4, 1, 1055, 2, 11, 1, 1, 2),
    _EventData_Type()
)
eventData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventData.setStatus("mandatory")
_Discovery_ObjectIdentity = ObjectIdentity
discovery = _Discovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 3)
)


class _DiscNodeName_Type(DisplayString):
    """Custom type discNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_DiscNodeName_Type.__name__ = "DisplayString"
_DiscNodeName_Object = MibScalar
discNodeName = _DiscNodeName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 3, 1),
    _DiscNodeName_Type()
)
discNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discNodeName.setStatus("mandatory")


class _DiscModel_Type(Integer32):
    """Custom type discModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              257,
              258,
              259,
              260)
        )
    )
    namedValues = NamedValues(
        *(("central", 257),
          ("routeman", 259),
          ("routemanxl", 260),
          ("soho", 256),
          ("torte", 258))
    )


_DiscModel_Type.__name__ = "Integer32"
_DiscModel_Object = MibScalar
discModel = _DiscModel_Object(
    (1, 3, 6, 1, 4, 1, 1055, 3, 2),
    _DiscModel_Type()
)
discModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discModel.setStatus("mandatory")


class _DiscProto_Type(Integer32):
    """Custom type discProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("mac", 1))
    )


_DiscProto_Type.__name__ = "Integer32"
_DiscProto_Object = MibScalar
discProto = _DiscProto_Object(
    (1, 3, 6, 1, 4, 1, 1055, 3, 3),
    _DiscProto_Type()
)
discProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discProto.setStatus("mandatory")
_FileMgmt_ObjectIdentity = ObjectIdentity
fileMgmt = _FileMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 4)
)


class _SyFMOperation_Type(Integer32):
    """Custom type syFMOperation based on Integer32"""
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
        *(("abortCopy", 8),
          ("beginCopy", 2),
          ("checkSum", 7),
          ("copyDone", 3),
          ("deleteFile", 4),
          ("getFileInfo", 9),
          ("listDir", 6),
          ("other", 1),
          ("renameFile", 5))
    )


_SyFMOperation_Type.__name__ = "Integer32"
_SyFMOperation_Object = MibScalar
syFMOperation = _SyFMOperation_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 1),
    _SyFMOperation_Type()
)
syFMOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syFMOperation.setStatus("mandatory")
_SyFMTimeStamp_Type = TimeTicks
_SyFMTimeStamp_Object = MibScalar
syFMTimeStamp = _SyFMTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 2),
    _SyFMTimeStamp_Type()
)
syFMTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syFMTimeStamp.setStatus("mandatory")


class _SyFMError_Type(Integer32):
    """Custom type syFMError based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 11),
          ("badChecksum", 9),
          ("badOperation", 10),
          ("inProgress", 3),
          ("noFile", 5),
          ("noPermission", 7),
          ("noResponse", 4),
          ("noSpace", 6),
          ("none", 1),
          ("other", 12),
          ("successful", 2),
          ("timeout", 8))
    )


_SyFMError_Type.__name__ = "Integer32"
_SyFMError_Object = MibScalar
syFMError = _SyFMError_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 3),
    _SyFMError_Type()
)
syFMError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syFMError.setStatus("mandatory")
_SyFileTransfer_ObjectIdentity = ObjectIdentity
syFileTransfer = _SyFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 4, 4)
)


class _FileTransferStatus_Type(Integer32):
    """Custom type fileTransferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inActive", 1),
          ("inProgress", 2),
          ("waitingCopy", 3))
    )


_FileTransferStatus_Type.__name__ = "Integer32"
_FileTransferStatus_Object = MibScalar
fileTransferStatus = _FileTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 4, 1),
    _FileTransferStatus_Type()
)
fileTransferStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferStatus.setStatus("mandatory")
_FileTransferStartTime_Type = TimeTicks
_FileTransferStartTime_Object = MibScalar
fileTransferStartTime = _FileTransferStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 4, 2),
    _FileTransferStartTime_Type()
)
fileTransferStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileTransferStartTime.setStatus("mandatory")


class _FileTransferFileLength_Type(OctetString):
    """Custom type fileTransferFileLength based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_FileTransferFileLength_Type.__name__ = "OctetString"
_FileTransferFileLength_Object = MibScalar
fileTransferFileLength = _FileTransferFileLength_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 4, 3),
    _FileTransferFileLength_Type()
)
fileTransferFileLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferFileLength.setStatus("mandatory")
_FileTransferCheckSum_Type = Integer32
_FileTransferCheckSum_Object = MibScalar
fileTransferCheckSum = _FileTransferCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 4, 4),
    _FileTransferCheckSum_Type()
)
fileTransferCheckSum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferCheckSum.setStatus("mandatory")


class _FileTransferDirection_Type(Integer32):
    """Custom type fileTransferDirection based on Integer32"""
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
        *(("copyingFromLX", 2),
          ("copyingToLXFlash", 4),
          ("copyingToLXRAM", 3),
          ("none", 1))
    )


_FileTransferDirection_Type.__name__ = "Integer32"
_FileTransferDirection_Object = MibScalar
fileTransferDirection = _FileTransferDirection_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 4, 5),
    _FileTransferDirection_Type()
)
fileTransferDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileTransferDirection.setStatus("mandatory")
_FileTransferLastRcvTime_Type = TimeTicks
_FileTransferLastRcvTime_Object = MibScalar
fileTransferLastRcvTime = _FileTransferLastRcvTime_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 4, 6),
    _FileTransferLastRcvTime_Type()
)
fileTransferLastRcvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileTransferLastRcvTime.setStatus("mandatory")
_FileTransferRemoteAddr_Type = MacAddress
_FileTransferRemoteAddr_Object = MibScalar
fileTransferRemoteAddr = _FileTransferRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 4, 7),
    _FileTransferRemoteAddr_Type()
)
fileTransferRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileTransferRemoteAddr.setStatus("mandatory")


class _FileTransferRemoteFileName_Type(OctetString):
    """Custom type fileTransferRemoteFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_FileTransferRemoteFileName_Type.__name__ = "OctetString"
_FileTransferRemoteFileName_Object = MibScalar
fileTransferRemoteFileName = _FileTransferRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 4, 8),
    _FileTransferRemoteFileName_Type()
)
fileTransferRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferRemoteFileName.setStatus("mandatory")


class _FileTransferLocalFileName_Type(DisplayString):
    """Custom type fileTransferLocalFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_FileTransferLocalFileName_Type.__name__ = "DisplayString"
_FileTransferLocalFileName_Object = MibScalar
fileTransferLocalFileName = _FileTransferLocalFileName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 4, 9),
    _FileTransferLocalFileName_Type()
)
fileTransferLocalFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferLocalFileName.setStatus("mandatory")


class _FileTransferData_Type(OctetString):
    """Custom type fileTransferData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(532, 532),
    )


_FileTransferData_Type.__name__ = "OctetString"
_FileTransferData_Object = MibScalar
fileTransferData = _FileTransferData_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 4, 10),
    _FileTransferData_Type()
)
fileTransferData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferData.setStatus("mandatory")
_SyFileInfo_ObjectIdentity = ObjectIdentity
syFileInfo = _SyFileInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 4, 5)
)


class _SyFileInfoVersion_Type(OctetString):
    """Custom type syFileInfoVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_SyFileInfoVersion_Type.__name__ = "OctetString"
_SyFileInfoVersion_Object = MibScalar
syFileInfoVersion = _SyFileInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 5, 1),
    _SyFileInfoVersion_Type()
)
syFileInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syFileInfoVersion.setStatus("mandatory")


class _SyFileInfoChecksum_Type(OctetString):
    """Custom type syFileInfoChecksum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SyFileInfoChecksum_Type.__name__ = "OctetString"
_SyFileInfoChecksum_Object = MibScalar
syFileInfoChecksum = _SyFileInfoChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 5, 2),
    _SyFileInfoChecksum_Type()
)
syFileInfoChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syFileInfoChecksum.setStatus("mandatory")


class _SyFileInfoLength_Type(OctetString):
    """Custom type syFileInfoLength based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SyFileInfoLength_Type.__name__ = "OctetString"
_SyFileInfoLength_Object = MibScalar
syFileInfoLength = _SyFileInfoLength_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 5, 3),
    _SyFileInfoLength_Type()
)
syFileInfoLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syFileInfoLength.setStatus("mandatory")
_SyDirTable_Object = MibTable
syDirTable = _SyDirTable_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 6)
)
if mibBuilder.loadTexts:
    syDirTable.setStatus("mandatory")
_SyDirEntry_Object = MibTableRow
syDirEntry = _SyDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 6, 1)
)
syDirEntry.setIndexNames(
    (0, "SBE-MIB", "syDirName"),
)
if mibBuilder.loadTexts:
    syDirEntry.setStatus("mandatory")


class _SyDirStatus_Type(Integer32):
    """Custom type syDirStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("create-request", 2),
          ("invalid", 4),
          ("modify", 5),
          ("under-creation", 3),
          ("valid", 1))
    )


_SyDirStatus_Type.__name__ = "Integer32"
_SyDirStatus_Object = MibTableColumn
syDirStatus = _SyDirStatus_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 6, 1, 1),
    _SyDirStatus_Type()
)
syDirStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syDirStatus.setStatus("mandatory")


class _SyDirName_Type(OctetString):
    """Custom type syDirName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_SyDirName_Type.__name__ = "OctetString"
_SyDirName_Object = MibTableColumn
syDirName = _SyDirName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 6, 1, 2),
    _SyDirName_Type()
)
syDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syDirName.setStatus("mandatory")
_SyDirCompressSize_Type = Integer32
_SyDirCompressSize_Object = MibTableColumn
syDirCompressSize = _SyDirCompressSize_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 6, 1, 3),
    _SyDirCompressSize_Type()
)
syDirCompressSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syDirCompressSize.setStatus("mandatory")


class _SyDirVersion_Type(OctetString):
    """Custom type syDirVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SyDirVersion_Type.__name__ = "OctetString"
_SyDirVersion_Object = MibTableColumn
syDirVersion = _SyDirVersion_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 6, 1, 4),
    _SyDirVersion_Type()
)
syDirVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syDirVersion.setStatus("mandatory")
_SyDirUncompressSize_Type = Integer32
_SyDirUncompressSize_Object = MibTableColumn
syDirUncompressSize = _SyDirUncompressSize_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 6, 1, 5),
    _SyDirUncompressSize_Type()
)
syDirUncompressSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syDirUncompressSize.setStatus("mandatory")


class _FileName_Type(OctetString):
    """Custom type fileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_FileName_Type.__name__ = "OctetString"
_FileName_Object = MibScalar
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 7),
    _FileName_Type()
)
fileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileName.setStatus("mandatory")


class _FileNameFrom_Type(OctetString):
    """Custom type fileNameFrom based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_FileNameFrom_Type.__name__ = "OctetString"
_FileNameFrom_Object = MibScalar
fileNameFrom = _FileNameFrom_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 8),
    _FileNameFrom_Type()
)
fileNameFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileNameFrom.setStatus("mandatory")


class _FileNameTo_Type(OctetString):
    """Custom type fileNameTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_FileNameTo_Type.__name__ = "OctetString"
_FileNameTo_Object = MibScalar
fileNameTo = _FileNameTo_Object(
    (1, 3, 6, 1, 4, 1, 1055, 4, 9),
    _FileNameTo_Type()
)
fileNameTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileNameTo.setStatus("mandatory")
_Modempool_ObjectIdentity = ObjectIdentity
modempool = _Modempool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 6)
)


class _ModempoolEnabled_Type(Integer32):
    """Custom type modempoolEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ModempoolEnabled_Type.__name__ = "Integer32"
_ModempoolEnabled_Object = MibScalar
modempoolEnabled = _ModempoolEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1055, 6, 1),
    _ModempoolEnabled_Type()
)
modempoolEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modempoolEnabled.setStatus("mandatory")


class _ModempoolNodeName_Type(DisplayString):
    """Custom type modempoolNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ModempoolNodeName_Type.__name__ = "DisplayString"
_ModempoolNodeName_Object = MibScalar
modempoolNodeName = _ModempoolNodeName_Object(
    (1, 3, 6, 1, 4, 1, 1055, 6, 2),
    _ModempoolNodeName_Type()
)
modempoolNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modempoolNodeName.setStatus("mandatory")


class _ModempoolProtoSupport_Type(Integer32):
    """Custom type modempoolProtoSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_ModempoolProtoSupport_Type.__name__ = "Integer32"
_ModempoolProtoSupport_Object = MibScalar
modempoolProtoSupport = _ModempoolProtoSupport_Object(
    (1, 3, 6, 1, 4, 1, 1055, 6, 3),
    _ModempoolProtoSupport_Type()
)
modempoolProtoSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modempoolProtoSupport.setStatus("mandatory")
_EndOfSBEMib_ObjectIdentity = ObjectIdentity
endOfSBEMib = _EndOfSBEMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1055, 65535)
)
_DummyStopperForWorkshopForGetNext_Type = Integer32
_DummyStopperForWorkshopForGetNext_Object = MibScalar
dummyStopperForWorkshopForGetNext = _DummyStopperForWorkshopForGetNext_Object(
    (1, 3, 6, 1, 4, 1, 1055, 65535, 1),
    _DummyStopperForWorkshopForGetNext_Type()
)
dummyStopperForWorkshopForGetNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dummyStopperForWorkshopForGetNext.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SBE-MIB",
    **{"sbe": sbe,
       "system": system,
       "syDateTime": syDateTime,
       "syRAMConfigurationChangedFlag": syRAMConfigurationChangedFlag,
       "syConfigurationLockFlag": syConfigurationLockFlag,
       "syModel": syModel,
       "syBootInfo": syBootInfo,
       "syActivatedLevel": syActivatedLevel,
       "sySerialNumber": sySerialNumber,
       "syBaseActivationLevel": syBaseActivationLevel,
       "router": router,
       "routsys": routsys,
       "syBootOrder": syBootOrder,
       "syMtuMru": syMtuMru,
       "syEventToLogThreshold": syEventToLogThreshold,
       "syEventToTrapThreshold": syEventToTrapThreshold,
       "syControlOperation": syControlOperation,
       "syControlVariableStringOne": syControlVariableStringOne,
       "syControlVariableIntegerOne": syControlVariableIntegerOne,
       "syDialinAuthentication": syDialinAuthentication,
       "syEventToSpeakThreshold": syEventToSpeakThreshold,
       "syNumberOfTimesToSpeak": syNumberOfTimesToSpeak,
       "sySaveRamToFlashState": sySaveRamToFlashState,
       "syDialbackRetryInterval": syDialbackRetryInterval,
       "syDialbackRetryLimit": syDialbackRetryLimit,
       "syReverseCallbackTimeout": syReverseCallbackTimeout,
       "bridge": bridge,
       "syBridgeConfiguredFlag": syBridgeConfiguredFlag,
       "syBridgeFilterFlag": syBridgeFilterFlag,
       "syBridgePriority": syBridgePriority,
       "syBridgeTable": syBridgeTable,
       "syBridgeEntry": syBridgeEntry,
       "syBridgeStatus": syBridgeStatus,
       "syBridgeProtocol": syBridgeProtocol,
       "ip": ip,
       "ipConfiguredFlag": ipConfiguredFlag,
       "ipLANAddress": ipLANAddress,
       "ipLANSubnetMask": ipLANSubnetMask,
       "ipBroadcastAddress": ipBroadcastAddress,
       "ipDefaultGateway": ipDefaultGateway,
       "ipRipReceiveAdvertisementFlag": ipRipReceiveAdvertisementFlag,
       "ipRipSendInterval": ipRipSendInterval,
       "ipDefaultGatewayType": ipDefaultGatewayType,
       "ipWanDestinationName": ipWanDestinationName,
       "ipWanUserName": ipWanUserName,
       "ipStaticRouteMaxEntry": ipStaticRouteMaxEntry,
       "ipStaticRouteTable": ipStaticRouteTable,
       "ipStaticRouteEntry": ipStaticRouteEntry,
       "ipStaticRouteStatus": ipStaticRouteStatus,
       "ipStaticRouteDestinationAddress": ipStaticRouteDestinationAddress,
       "ipStaticRouteDestinationSubnetMask": ipStaticRouteDestinationSubnetMask,
       "ipStaticRouteDestinationHopCount": ipStaticRouteDestinationHopCount,
       "ipStaticRouteDestinationName": ipStaticRouteDestinationName,
       "ipStaticRouteNetworkInterface": ipStaticRouteNetworkInterface,
       "ipStaticRouteUserName": ipStaticRouteUserName,
       "ipStaticRouteGateway": ipStaticRouteGateway,
       "ipDefaultGatewayIfType": ipDefaultGatewayIfType,
       "ipBroadcastForwardTypes": ipBroadcastForwardTypes,
       "ipx": ipx,
       "ipxConfiguredFlag": ipxConfiguredFlag,
       "ipxNetbios": ipxNetbios,
       "ipxMultiFrameTable": ipxMultiFrameTable,
       "ipxMultiFrameEntry": ipxMultiFrameEntry,
       "ipxMultiFrameStatus": ipxMultiFrameStatus,
       "ipxMultiFrameType": ipxMultiFrameType,
       "ipxMultiFrameSelectFlag": ipxMultiFrameSelectFlag,
       "ipxMultiFrameNetworkAddress": ipxMultiFrameNetworkAddress,
       "ipxNetAddressAutoLearnStateCounter": ipxNetAddressAutoLearnStateCounter,
       "wan": wan,
       "wanPortTable": wanPortTable,
       "wanPortEntry": wanPortEntry,
       "wanPortEntryStatus": wanPortEntryStatus,
       "wanPortNumber": wanPortNumber,
       "wanPortEnabled": wanPortEnabled,
       "wanDefaultDialinIPAddress": wanDefaultDialinIPAddress,
       "wanDefaultDialinSubnetMask": wanDefaultDialinSubnetMask,
       "wanDefaultIPXNetworkAddress": wanDefaultIPXNetworkAddress,
       "wanDefaultDialinIPXNodeAddress": wanDefaultDialinIPXNodeAddress,
       "wanDialinAllowedFlag": wanDialinAllowedFlag,
       "wanDialoutAllowedFlag": wanDialoutAllowedFlag,
       "wanLinkLayerType": wanLinkLayerType,
       "wanLinkLayerNRZFlag": wanLinkLayerNRZFlag,
       "wanLinkLayerProtocolType": wanLinkLayerProtocolType,
       "wanLinkDialupFlag": wanLinkDialupFlag,
       "wanModemName": wanModemName,
       "wanModemSpeed": wanModemSpeed,
       "wanModemInitializationString": wanModemInitializationString,
       "wanModemDialPrefix": wanModemDialPrefix,
       "wanPortType": wanPortType,
       "wanPCMCIACardName": wanPCMCIACardName,
       "wanIpRipReceiveAdvertisementFlag": wanIpRipReceiveAdvertisementFlag,
       "wanIpRipSendInterval": wanIpRipSendInterval,
       "wanIpxRipReceiveBroadcastFlag": wanIpxRipReceiveBroadcastFlag,
       "wanIpxRipSendInterval": wanIpxRipSendInterval,
       "wanIpxSapReceiveAdvertisementFlag": wanIpxSapReceiveAdvertisementFlag,
       "wanIpxSapSendInterval": wanIpxSapSendInterval,
       "wanIpxNetbios": wanIpxNetbios,
       "wanISDNSwitchType": wanISDNSwitchType,
       "wanISDNCallingPhoneNoB1": wanISDNCallingPhoneNoB1,
       "wanISDNCallingPhoneNoB2": wanISDNCallingPhoneNoB2,
       "wanISDNSPID1": wanISDNSPID1,
       "wanISDNSPID2": wanISDNSPID2,
       "wanPortGroup": wanPortGroup,
       "wanISDNSubAddress1": wanISDNSubAddress1,
       "wanISDNSubAddress2": wanISDNSubAddress2,
       "wanISDNNTTCard": wanISDNNTTCard,
       "wanISDNChannels": wanISDNChannels,
       "wanEnableDataCompression": wanEnableDataCompression,
       "wanISDNChannelSpeed": wanISDNChannelSpeed,
       "wanUsageMode": wanUsageMode,
       "wanModemPoolGSN": wanModemPoolGSN,
       "wanModemPoolSSN": wanModemPoolSSN,
       "wanIPAddressTable": wanIPAddressTable,
       "wanIPAddressEntry": wanIPAddressEntry,
       "wanIPAddressStatus": wanIPAddressStatus,
       "wanIPAddress": wanIPAddress,
       "wanStatPortTable": wanStatPortTable,
       "wanStatPortEntry": wanStatPortEntry,
       "wanStatPortEntryStatus": wanStatPortEntryStatus,
       "wanStatPortNumber": wanStatPortNumber,
       "wanStatPortState": wanStatPortState,
       "wanStatPortUserName": wanStatPortUserName,
       "wanStatPortFrameTransmitted": wanStatPortFrameTransmitted,
       "wanStatPortFrameReceived": wanStatPortFrameReceived,
       "wanStatPortTransmitError": wanStatPortTransmitError,
       "wanStatPortReceiveError": wanStatPortReceiveError,
       "wanStatPortTransmitQueueFull": wanStatPortTransmitQueueFull,
       "wanStatPortCallOriginated": wanStatPortCallOriginated,
       "wanStatPortCallAnswered": wanStatPortCallAnswered,
       "wanStatPortNoDialTone": wanStatPortNoDialTone,
       "wanStatPortNoAnswer": wanStatPortNoAnswer,
       "wanStatPortBusyDetected": wanStatPortBusyDetected,
       "wanStatPortNoCarrier": wanStatPortNoCarrier,
       "wanStatPortModemSignal": wanStatPortModemSignal,
       "wanStatPortConnDirection": wanStatPortConnDirection,
       "wanStatPortProtoUp": wanStatPortProtoUp,
       "wanIPAddressMaxEntry": wanIPAddressMaxEntry,
       "destination": destination,
       "destTable": destTable,
       "destEntry": destEntry,
       "destStatus": destStatus,
       "destName": destName,
       "destType": destType,
       "destDialoutPhoneNumber": destDialoutPhoneNumber,
       "destDialoutProtoSupport": destDialoutProtoSupport,
       "destDialoutIpxSupport": destDialoutIpxSupport,
       "destDialoutModemSpeed": destDialoutModemSpeed,
       "destPppMtuMru": destPppMtuMru,
       "destDialoutHandshake": destDialoutHandshake,
       "destDialoutUserName": destDialoutUserName,
       "destDialoutPassword": destDialoutPassword,
       "destPorts": destPorts,
       "destMaximumDialoutConnectTime": destMaximumDialoutConnectTime,
       "destDialoutStatus": destDialoutStatus,
       "destDialoutSchedule": destDialoutSchedule,
       "destHolidaySchedule": destHolidaySchedule,
       "destLinkLayerNRZFlag": destLinkLayerNRZFlag,
       "destLinkLayerProtocolType": destLinkLayerProtocolType,
       "destLinkDialupFlag": destLinkDialupFlag,
       "destPortType": destPortType,
       "destLinkLayerType": destLinkLayerType,
       "destDialoutStatusData": destDialoutStatusData,
       "destDialoutScheduleFlag": destDialoutScheduleFlag,
       "destDialinUserName": destDialinUserName,
       "destDialinPassword": destDialinPassword,
       "destMaximumDialinConnectTime": destMaximumDialinConnectTime,
       "destTSDFlag": destTSDFlag,
       "destTSDInactivityTime": destTSDInactivityTime,
       "destTSDMaxDownTime": destTSDMaxDownTime,
       "destTSDPortGroup": destTSDPortGroup,
       "destManualDialCallback": destManualDialCallback,
       "destAllowDynamicIPAddr": destAllowDynamicIPAddr,
       "destISDNChannels": destISDNChannels,
       "destDialoutPhoneNumber2": destDialoutPhoneNumber2,
       "destTSDExpectCallback": destTSDExpectCallback,
       "destMaxEntry": destMaxEntry,
       "destScriptTable": destScriptTable,
       "destScriptEntry": destScriptEntry,
       "destScriptEntryStatus": destScriptEntryStatus,
       "destinationName": destinationName,
       "destScriptUseFlag": destScriptUseFlag,
       "destScriptTimeout": destScriptTimeout,
       "destScriptName": destScriptName,
       "destScript": destScript,
       "destScriptStartupCmd": destScriptStartupCmd,
       "user": user,
       "userMaxEntries": userMaxEntries,
       "userTable": userTable,
       "userEntry": userEntry,
       "userStatus": userStatus,
       "userName": userName,
       "userPassword": userPassword,
       "userPermissions": userPermissions,
       "userCallbackType": userCallbackType,
       "userPhoneNo": userPhoneNo,
       "userDialInMax": userDialInMax,
       "userIpAddress": userIpAddress,
       "manager": manager,
       "mgrTimeoutForMACProtocolResponses": mgrTimeoutForMACProtocolResponses,
       "mgrNumberOfRetriesForMACProtocolResponses": mgrNumberOfRetriesForMACProtocolResponses,
       "mgrEventPollingInterval": mgrEventPollingInterval,
       "holiday": holiday,
       "holidayMaxEntries": holidayMaxEntries,
       "holidayTable": holidayTable,
       "holidayEntry": holidayEntry,
       "holidayStatus": holidayStatus,
       "holidayDate": holidayDate,
       "snmp": snmp,
       "snmpCommunityNameTable": snmpCommunityNameTable,
       "snmpCommunityNameEntry": snmpCommunityNameEntry,
       "snmpCommunityNameStatus": snmpCommunityNameStatus,
       "snmpCommunityName": snmpCommunityName,
       "snmpCommunityPermission": snmpCommunityPermission,
       "snmpMacServerTable": snmpMacServerTable,
       "snmpMacServerEntry": snmpMacServerEntry,
       "snmpMacServerStatus": snmpMacServerStatus,
       "snmpMacServerAddress": snmpMacServerAddress,
       "snmpIpServerTable": snmpIpServerTable,
       "snmpIpServerEntry": snmpIpServerEntry,
       "snmpIpServerStatus": snmpIpServerStatus,
       "snmpIpServerAddress": snmpIpServerAddress,
       "snmpCommunityNameMaxEntry": snmpCommunityNameMaxEntry,
       "event": event,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "eventGroupIndex": eventGroupIndex,
       "eventData": eventData,
       "discovery": discovery,
       "discNodeName": discNodeName,
       "discModel": discModel,
       "discProto": discProto,
       "fileMgmt": fileMgmt,
       "syFMOperation": syFMOperation,
       "syFMTimeStamp": syFMTimeStamp,
       "syFMError": syFMError,
       "syFileTransfer": syFileTransfer,
       "fileTransferStatus": fileTransferStatus,
       "fileTransferStartTime": fileTransferStartTime,
       "fileTransferFileLength": fileTransferFileLength,
       "fileTransferCheckSum": fileTransferCheckSum,
       "fileTransferDirection": fileTransferDirection,
       "fileTransferLastRcvTime": fileTransferLastRcvTime,
       "fileTransferRemoteAddr": fileTransferRemoteAddr,
       "fileTransferRemoteFileName": fileTransferRemoteFileName,
       "fileTransferLocalFileName": fileTransferLocalFileName,
       "fileTransferData": fileTransferData,
       "syFileInfo": syFileInfo,
       "syFileInfoVersion": syFileInfoVersion,
       "syFileInfoChecksum": syFileInfoChecksum,
       "syFileInfoLength": syFileInfoLength,
       "syDirTable": syDirTable,
       "syDirEntry": syDirEntry,
       "syDirStatus": syDirStatus,
       "syDirName": syDirName,
       "syDirCompressSize": syDirCompressSize,
       "syDirVersion": syDirVersion,
       "syDirUncompressSize": syDirUncompressSize,
       "fileName": fileName,
       "fileNameFrom": fileNameFrom,
       "fileNameTo": fileNameTo,
       "modempool": modempool,
       "modempoolEnabled": modempoolEnabled,
       "modempoolNodeName": modempoolNodeName,
       "modempoolProtoSupport": modempoolProtoSupport,
       "endOfSBEMib": endOfSBEMib,
       "dummyStopperForWorkshopForGetNext": dummyStopperForWorkshopForGetNext}
)
