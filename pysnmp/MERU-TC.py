# SNMP MIB module (MERU-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:59 2024
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

(meru_modules,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "meru-modules")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

meruTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MwlAclEnvState(Integer32, TextualConvention):
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
        *(("aclEnvAllow", 1),
          ("aclEnvDeny", 2),
          ("aclEnvDisabled", 0))
    )



class MwlAddressAssignmentType(Integer32, TextualConvention):
    status = "current"
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
        *(("ipAssignmentDynamic", 2),
          ("ipAssignmentDynamicDhcp", 3),
          ("ipAssignmentStatic", 1),
          ("ipAssignmentUnknown", 4))
    )



class MwlAddressIfAssignmentType(Integer32, TextualConvention):
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
        *(("ifIpAssignmentDhcp", 2),
          ("ifIpAssignmentNone", 0),
          ("ifIpAssignmentStatic", 1))
    )



class MwlApIpAssignmentType(Integer32, TextualConvention):
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
        *(("apIpAssignmentDhcp", 2),
          ("apIpAssignmentNone", 0),
          ("apIpAssignmentStatic", 1))
    )



class MwlAdministrativeState(Integer32, TextualConvention):
    status = "current"
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
        *(("adminStateForceShuttingDown", 5),
          ("adminStateLocked", 2),
          ("adminStateShuttingDown", 3),
          ("adminStateUnknown", 4),
          ("adminStateUnlocked", 1))
    )



class MwlAdmissionControl(Integer32, TextualConvention):
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
        *(("admitall", 0),
          ("pendingflag", 1),
          ("rejectflag", 2))
    )



class MwlAntennaSet(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("antennaSetExternal", 2),
          ("antennaSetExternalDualMode", 3),
          ("antennaSetInternal", 1),
          ("antennaSetRsAntenna", 4),
          ("antennaSetUnknown", 0))
    )



class MwlApAssignType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assignApUnknown", 0),
          ("assignedAp", 2),
          ("discoveredAp", 3),
          ("siblingAp", 1))
    )



class MwlApType(Integer32, TextualConvention):
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
        *(("apAccessPoint", 2),
          ("apStation", 1),
          ("apUnknown", 0))
    )



class MwlApIndoorOutdoorType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("apIndoor", 0),
          ("apOutdoor", 1))
    )



class MwlApMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              100)
        )
    )
    namedValues = NamedValues(
        *(("apModeNormal", 1),
          ("apModeScanning", 100))
    )



class MwlAuthenticationAlgorithm(Integer32, TextualConvention):
    status = "current"
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
        *(("nmsAuthenticationAlg8021x", 1),
          ("nmsAuthenticationAlgMd5", 2),
          ("nmsAuthenticationAlgPeap", 5),
          ("nmsAuthenticationAlgTls", 3),
          ("nmsAuthenticationAlgTtls", 4),
          ("nmsAuthenticationAlgWeb", 6))
    )



class MwlAuthenticationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nmsAuthenticationTypeLocal", 1),
          ("nmsAuthenticationTypeRadius", 2),
          ("nmsAuthenticationTypeTacacs", 3))
    )



class MwlCaptivePortalAuthenticationType(Integer32, TextualConvention):
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
        *(("nmsCaptivePortalAuthenticationTypeLocal", 1),
          ("nmsCaptivePortalAuthenticationTypeLocalRadius", 2),
          ("nmsCaptivePortalAuthenticationTypeRadius", 0))
    )



class MwlAuthSuiteBits(Bits, TextualConvention):
    status = "current"


class MwlActionStatus(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("actionDone", 5),
          ("actionError", 4),
          ("actionForceStart", 6),
          ("actionInProgress", 3),
          ("actionNone", 0),
          ("actionStart", 1),
          ("actionStop", 2))
    )



class MwlAlarmState(Integer32, TextualConvention):
    status = "current"
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
        *(("alarmStateCritical", 4),
          ("alarmStateMajor", 3),
          ("alarmStateMinor", 2),
          ("alarmStateNoAlarm", 1))
    )



class MwlAlarmType(Integer32, TextualConvention):
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
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48)
        )
    )
    namedValues = NamedValues(
        *(("alarm8021xAuthAttempt", 42),
          ("alarm8021xAuthFailure", 28),
          ("alarmAcctRadiusServerSwitchover", 34),
          ("alarmAcctRadiusServerSwitchoverFailed", 35),
          ("alarmApBootimageVersionMismatch", 22),
          ("alarmApDown", 7),
          ("alarmApInitFailure", 25),
          ("alarmApNeighborLoss", 8),
          ("alarmApRuntimeError", 47),
          ("alarmApSoftwareVersionMismatch", 21),
          ("alarmApTemperature", 23),
          ("alarmAscApAdd", 13),
          ("alarmAscApModify", 15),
          ("alarmAscApRemove", 14),
          ("alarmAscDown", 6),
          ("alarmAuthFail", 5),
          ("alarmCacLimitReached", 39),
          ("alarmColdStart", 3),
          ("alarmHandOffFail", 9),
          ("alarmHardwareDiagnostic", 24),
          ("alarmLicensingServerDown", 44),
          ("alarmLinkDown", 2),
          ("alarmLinkUp", 1),
          ("alarmMacFilterDeny", 38),
          ("alarmMasterDown", 36),
          ("alarmMasterUp", 37),
          ("alarmMicCountermeasureActivation", 30),
          ("alarmMicFailureAp", 29),
          ("alarmNoLicenseEnforcementExpired", 46),
          ("alarmNupgradeLicenseCheckoutFail", 45),
          ("alarmOperChannelChange", 41),
          ("alarmPrimaryRadiusServerRestored", 33),
          ("alarmRadarDetected", 40),
          ("alarmRadioCardFailure", 26),
          ("alarmRadiusServerSwitchover", 31),
          ("alarmRadiusServerSwitchoverFailed", 32),
          ("alarmResourceThresholdExceed", 10),
          ("alarmRogueApDetected", 19),
          ("alarmSoftwareLicenseExpired", 27),
          ("alarmStaApAdd", 16),
          ("alarmStaApModify", 18),
          ("alarmStaApRemove", 17),
          ("alarmSystemFailure", 11),
          ("alarmTotal", 48),
          ("alarmUnknown", 0),
          ("alarmWarmStart", 4),
          ("alarmWatchdogFailure", 12),
          ("alarmWirelessAssoc", 43),
          ("alarmWncCertError", 20))
    )



class MwlAlarmSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alarmSevClear", 4),
          ("alarmSevCritical", 3),
          ("alarmSevInfo", 0),
          ("alarmSevMajor", 1),
          ("alarmSevMinor", 2))
    )



class MwlAntenna(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("antenna1", 1),
          ("antenna2", 2),
          ("antennaAll", 4),
          ("antennaBoth", 3),
          ("antennaNothing", 0))
    )



class MwlAssignmentAlgorithm(Integer32, TextualConvention):
    status = "current"
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
        *(("assignmentAlgoActivity", 3),
          ("assignmentAlgoAvailRsrc", 5),
          ("assignmentAlgoPressure", 2),
          ("assignmentAlgoRssi", 1),
          ("assignmentAlgoRssiTrending", 4),
          ("assignmentAlgoUnknown", 6))
    )



class MwlAssociationState(Integer32, TextualConvention):
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
        *(("assocstateassociated", 2),
          ("assocstateauthentication", 1),
          ("assocstateprobing", 0))
    )



class MwlApAuthState(Integer32, TextualConvention):
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
        *(("apAuthKeyed", 0),
          ("apAuthNokey", 1),
          ("apUnauth", 2))
    )



class MwlAvailabilityStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("availStatusFailed", 4),
          ("availStatusInTest", 5),
          ("availStatusNotInstalled", 6),
          ("availStatusOffline", 2),
          ("availStatusOnline", 3),
          ("availStatusPowerOff", 1))
    )



class MwlBeaconCoordinationMode(Integer32, TextualConvention):
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
        *(("beaconCoordinationModeCoordinated", 0),
          ("beaconCoordinationModeDistributed", 2),
          ("beaconCoordinationModeLocal", 1))
    )



class MwlBlock(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blockAll", 2),
          ("blockNone", 0),
          ("blockSelected", 1),
          ("wiredRogue", 3))
    )



class MwlCoordAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coordAlgoDefault", 1),
          ("coordAlgoUnknown", 2))
    )



class MwlCypherSuiteBits(Bits, TextualConvention):
    status = "current"


class MwlL2BridgingsBits(Bits, TextualConvention):
    status = "current"


class MwlDropPolicy(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("drophead", 0),
          ("droptail", 1))
    )



class MwlDataplaneMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dataplaneModeBridged", 1),
          ("dataplaneModeTunneled", 0))
    )



class MwlProfileOwner(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("profileOwnerController", 0),
          ("profileOwnerNmsServer", 1))
    )



class MwlApRole(Integer32, TextualConvention):
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
        *(("apRoleAccess", 0),
          ("apRoleGateway", 1),
          ("apRoleWireless", 2))
    )



class MwlEncryptionAlgorithm(Integer32, TextualConvention):
    status = "current"
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
        *(("encryptionCcmp", 3),
          ("encryptionClear", 5),
          ("encryptionTkip", 2),
          ("encryptionUnknown", 4),
          ("encryptionWep", 1))
    )



class MwlIfAdministrativeState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminStateDown", 1),
          ("adminStateTesting", 3),
          ("adminStateUp", 2))
    )



class MwlEssApAdminMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("essAdminModeDisabled", 5),
          ("essAdminModeNoservice", 6),
          ("essApAdminModeDown", 1),
          ("essApAdminModePowerdown", 7),
          ("essApAdminModeScan", 3),
          ("essApAdminModeUnlicensed", 4),
          ("essApAdminModeUp", 2))
    )



class MwlLedMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ledModeBlink", 2),
          ("ledModeDark", 3),
          ("ledModeNodeId", 1),
          ("ledModeNormal", 0))
    )



class MwlLogSeverity(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("logSevAlert", 1),
          ("logSevCritical", 2),
          ("logSevDebug", 7),
          ("logSevEmerg", 0),
          ("logSevError", 3),
          ("logSevInfo", 6),
          ("logSevNotice", 5),
          ("logSevTotal", 8),
          ("logSevWarn", 4))
    )



class MwlLogType(Integer32, TextualConvention):
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("logApAdministrativeReboot", 16),
          ("logApDetected", 1),
          ("logCertExpiry", 8),
          ("logConfigAdd", 5),
          ("logConfigDel", 7),
          ("logConfigMod", 6),
          ("logControllerAdministrativeReboot", 17),
          ("logDbBackup", 2),
          ("logDbRestore", 3),
          ("logDiscLicensingFailure", 18),
          ("logHaConfigErr", 14),
          ("logHaLinkStatus", 15),
          ("logHaNodeDead", 12),
          ("logHaShutdown", 11),
          ("logHaStart", 10),
          ("logHaStatus", 13),
          ("logMicCountermeasure", 19),
          ("logMicFailureAp", 20),
          ("logMicFailureClient", 21),
          ("logSwUpgrade", 4),
          ("logTypeTotal", 22),
          ("logUnknown", 0),
          ("logVlan", 9))
    )



class MwlMimoMode(Integer32, TextualConvention):
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
        *(("nmsMimoMode1x1", 2),
          ("nmsMimoMode2x2", 0),
          ("nmsMimoMode3x3", 1))
    )



class MwlNatType(Integer32, TextualConvention):
    status = "current"
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
        *(("natTypeDynamicNapt", 4),
          ("natTypeDynamicOneToOne", 3),
          ("natTypeNone", 1),
          ("natTypeStaticOneToOne", 2),
          ("natTypeUnknown", 5))
    )



class MwlNetProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("nmsIpprotoTcp", 6),
          ("nmsIpprotoUdp", 17),
          ("nmsIpprotoUnknown", 0))
    )



class MwlNmsInterfaceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ifTypeActive", 0),
          ("ifTypeRedundant", 1))
    )



class MwlNodeRelationship(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noderelationshipbound", 2),
          ("noderelationshipnone", 1),
          ("noderelationshipvisible", 3))
    )



class MwlNodeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("nodeTypeAp", 2),
          ("nodeTypeAsc", 3),
          ("nodeTypeOther", 11),
          ("nodeTypeSta", 10),
          ("nodeTypeUnknown", 12),
          ("nodeTypeWnc", 1))
    )



