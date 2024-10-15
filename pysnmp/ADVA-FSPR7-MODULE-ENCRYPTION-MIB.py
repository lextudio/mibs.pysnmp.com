# SNMP MIB module (ADVA-FSPR7-MODULE-ENCRYPTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADVA-FSPR7-MODULE-ENCRYPTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:46 2024
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

(entityEqptClassName,
 entityEqptExtNo,
 entityEqptPortNo,
 entityEqptShelfNo,
 entityEqptSlotNo,
 entityFacilityClassName,
 entityFacilityExtNo,
 entityFacilityPortNo,
 entityFacilityShelfNo,
 entityFacilitySlotNo) = mibBuilder.importSymbols(
    "ADVA-FSPR7-MIB",
    "entityEqptClassName",
    "entityEqptExtNo",
    "entityEqptPortNo",
    "entityEqptShelfNo",
    "entityEqptSlotNo",
    "entityFacilityClassName",
    "entityFacilityExtNo",
    "entityFacilityPortNo",
    "entityFacilityShelfNo",
    "entityFacilitySlotNo")

(EntityIndex,
 entityIndex,
 fspR7) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "EntityIndex",
    "entityIndex",
    "fspR7")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

moduleEncryptionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5)
)
moduleEncryptionMIB.setRevisions(
        ("2013-08-20 00:00",
         "2011-02-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CryptoFspR7EnableDisable(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("undefined", 0))
    )



class CryptoFspR7EnableDisableCaps(Bits, TextualConvention):
    status = "current"


class CryptoFspR7EncryptionReset(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rls", 1),
          ("rtf", 2),
          ("undefined", 0))
    )



class CryptoFspR7EncryptionResetCaps(Bits, TextualConvention):
    status = "current"


class CryptoFspR7EncryptionSwitch(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oprCryptoOff", 2),
          ("rls", 1),
          ("undefined", 0))
    )



class CryptoFspR7EncryptionSwitchCaps(Bits, TextualConvention):
    status = "current"


class CryptoFspR7ForceKeyExchange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oprKeyExchg", 2),
          ("rls", 1),
          ("undefined", 0))
    )



class CryptoFspR7ForceKeyExchangeCaps(Bits, TextualConvention):
    status = "current"


class CryptoFspR7KeyExchangeForcedClear(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("rls", 1),
          ("undefined", 0))
    )



class CryptoFspR7KeyExchangeForcedClearCaps(Bits, TextualConvention):
    status = "current"


class CryptoFspR7SelfTestOperation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oprSelfTest", 2),
          ("rls", 1),
          ("undefined", 0))
    )



class CryptoFspR7SelfTestOperationCaps(Bits, TextualConvention):
    status = "current"


class CryptoFspR7SessionKeyLifetime(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("lifetime12h", 6),
          ("lifetime1d", 7),
          ("lifetime1h", 2),
          ("lifetime1w", 10),
          ("lifetime2d", 8),
          ("lifetime2h", 3),
          ("lifetime2w", 11),
          ("lifetime30min", 1),
          ("lifetime3d", 9),
          ("lifetime3h", 4),
          ("lifetime3w", 12),
          ("lifetime6h", 5),
          ("lifetimeMax", 13),
          ("undefined", 0))
    )



class CryptoFspR7SessionKeyLifetimeCaps(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_EncryptionMIB_ObjectIdentity = ObjectIdentity
encryptionMIB = _EncryptionMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1)
)
_EncryptionMIBConformance_ObjectIdentity = ObjectIdentity
encryptionMIBConformance = _EncryptionMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 1)
)
_EncryptionMIBCompliances_ObjectIdentity = ObjectIdentity
encryptionMIBCompliances = _EncryptionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 1, 1)
)
_EncryptionMIBGroups_ObjectIdentity = ObjectIdentity
encryptionMIBGroups = _EncryptionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 1, 2)
)
_ModuleEncryptionObjects_ObjectIdentity = ObjectIdentity
moduleEncryptionObjects = _ModuleEncryptionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2)
)
_CryptoOfficerPassword_Type = SnmpAdminString
_CryptoOfficerPassword_Object = MibScalar
cryptoOfficerPassword = _CryptoOfficerPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 1),
    _CryptoOfficerPassword_Type()
)
cryptoOfficerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoOfficerPassword.setStatus("current")


class _CryptoOfficerPasswordError_Type(Integer32):
    """Custom type cryptoOfficerPasswordError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 7),
          ("passwdInvalid", 2),
          ("passwdNotInit", 4),
          ("passwdOk", 1),
          ("passwdRejected", 3),
          ("passwdTooSimple", 5),
          ("passwdValidationAborted", 6),
          ("undefined", 0))
    )


_CryptoOfficerPasswordError_Type.__name__ = "Integer32"
_CryptoOfficerPasswordError_Object = MibScalar
cryptoOfficerPasswordError = _CryptoOfficerPasswordError_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 2),
    _CryptoOfficerPasswordError_Type()
)
cryptoOfficerPasswordError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoOfficerPasswordError.setStatus("current")
_CryptoOfficerPasswordReqId_Type = Unsigned32
_CryptoOfficerPasswordReqId_Object = MibScalar
cryptoOfficerPasswordReqId = _CryptoOfficerPasswordReqId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 3),
    _CryptoOfficerPasswordReqId_Type()
)
cryptoOfficerPasswordReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoOfficerPasswordReqId.setStatus("current")
_CryptoModuleConfigTable_Object = MibTable
cryptoModuleConfigTable = _CryptoModuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cryptoModuleConfigTable.setStatus("current")
_CryptoModuleConfigEntry_Object = MibTableRow
cryptoModuleConfigEntry = _CryptoModuleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 10, 1)
)
cryptoModuleConfigEntry.setIndexNames(
    (0, "ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoModuleConfigIndex"),
)
if mibBuilder.loadTexts:
    cryptoModuleConfigEntry.setStatus("current")
_CryptoModuleConfigIndex_Type = EntityIndex
_CryptoModuleConfigIndex_Object = MibTableColumn
cryptoModuleConfigIndex = _CryptoModuleConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 10, 1, 1),
    _CryptoModuleConfigIndex_Type()
)
cryptoModuleConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cryptoModuleConfigIndex.setStatus("current")
_CryptoModuleConfigCryptoOfficerPassword_Type = SnmpAdminString
_CryptoModuleConfigCryptoOfficerPassword_Object = MibTableColumn
cryptoModuleConfigCryptoOfficerPassword = _CryptoModuleConfigCryptoOfficerPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 10, 1, 2),
    _CryptoModuleConfigCryptoOfficerPassword_Type()
)
cryptoModuleConfigCryptoOfficerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoModuleConfigCryptoOfficerPassword.setStatus("current")
_CryptoModuleConfigResetToFactory_Type = CryptoFspR7EncryptionReset
_CryptoModuleConfigResetToFactory_Object = MibTableColumn
cryptoModuleConfigResetToFactory = _CryptoModuleConfigResetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 10, 1, 3),
    _CryptoModuleConfigResetToFactory_Type()
)
cryptoModuleConfigResetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoModuleConfigResetToFactory.setStatus("current")
_CryptoModuleConfigFirmwareUpdateState_Type = CryptoFspR7EnableDisable
_CryptoModuleConfigFirmwareUpdateState_Object = MibTableColumn
cryptoModuleConfigFirmwareUpdateState = _CryptoModuleConfigFirmwareUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 10, 1, 4),
    _CryptoModuleConfigFirmwareUpdateState_Type()
)
cryptoModuleConfigFirmwareUpdateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoModuleConfigFirmwareUpdateState.setStatus("current")
_CryptoModuleConfigFirmwareVersion_Type = SnmpAdminString
_CryptoModuleConfigFirmwareVersion_Object = MibTableColumn
cryptoModuleConfigFirmwareVersion = _CryptoModuleConfigFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 10, 1, 5),
    _CryptoModuleConfigFirmwareVersion_Type()
)
cryptoModuleConfigFirmwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoModuleConfigFirmwareVersion.setStatus("current")
_CryptoModuleConfigSelfTestOperation_Type = CryptoFspR7SelfTestOperation
_CryptoModuleConfigSelfTestOperation_Object = MibTableColumn
cryptoModuleConfigSelfTestOperation = _CryptoModuleConfigSelfTestOperation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 10, 1, 6),
    _CryptoModuleConfigSelfTestOperation_Type()
)
cryptoModuleConfigSelfTestOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoModuleConfigSelfTestOperation.setStatus("current")
_CryptoModuleStatusTable_Object = MibTable
cryptoModuleStatusTable = _CryptoModuleStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cryptoModuleStatusTable.setStatus("current")
_CryptoModuleStatusEntry_Object = MibTableRow
cryptoModuleStatusEntry = _CryptoModuleStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 11, 1)
)
cryptoModuleStatusEntry.setIndexNames(
    (0, "ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoModuleConfigIndex"),
)
if mibBuilder.loadTexts:
    cryptoModuleStatusEntry.setStatus("current")
_CryptoModuleStatusIndex_Type = EntityIndex
_CryptoModuleStatusIndex_Object = MibTableColumn
cryptoModuleStatusIndex = _CryptoModuleStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 11, 1, 1),
    _CryptoModuleStatusIndex_Type()
)
cryptoModuleStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cryptoModuleStatusIndex.setStatus("current")


class _CryptoModuleStatusFailureLoginCount_Type(Unsigned32):
    """Custom type cryptoModuleStatusFailureLoginCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_CryptoModuleStatusFailureLoginCount_Type.__name__ = "Unsigned32"