class MwlOperationalState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("operationalStateDisabled", 2),
          ("operationalStateEnabled", 1),
          ("operationalStateEnabledWith11nlic", 4),
          ("operationalStatePowerDown", 5),
          ("operationalStateUnknown", 0),
          ("operationalStateUnlicensed", 3))
    )



class MwlPowerSupply(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("powerSupply12vDc", 4),
          ("powerSupply5vDc", 2),
          ("powerSupply8023Af", 0),
          ("powerSupply8023At", 1),
          ("powerSupplyDual8023Af", 3))
    )



class MwlRadiusMacDelimiter(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("radiusMacDelimiterColon", 4),
          ("radiusMacDelimiterHyphen", 1),
          ("radiusMacDelimiterNone", 0),
          ("radiusMacDelimiterSingleHyphen", 2))
    )



class MwlRadiusPasswordType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("radiusPasswordTypeMacAddress", 1),
          ("radiusPasswordTypeSharedSecret", 0))
    )



class MwlWlanOptimize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("optimizeCoverage", 3),
          ("optimizeHandoff", 2),
          ("optimizeInteroperability", 4),
          ("optimizeNone", 0),
          ("optimizePerformance", 1),
          ("optimizeRogueap", 5))
    )



class MwlOnOffSwitch(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsOff", 0),
          ("nmsOn", 1))
    )



class MwlPublishEssId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("publishEssid24g", 2),
          ("publishEssid5g", 3),
          ("publishEssidOff", 0),
          ("publishEssidOn", 1))
    )



class MwlAllOnSelectedSwitch(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsAllOn", 1),
          ("nmsSelected", 0))
    )



class MwlPrivacyBit(Integer32, TextualConvention):
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
        *(("privacyBitAuto", 0),
          ("privacyBitOff", 2),
          ("privacyBitOn", 1))
    )



class MwlQosAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nmsQosActionCapture", 2),
          ("nmsQosActionDrop", 3),
          ("nmsQosActionForward", 1))
    )



class MwlQosCodec(Integer32, TextualConvention):
    status = "current"
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("nmsCodecDefault", 1),
          ("nmsCodeca1016", 3),
          ("nmsCodecaDv14", 7),
          ("nmsCodecaDv142", 8),
          ("nmsCodecaG711ALaw64k", 10),
          ("nmsCodecaG711ULaw64k", 2),
          ("nmsCodecaG721", 4),
          ("nmsCodecaG722", 11),
          ("nmsCodecaG7221", 12),
          ("nmsCodecaG722132k", 13),
          ("nmsCodecaG7231", 6),
          ("nmsCodecaG728", 15),
          ("nmsCodecaG729", 16),
          ("nmsCodecaGsm", 5),
          ("nmsCodecaLpc", 9),
          ("nmsCodecaMpa", 14),
          ("nmsCodecaRed", 17),
          ("nmsCodecaSiren", 18),
          ("nmsCodecvH261", 19),
          ("nmsCodecvH263", 20))
    )



class MwlQosProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("qosprotocolh323", 2),
          ("qosprotocolhttp", 4),
          ("qosprotocolnone", 6),
          ("qosprotocolother", 5),
          ("qosprotocolsccp", 3),
          ("qosprotocolsip", 1),
          ("qosprotocolunknown", 7))
    )



class MwlQosCodecProtocol(Integer32, TextualConvention):
    status = "current"
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
        *(("qoscodecprotocolh323", 2),
          ("qoscodecprotocolhttp", 4),
          ("qoscodecprotocolnone", 5),
          ("qoscodecprotocolsccp", 3),
          ("qoscodecprotocolsip", 1),
          ("qoscodecprotocolunknown", 6))
    )



class MwlQosCallState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qoscallconferencingstate", 3),
          ("qoscallconnectedstate", 1),
          ("qoscalldisconnectedstate", 0),
          ("qoscallholdstate", 2))
    )



class MwlServiceAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nmsServiceActionAdd", 1),
          ("nmsServiceActionChange", 3),
          ("nmsServiceActionRemove", 2))
    )



class MwlSecurityPolicyAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("securityPolicyActionAllow", 1),
          ("securityPolicyActionDeny", 0),
          ("securityPolicyActionNum", 3),
          ("securityPolicyActionRedirect", 2))
    )



class MwlL2SecurityModeBits(Bits, TextualConvention):
    status = "current"


class MwlL2SecurityMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2047)
        )
    )
    namedValues = NamedValues(
        *(("l2SecurityMode8021x", 2),
          ("l2SecurityModeAll", 2047),
          ("l2SecurityModeMixed", 128),
          ("l2SecurityModeMixedPsk", 256),
          ("l2SecurityModeNone", 0),
          ("l2SecurityModeOpen", 1),
          ("l2SecurityModeSwk", 4),
          ("l2SecurityModeWai", 512),
          ("l2SecurityModeWaiPsk", 1024),
          ("l2SecurityModeWpa", 8),
          ("l2SecurityModeWpa2", 32),
          ("l2SecurityModeWpa2Psk", 64),
          ("l2SecurityModeWpaPsk", 16))
    )



class MwlTunnelTerminationModeBits(Bits, TextualConvention):
    status = "current"


class MwlL2SecurityDetailMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              511,
              512,
              1024,
              2048,
              4096,
              8192,
              16384,
              32768)
        )
    )
    namedValues = NamedValues(
        *(("stationSecurityMode8021x", 2),
          ("stationSecurityMode8021xInProgress", 512),
          ("stationSecurityModeAll", 511),
          ("stationSecurityModeMixed", 128),
          ("stationSecurityModeMixedInProgress", 16384),
          ("stationSecurityModeMixedPsk", 256),
          ("stationSecurityModeMixedPskInProgress", 32768),
          ("stationSecurityModeNone", 0),
          ("stationSecurityModeOpen", 1),
          ("stationSecurityModeSwk", 4),
          ("stationSecurityModeWpa", 8),
          ("stationSecurityModeWpa2", 32),
          ("stationSecurityModeWpa2InProgress", 4096),
          ("stationSecurityModeWpa2Psk", 64),
          ("stationSecurityModeWpa2PskInProgress", 8192),
          ("stationSecurityModeWpaInProgress", 1024),
          ("stationSecurityModeWpaPsk", 16),
          ("stationSecurityModeWpaPskInProgress", 2048))
    )



class MwlL3SecurityMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("l3SecurityModeAll", 7),
          ("l3SecurityModeOpen", 1),
          ("l3SecurityModeVpn", 2),
          ("l3SecurityModeWebauth", 4))
    )



class MwlCaptivePortalMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("captivePortalDisabled", 0),
          ("captivePortalModeAll", 3),
          ("captivePortalModeVpn", 1),
          ("captivePortalModeWebauth", 2))
    )



class MwlCaptivePortalAuthState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("captivePortalStateClear", 0),
          ("captivePortalStateWebauth", 1))
    )



class MwlCaptivePortalAuthMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("captivePortalAuthMethodExternal", 1),
          ("captivePortalAuthMethodInternal", 0))
    )



class MwlSnmpPrivilege(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpRo", 1),
          ("snmpRw", 2))
    )



class MwlSnmpV3AuthProtocol(Integer32, TextualConvention):
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
        *(("snmpV3UsmHmacMd5Auth", 1),
          ("snmpV3UsmHmacShaAuth", 2),
          ("snmpV3UsmNoAuth", 0))
    )



class MwlSnmpV3PrivProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("snmpV3UsmDesPriv", 1),
          ("snmpV3UsmNoPriv", 0))
    )



class MwlTransmitRateBGBits(Bits, TextualConvention):
    status = "current"


class MwlTransmitRateBits(Bits, TextualConvention):
    status = "current"


class MwlTransmitRateAGBits(Bits, TextualConvention):
    status = "current"


class MwlTransmitRateHTBits(Bits, TextualConvention):
    status = "current"


class MwlUpgradeState(Integer32, TextualConvention):
    status = "current"
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
        *(("upgradeDone", 4),
          ("upgradeFailed", 3),
          ("upgradeInProgress", 2),
          ("upgradeStart", 1))
    )



class MwlVlanType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("vlanDefaultOnly", 1),
          ("vlanGre", 4),
          ("vlanNone", 0),
          ("vlanRadiusAndDefault", 3),
          ("vlanRadiusOnly", 2))
    )



class MwlAirFirewall(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("airfirewallNone", 0),
          ("airfirewallOuis", 1))
    )



class MwlOffHours(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offhours", 1),
          ("offhoursNone", 0))
    )



class MwlOffHoursService(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offhoursNoservice", 0),
          ("offhoursNowireless", 1))
    )



class MwlDailyOutOfService(Integer32, TextualConvention):
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
        *(("dailyOutOfServiceOff", 1),
          ("dailyOutOfServiceOn", 2),
          ("noDailyOutOfService", 0))
    )



class MwlVpnStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clearActive", 0),
          ("vpnActive", 2),
          ("vpnBypass", 1),
          ("vpnWebActive", 5),
          ("webAuthActive", 4))
    )



class MwlVpnDetailStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("stationClearActive", 0),
          ("stationVpnActive", 2),
          ("stationVpnBypass", 1),
          ("stationVpnInProgress", 8),
          ("stationVpnWebActive", 5),
          ("stationVpnWebauthInProgress", 32),
          ("stationWebAuthActive", 4),
          ("stationWebauthInProgress", 16))
    )



class MwlSslUsrAuthProtocolType(Integer32, TextualConvention):
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
        *(("sslAuthProtocolChap", 2),
          ("sslAuthProtocolNone", 1),
          ("sslAuthProtocolUnknown", 0))
    )



class MwlDhGroupType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dhGroup2", 2),
          ("dhGroup3", 3),
          ("dhGroup4", 4),
          ("dhGroup5", 5))
    )



class MwlIpSecModeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipsecTunnelMode", 1),
          ("ipsecUnknownMode", 0))
    )



class MwlIpSecDataChannelType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipsecEsp", 1),
          ("ipsecUnknown", 0))
    )



class MwlIpEncryptionAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("encryption3des", 1),
          ("encryptionUnknownAlgorithm", 0))
    )



class MwlIpAuthenticateAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("authPreShareKey", 1),
          ("authUnknown", 0))
    )



class MwlIpHashAlgorithm(Integer32, TextualConvention):
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
        *(("hashMd5", 2),
          ("hashSha", 1),
          ("hashUnknown", 0))
    )



class MwlIpSecAuthAlgorithm(Integer32, TextualConvention):
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
        *(("ipsecAuthMd5Hmac", 2),
          ("ipsecAuthShaHmac", 1),
          ("ipsecAuthUnknown", 0))
    )



class MwlCertFileType(Integer32, TextualConvention):
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
        *(("certPemType", 1),
          ("certPfxType", 2),
          ("certUnknownType", 0))
    )



class MwlUrlType(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("cliBadUrl", 0),
          ("cliFileUrl", 7),
          ("cliFtpUrl", 1),
          ("cliHttpUrl", 4),
          ("cliHttpsUrl", 5),
          ("cliScpUrl", 6),
          ("cliSftpUrl", 3),
          ("cliTftpUrl", 2))
    )



class MwlCertificateFormType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsLongForm", 1),
          ("nmsShortForm", 0))
    )



class MwlRadiusServerSelect(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nmsRadiusServerAll", 3),
          ("nmsRadiusServerNone", 0),
          ("nmsRadiusServerPrimary", 1),
          ("nmsRadiusServerSecondary", 2))
    )



class MwlDiscoveryOrder(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discoveryFromL2First", 0),
          ("discoveryFromL2Only", 1),
          ("discoveryFromL3First", 2),
          ("discoveryFromL3Only", 3))
    )



class MwlApDiscoveryState(Integer32, TextualConvention):
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
        *(("discoveryFromL2", 1),
          ("discoveryFromL3", 2),
          ("noDiscoveryLayer", 0))
    )



class MwlLicenseType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("featurePermanent", 1),
          ("featureTrial", 0))
    )



class MwlLicenseReserveType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("countedLicense", 0),
          ("uncountedLicense", 1))
    )



class MwlSofwFeatureType(Integer32, TextualConvention):
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
        *(("sofwApBasic", 1),
          ("sofwControllerBasic", 0),
          ("sofwFeatMax", 2))
    )