_CryptoModuleStatusFailureLoginCount_Object = MibTableColumn
cryptoModuleStatusFailureLoginCount = _CryptoModuleStatusFailureLoginCount_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 11, 1, 2),
    _CryptoModuleStatusFailureLoginCount_Type()
)
cryptoModuleStatusFailureLoginCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoModuleStatusFailureLoginCount.setStatus("current")
_CryptoModuleStatusSuccessfulLoginDateAndTime_Type = DateAndTime
_CryptoModuleStatusSuccessfulLoginDateAndTime_Object = MibTableColumn
cryptoModuleStatusSuccessfulLoginDateAndTime = _CryptoModuleStatusSuccessfulLoginDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 11, 1, 3),
    _CryptoModuleStatusSuccessfulLoginDateAndTime_Type()
)
cryptoModuleStatusSuccessfulLoginDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoModuleStatusSuccessfulLoginDateAndTime.setStatus("current")
_CryptoModuleStatusUnsuccessfulLoginDateAndTime_Type = DateAndTime
_CryptoModuleStatusUnsuccessfulLoginDateAndTime_Object = MibTableColumn
cryptoModuleStatusUnsuccessfulLoginDateAndTime = _CryptoModuleStatusUnsuccessfulLoginDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 11, 1, 4),
    _CryptoModuleStatusUnsuccessfulLoginDateAndTime_Type()
)
cryptoModuleStatusUnsuccessfulLoginDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoModuleStatusUnsuccessfulLoginDateAndTime.setStatus("current")
_CryptoModuleStatusResetToFactoryCapability_Type = CryptoFspR7EnableDisable
_CryptoModuleStatusResetToFactoryCapability_Object = MibTableColumn
cryptoModuleStatusResetToFactoryCapability = _CryptoModuleStatusResetToFactoryCapability_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 11, 1, 5),
    _CryptoModuleStatusResetToFactoryCapability_Type()
)
cryptoModuleStatusResetToFactoryCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoModuleStatusResetToFactoryCapability.setStatus("current")
_CryptoModuleTable_Object = MibTable
cryptoModuleTable = _CryptoModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 20)
)
if mibBuilder.loadTexts:
    cryptoModuleTable.setStatus("current")
_CryptoModuleEntry_Object = MibTableRow
cryptoModuleEntry = _CryptoModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 20, 1)
)
cryptoModuleEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityEqptShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptClassName"),
)
if mibBuilder.loadTexts:
    cryptoModuleEntry.setStatus("current")
_CryptoModuleCryptoOfficerPassword_Type = SnmpAdminString
_CryptoModuleCryptoOfficerPassword_Object = MibTableColumn
cryptoModuleCryptoOfficerPassword = _CryptoModuleCryptoOfficerPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 20, 1, 1),
    _CryptoModuleCryptoOfficerPassword_Type()
)
cryptoModuleCryptoOfficerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoModuleCryptoOfficerPassword.setStatus("current")
_CryptoModuleResetToFactory_Type = CryptoFspR7EncryptionReset
_CryptoModuleResetToFactory_Object = MibTableColumn
cryptoModuleResetToFactory = _CryptoModuleResetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 20, 1, 2),
    _CryptoModuleResetToFactory_Type()
)
cryptoModuleResetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoModuleResetToFactory.setStatus("current")
_CryptoModuleFirmwareUpdateState_Type = CryptoFspR7EnableDisable
_CryptoModuleFirmwareUpdateState_Object = MibTableColumn
cryptoModuleFirmwareUpdateState = _CryptoModuleFirmwareUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 20, 1, 3),
    _CryptoModuleFirmwareUpdateState_Type()
)
cryptoModuleFirmwareUpdateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoModuleFirmwareUpdateState.setStatus("current")
_CryptoModuleFirmwareVersion_Type = SnmpAdminString
_CryptoModuleFirmwareVersion_Object = MibTableColumn
cryptoModuleFirmwareVersion = _CryptoModuleFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 20, 1, 4),
    _CryptoModuleFirmwareVersion_Type()
)
cryptoModuleFirmwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoModuleFirmwareVersion.setStatus("current")
_CryptoModuleSelfTestOperation_Type = CryptoFspR7SelfTestOperation
_CryptoModuleSelfTestOperation_Object = MibTableColumn
cryptoModuleSelfTestOperation = _CryptoModuleSelfTestOperation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 20, 1, 5),
    _CryptoModuleSelfTestOperation_Type()
)
cryptoModuleSelfTestOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoModuleSelfTestOperation.setStatus("current")


class _CryptoModuleFailureLoginCount_Type(Unsigned32):
    """Custom type cryptoModuleFailureLoginCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_CryptoModuleFailureLoginCount_Type.__name__ = "Unsigned32"
_CryptoModuleFailureLoginCount_Object = MibTableColumn
cryptoModuleFailureLoginCount = _CryptoModuleFailureLoginCount_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 20, 1, 6),
    _CryptoModuleFailureLoginCount_Type()
)
cryptoModuleFailureLoginCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoModuleFailureLoginCount.setStatus("current")
_CryptoModuleSuccessfulLoginDateAndTime_Type = DateAndTime
_CryptoModuleSuccessfulLoginDateAndTime_Object = MibTableColumn
cryptoModuleSuccessfulLoginDateAndTime = _CryptoModuleSuccessfulLoginDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 20, 1, 7),
    _CryptoModuleSuccessfulLoginDateAndTime_Type()
)
cryptoModuleSuccessfulLoginDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoModuleSuccessfulLoginDateAndTime.setStatus("current")
_CryptoModuleUnsuccessfulLoginDateAndTime_Type = DateAndTime
_CryptoModuleUnsuccessfulLoginDateAndTime_Object = MibTableColumn
cryptoModuleUnsuccessfulLoginDateAndTime = _CryptoModuleUnsuccessfulLoginDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 20, 1, 8),
    _CryptoModuleUnsuccessfulLoginDateAndTime_Type()
)
cryptoModuleUnsuccessfulLoginDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoModuleUnsuccessfulLoginDateAndTime.setStatus("current")
_CryptoModuleCapTable_Object = MibTable
cryptoModuleCapTable = _CryptoModuleCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 21)
)
if mibBuilder.loadTexts:
    cryptoModuleCapTable.setStatus("current")
_CryptoModuleCapEntry_Object = MibTableRow
cryptoModuleCapEntry = _CryptoModuleCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 21, 1)
)
cryptoModuleCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityEqptShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptClassName"),
)
if mibBuilder.loadTexts:
    cryptoModuleCapEntry.setStatus("current")
_CryptoModuleCapCryptoOfficerPassword_Type = Integer32
_CryptoModuleCapCryptoOfficerPassword_Object = MibTableColumn
cryptoModuleCapCryptoOfficerPassword = _CryptoModuleCapCryptoOfficerPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 21, 1, 1),
    _CryptoModuleCapCryptoOfficerPassword_Type()
)
cryptoModuleCapCryptoOfficerPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoModuleCapCryptoOfficerPassword.setStatus("current")
_CryptoModuleCapResetToFactory_Type = CryptoFspR7EncryptionResetCaps
_CryptoModuleCapResetToFactory_Object = MibTableColumn
cryptoModuleCapResetToFactory = _CryptoModuleCapResetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 21, 1, 2),
    _CryptoModuleCapResetToFactory_Type()
)
cryptoModuleCapResetToFactory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoModuleCapResetToFactory.setStatus("current")
_CryptoModuleCapFirmwareUpdateState_Type = CryptoFspR7EnableDisableCaps
_CryptoModuleCapFirmwareUpdateState_Object = MibTableColumn
cryptoModuleCapFirmwareUpdateState = _CryptoModuleCapFirmwareUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 21, 1, 3),
    _CryptoModuleCapFirmwareUpdateState_Type()
)
cryptoModuleCapFirmwareUpdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoModuleCapFirmwareUpdateState.setStatus("current")
_CryptoModuleCapFirmwareVersion_Type = Integer32
_CryptoModuleCapFirmwareVersion_Object = MibTableColumn
cryptoModuleCapFirmwareVersion = _CryptoModuleCapFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 21, 1, 4),
    _CryptoModuleCapFirmwareVersion_Type()
)
cryptoModuleCapFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoModuleCapFirmwareVersion.setStatus("current")
_CryptoModuleCapSelfTestOperation_Type = CryptoFspR7SelfTestOperationCaps
_CryptoModuleCapSelfTestOperation_Object = MibTableColumn
cryptoModuleCapSelfTestOperation = _CryptoModuleCapSelfTestOperation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 2, 21, 1, 5),
    _CryptoModuleCapSelfTestOperation_Type()
)
cryptoModuleCapSelfTestOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoModuleCapSelfTestOperation.setStatus("current")
_PortEncryptionObjects_ObjectIdentity = ObjectIdentity
portEncryptionObjects = _PortEncryptionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3)
)
_CryptoPortConfigTable_Object = MibTable
cryptoPortConfigTable = _CryptoPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 12)
)
if mibBuilder.loadTexts:
    cryptoPortConfigTable.setStatus("current")
_CryptoPortConfigEntry_Object = MibTableRow
cryptoPortConfigEntry = _CryptoPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 12, 1)
)
cryptoPortConfigEntry.setIndexNames(
    (0, "ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoPortConfigIndex"),
)
if mibBuilder.loadTexts:
    cryptoPortConfigEntry.setStatus("current")
_CryptoPortConfigIndex_Type = EntityIndex
_CryptoPortConfigIndex_Object = MibTableColumn
cryptoPortConfigIndex = _CryptoPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 12, 1, 1),
    _CryptoPortConfigIndex_Type()
)
cryptoPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cryptoPortConfigIndex.setStatus("current")
_CryptoPortConfigAuthKey_Type = SnmpAdminString
_CryptoPortConfigAuthKey_Object = MibTableColumn
cryptoPortConfigAuthKey = _CryptoPortConfigAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 12, 1, 2),
    _CryptoPortConfigAuthKey_Type()
)
cryptoPortConfigAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoPortConfigAuthKey.setStatus("current")
_CryptoPortConfigAuthKeyLifeTime_Type = CryptoFspR7SessionKeyLifetime
_CryptoPortConfigAuthKeyLifeTime_Object = MibTableColumn
cryptoPortConfigAuthKeyLifeTime = _CryptoPortConfigAuthKeyLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 12, 1, 3),
    _CryptoPortConfigAuthKeyLifeTime_Type()
)
cryptoPortConfigAuthKeyLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoPortConfigAuthKeyLifeTime.setStatus("current")
_CryptoPortConfigEncryptionOffState_Type = CryptoFspR7EnableDisable
_CryptoPortConfigEncryptionOffState_Object = MibTableColumn
cryptoPortConfigEncryptionOffState = _CryptoPortConfigEncryptionOffState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 12, 1, 4),
    _CryptoPortConfigEncryptionOffState_Type()
)
cryptoPortConfigEncryptionOffState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoPortConfigEncryptionOffState.setStatus("current")
_CryptoPortConfigEncryptionOff_Type = CryptoFspR7EncryptionSwitch
_CryptoPortConfigEncryptionOff_Object = MibTableColumn
cryptoPortConfigEncryptionOff = _CryptoPortConfigEncryptionOff_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 12, 1, 5),
    _CryptoPortConfigEncryptionOff_Type()
)
cryptoPortConfigEncryptionOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoPortConfigEncryptionOff.setStatus("current")
_CryptoPortConfigForceKeyExchange_Type = CryptoFspR7ForceKeyExchange
_CryptoPortConfigForceKeyExchange_Object = MibTableColumn
cryptoPortConfigForceKeyExchange = _CryptoPortConfigForceKeyExchange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 12, 1, 6),
    _CryptoPortConfigForceKeyExchange_Type()
)
cryptoPortConfigForceKeyExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoPortConfigForceKeyExchange.setStatus("current")
_CryptoPortConfigKeyExchangeForcedClear_Type = CryptoFspR7KeyExchangeForcedClear
_CryptoPortConfigKeyExchangeForcedClear_Object = MibTableColumn
cryptoPortConfigKeyExchangeForcedClear = _CryptoPortConfigKeyExchangeForcedClear_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 12, 1, 7),
    _CryptoPortConfigKeyExchangeForcedClear_Type()
)
cryptoPortConfigKeyExchangeForcedClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoPortConfigKeyExchangeForcedClear.setStatus("current")
_CryptoPortStatusTable_Object = MibTable
cryptoPortStatusTable = _CryptoPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 13)
)
if mibBuilder.loadTexts:
    cryptoPortStatusTable.setStatus("current")
_CryptoPortStatusEntry_Object = MibTableRow
cryptoPortStatusEntry = _CryptoPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 13, 1)
)
cryptoPortStatusEntry.setIndexNames(
    (0, "ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoPortStatusIndex"),
)
if mibBuilder.loadTexts:
    cryptoPortStatusEntry.setStatus("current")
_CryptoPortStatusIndex_Type = EntityIndex
_CryptoPortStatusIndex_Object = MibTableColumn
cryptoPortStatusIndex = _CryptoPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 13, 1, 1),
    _CryptoPortStatusIndex_Type()
)
cryptoPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cryptoPortStatusIndex.setStatus("current")
_CryptoPortStatusEncryptionOffTimeRemaining_Type = Unsigned32
_CryptoPortStatusEncryptionOffTimeRemaining_Object = MibTableColumn
cryptoPortStatusEncryptionOffTimeRemaining = _CryptoPortStatusEncryptionOffTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 13, 1, 2),
    _CryptoPortStatusEncryptionOffTimeRemaining_Type()
)
cryptoPortStatusEncryptionOffTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortStatusEncryptionOffTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    cryptoPortStatusEncryptionOffTimeRemaining.setUnits("s")


class _CryptoPortStatusFailureKeyExchangeCount_Type(Unsigned32):
    """Custom type cryptoPortStatusFailureKeyExchangeCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_CryptoPortStatusFailureKeyExchangeCount_Type.__name__ = "Unsigned32"