class MwlSofwControllerType(Integer32, TextualConvention):
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
        *(("sofwAll", 0),
          ("sofwController", 1),
          ("sofwStdbyController", 2))
    )



class MwlDscpType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              8,
              10,
              12,
              14,
              16,
              18,
              20,
              22,
              24,
              26,
              28,
              30,
              32,
              34,
              36,
              38,
              40,
              46,
              48,
              56)
        )
    )
    namedValues = NamedValues(
        *(("dscpAf11", 10),
          ("dscpAf12", 12),
          ("dscpAf13", 14),
          ("dscpAf21", 18),
          ("dscpAf22", 20),
          ("dscpAf23", 22),
          ("dscpAf31", 26),
          ("dscpAf32", 28),
          ("dscpAf33", 30),
          ("dscpAf41", 34),
          ("dscpAf42", 36),
          ("dscpAf43", 38),
          ("dscpCs0", 0),
          ("dscpCs1", 8),
          ("dscpCs2", 16),
          ("dscpCs3", 24),
          ("dscpCs4", 32),
          ("dscpCs5", 40),
          ("dscpCs6", 48),
          ("dscpCs7", 56),
          ("dscpDisabled", -1),
          ("dscpEfphb", 46))
    )



class MwlControllerHwType(Integer32, TextualConvention):
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
              11,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("wncDevelPc", 1),
          ("wncMc1000", 2),
          ("wncMc1100", 3),
          ("wncMc1500", 11),
          ("wncMc1500v", 16),
          ("wncMc1550", 19),
          ("wncMc1550v", 20),
          ("wncMc3000", 4),
          ("wncMc3200", 13),
          ("wncMc3200v", 17),
          ("wncMc4000", 8),
          ("wncMc4100", 9),
          ("wncMc4200", 14),
          ("wncMc4200v", 18),
          ("wncMc500", 5),
          ("wncMc5000", 7),
          ("wncMc500a", 6),
          ("wncMc6000", 15),
          ("wncUnknownModel", 0))
    )



class MwlWncControllerState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wncCluster", 3),
          ("wncMaster", 1),
          ("wncSlave", 2),
          ("wncStandalone", 0))
    )



class MwlApHwType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              12,
              13,
              14,
              15,
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
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("ap1010", 24),
          ("ap1010e", 32),
          ("ap1014i", 41),
          ("ap1020", 25),
          ("ap1020e", 33),
          ("ap110", 39),
          ("ap120", 40),
          ("ap300", 12),
          ("ap301", 18),
          ("ap301i", 20),
          ("ap302", 19),
          ("ap302i", 22),
          ("ap310", 13),
          ("ap310i", 21),
          ("ap311", 14),
          ("ap320", 15),
          ("ap320i", 23),
          ("ap332e", 42),
          ("ap332i", 43),
          ("ap400", 27),
          ("ap432e", 30),
          ("ap432i", 31),
          ("ap433e", 28),
          ("ap433es", 35),
          ("ap433i", 29),
          ("ap433is", 34),
          ("apUnknownModel", 0),
          ("oap432e", 36),
          ("oap433e", 37),
          ("oap433es", 38),
          ("psm3x", 26))
    )



class MwlApRegulatoryType(Integer32, TextualConvention):
    status = "current"
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
        *(("ap1000RegIndex", 1),
          ("ap110RegIndex", 5),
          ("ap300Mb72RegIndex", 2),
          ("ap300Mb82RegIndex", 3),
          ("ap330RegIndex", 6),
          ("ap400RegIndex", 4))
    )



class MwlApRfType(Integer32, TextualConvention):
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
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("apRf1", 1),
          ("apRf10", 10),
          ("apRf11", 11),
          ("apRf12", 12),
          ("apRf13", 13),
          ("apRf14", 14),
          ("apRf15", 15),
          ("apRf2", 2),
          ("apRf3", 3),
          ("apRf4", 4),
          ("apRf5", 5),
          ("apRf6", 6),
          ("apRf7", 7),
          ("apRf8", 8),
          ("apRf9", 9),
          ("apRfUnknownModel", 0))
    )



class MwlApIfModeType(Integer32, TextualConvention):
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
              27)
        )
    )
    namedValues = NamedValues(
        *(("apAMode", 2),
          ("apAbMode", 3),
          ("apAbgMode", 7),
          ("apAbgnMode", 15),
          ("apAbnMode", 11),
          ("apAgMode", 6),
          ("apAgnMode", 14),
          ("apAn1s20Mode", 16),
          ("apAn1s40Mode", 17),
          ("apAn2s20Mode", 18),
          ("apAn2s40Mode", 19),
          ("apAn3s20Mode", 20),
          ("apAn3s40Mode", 21),
          ("apAnMode", 10),
          ("apBMode", 1),
          ("apBgMode", 5),
          ("apBgn1s20Mode", 22),
          ("apBgn1s40Mode", 23),
          ("apBgn2s20Mode", 24),
          ("apBgn2s40Mode", 25),
          ("apBgn3s20Mode", 26),
          ("apBgn3s40Mode", 27),
          ("apBgnMode", 13),
          ("apBnMode", 9),
          ("apGMode", 4),
          ("apGnMode", 12),
          ("apModeUnknown", 0),
          ("apNMode", 8))
    )



class MwlApIfConfigModeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              10,
              13)
        )
    )
    namedValues = NamedValues(
        *(("apConfigAMode", 2),
          ("apConfigAnMode", 10),
          ("apConfigBMode", 1),
          ("apConfigBgMode", 5),
          ("apConfigBgnMode", 13),
          ("apConfigGMode", 4),
          ("apConfigModeUnknown", 0))
    )



class MwlAntennaType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("antennaConn24g", 1),
          ("antennaConn5g", 2),
          ("antennaConnDual", 3),
          ("antennaConnExt", 4),
          ("antennaConnInt", 5),
          ("antennaConnNone", 0))
    )



class MwlBandType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfband24g", 1),
          ("rfband5g", 2))
    )



class MwlChannelBandType(Integer32, TextualConvention):
    status = "current"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("channelAMode", 2),
          ("channelAbgnMode20mhz", 5),
          ("channelAbgnMode40mhzAbove", 6),
          ("channelAbgnMode40mhzBelow", 7),
          ("channelBMode", 1),
          ("channelBgMode", 4),
          ("channelGMode", 3),
          ("channelNMode20mhz", 8),
          ("channelNMode40mhzAbove", 9),
          ("channelNMode40mhzBelow", 10))
    )



class MwlAntennaSetLocation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("antennaSetLoc1", 4),
          ("antennaSetLoc2", 8),
          ("antennaSetLoc3", 16),
          ("antennaSetLoc4", 32),
          ("antennaSetLoc5", 64),
          ("antennaSetLoc6", 128),
          ("antennaSetLoc7", 256),
          ("antennaSetLoc8", 512),
          ("antennaSetLoc9", 1024),
          ("antennaSetLocIntegrated", 2048),
          ("antennaSetLocInternal", 4096),
          ("antennaSetLocLeft", 1),
          ("antennaSetLocRight", 2),
          ("antennaSetLocUnknown", 0))
    )



class MwlIfDataRateOptionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dataRateAuto", 1),
          ("dataRateManual", 0))
    )



class MwlAntennaLinkType(Integer32, TextualConvention):
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
        *(("antennaLinkPmp", 1),
          ("antennaLinkPtp", 2),
          ("antennaLinkUnknown", 0))
    )



class MwlDuplexModeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsDuplexFull", 0),
          ("nmsDuplexHalf", 1))
    )



class MwlBgProtectionModeType(Integer32, TextualConvention):
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
        *(("bgProtectionAuto", 0),
          ("bgProtectionOff", 2),
          ("bgProtectionOn", 1))
    )



class MwlHtProtectionModeType(Integer32, TextualConvention):
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
        *(("htProtectionAuto", 0),
          ("htProtectionOff", 2),
          ("htProtectionOn", 1))
    )



class MwlIpProxyType(Integer32, TextualConvention):
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
        *(("nmsEnumerationHeader", 2),
          ("nmsGeneric", 0),
          ("nmsIpPathFinder", 1))
    )



class MwlFirewallCapability(Integer32, TextualConvention):
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
        *(("firewallConfigured", 1),
          ("firewallNone", 0),
          ("firewallRadiusConfigured", 2))
    )



class MwlSecurityLogging(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("securityloggingAll", 3),
          ("securityloggingAllow", 1),
          ("securityloggingDeny", 2),
          ("securityloggingOff", 0))
    )



class MwlPMKcachingBits(Bits, TextualConvention):
    status = "current"


class MwlKDDI(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("kddiDisabled", 0),
          ("kddiEnabled", 1))
    )



class MwlVcellType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsVcellPap", 0),
          ("nmsVcellVcell", 1))
    )



class MwlFilterModeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 0),
          ("include", 1))
    )



class MwlBgRadioMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonVirtualMode", 2),
          ("virtualMode", 1))
    )



class MwlThrdPartyIdsIps(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("thrdPidsIpsNone", 2),
          ("thrdPidsIpsSnortWireless", 1))
    )



class MwlQosRulesMatchClassBits(Bits, TextualConvention):
    status = "current"


class MwlQosRulesMatchClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosrulesmatchclassOff", 0),
          ("qosrulesmatchclassOn", 1))
    )



class MwlChannelWidth(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("channelWidth20", 1),
          ("channelWidth40Above", 2),
          ("channelWidth40Below", 3))
    )



class MwlBonding(Integer32, TextualConvention):
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
        *(("bondingDual", 1),
          ("bondingNone", 2),
          ("bondingSingle", 0))
    )



class MwlConnectivityStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsConnected", 1),
          ("nmsDisconnected", 0))
    )



class MwlCapabilityModeBits(Bits, TextualConvention):
    status = "current"


class MwlClientType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nmsClientData", 1),
          ("nmsClientSipPhone", 2))
    )



class MwlDeviceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsStationWired", 1),
          ("nmsStationWireless", 0))
    )



class MwlStationState(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("nmsStationState8021x", 5),
          ("nmsStationStateAssign", 3),
          ("nmsStationStateAssociated", 4),
          ("nmsStationStateCaptivePortal", 8),
          ("nmsStationStateDisassociated", 9),
          ("nmsStationStateInit", 1),
          ("nmsStationStateIpDiscover", 7),
          ("nmsStationStateKey", 6),
          ("nmsStationStateUnknown", 0),
          ("nmsStationStateVlan", 2))
    )



class MwlStaDiagStap(Integer32, TextualConvention):
    status = "current"
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("staAssignFailCnt", 4),
          ("staAssociationCnt", 5),
          ("staCpGuestUserAuthCnt", 12),
          ("staCpGuestUserFailCnt", 13),
          ("staDecryptFailCnt", 14),
          ("staIpDiscoveryCnt", 9),
          ("staKeyExchangeCnt", 6),
          ("staKeyExchangeFailCnt", 7),
          ("staMacFilterAclCnt", 1),
          ("staMacFilterAclFailCnt", 2),
          ("staMicFailCnt", 8),
          ("staRadiusAuthCnt", 10),
          ("staRadiusAuthFailCnt", 11),
          ("staSoftHandoffCnt", 15),
          ("staWepKeyIndexMismatchCnt", 3))
    )



class MwlEnableDisableOption(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsDisable", 0),
          ("nmsEnable", 1))
    )



class MwlPacketCaptureMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("l2Mode", 0),
          ("l3Mode", 1))
    )



class MwlRxTxOption(Integer32, TextualConvention):
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
        *(("rxOnly", 0),
          ("rxTxBoth", 2),
          ("txOnly", 1))
    )



class MwlRateLimitMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cumulative", 1),
          ("station", 0))
    )



class MwlBandSteeringMode(Integer32, TextualConvention):
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
        *(("bandASteering", 1),
          ("bandNSteering", 2),
          ("bandSteeringDisable", 0))
    )



class MwlPapBroadcastSsidMode(Integer32, TextualConvention):
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
        *(("papBroadcastSsidAlways", 1),
          ("papBroadcastSsidDisabled", 0),
          ("papBroadcastSsidTillAssociation", 2))
    )



class MwlEncapsulationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("legacy", 1),
          ("ppi", 0))
    )