_CryptoPortStatusFailureKeyExchangeCount_Object = MibTableColumn
cryptoPortStatusFailureKeyExchangeCount = _CryptoPortStatusFailureKeyExchangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 13, 1, 3),
    _CryptoPortStatusFailureKeyExchangeCount_Type()
)
cryptoPortStatusFailureKeyExchangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortStatusFailureKeyExchangeCount.setStatus("current")
_CryptoPortStatusSuccessfulKeyExchangeDateAndTime_Type = DateAndTime
_CryptoPortStatusSuccessfulKeyExchangeDateAndTime_Object = MibTableColumn
cryptoPortStatusSuccessfulKeyExchangeDateAndTime = _CryptoPortStatusSuccessfulKeyExchangeDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 13, 1, 4),
    _CryptoPortStatusSuccessfulKeyExchangeDateAndTime_Type()
)
cryptoPortStatusSuccessfulKeyExchangeDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortStatusSuccessfulKeyExchangeDateAndTime.setStatus("current")
_CryptoPortStatusUnsuccessfulKeyExchangeDateAndTime_Type = DateAndTime
_CryptoPortStatusUnsuccessfulKeyExchangeDateAndTime_Object = MibTableColumn
cryptoPortStatusUnsuccessfulKeyExchangeDateAndTime = _CryptoPortStatusUnsuccessfulKeyExchangeDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 13, 1, 5),
    _CryptoPortStatusUnsuccessfulKeyExchangeDateAndTime_Type()
)
cryptoPortStatusUnsuccessfulKeyExchangeDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortStatusUnsuccessfulKeyExchangeDateAndTime.setStatus("current")
_CryptoPortStatusAuthKeyLifeTimeRemaining_Type = Unsigned32
_CryptoPortStatusAuthKeyLifeTimeRemaining_Object = MibTableColumn
cryptoPortStatusAuthKeyLifeTimeRemaining = _CryptoPortStatusAuthKeyLifeTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 13, 1, 6),
    _CryptoPortStatusAuthKeyLifeTimeRemaining_Type()
)
cryptoPortStatusAuthKeyLifeTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortStatusAuthKeyLifeTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    cryptoPortStatusAuthKeyLifeTimeRemaining.setUnits("s")
_CryptoPortStatusEncryptionOffCapability_Type = CryptoFspR7EnableDisable
_CryptoPortStatusEncryptionOffCapability_Object = MibTableColumn
cryptoPortStatusEncryptionOffCapability = _CryptoPortStatusEncryptionOffCapability_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 13, 1, 7),
    _CryptoPortStatusEncryptionOffCapability_Type()
)
cryptoPortStatusEncryptionOffCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortStatusEncryptionOffCapability.setStatus("current")
_CryptoPortTable_Object = MibTable
cryptoPortTable = _CryptoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 20)
)
if mibBuilder.loadTexts:
    cryptoPortTable.setStatus("current")
_CryptoPortEntry_Object = MibTableRow
cryptoPortEntry = _CryptoPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 20, 1)
)
cryptoPortEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    cryptoPortEntry.setStatus("current")
_CryptoPortAuthKey_Type = SnmpAdminString
_CryptoPortAuthKey_Object = MibTableColumn
cryptoPortAuthKey = _CryptoPortAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 20, 1, 1),
    _CryptoPortAuthKey_Type()
)
cryptoPortAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoPortAuthKey.setStatus("current")
_CryptoPortAuthKeyLifeTime_Type = CryptoFspR7SessionKeyLifetime
_CryptoPortAuthKeyLifeTime_Object = MibTableColumn
cryptoPortAuthKeyLifeTime = _CryptoPortAuthKeyLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 20, 1, 2),
    _CryptoPortAuthKeyLifeTime_Type()
)
cryptoPortAuthKeyLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoPortAuthKeyLifeTime.setStatus("current")
_CryptoPortEncryptionOffState_Type = CryptoFspR7EnableDisable
_CryptoPortEncryptionOffState_Object = MibTableColumn
cryptoPortEncryptionOffState = _CryptoPortEncryptionOffState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 20, 1, 3),
    _CryptoPortEncryptionOffState_Type()
)
cryptoPortEncryptionOffState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoPortEncryptionOffState.setStatus("current")
_CryptoPortEncryptionOff_Type = CryptoFspR7EncryptionSwitch
_CryptoPortEncryptionOff_Object = MibTableColumn
cryptoPortEncryptionOff = _CryptoPortEncryptionOff_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 20, 1, 4),
    _CryptoPortEncryptionOff_Type()
)
cryptoPortEncryptionOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoPortEncryptionOff.setStatus("current")
_CryptoPortForceKeyExchange_Type = CryptoFspR7ForceKeyExchange
_CryptoPortForceKeyExchange_Object = MibTableColumn
cryptoPortForceKeyExchange = _CryptoPortForceKeyExchange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 20, 1, 5),
    _CryptoPortForceKeyExchange_Type()
)
cryptoPortForceKeyExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoPortForceKeyExchange.setStatus("current")
_CryptoPortKeyExchangeForcedClear_Type = CryptoFspR7KeyExchangeForcedClear
_CryptoPortKeyExchangeForcedClear_Object = MibTableColumn
cryptoPortKeyExchangeForcedClear = _CryptoPortKeyExchangeForcedClear_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 20, 1, 6),
    _CryptoPortKeyExchangeForcedClear_Type()
)
cryptoPortKeyExchangeForcedClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoPortKeyExchangeForcedClear.setStatus("current")
_CryptoPortEncryptionOffTimeRemaining_Type = Unsigned32
_CryptoPortEncryptionOffTimeRemaining_Object = MibTableColumn
cryptoPortEncryptionOffTimeRemaining = _CryptoPortEncryptionOffTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 20, 1, 7),
    _CryptoPortEncryptionOffTimeRemaining_Type()
)
cryptoPortEncryptionOffTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortEncryptionOffTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    cryptoPortEncryptionOffTimeRemaining.setUnits("s")


class _CryptoPortFailureKeyExchangeCount_Type(Unsigned32):
    """Custom type cryptoPortFailureKeyExchangeCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_CryptoPortFailureKeyExchangeCount_Type.__name__ = "Unsigned32"
_CryptoPortFailureKeyExchangeCount_Object = MibTableColumn
cryptoPortFailureKeyExchangeCount = _CryptoPortFailureKeyExchangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 20, 1, 8),
    _CryptoPortFailureKeyExchangeCount_Type()
)
cryptoPortFailureKeyExchangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortFailureKeyExchangeCount.setStatus("current")
_CryptoPortSuccessfulKeyExchangeDateAndTime_Type = DateAndTime
_CryptoPortSuccessfulKeyExchangeDateAndTime_Object = MibTableColumn
cryptoPortSuccessfulKeyExchangeDateAndTime = _CryptoPortSuccessfulKeyExchangeDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 20, 1, 9),
    _CryptoPortSuccessfulKeyExchangeDateAndTime_Type()
)
cryptoPortSuccessfulKeyExchangeDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortSuccessfulKeyExchangeDateAndTime.setStatus("current")
_CryptoPortUnsuccessfulKeyExchangeDateAndTime_Type = DateAndTime
_CryptoPortUnsuccessfulKeyExchangeDateAndTime_Object = MibTableColumn
cryptoPortUnsuccessfulKeyExchangeDateAndTime = _CryptoPortUnsuccessfulKeyExchangeDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 20, 1, 10),
    _CryptoPortUnsuccessfulKeyExchangeDateAndTime_Type()
)
cryptoPortUnsuccessfulKeyExchangeDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortUnsuccessfulKeyExchangeDateAndTime.setStatus("current")
_CryptoPortAuthKeyLifeTimeRemaining_Type = Unsigned32
_CryptoPortAuthKeyLifeTimeRemaining_Object = MibTableColumn
cryptoPortAuthKeyLifeTimeRemaining = _CryptoPortAuthKeyLifeTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 20, 1, 11),
    _CryptoPortAuthKeyLifeTimeRemaining_Type()
)
cryptoPortAuthKeyLifeTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortAuthKeyLifeTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    cryptoPortAuthKeyLifeTimeRemaining.setUnits("s")
_CryptoPortCapTable_Object = MibTable
cryptoPortCapTable = _CryptoPortCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 21)
)
if mibBuilder.loadTexts:
    cryptoPortCapTable.setStatus("current")
_CryptoPortCapEntry_Object = MibTableRow
cryptoPortCapEntry = _CryptoPortCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 21, 1)
)
cryptoPortCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    cryptoPortCapEntry.setStatus("current")
_CryptoPortCapAuthKey_Type = Integer32
_CryptoPortCapAuthKey_Object = MibTableColumn
cryptoPortCapAuthKey = _CryptoPortCapAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 21, 1, 1),
    _CryptoPortCapAuthKey_Type()
)
cryptoPortCapAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortCapAuthKey.setStatus("current")
_CryptoPortCapAuthKeyLifeTime_Type = CryptoFspR7SessionKeyLifetimeCaps
_CryptoPortCapAuthKeyLifeTime_Object = MibTableColumn
cryptoPortCapAuthKeyLifeTime = _CryptoPortCapAuthKeyLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 21, 1, 2),
    _CryptoPortCapAuthKeyLifeTime_Type()
)
cryptoPortCapAuthKeyLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortCapAuthKeyLifeTime.setStatus("current")
_CryptoPortCapEncryptionOffState_Type = CryptoFspR7EnableDisableCaps
_CryptoPortCapEncryptionOffState_Object = MibTableColumn
cryptoPortCapEncryptionOffState = _CryptoPortCapEncryptionOffState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 21, 1, 3),
    _CryptoPortCapEncryptionOffState_Type()
)
cryptoPortCapEncryptionOffState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortCapEncryptionOffState.setStatus("current")
_CryptoPortCapEncryptionOff_Type = CryptoFspR7EncryptionSwitchCaps
_CryptoPortCapEncryptionOff_Object = MibTableColumn
cryptoPortCapEncryptionOff = _CryptoPortCapEncryptionOff_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 21, 1, 4),
    _CryptoPortCapEncryptionOff_Type()
)
cryptoPortCapEncryptionOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortCapEncryptionOff.setStatus("current")
_CryptoPortCapForceKeyExchange_Type = CryptoFspR7ForceKeyExchangeCaps
_CryptoPortCapForceKeyExchange_Object = MibTableColumn
cryptoPortCapForceKeyExchange = _CryptoPortCapForceKeyExchange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 21, 1, 5),
    _CryptoPortCapForceKeyExchange_Type()
)
cryptoPortCapForceKeyExchange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortCapForceKeyExchange.setStatus("current")
_CryptoPortCapKeyExchangeForcedClear_Type = CryptoFspR7KeyExchangeForcedClearCaps
_CryptoPortCapKeyExchangeForcedClear_Object = MibTableColumn
cryptoPortCapKeyExchangeForcedClear = _CryptoPortCapKeyExchangeForcedClear_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 3, 21, 1, 6),
    _CryptoPortCapKeyExchangeForcedClear_Type()
)
cryptoPortCapKeyExchangeForcedClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPortCapKeyExchangeForcedClear.setStatus("current")
_EncryptionPerformanceMonitoring_ObjectIdentity = ObjectIdentity
encryptionPerformanceMonitoring = _EncryptionPerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4)
)
_IntervalEncryptionSublayerPm15minTable_Object = MibTable
intervalEncryptionSublayerPm15minTable = _IntervalEncryptionSublayerPm15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    intervalEncryptionSublayerPm15minTable.setStatus("current")
_IntervalEncryptionSublayerPm15minEntry_Object = MibTableRow
intervalEncryptionSublayerPm15minEntry = _IntervalEncryptionSublayerPm15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 1, 1)
)
intervalEncryptionSublayerPm15minEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
    (0, "ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "intervalEncryptionSublayerPm15minNumber"),
)
if mibBuilder.loadTexts:
    intervalEncryptionSublayerPm15minEntry.setStatus("current")


class _IntervalEncryptionSublayerPm15minNumber_Type(Integer32):
    """Custom type intervalEncryptionSublayerPm15minNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_IntervalEncryptionSublayerPm15minNumber_Type.__name__ = "Integer32"
_IntervalEncryptionSublayerPm15minNumber_Object = MibTableColumn
intervalEncryptionSublayerPm15minNumber = _IntervalEncryptionSublayerPm15minNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 1, 1, 1),
    _IntervalEncryptionSublayerPm15minNumber_Type()
)
intervalEncryptionSublayerPm15minNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    intervalEncryptionSublayerPm15minNumber.setStatus("current")
_IntervalEncryptionSublayerPm15minEncryptionRunSeconds_Type = Unsigned32
_IntervalEncryptionSublayerPm15minEncryptionRunSeconds_Object = MibTableColumn
intervalEncryptionSublayerPm15minEncryptionRunSeconds = _IntervalEncryptionSublayerPm15minEncryptionRunSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 1, 1, 2),
    _IntervalEncryptionSublayerPm15minEncryptionRunSeconds_Type()
)
intervalEncryptionSublayerPm15minEncryptionRunSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalEncryptionSublayerPm15minEncryptionRunSeconds.setStatus("current")
_IntervalEncryptionSublayerPm15minEncryptionRunErrorSeconds_Type = Unsigned32
_IntervalEncryptionSublayerPm15minEncryptionRunErrorSeconds_Object = MibTableColumn
intervalEncryptionSublayerPm15minEncryptionRunErrorSeconds = _IntervalEncryptionSublayerPm15minEncryptionRunErrorSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 1, 1, 3),
    _IntervalEncryptionSublayerPm15minEncryptionRunErrorSeconds_Type()
)
intervalEncryptionSublayerPm15minEncryptionRunErrorSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalEncryptionSublayerPm15minEncryptionRunErrorSeconds.setStatus("current")
_IntervalEncryptionSublayerPm15minEncryptionRunDegradeSeconds_Type = Unsigned32
_IntervalEncryptionSublayerPm15minEncryptionRunDegradeSeconds_Object = MibTableColumn
intervalEncryptionSublayerPm15minEncryptionRunDegradeSeconds = _IntervalEncryptionSublayerPm15minEncryptionRunDegradeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 1, 1, 4),
    _IntervalEncryptionSublayerPm15minEncryptionRunDegradeSeconds_Type()
)
intervalEncryptionSublayerPm15minEncryptionRunDegradeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalEncryptionSublayerPm15minEncryptionRunDegradeSeconds.setStatus("current")
_IntervalEncryptionSublayerPm15minValidFlag_Type = TruthValue
_IntervalEncryptionSublayerPm15minValidFlag_Object = MibTableColumn
intervalEncryptionSublayerPm15minValidFlag = _IntervalEncryptionSublayerPm15minValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 1, 1, 5),
    _IntervalEncryptionSublayerPm15minValidFlag_Type()
)
intervalEncryptionSublayerPm15minValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalEncryptionSublayerPm15minValidFlag.setStatus("current")
_IntervalEncryptionSublayerPm15minTimeStamp_Type = DateAndTime
_IntervalEncryptionSublayerPm15minTimeStamp_Object = MibTableColumn
intervalEncryptionSublayerPm15minTimeStamp = _IntervalEncryptionSublayerPm15minTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 1, 1, 6),
    _IntervalEncryptionSublayerPm15minTimeStamp_Type()
)
intervalEncryptionSublayerPm15minTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalEncryptionSublayerPm15minTimeStamp.setStatus("current")
_IntervalEncryptionSublayerPm1dayTable_Object = MibTable
intervalEncryptionSublayerPm1dayTable = _IntervalEncryptionSublayerPm1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 2)
)
if mibBuilder.loadTexts:
    intervalEncryptionSublayerPm1dayTable.setStatus("current")
_IntervalEncryptionSublayerPm1dayEntry_Object = MibTableRow
intervalEncryptionSublayerPm1dayEntry = _IntervalEncryptionSublayerPm1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 2, 1)
)
intervalEncryptionSublayerPm1dayEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
    (0, "ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "intervalEncryptionSublayerPm1dayNumber"),
)
if mibBuilder.loadTexts:
    intervalEncryptionSublayerPm1dayEntry.setStatus("current")