class MwlUplinkType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsDownlink", 1),
          ("nmsUplink", 0))
    )



class MwlVpnConnectivityStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vpnConnected", 1),
          ("vpnDisconnected", 0))
    )



class MwlVpnAuthenticationStatus(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("vpnCertificateExpired", 5),
          ("vpnCertificateRevoked", 4),
          ("vpnCertificateUnknownCa", 6),
          ("vpnInvalidCertificate", 3),
          ("vpnNoCertificate", 1),
          ("vpnUnknown", 0),
          ("vpnValidCertificate", 2))
    )



class MwlVpnAuthenticationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vpnAuthTypeUnknown", 0),
          ("vpnAuthTypeX509Certificate", 1))
    )



class MwlCertificateStatus(Integer32, TextualConvention):
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
        *(("certStatusInstalled", 2),
          ("certStatusNotInstalled", 1),
          ("certStatusUnknown", 0))
    )



class MwlCertRequestStatus(Integer32, TextualConvention):
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
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("certReqStatusCaCertDownloadFailed", 14),
          ("certReqStatusCaCertDownloadInProgress", 13),
          ("certReqStatusCaCertDownloaded", 12),
          ("certReqStatusCertDeleted", 9),
          ("certReqStatusCertDeletionFailed", 11),
          ("certReqStatusCertDeletionInProgress", 10),
          ("certReqStatusCertDownloadFailed", 7),
          ("certReqStatusCertInstallationFailed", 8),
          ("certReqStatusCertInstallationInProgress", 6),
          ("certReqStatusCertInstalled", 5),
          ("certReqStatusCsrGenerated", 1),
          ("certReqStatusCsrGenerationFailed", 3),
          ("certReqStatusCsrGenerationInProgress", 2),
          ("certReqStatusCsrUploadFailed", 4),
          ("certReqStatusNone", 0))
    )



class MwlFastEthernetType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nmsPrimaryFastethernet", 1),
          ("nmsSecondaryFastethernet", 2))
    )



class MwlVpnMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("modeNonVpn", 0),
          ("modeVpn", 1))
    )



class MwlRegionSettings(Integer32, TextualConvention):
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
        *(("regionIntl", 2),
          ("regionUnknown", 0),
          ("regionUs", 1))
    )



class MwlArrayDataTypeAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addValue", 1),
          ("deleteValue", 2),
          ("updateValue", 3))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-TC",
    **{"MwlAclEnvState": MwlAclEnvState,
       "MwlAddressAssignmentType": MwlAddressAssignmentType,
       "MwlAddressIfAssignmentType": MwlAddressIfAssignmentType,
       "MwlApIpAssignmentType": MwlApIpAssignmentType,
       "MwlAdministrativeState": MwlAdministrativeState,
       "MwlAdmissionControl": MwlAdmissionControl,
       "MwlAntennaSet": MwlAntennaSet,
       "MwlApAssignType": MwlApAssignType,
       "MwlApType": MwlApType,
       "MwlApIndoorOutdoorType": MwlApIndoorOutdoorType,
       "MwlApMode": MwlApMode,
       "MwlAuthenticationAlgorithm": MwlAuthenticationAlgorithm,
       "MwlAuthenticationType": MwlAuthenticationType,
       "MwlCaptivePortalAuthenticationType": MwlCaptivePortalAuthenticationType,
       "MwlAuthSuiteBits": MwlAuthSuiteBits,
       "MwlActionStatus": MwlActionStatus,
       "MwlAlarmState": MwlAlarmState,
       "MwlAlarmType": MwlAlarmType,
       "MwlAlarmSeverity": MwlAlarmSeverity,
       "MwlAntenna": MwlAntenna,
       "MwlAssignmentAlgorithm": MwlAssignmentAlgorithm,
       "MwlAssociationState": MwlAssociationState,
       "MwlApAuthState": MwlApAuthState,
       "MwlAvailabilityStatus": MwlAvailabilityStatus,
       "MwlBeaconCoordinationMode": MwlBeaconCoordinationMode,
       "MwlBlock": MwlBlock,
       "MwlCoordAlgorithm": MwlCoordAlgorithm,
       "MwlCypherSuiteBits": MwlCypherSuiteBits,
       "MwlL2BridgingsBits": MwlL2BridgingsBits,
       "MwlDropPolicy": MwlDropPolicy,
       "MwlDataplaneMode": MwlDataplaneMode,
       "MwlProfileOwner": MwlProfileOwner,
       "MwlApRole": MwlApRole,
       "MwlEncryptionAlgorithm": MwlEncryptionAlgorithm,
       "MwlIfAdministrativeState": MwlIfAdministrativeState,
       "MwlEssApAdminMode": MwlEssApAdminMode,
       "MwlLedMode": MwlLedMode,
       "MwlLogSeverity": MwlLogSeverity,
       "MwlLogType": MwlLogType,
       "MwlMimoMode": MwlMimoMode,
       "MwlNatType": MwlNatType,
       "MwlNetProtocol": MwlNetProtocol,
       "MwlNmsInterfaceType": MwlNmsInterfaceType,
       "MwlNodeRelationship": MwlNodeRelationship,
       "MwlNodeType": MwlNodeType,
       "MwlOperationalState": MwlOperationalState,
       "MwlPowerSupply": MwlPowerSupply,
       "MwlRadiusMacDelimiter": MwlRadiusMacDelimiter,
       "MwlRadiusPasswordType": MwlRadiusPasswordType,
       "MwlWlanOptimize": MwlWlanOptimize,
       "MwlOnOffSwitch": MwlOnOffSwitch,
       "MwlPublishEssId": MwlPublishEssId,
       "MwlAllOnSelectedSwitch": MwlAllOnSelectedSwitch,
       "MwlPrivacyBit": MwlPrivacyBit,
       "MwlQosAction": MwlQosAction,
       "MwlQosCodec": MwlQosCodec,
       "MwlQosProtocol": MwlQosProtocol,
       "MwlQosCodecProtocol": MwlQosCodecProtocol,
       "MwlQosCallState": MwlQosCallState,
       "MwlServiceAction": MwlServiceAction,
       "MwlSecurityPolicyAction": MwlSecurityPolicyAction,
       "MwlL2SecurityModeBits": MwlL2SecurityModeBits,
       "MwlL2SecurityMode": MwlL2SecurityMode,
       "MwlTunnelTerminationModeBits": MwlTunnelTerminationModeBits,
       "MwlL2SecurityDetailMode": MwlL2SecurityDetailMode,
       "MwlL3SecurityMode": MwlL3SecurityMode,
       "MwlCaptivePortalMode": MwlCaptivePortalMode,
       "MwlCaptivePortalAuthState": MwlCaptivePortalAuthState,
       "MwlCaptivePortalAuthMethod": MwlCaptivePortalAuthMethod,
       "MwlSnmpPrivilege": MwlSnmpPrivilege,
       "MwlSnmpV3AuthProtocol": MwlSnmpV3AuthProtocol,
       "MwlSnmpV3PrivProtocol": MwlSnmpV3PrivProtocol,
       "MwlTransmitRateBGBits": MwlTransmitRateBGBits,
       "MwlTransmitRateBits": MwlTransmitRateBits,
       "MwlTransmitRateAGBits": MwlTransmitRateAGBits,
       "MwlTransmitRateHTBits": MwlTransmitRateHTBits,
       "MwlUpgradeState": MwlUpgradeState,
       "MwlVlanType": MwlVlanType,
       "MwlAirFirewall": MwlAirFirewall,
       "MwlOffHours": MwlOffHours,
       "MwlOffHoursService": MwlOffHoursService,
       "MwlDailyOutOfService": MwlDailyOutOfService,
       "MwlVpnStatus": MwlVpnStatus,
       "MwlVpnDetailStatus": MwlVpnDetailStatus,
       "MwlSslUsrAuthProtocolType": MwlSslUsrAuthProtocolType,
       "MwlDhGroupType": MwlDhGroupType,
       "MwlIpSecModeType": MwlIpSecModeType,
       "MwlIpSecDataChannelType": MwlIpSecDataChannelType,
       "MwlIpEncryptionAlgorithm": MwlIpEncryptionAlgorithm,
       "MwlIpAuthenticateAlgorithm": MwlIpAuthenticateAlgorithm,
       "MwlIpHashAlgorithm": MwlIpHashAlgorithm,
       "MwlIpSecAuthAlgorithm": MwlIpSecAuthAlgorithm,
       "MwlCertFileType": MwlCertFileType,
       "MwlUrlType": MwlUrlType,
       "MwlCertificateFormType": MwlCertificateFormType,
       "MwlRadiusServerSelect": MwlRadiusServerSelect,
       "MwlDiscoveryOrder": MwlDiscoveryOrder,
       "MwlApDiscoveryState": MwlApDiscoveryState,
       "MwlLicenseType": MwlLicenseType,
       "MwlLicenseReserveType": MwlLicenseReserveType,
       "MwlSofwFeatureType": MwlSofwFeatureType,
       "MwlSofwControllerType": MwlSofwControllerType,
       "MwlDscpType": MwlDscpType,
       "MwlControllerHwType": MwlControllerHwType,
       "MwlWncControllerState": MwlWncControllerState,
       "MwlApHwType": MwlApHwType,
       "MwlApRegulatoryType": MwlApRegulatoryType,
       "MwlApRfType": MwlApRfType,
       "MwlApIfModeType": MwlApIfModeType,
       "MwlApIfConfigModeType": MwlApIfConfigModeType,
       "MwlAntennaType": MwlAntennaType,
       "MwlBandType": MwlBandType,
       "MwlChannelBandType": MwlChannelBandType,
       "MwlAntennaSetLocation": MwlAntennaSetLocation,
       "MwlIfDataRateOptionType": MwlIfDataRateOptionType,
       "MwlAntennaLinkType": MwlAntennaLinkType,
       "MwlDuplexModeType": MwlDuplexModeType,
       "MwlBgProtectionModeType": MwlBgProtectionModeType,
       "MwlHtProtectionModeType": MwlHtProtectionModeType,
       "MwlIpProxyType": MwlIpProxyType,
       "MwlFirewallCapability": MwlFirewallCapability,
       "MwlSecurityLogging": MwlSecurityLogging,
       "MwlPMKcachingBits": MwlPMKcachingBits,
       "MwlKDDI": MwlKDDI,
       "MwlVcellType": MwlVcellType,
       "MwlFilterModeType": MwlFilterModeType,
       "MwlBgRadioMode": MwlBgRadioMode,
       "MwlThrdPartyIdsIps": MwlThrdPartyIdsIps,
       "MwlQosRulesMatchClassBits": MwlQosRulesMatchClassBits,
       "MwlQosRulesMatchClass": MwlQosRulesMatchClass,
       "MwlChannelWidth": MwlChannelWidth,
       "MwlBonding": MwlBonding,
       "MwlConnectivityStatus": MwlConnectivityStatus,
       "MwlCapabilityModeBits": MwlCapabilityModeBits,
       "MwlClientType": MwlClientType,
       "MwlDeviceType": MwlDeviceType,
       "MwlStationState": MwlStationState,
       "MwlStaDiagStap": MwlStaDiagStap,
       "MwlEnableDisableOption": MwlEnableDisableOption,
       "MwlPacketCaptureMode": MwlPacketCaptureMode,
       "MwlRxTxOption": MwlRxTxOption,
       "MwlRateLimitMode": MwlRateLimitMode,
       "MwlBandSteeringMode": MwlBandSteeringMode,
       "MwlPapBroadcastSsidMode": MwlPapBroadcastSsidMode,
       "MwlEncapsulationType": MwlEncapsulationType,
       "MwlUplinkType": MwlUplinkType,
       "MwlVpnConnectivityStatus": MwlVpnConnectivityStatus,
       "MwlVpnAuthenticationStatus": MwlVpnAuthenticationStatus,
       "MwlVpnAuthenticationType": MwlVpnAuthenticationType,
       "MwlCertificateStatus": MwlCertificateStatus,
       "MwlCertRequestStatus": MwlCertRequestStatus,
       "MwlFastEthernetType": MwlFastEthernetType,
       "MwlVpnMode": MwlVpnMode,
       "MwlRegionSettings": MwlRegionSettings,
       "MwlArrayDataTypeAction": MwlArrayDataTypeAction,
       "meruTextualConventions": meruTextualConventions}
)