class _IntervalEncryptionSublayerPm1dayNumber_Type(Integer32):
    """Custom type intervalEncryptionSublayerPm1dayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_IntervalEncryptionSublayerPm1dayNumber_Type.__name__ = "Integer32"
_IntervalEncryptionSublayerPm1dayNumber_Object = MibTableColumn
intervalEncryptionSublayerPm1dayNumber = _IntervalEncryptionSublayerPm1dayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 2, 1, 1),
    _IntervalEncryptionSublayerPm1dayNumber_Type()
)
intervalEncryptionSublayerPm1dayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    intervalEncryptionSublayerPm1dayNumber.setStatus("current")
_IntervalEncryptionSublayerPm1dayEncryptionRunSeconds_Type = Unsigned32
_IntervalEncryptionSublayerPm1dayEncryptionRunSeconds_Object = MibTableColumn
intervalEncryptionSublayerPm1dayEncryptionRunSeconds = _IntervalEncryptionSublayerPm1dayEncryptionRunSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 2, 1, 2),
    _IntervalEncryptionSublayerPm1dayEncryptionRunSeconds_Type()
)
intervalEncryptionSublayerPm1dayEncryptionRunSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalEncryptionSublayerPm1dayEncryptionRunSeconds.setStatus("current")
_IntervalEncryptionSublayerPm1dayEncryptionRunErrorSeconds_Type = Unsigned32
_IntervalEncryptionSublayerPm1dayEncryptionRunErrorSeconds_Object = MibTableColumn
intervalEncryptionSublayerPm1dayEncryptionRunErrorSeconds = _IntervalEncryptionSublayerPm1dayEncryptionRunErrorSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 2, 1, 3),
    _IntervalEncryptionSublayerPm1dayEncryptionRunErrorSeconds_Type()
)
intervalEncryptionSublayerPm1dayEncryptionRunErrorSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalEncryptionSublayerPm1dayEncryptionRunErrorSeconds.setStatus("current")
_IntervalEncryptionSublayerPm1dayEncryptionRunDegradeSeconds_Type = Unsigned32
_IntervalEncryptionSublayerPm1dayEncryptionRunDegradeSeconds_Object = MibTableColumn
intervalEncryptionSublayerPm1dayEncryptionRunDegradeSeconds = _IntervalEncryptionSublayerPm1dayEncryptionRunDegradeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 2, 1, 4),
    _IntervalEncryptionSublayerPm1dayEncryptionRunDegradeSeconds_Type()
)
intervalEncryptionSublayerPm1dayEncryptionRunDegradeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalEncryptionSublayerPm1dayEncryptionRunDegradeSeconds.setStatus("current")
_IntervalEncryptionSublayerPm1dayValidFlag_Type = TruthValue
_IntervalEncryptionSublayerPm1dayValidFlag_Object = MibTableColumn
intervalEncryptionSublayerPm1dayValidFlag = _IntervalEncryptionSublayerPm1dayValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 2, 1, 5),
    _IntervalEncryptionSublayerPm1dayValidFlag_Type()
)
intervalEncryptionSublayerPm1dayValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalEncryptionSublayerPm1dayValidFlag.setStatus("current")
_IntervalEncryptionSublayerPm1dayTimeStamp_Type = DateAndTime
_IntervalEncryptionSublayerPm1dayTimeStamp_Object = MibTableColumn
intervalEncryptionSublayerPm1dayTimeStamp = _IntervalEncryptionSublayerPm1dayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 2, 1, 6),
    _IntervalEncryptionSublayerPm1dayTimeStamp_Type()
)
intervalEncryptionSublayerPm1dayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalEncryptionSublayerPm1dayTimeStamp.setStatus("current")
_CurrentEncryptionSublayerPm15minTable_Object = MibTable
currentEncryptionSublayerPm15minTable = _CurrentEncryptionSublayerPm15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 3)
)
if mibBuilder.loadTexts:
    currentEncryptionSublayerPm15minTable.setStatus("current")
_CurrentEncryptionSublayerPm15minEntry_Object = MibTableRow
currentEncryptionSublayerPm15minEntry = _CurrentEncryptionSublayerPm15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 3, 1)
)
currentEncryptionSublayerPm15minEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    currentEncryptionSublayerPm15minEntry.setStatus("current")
_CurrentEncryptionSublayerPm15minEncryptionRunSeconds_Type = Unsigned32
_CurrentEncryptionSublayerPm15minEncryptionRunSeconds_Object = MibTableColumn
currentEncryptionSublayerPm15minEncryptionRunSeconds = _CurrentEncryptionSublayerPm15minEncryptionRunSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 3, 1, 1),
    _CurrentEncryptionSublayerPm15minEncryptionRunSeconds_Type()
)
currentEncryptionSublayerPm15minEncryptionRunSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentEncryptionSublayerPm15minEncryptionRunSeconds.setStatus("current")
_CurrentEncryptionSublayerPm15minEncryptionRunErrorSeconds_Type = Unsigned32
_CurrentEncryptionSublayerPm15minEncryptionRunErrorSeconds_Object = MibTableColumn
currentEncryptionSublayerPm15minEncryptionRunErrorSeconds = _CurrentEncryptionSublayerPm15minEncryptionRunErrorSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 3, 1, 2),
    _CurrentEncryptionSublayerPm15minEncryptionRunErrorSeconds_Type()
)
currentEncryptionSublayerPm15minEncryptionRunErrorSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentEncryptionSublayerPm15minEncryptionRunErrorSeconds.setStatus("current")
_CurrentEncryptionSublayerPm15minEncryptionRunDegradeSeconds_Type = Unsigned32
_CurrentEncryptionSublayerPm15minEncryptionRunDegradeSeconds_Object = MibTableColumn
currentEncryptionSublayerPm15minEncryptionRunDegradeSeconds = _CurrentEncryptionSublayerPm15minEncryptionRunDegradeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 3, 1, 3),
    _CurrentEncryptionSublayerPm15minEncryptionRunDegradeSeconds_Type()
)
currentEncryptionSublayerPm15minEncryptionRunDegradeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentEncryptionSublayerPm15minEncryptionRunDegradeSeconds.setStatus("current")


class _CurrentEncryptionSublayerPm15minElapsedTime_Type(Integer32):
    """Custom type currentEncryptionSublayerPm15minElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CurrentEncryptionSublayerPm15minElapsedTime_Type.__name__ = "Integer32"
_CurrentEncryptionSublayerPm15minElapsedTime_Object = MibTableColumn
currentEncryptionSublayerPm15minElapsedTime = _CurrentEncryptionSublayerPm15minElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 3, 1, 4),
    _CurrentEncryptionSublayerPm15minElapsedTime_Type()
)
currentEncryptionSublayerPm15minElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentEncryptionSublayerPm15minElapsedTime.setStatus("current")
_CurrentEncryptionSublayerPm1dayTable_Object = MibTable
currentEncryptionSublayerPm1dayTable = _CurrentEncryptionSublayerPm1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 4)
)
if mibBuilder.loadTexts:
    currentEncryptionSublayerPm1dayTable.setStatus("current")
_CurrentEncryptionSublayerPm1dayEntry_Object = MibTableRow
currentEncryptionSublayerPm1dayEntry = _CurrentEncryptionSublayerPm1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 4, 1)
)
currentEncryptionSublayerPm1dayEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    currentEncryptionSublayerPm1dayEntry.setStatus("current")
_CurrentEncryptionSublayerPm1dayEncryptionRunSeconds_Type = Unsigned32
_CurrentEncryptionSublayerPm1dayEncryptionRunSeconds_Object = MibTableColumn
currentEncryptionSublayerPm1dayEncryptionRunSeconds = _CurrentEncryptionSublayerPm1dayEncryptionRunSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 4, 1, 1),
    _CurrentEncryptionSublayerPm1dayEncryptionRunSeconds_Type()
)
currentEncryptionSublayerPm1dayEncryptionRunSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentEncryptionSublayerPm1dayEncryptionRunSeconds.setStatus("current")
_CurrentEncryptionSublayerPm1dayEncryptionRunErrorSeconds_Type = Unsigned32
_CurrentEncryptionSublayerPm1dayEncryptionRunErrorSeconds_Object = MibTableColumn
currentEncryptionSublayerPm1dayEncryptionRunErrorSeconds = _CurrentEncryptionSublayerPm1dayEncryptionRunErrorSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 4, 1, 2),
    _CurrentEncryptionSublayerPm1dayEncryptionRunErrorSeconds_Type()
)
currentEncryptionSublayerPm1dayEncryptionRunErrorSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentEncryptionSublayerPm1dayEncryptionRunErrorSeconds.setStatus("current")
_CurrentEncryptionSublayerPm1dayEncryptionRunDegradeSeconds_Type = Unsigned32
_CurrentEncryptionSublayerPm1dayEncryptionRunDegradeSeconds_Object = MibTableColumn
currentEncryptionSublayerPm1dayEncryptionRunDegradeSeconds = _CurrentEncryptionSublayerPm1dayEncryptionRunDegradeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 4, 1, 3),
    _CurrentEncryptionSublayerPm1dayEncryptionRunDegradeSeconds_Type()
)
currentEncryptionSublayerPm1dayEncryptionRunDegradeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentEncryptionSublayerPm1dayEncryptionRunDegradeSeconds.setStatus("current")


class _CurrentEncryptionSublayerPm1dayElapsedTime_Type(Integer32):
    """Custom type currentEncryptionSublayerPm1dayElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CurrentEncryptionSublayerPm1dayElapsedTime_Type.__name__ = "Integer32"
_CurrentEncryptionSublayerPm1dayElapsedTime_Object = MibTableColumn
currentEncryptionSublayerPm1dayElapsedTime = _CurrentEncryptionSublayerPm1dayElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 4, 1, 4),
    _CurrentEncryptionSublayerPm1dayElapsedTime_Type()
)
currentEncryptionSublayerPm1dayElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentEncryptionSublayerPm1dayElapsedTime.setStatus("current")
_CryFacilityCurrent15minTable_Object = MibTable
cryFacilityCurrent15minTable = _CryFacilityCurrent15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 10)
)
if mibBuilder.loadTexts:
    cryFacilityCurrent15minTable.setStatus("current")
_CryFacilityCurrent15minEntry_Object = MibTableRow
cryFacilityCurrent15minEntry = _CryFacilityCurrent15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 10, 1)
)
cryFacilityCurrent15minEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    cryFacilityCurrent15minEntry.setStatus("current")
_CryFacilityCurrent15minEncryptionRunSeconds_Type = Unsigned32
_CryFacilityCurrent15minEncryptionRunSeconds_Object = MibTableColumn
cryFacilityCurrent15minEncryptionRunSeconds = _CryFacilityCurrent15minEncryptionRunSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 10, 1, 1),
    _CryFacilityCurrent15minEncryptionRunSeconds_Type()
)
cryFacilityCurrent15minEncryptionRunSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityCurrent15minEncryptionRunSeconds.setStatus("current")
_CryFacilityCurrent15minEncryptionRunErrorSeconds_Type = Unsigned32
_CryFacilityCurrent15minEncryptionRunErrorSeconds_Object = MibTableColumn
cryFacilityCurrent15minEncryptionRunErrorSeconds = _CryFacilityCurrent15minEncryptionRunErrorSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 10, 1, 2),
    _CryFacilityCurrent15minEncryptionRunErrorSeconds_Type()
)
cryFacilityCurrent15minEncryptionRunErrorSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityCurrent15minEncryptionRunErrorSeconds.setStatus("current")
_CryFacilityCurrent15minEncryptionRunDegradeSeconds_Type = Unsigned32
_CryFacilityCurrent15minEncryptionRunDegradeSeconds_Object = MibTableColumn
cryFacilityCurrent15minEncryptionRunDegradeSeconds = _CryFacilityCurrent15minEncryptionRunDegradeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 10, 1, 3),
    _CryFacilityCurrent15minEncryptionRunDegradeSeconds_Type()
)
cryFacilityCurrent15minEncryptionRunDegradeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityCurrent15minEncryptionRunDegradeSeconds.setStatus("current")


class _CryFacilityCurrent15minElapsedTime_Type(Integer32):
    """Custom type cryFacilityCurrent15minElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CryFacilityCurrent15minElapsedTime_Type.__name__ = "Integer32"
_CryFacilityCurrent15minElapsedTime_Object = MibTableColumn
cryFacilityCurrent15minElapsedTime = _CryFacilityCurrent15minElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 10, 1, 4),
    _CryFacilityCurrent15minElapsedTime_Type()
)
cryFacilityCurrent15minElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityCurrent15minElapsedTime.setStatus("current")
_CryFacilityCurrent1dayTable_Object = MibTable
cryFacilityCurrent1dayTable = _CryFacilityCurrent1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 11)
)
if mibBuilder.loadTexts:
    cryFacilityCurrent1dayTable.setStatus("current")
_CryFacilityCurrent1dayEntry_Object = MibTableRow
cryFacilityCurrent1dayEntry = _CryFacilityCurrent1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 11, 1)
)
cryFacilityCurrent1dayEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    cryFacilityCurrent1dayEntry.setStatus("current")
_CryFacilityCurrent1dayEncryptionRunSeconds_Type = Unsigned32
_CryFacilityCurrent1dayEncryptionRunSeconds_Object = MibTableColumn
cryFacilityCurrent1dayEncryptionRunSeconds = _CryFacilityCurrent1dayEncryptionRunSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 11, 1, 1),
    _CryFacilityCurrent1dayEncryptionRunSeconds_Type()
)
cryFacilityCurrent1dayEncryptionRunSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityCurrent1dayEncryptionRunSeconds.setStatus("current")
_CryFacilityCurrent1dayEncryptionRunErrorSeconds_Type = Unsigned32
_CryFacilityCurrent1dayEncryptionRunErrorSeconds_Object = MibTableColumn
cryFacilityCurrent1dayEncryptionRunErrorSeconds = _CryFacilityCurrent1dayEncryptionRunErrorSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 11, 1, 2),
    _CryFacilityCurrent1dayEncryptionRunErrorSeconds_Type()
)
cryFacilityCurrent1dayEncryptionRunErrorSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityCurrent1dayEncryptionRunErrorSeconds.setStatus("current")
_CryFacilityCurrent1dayEncryptionRunDegradeSeconds_Type = Unsigned32
_CryFacilityCurrent1dayEncryptionRunDegradeSeconds_Object = MibTableColumn
cryFacilityCurrent1dayEncryptionRunDegradeSeconds = _CryFacilityCurrent1dayEncryptionRunDegradeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 11, 1, 3),
    _CryFacilityCurrent1dayEncryptionRunDegradeSeconds_Type()
)
cryFacilityCurrent1dayEncryptionRunDegradeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityCurrent1dayEncryptionRunDegradeSeconds.setStatus("current")


class _CryFacilityCurrent1dayElapsedTime_Type(Integer32):
    """Custom type cryFacilityCurrent1dayElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CryFacilityCurrent1dayElapsedTime_Type.__name__ = "Integer32"
_CryFacilityCurrent1dayElapsedTime_Object = MibTableColumn
cryFacilityCurrent1dayElapsedTime = _CryFacilityCurrent1dayElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 11, 1, 4),
    _CryFacilityCurrent1dayElapsedTime_Type()
)
cryFacilityCurrent1dayElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityCurrent1dayElapsedTime.setStatus("current")
_CryFacilityHistorical15minTable_Object = MibTable
cryFacilityHistorical15minTable = _CryFacilityHistorical15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 12)
)
if mibBuilder.loadTexts:
    cryFacilityHistorical15minTable.setStatus("current")
_CryFacilityHistorical15minEntry_Object = MibTableRow
cryFacilityHistorical15minEntry = _CryFacilityHistorical15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 12, 1)
)
cryFacilityHistorical15minEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
    (0, "ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryFacilityHistorical15minNumber"),
)
if mibBuilder.loadTexts:
    cryFacilityHistorical15minEntry.setStatus("current")


class _CryFacilityHistorical15minNumber_Type(Integer32):
    """Custom type cryFacilityHistorical15minNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CryFacilityHistorical15minNumber_Type.__name__ = "Integer32"
_CryFacilityHistorical15minNumber_Object = MibTableColumn
cryFacilityHistorical15minNumber = _CryFacilityHistorical15minNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 12, 1, 1),
    _CryFacilityHistorical15minNumber_Type()
)
cryFacilityHistorical15minNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cryFacilityHistorical15minNumber.setStatus("current")
_CryFacilityHistorical15minEncryptionRunSeconds_Type = Unsigned32
_CryFacilityHistorical15minEncryptionRunSeconds_Object = MibTableColumn
cryFacilityHistorical15minEncryptionRunSeconds = _CryFacilityHistorical15minEncryptionRunSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 12, 1, 2),
    _CryFacilityHistorical15minEncryptionRunSeconds_Type()
)
cryFacilityHistorical15minEncryptionRunSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityHistorical15minEncryptionRunSeconds.setStatus("current")
_CryFacilityHistorical15minEncryptionRunErrorSeconds_Type = Unsigned32
_CryFacilityHistorical15minEncryptionRunErrorSeconds_Object = MibTableColumn
cryFacilityHistorical15minEncryptionRunErrorSeconds = _CryFacilityHistorical15minEncryptionRunErrorSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 12, 1, 3),
    _CryFacilityHistorical15minEncryptionRunErrorSeconds_Type()
)
cryFacilityHistorical15minEncryptionRunErrorSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityHistorical15minEncryptionRunErrorSeconds.setStatus("current")
_CryFacilityHistorical15minEncryptionRunDegradeSeconds_Type = Unsigned32
_CryFacilityHistorical15minEncryptionRunDegradeSeconds_Object = MibTableColumn
cryFacilityHistorical15minEncryptionRunDegradeSeconds = _CryFacilityHistorical15minEncryptionRunDegradeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 12, 1, 4),
    _CryFacilityHistorical15minEncryptionRunDegradeSeconds_Type()
)
cryFacilityHistorical15minEncryptionRunDegradeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityHistorical15minEncryptionRunDegradeSeconds.setStatus("current")
_CryFacilityHistorical15minValidFlag_Type = TruthValue
_CryFacilityHistorical15minValidFlag_Object = MibTableColumn
cryFacilityHistorical15minValidFlag = _CryFacilityHistorical15minValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 12, 1, 5),
    _CryFacilityHistorical15minValidFlag_Type()
)
cryFacilityHistorical15minValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityHistorical15minValidFlag.setStatus("current")
_CryFacilityHistorical15minTimeStamp_Type = DateAndTime
_CryFacilityHistorical15minTimeStamp_Object = MibTableColumn
cryFacilityHistorical15minTimeStamp = _CryFacilityHistorical15minTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 12, 1, 6),
    _CryFacilityHistorical15minTimeStamp_Type()
)
cryFacilityHistorical15minTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityHistorical15minTimeStamp.setStatus("current")
_CryFacilityHistorical1dayTable_Object = MibTable
cryFacilityHistorical1dayTable = _CryFacilityHistorical1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 13)
)
if mibBuilder.loadTexts:
    cryFacilityHistorical1dayTable.setStatus("current")
_CryFacilityHistorical1dayEntry_Object = MibTableRow
cryFacilityHistorical1dayEntry = _CryFacilityHistorical1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 13, 1)
)
cryFacilityHistorical1dayEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
    (0, "ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryFacilityHistorical1dayNumber"),
)
if mibBuilder.loadTexts:
    cryFacilityHistorical1dayEntry.setStatus("current")


class _CryFacilityHistorical1dayNumber_Type(Integer32):
    """Custom type cryFacilityHistorical1dayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CryFacilityHistorical1dayNumber_Type.__name__ = "Integer32"
_CryFacilityHistorical1dayNumber_Object = MibTableColumn
cryFacilityHistorical1dayNumber = _CryFacilityHistorical1dayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 13, 1, 1),
    _CryFacilityHistorical1dayNumber_Type()
)
cryFacilityHistorical1dayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cryFacilityHistorical1dayNumber.setStatus("current")
_CryFacilityHistorical1dayEncryptionRunSeconds_Type = Unsigned32
_CryFacilityHistorical1dayEncryptionRunSeconds_Object = MibTableColumn
cryFacilityHistorical1dayEncryptionRunSeconds = _CryFacilityHistorical1dayEncryptionRunSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 13, 1, 2),
    _CryFacilityHistorical1dayEncryptionRunSeconds_Type()
)
cryFacilityHistorical1dayEncryptionRunSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityHistorical1dayEncryptionRunSeconds.setStatus("current")
_CryFacilityHistorical1dayEncryptionRunErrorSeconds_Type = Unsigned32
_CryFacilityHistorical1dayEncryptionRunErrorSeconds_Object = MibTableColumn
cryFacilityHistorical1dayEncryptionRunErrorSeconds = _CryFacilityHistorical1dayEncryptionRunErrorSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 13, 1, 3),
    _CryFacilityHistorical1dayEncryptionRunErrorSeconds_Type()
)
cryFacilityHistorical1dayEncryptionRunErrorSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityHistorical1dayEncryptionRunErrorSeconds.setStatus("current")
_CryFacilityHistorical1dayEncryptionRunDegradeSeconds_Type = Unsigned32
_CryFacilityHistorical1dayEncryptionRunDegradeSeconds_Object = MibTableColumn
cryFacilityHistorical1dayEncryptionRunDegradeSeconds = _CryFacilityHistorical1dayEncryptionRunDegradeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 13, 1, 4),
    _CryFacilityHistorical1dayEncryptionRunDegradeSeconds_Type()
)
cryFacilityHistorical1dayEncryptionRunDegradeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityHistorical1dayEncryptionRunDegradeSeconds.setStatus("current")
_CryFacilityHistorical1dayValidFlag_Type = TruthValue
_CryFacilityHistorical1dayValidFlag_Object = MibTableColumn
cryFacilityHistorical1dayValidFlag = _CryFacilityHistorical1dayValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 13, 1, 5),
    _CryFacilityHistorical1dayValidFlag_Type()
)
cryFacilityHistorical1dayValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityHistorical1dayValidFlag.setStatus("current")
_CryFacilityHistorical1dayTimeStamp_Type = DateAndTime
_CryFacilityHistorical1dayTimeStamp_Object = MibTableColumn
cryFacilityHistorical1dayTimeStamp = _CryFacilityHistorical1dayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 4, 13, 1, 6),
    _CryFacilityHistorical1dayTimeStamp_Type()
)
cryFacilityHistorical1dayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryFacilityHistorical1dayTimeStamp.setStatus("current")

# Managed Objects groups

encryptionMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 1, 2, 1)
)
encryptionMIBGroup.setObjects(
      *(("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoOfficerPassword"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoModuleConfigCryptoOfficerPassword"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoModuleConfigResetToFactory"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoModuleConfigFirmwareUpdateState"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoModuleConfigFirmwareVersion"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoModuleStatusFailureLoginCount"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoModuleStatusSuccessfulLoginDateAndTime"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoModuleStatusUnsuccessfulLoginDateAndTime"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoPortConfigAuthKey"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoPortConfigAuthKeyLifeTime"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoPortConfigEncryptionOffState"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoPortConfigEncryptionOff"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoPortConfigForceKeyExchange"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoPortConfigKeyExchangeForcedClear"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoPortStatusEncryptionOffTimeRemaining"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoPortStatusFailureKeyExchangeCount"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoPortStatusSuccessfulKeyExchangeDateAndTime"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoPortStatusUnsuccessfulKeyExchangeDateAndTime"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "cryptoPortStatusAuthKeyLifeTimeRemaining"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "intervalEncryptionSublayerPm15minEncryptionRunSeconds"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "intervalEncryptionSublayerPm15minEncryptionRunErrorSeconds"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "intervalEncryptionSublayerPm15minEncryptionRunDegradeSeconds"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "intervalEncryptionSublayerPm15minValidFlag"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "intervalEncryptionSublayerPm15minTimeStamp"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "intervalEncryptionSublayerPm1dayEncryptionRunSeconds"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "intervalEncryptionSublayerPm1dayEncryptionRunErrorSeconds"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "intervalEncryptionSublayerPm1dayEncryptionRunDegradeSeconds"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "intervalEncryptionSublayerPm1dayValidFlag"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "intervalEncryptionSublayerPm1dayTimeStamp"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "currentEncryptionSublayerPm15minEncryptionRunSeconds"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "currentEncryptionSublayerPm15minEncryptionRunErrorSeconds"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "currentEncryptionSublayerPm15minEncryptionRunDegradeSeconds"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "currentEncryptionSublayerPm15minElapsedTime"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "currentEncryptionSublayerPm1dayEncryptionRunSeconds"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "currentEncryptionSublayerPm1dayEncryptionRunErrorSeconds"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "currentEncryptionSublayerPm1dayEncryptionRunDegradeSeconds"),
        ("ADVA-FSPR7-MODULE-ENCRYPTION-MIB", "currentEncryptionSublayerPm1dayElapsedTime"))
)
if mibBuilder.loadTexts:
    encryptionMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

encryptionMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 5, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    encryptionMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADVA-FSPR7-MODULE-ENCRYPTION-MIB",
    **{"CryptoFspR7EnableDisable": CryptoFspR7EnableDisable,
       "CryptoFspR7EnableDisableCaps": CryptoFspR7EnableDisableCaps,
       "CryptoFspR7EncryptionReset": CryptoFspR7EncryptionReset,
       "CryptoFspR7EncryptionResetCaps": CryptoFspR7EncryptionResetCaps,
       "CryptoFspR7EncryptionSwitch": CryptoFspR7EncryptionSwitch,
       "CryptoFspR7EncryptionSwitchCaps": CryptoFspR7EncryptionSwitchCaps,
       "CryptoFspR7ForceKeyExchange": CryptoFspR7ForceKeyExchange,
       "CryptoFspR7ForceKeyExchangeCaps": CryptoFspR7ForceKeyExchangeCaps,
       "CryptoFspR7KeyExchangeForcedClear": CryptoFspR7KeyExchangeForcedClear,
       "CryptoFspR7KeyExchangeForcedClearCaps": CryptoFspR7KeyExchangeForcedClearCaps,
       "CryptoFspR7SelfTestOperation": CryptoFspR7SelfTestOperation,
       "CryptoFspR7SelfTestOperationCaps": CryptoFspR7SelfTestOperationCaps,
       "CryptoFspR7SessionKeyLifetime": CryptoFspR7SessionKeyLifetime,
       "CryptoFspR7SessionKeyLifetimeCaps": CryptoFspR7SessionKeyLifetimeCaps,
       "moduleEncryptionMIB": moduleEncryptionMIB,
       "encryptionMIB": encryptionMIB,
       "encryptionMIBConformance": encryptionMIBConformance,
       "encryptionMIBCompliances": encryptionMIBCompliances,
       "encryptionMIBCompliance": encryptionMIBCompliance,
       "encryptionMIBGroups": encryptionMIBGroups,
       "encryptionMIBGroup": encryptionMIBGroup,
       "moduleEncryptionObjects": moduleEncryptionObjects,
       "cryptoOfficerPassword": cryptoOfficerPassword,
       "cryptoOfficerPasswordError": cryptoOfficerPasswordError,
       "cryptoOfficerPasswordReqId": cryptoOfficerPasswordReqId,
       "cryptoModuleConfigTable": cryptoModuleConfigTable,
       "cryptoModuleConfigEntry": cryptoModuleConfigEntry,
       "cryptoModuleConfigIndex": cryptoModuleConfigIndex,
       "cryptoModuleConfigCryptoOfficerPassword": cryptoModuleConfigCryptoOfficerPassword,
       "cryptoModuleConfigResetToFactory": cryptoModuleConfigResetToFactory,
       "cryptoModuleConfigFirmwareUpdateState": cryptoModuleConfigFirmwareUpdateState,
       "cryptoModuleConfigFirmwareVersion": cryptoModuleConfigFirmwareVersion,
       "cryptoModuleConfigSelfTestOperation": cryptoModuleConfigSelfTestOperation,
       "cryptoModuleStatusTable": cryptoModuleStatusTable,
       "cryptoModuleStatusEntry": cryptoModuleStatusEntry,
       "cryptoModuleStatusIndex": cryptoModuleStatusIndex,
       "cryptoModuleStatusFailureLoginCount": cryptoModuleStatusFailureLoginCount,
       "cryptoModuleStatusSuccessfulLoginDateAndTime": cryptoModuleStatusSuccessfulLoginDateAndTime,
       "cryptoModuleStatusUnsuccessfulLoginDateAndTime": cryptoModuleStatusUnsuccessfulLoginDateAndTime,
       "cryptoModuleStatusResetToFactoryCapability": cryptoModuleStatusResetToFactoryCapability,
       "cryptoModuleTable": cryptoModuleTable,
       "cryptoModuleEntry": cryptoModuleEntry,
       "cryptoModuleCryptoOfficerPassword": cryptoModuleCryptoOfficerPassword,
       "cryptoModuleResetToFactory": cryptoModuleResetToFactory,
       "cryptoModuleFirmwareUpdateState": cryptoModuleFirmwareUpdateState,
       "cryptoModuleFirmwareVersion": cryptoModuleFirmwareVersion,
       "cryptoModuleSelfTestOperation": cryptoModuleSelfTestOperation,
       "cryptoModuleFailureLoginCount": cryptoModuleFailureLoginCount,
       "cryptoModuleSuccessfulLoginDateAndTime": cryptoModuleSuccessfulLoginDateAndTime,
       "cryptoModuleUnsuccessfulLoginDateAndTime": cryptoModuleUnsuccessfulLoginDateAndTime,
       "cryptoModuleCapTable": cryptoModuleCapTable,
       "cryptoModuleCapEntry": cryptoModuleCapEntry,
       "cryptoModuleCapCryptoOfficerPassword": cryptoModuleCapCryptoOfficerPassword,
       "cryptoModuleCapResetToFactory": cryptoModuleCapResetToFactory,
       "cryptoModuleCapFirmwareUpdateState": cryptoModuleCapFirmwareUpdateState,
       "cryptoModuleCapFirmwareVersion": cryptoModuleCapFirmwareVersion,
       "cryptoModuleCapSelfTestOperation": cryptoModuleCapSelfTestOperation,
       "portEncryptionObjects": portEncryptionObjects,
       "cryptoPortConfigTable": cryptoPortConfigTable,
       "cryptoPortConfigEntry": cryptoPortConfigEntry,
       "cryptoPortConfigIndex": cryptoPortConfigIndex,
       "cryptoPortConfigAuthKey": cryptoPortConfigAuthKey,
       "cryptoPortConfigAuthKeyLifeTime": cryptoPortConfigAuthKeyLifeTime,
       "cryptoPortConfigEncryptionOffState": cryptoPortConfigEncryptionOffState,
       "cryptoPortConfigEncryptionOff": cryptoPortConfigEncryptionOff,
       "cryptoPortConfigForceKeyExchange": cryptoPortConfigForceKeyExchange,
       "cryptoPortConfigKeyExchangeForcedClear": cryptoPortConfigKeyExchangeForcedClear,
       "cryptoPortStatusTable": cryptoPortStatusTable,
       "cryptoPortStatusEntry": cryptoPortStatusEntry,
       "cryptoPortStatusIndex": cryptoPortStatusIndex,
       "cryptoPortStatusEncryptionOffTimeRemaining": cryptoPortStatusEncryptionOffTimeRemaining,
       "cryptoPortStatusFailureKeyExchangeCount": cryptoPortStatusFailureKeyExchangeCount,
       "cryptoPortStatusSuccessfulKeyExchangeDateAndTime": cryptoPortStatusSuccessfulKeyExchangeDateAndTime,
       "cryptoPortStatusUnsuccessfulKeyExchangeDateAndTime": cryptoPortStatusUnsuccessfulKeyExchangeDateAndTime,
       "cryptoPortStatusAuthKeyLifeTimeRemaining": cryptoPortStatusAuthKeyLifeTimeRemaining,
       "cryptoPortStatusEncryptionOffCapability": cryptoPortStatusEncryptionOffCapability,
       "cryptoPortTable": cryptoPortTable,
       "cryptoPortEntry": cryptoPortEntry,
       "cryptoPortAuthKey": cryptoPortAuthKey,
       "cryptoPortAuthKeyLifeTime": cryptoPortAuthKeyLifeTime,
       "cryptoPortEncryptionOffState": cryptoPortEncryptionOffState,
       "cryptoPortEncryptionOff": cryptoPortEncryptionOff,
       "cryptoPortForceKeyExchange": cryptoPortForceKeyExchange,
       "cryptoPortKeyExchangeForcedClear": cryptoPortKeyExchangeForcedClear,
       "cryptoPortEncryptionOffTimeRemaining": cryptoPortEncryptionOffTimeRemaining,
       "cryptoPortFailureKeyExchangeCount": cryptoPortFailureKeyExchangeCount,
       "cryptoPortSuccessfulKeyExchangeDateAndTime": cryptoPortSuccessfulKeyExchangeDateAndTime,
       "cryptoPortUnsuccessfulKeyExchangeDateAndTime": cryptoPortUnsuccessfulKeyExchangeDateAndTime,
       "cryptoPortAuthKeyLifeTimeRemaining": cryptoPortAuthKeyLifeTimeRemaining,
       "cryptoPortCapTable": cryptoPortCapTable,
       "cryptoPortCapEntry": cryptoPortCapEntry,
       "cryptoPortCapAuthKey": cryptoPortCapAuthKey,
       "cryptoPortCapAuthKeyLifeTime": cryptoPortCapAuthKeyLifeTime,
       "cryptoPortCapEncryptionOffState": cryptoPortCapEncryptionOffState,
       "cryptoPortCapEncryptionOff": cryptoPortCapEncryptionOff,
       "cryptoPortCapForceKeyExchange": cryptoPortCapForceKeyExchange,
       "cryptoPortCapKeyExchangeForcedClear": cryptoPortCapKeyExchangeForcedClear,
       "encryptionPerformanceMonitoring": encryptionPerformanceMonitoring,
       "intervalEncryptionSublayerPm15minTable": intervalEncryptionSublayerPm15minTable,
       "intervalEncryptionSublayerPm15minEntry": intervalEncryptionSublayerPm15minEntry,
       "intervalEncryptionSublayerPm15minNumber": intervalEncryptionSublayerPm15minNumber,
       "intervalEncryptionSublayerPm15minEncryptionRunSeconds": intervalEncryptionSublayerPm15minEncryptionRunSeconds,
       "intervalEncryptionSublayerPm15minEncryptionRunErrorSeconds": intervalEncryptionSublayerPm15minEncryptionRunErrorSeconds,
       "intervalEncryptionSublayerPm15minEncryptionRunDegradeSeconds": intervalEncryptionSublayerPm15minEncryptionRunDegradeSeconds,
       "intervalEncryptionSublayerPm15minValidFlag": intervalEncryptionSublayerPm15minValidFlag,
       "intervalEncryptionSublayerPm15minTimeStamp": intervalEncryptionSublayerPm15minTimeStamp,
       "intervalEncryptionSublayerPm1dayTable": intervalEncryptionSublayerPm1dayTable,
       "intervalEncryptionSublayerPm1dayEntry": intervalEncryptionSublayerPm1dayEntry,
       "intervalEncryptionSublayerPm1dayNumber": intervalEncryptionSublayerPm1dayNumber,
       "intervalEncryptionSublayerPm1dayEncryptionRunSeconds": intervalEncryptionSublayerPm1dayEncryptionRunSeconds,
       "intervalEncryptionSublayerPm1dayEncryptionRunErrorSeconds": intervalEncryptionSublayerPm1dayEncryptionRunErrorSeconds,
       "intervalEncryptionSublayerPm1dayEncryptionRunDegradeSeconds": intervalEncryptionSublayerPm1dayEncryptionRunDegradeSeconds,
       "intervalEncryptionSublayerPm1dayValidFlag": intervalEncryptionSublayerPm1dayValidFlag,
       "intervalEncryptionSublayerPm1dayTimeStamp": intervalEncryptionSublayerPm1dayTimeStamp,
       "currentEncryptionSublayerPm15minTable": currentEncryptionSublayerPm15minTable,
       "currentEncryptionSublayerPm15minEntry": currentEncryptionSublayerPm15minEntry,
       "currentEncryptionSublayerPm15minEncryptionRunSeconds": currentEncryptionSublayerPm15minEncryptionRunSeconds,
       "currentEncryptionSublayerPm15minEncryptionRunErrorSeconds": currentEncryptionSublayerPm15minEncryptionRunErrorSeconds,
       "currentEncryptionSublayerPm15minEncryptionRunDegradeSeconds": currentEncryptionSublayerPm15minEncryptionRunDegradeSeconds,
       "currentEncryptionSublayerPm15minElapsedTime": currentEncryptionSublayerPm15minElapsedTime,
       "currentEncryptionSublayerPm1dayTable": currentEncryptionSublayerPm1dayTable,
       "currentEncryptionSublayerPm1dayEntry": currentEncryptionSublayerPm1dayEntry,
       "currentEncryptionSublayerPm1dayEncryptionRunSeconds": currentEncryptionSublayerPm1dayEncryptionRunSeconds,
       "currentEncryptionSublayerPm1dayEncryptionRunErrorSeconds": currentEncryptionSublayerPm1dayEncryptionRunErrorSeconds,
       "currentEncryptionSublayerPm1dayEncryptionRunDegradeSeconds": currentEncryptionSublayerPm1dayEncryptionRunDegradeSeconds,
       "currentEncryptionSublayerPm1dayElapsedTime": currentEncryptionSublayerPm1dayElapsedTime,
       "cryFacilityCurrent15minTable": cryFacilityCurrent15minTable,
       "cryFacilityCurrent15minEntry": cryFacilityCurrent15minEntry,
       "cryFacilityCurrent15minEncryptionRunSeconds": cryFacilityCurrent15minEncryptionRunSeconds,
       "cryFacilityCurrent15minEncryptionRunErrorSeconds": cryFacilityCurrent15minEncryptionRunErrorSeconds,
       "cryFacilityCurrent15minEncryptionRunDegradeSeconds": cryFacilityCurrent15minEncryptionRunDegradeSeconds,
       "cryFacilityCurrent15minElapsedTime": cryFacilityCurrent15minElapsedTime,
       "cryFacilityCurrent1dayTable": cryFacilityCurrent1dayTable,
       "cryFacilityCurrent1dayEntry": cryFacilityCurrent1dayEntry,
       "cryFacilityCurrent1dayEncryptionRunSeconds": cryFacilityCurrent1dayEncryptionRunSeconds,
       "cryFacilityCurrent1dayEncryptionRunErrorSeconds": cryFacilityCurrent1dayEncryptionRunErrorSeconds,
       "cryFacilityCurrent1dayEncryptionRunDegradeSeconds": cryFacilityCurrent1dayEncryptionRunDegradeSeconds,
       "cryFacilityCurrent1dayElapsedTime": cryFacilityCurrent1dayElapsedTime,
       "cryFacilityHistorical15minTable": cryFacilityHistorical15minTable,
       "cryFacilityHistorical15minEntry": cryFacilityHistorical15minEntry,
       "cryFacilityHistorical15minNumber": cryFacilityHistorical15minNumber,
       "cryFacilityHistorical15minEncryptionRunSeconds": cryFacilityHistorical15minEncryptionRunSeconds,
       "cryFacilityHistorical15minEncryptionRunErrorSeconds": cryFacilityHistorical15minEncryptionRunErrorSeconds,
       "cryFacilityHistorical15minEncryptionRunDegradeSeconds": cryFacilityHistorical15minEncryptionRunDegradeSeconds,
       "cryFacilityHistorical15minValidFlag": cryFacilityHistorical15minValidFlag,
       "cryFacilityHistorical15minTimeStamp": cryFacilityHistorical15minTimeStamp,
       "cryFacilityHistorical1dayTable": cryFacilityHistorical1dayTable,
       "cryFacilityHistorical1dayEntry": cryFacilityHistorical1dayEntry,
       "cryFacilityHistorical1dayNumber": cryFacilityHistorical1dayNumber,
       "cryFacilityHistorical1dayEncryptionRunSeconds": cryFacilityHistorical1dayEncryptionRunSeconds,
       "cryFacilityHistorical1dayEncryptionRunErrorSeconds": cryFacilityHistorical1dayEncryptionRunErrorSeconds,
       "cryFacilityHistorical1dayEncryptionRunDegradeSeconds": cryFacilityHistorical1dayEncryptionRunDegradeSeconds,
       "cryFacilityHistorical1dayValidFlag": cryFacilityHistorical1dayValidFlag,
       "cryFacilityHistorical1dayTimeStamp": cryFacilityHistorical1dayTimeStamp}
)
