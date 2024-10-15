# SNMP MIB module (BLACKBERRYSERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLACKBERRYSERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:57 2024
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

_Rim_ObjectIdentity = ObjectIdentity
rim = _Rim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3530)
)
_BlackBerryServer_ObjectIdentity = ObjectIdentity
blackBerryServer = _BlackBerryServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3530, 5)
)
_Version_Type = Integer32
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 1),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("mandatory")
_BesTotMsgsPending_Type = Integer32
_BesTotMsgsPending_Object = MibScalar
besTotMsgsPending = _BesTotMsgsPending_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 2),
    _BesTotMsgsPending_Type()
)
besTotMsgsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTotMsgsPending.setStatus("mandatory")
_BesTotMsgsSent_Type = Integer32
_BesTotMsgsSent_Object = MibScalar
besTotMsgsSent = _BesTotMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 3),
    _BesTotMsgsSent_Type()
)
besTotMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTotMsgsSent.setStatus("mandatory")
_BesTotMsgsRecvd_Type = Integer32
_BesTotMsgsRecvd_Object = MibScalar
besTotMsgsRecvd = _BesTotMsgsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 4),
    _BesTotMsgsRecvd_Type()
)
besTotMsgsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTotMsgsRecvd.setStatus("mandatory")
_BesTotMsgsXpired_Type = Integer32
_BesTotMsgsXpired_Object = MibScalar
besTotMsgsXpired = _BesTotMsgsXpired_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 5),
    _BesTotMsgsXpired_Type()
)
besTotMsgsXpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTotMsgsXpired.setStatus("mandatory")
_BesTotMsgsFiltered_Type = Integer32
_BesTotMsgsFiltered_Object = MibScalar
besTotMsgsFiltered = _BesTotMsgsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 6),
    _BesTotMsgsFiltered_Type()
)
besTotMsgsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTotMsgsFiltered.setStatus("mandatory")
_BesTotMsgsSentPerMin_Type = Integer32
_BesTotMsgsSentPerMin_Object = MibScalar
besTotMsgsSentPerMin = _BesTotMsgsSentPerMin_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 7),
    _BesTotMsgsSentPerMin_Type()
)
besTotMsgsSentPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTotMsgsSentPerMin.setStatus("mandatory")
_BesTotMsgsRecvdPerMin_Type = Integer32
_BesTotMsgsRecvdPerMin_Object = MibScalar
besTotMsgsRecvdPerMin = _BesTotMsgsRecvdPerMin_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 8),
    _BesTotMsgsRecvdPerMin_Type()
)
besTotMsgsRecvdPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTotMsgsRecvdPerMin.setStatus("mandatory")
_BesTrapVariables_ObjectIdentity = ObjectIdentity
besTrapVariables = _BesTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3530, 5, 9)
)


class _BesSRPConnectState_Type(Integer32):
    """Custom type besSRPConnectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BesSRPConnectState_Type.__name__ = "Integer32"
_BesSRPConnectState_Object = MibScalar
besSRPConnectState = _BesSRPConnectState_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 9, 1),
    _BesSRPConnectState_Type()
)
besSRPConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSRPConnectState.setStatus("mandatory")
_BesNumServerInfoAvailable_Type = Integer32
_BesNumServerInfoAvailable_Object = MibScalar
besNumServerInfoAvailable = _BesNumServerInfoAvailable_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 15),
    _BesNumServerInfoAvailable_Type()
)
besNumServerInfoAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besNumServerInfoAvailable.setStatus("mandatory")
_BesConfigTable_Object = MibTable
besConfigTable = _BesConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20)
)
if mibBuilder.loadTexts:
    besConfigTable.setStatus("mandatory")
_BesConfigEntry_Object = MibTableRow
besConfigEntry = _BesConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1)
)
besConfigEntry.setIndexNames(
    (0, "BLACKBERRYSERVER-MIB", "besConfigServerInstance"),
)
if mibBuilder.loadTexts:
    besConfigEntry.setStatus("mandatory")
_BesConfigServerInstance_Type = Integer32
_BesConfigServerInstance_Object = MibTableColumn
besConfigServerInstance = _BesConfigServerInstance_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 1),
    _BesConfigServerInstance_Type()
)
besConfigServerInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigServerInstance.setStatus("mandatory")
_BesConfigServerName_Type = DisplayString
_BesConfigServerName_Object = MibTableColumn
besConfigServerName = _BesConfigServerName_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 2),
    _BesConfigServerName_Type()
)
besConfigServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigServerName.setStatus("mandatory")
_BesConfigVersionString_Type = DisplayString
_BesConfigVersionString_Object = MibTableColumn
besConfigVersionString = _BesConfigVersionString_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 10),
    _BesConfigVersionString_Type()
)
besConfigVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigVersionString.setStatus("mandatory")
_BesConfigReleaseMaj_Type = Integer32
_BesConfigReleaseMaj_Object = MibTableColumn
besConfigReleaseMaj = _BesConfigReleaseMaj_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 11),
    _BesConfigReleaseMaj_Type()
)
besConfigReleaseMaj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigReleaseMaj.setStatus("mandatory")
_BesConfigReleaseMin_Type = Integer32
_BesConfigReleaseMin_Object = MibTableColumn
besConfigReleaseMin = _BesConfigReleaseMin_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 12),
    _BesConfigReleaseMin_Type()
)
besConfigReleaseMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigReleaseMin.setStatus("mandatory")
_BesConfigReleaseServicePack_Type = Integer32
_BesConfigReleaseServicePack_Object = MibTableColumn
besConfigReleaseServicePack = _BesConfigReleaseServicePack_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 13),
    _BesConfigReleaseServicePack_Type()
)
besConfigReleaseServicePack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigReleaseServicePack.setStatus("mandatory")
_BesConfigReleaseBuild_Type = Integer32
_BesConfigReleaseBuild_Object = MibTableColumn
besConfigReleaseBuild = _BesConfigReleaseBuild_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 14),
    _BesConfigReleaseBuild_Type()
)
besConfigReleaseBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigReleaseBuild.setStatus("mandatory")
_BesConfigLicenceTotal_Type = Integer32
_BesConfigLicenceTotal_Object = MibTableColumn
besConfigLicenceTotal = _BesConfigLicenceTotal_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 20),
    _BesConfigLicenceTotal_Type()
)
besConfigLicenceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigLicenceTotal.setStatus("mandatory")
_BesConfigLicenceUsed_Type = Integer32
_BesConfigLicenceUsed_Object = MibTableColumn
besConfigLicenceUsed = _BesConfigLicenceUsed_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 21),
    _BesConfigLicenceUsed_Type()
)
besConfigLicenceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigLicenceUsed.setStatus("mandatory")
_BesConfigLicenceRemaining_Type = Integer32
_BesConfigLicenceRemaining_Object = MibTableColumn
besConfigLicenceRemaining = _BesConfigLicenceRemaining_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 22),
    _BesConfigLicenceRemaining_Type()
)
besConfigLicenceRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigLicenceRemaining.setStatus("mandatory")
_BesConfigServerUID_Type = DisplayString
_BesConfigServerUID_Object = MibTableColumn
besConfigServerUID = _BesConfigServerUID_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 30),
    _BesConfigServerUID_Type()
)
besConfigServerUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigServerUID.setStatus("mandatory")
_BesConfigSystemAttendant_Type = DisplayString
_BesConfigSystemAttendant_Object = MibTableColumn
besConfigSystemAttendant = _BesConfigSystemAttendant_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 40),
    _BesConfigSystemAttendant_Type()
)
besConfigSystemAttendant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigSystemAttendant.setStatus("mandatory")
_BesConfigSRPHost_Type = DisplayString
_BesConfigSRPHost_Object = MibTableColumn
besConfigSRPHost = _BesConfigSRPHost_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 50),
    _BesConfigSRPHost_Type()
)
besConfigSRPHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigSRPHost.setStatus("mandatory")
_BesConfigSRPPort_Type = Integer32
_BesConfigSRPPort_Object = MibTableColumn
besConfigSRPPort = _BesConfigSRPPort_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 51),
    _BesConfigSRPPort_Type()
)
besConfigSRPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigSRPPort.setStatus("mandatory")


class _BesConfigAutoBCCEnabled_Type(Integer32):
    """Custom type besConfigAutoBCCEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BesConfigAutoBCCEnabled_Type.__name__ = "Integer32"
_BesConfigAutoBCCEnabled_Object = MibTableColumn
besConfigAutoBCCEnabled = _BesConfigAutoBCCEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 60),
    _BesConfigAutoBCCEnabled_Type()
)
besConfigAutoBCCEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigAutoBCCEnabled.setStatus("mandatory")
_BesConfigAutoBCCAddress_Type = DisplayString
_BesConfigAutoBCCAddress_Object = MibTableColumn
besConfigAutoBCCAddress = _BesConfigAutoBCCAddress_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 61),
    _BesConfigAutoBCCAddress_Type()
)
besConfigAutoBCCAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigAutoBCCAddress.setStatus("mandatory")


class _BesConfigForceSaveInSentEnabled_Type(Integer32):
    """Custom type besConfigForceSaveInSentEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BesConfigForceSaveInSentEnabled_Type.__name__ = "Integer32"
_BesConfigForceSaveInSentEnabled_Object = MibTableColumn
besConfigForceSaveInSentEnabled = _BesConfigForceSaveInSentEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 70),
    _BesConfigForceSaveInSentEnabled_Type()
)
besConfigForceSaveInSentEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigForceSaveInSentEnabled.setStatus("mandatory")


class _BesConfigWirelessEmailRecoEnabled_Type(Integer32):
    """Custom type besConfigWirelessEmailRecoEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BesConfigWirelessEmailRecoEnabled_Type.__name__ = "Integer32"
_BesConfigWirelessEmailRecoEnabled_Object = MibTableColumn
besConfigWirelessEmailRecoEnabled = _BesConfigWirelessEmailRecoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 80),
    _BesConfigWirelessEmailRecoEnabled_Type()
)
besConfigWirelessEmailRecoEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigWirelessEmailRecoEnabled.setStatus("mandatory")
_BesSysHealthTable_Object = MibTable
besSysHealthTable = _BesSysHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25)
)
if mibBuilder.loadTexts:
    besSysHealthTable.setStatus("mandatory")
_BesSysHealthEntry_Object = MibTableRow
besSysHealthEntry = _BesSysHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1)
)
besSysHealthEntry.setIndexNames(
    (0, "BLACKBERRYSERVER-MIB", "besSysHealthServerInstance"),
)
if mibBuilder.loadTexts:
    besSysHealthEntry.setStatus("mandatory")
_BesSysHealthServerInstance_Type = Integer32
_BesSysHealthServerInstance_Object = MibTableColumn
besSysHealthServerInstance = _BesSysHealthServerInstance_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 1),
    _BesSysHealthServerInstance_Type()
)
besSysHealthServerInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthServerInstance.setStatus("mandatory")
_BesSysHealthSrpConnectedState_Type = Integer32
_BesSysHealthSrpConnectedState_Object = MibTableColumn
besSysHealthSrpConnectedState = _BesSysHealthSrpConnectedState_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 10),
    _BesSysHealthSrpConnectedState_Type()
)
besSysHealthSrpConnectedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthSrpConnectedState.setStatus("mandatory")
_BesSysHealthSrpLastConnectDate_Type = DisplayString
_BesSysHealthSrpLastConnectDate_Object = MibTableColumn
besSysHealthSrpLastConnectDate = _BesSysHealthSrpLastConnectDate_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 11),
    _BesSysHealthSrpLastConnectDate_Type()
)
besSysHealthSrpLastConnectDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthSrpLastConnectDate.setStatus("mandatory")
_BesSysHealthSrpReconnectSuccess_Type = Integer32
_BesSysHealthSrpReconnectSuccess_Object = MibTableColumn
besSysHealthSrpReconnectSuccess = _BesSysHealthSrpReconnectSuccess_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 12),
    _BesSysHealthSrpReconnectSuccess_Type()
)
besSysHealthSrpReconnectSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthSrpReconnectSuccess.setStatus("mandatory")
_BesSysHealthSrpReconnectsFail_Type = Integer32
_BesSysHealthSrpReconnectsFail_Object = MibTableColumn
besSysHealthSrpReconnectsFail = _BesSysHealthSrpReconnectsFail_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 13),
    _BesSysHealthSrpReconnectsFail_Type()
)
besSysHealthSrpReconnectsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthSrpReconnectsFail.setStatus("mandatory")
_BesSysHealthSrpTotalSecNotConnected_Type = Integer32
_BesSysHealthSrpTotalSecNotConnected_Object = MibTableColumn
besSysHealthSrpTotalSecNotConnected = _BesSysHealthSrpTotalSecNotConnected_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 14),
    _BesSysHealthSrpTotalSecNotConnected_Type()
)
besSysHealthSrpTotalSecNotConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthSrpTotalSecNotConnected.setStatus("mandatory")
_BesSysHealthSrpLastErrorText_Type = DisplayString
_BesSysHealthSrpLastErrorText_Object = MibTableColumn
besSysHealthSrpLastErrorText = _BesSysHealthSrpLastErrorText_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 15),
    _BesSysHealthSrpLastErrorText_Type()
)
besSysHealthSrpLastErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthSrpLastErrorText.setStatus("mandatory")
_BesSysHealthSrpLastErrorTime_Type = DisplayString
_BesSysHealthSrpLastErrorTime_Object = MibTableColumn
besSysHealthSrpLastErrorTime = _BesSysHealthSrpLastErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 16),
    _BesSysHealthSrpLastErrorTime_Type()
)
besSysHealthSrpLastErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthSrpLastErrorTime.setStatus("mandatory")
_BesSysHealthMsgTotalProc_Type = Integer32
_BesSysHealthMsgTotalProc_Object = MibTableColumn
besSysHealthMsgTotalProc = _BesSysHealthMsgTotalProc_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 20),
    _BesSysHealthMsgTotalProc_Type()
)
besSysHealthMsgTotalProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgTotalProc.setStatus("mandatory")
_BesSysHealthMsgToHandheld_Type = Integer32
_BesSysHealthMsgToHandheld_Object = MibTableColumn
besSysHealthMsgToHandheld = _BesSysHealthMsgToHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 21),
    _BesSysHealthMsgToHandheld_Type()
)
besSysHealthMsgToHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgToHandheld.setStatus("mandatory")
_BesSysHealthMsgFromHandheld_Type = Integer32
_BesSysHealthMsgFromHandheld_Object = MibTableColumn
besSysHealthMsgFromHandheld = _BesSysHealthMsgFromHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 22),
    _BesSysHealthMsgFromHandheld_Type()
)
besSysHealthMsgFromHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgFromHandheld.setStatus("mandatory")
_BesSysHealthMsgFilteredByUser_Type = Integer32
_BesSysHealthMsgFilteredByUser_Object = MibTableColumn
besSysHealthMsgFilteredByUser = _BesSysHealthMsgFilteredByUser_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 23),
    _BesSysHealthMsgFilteredByUser_Type()
)
besSysHealthMsgFilteredByUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgFilteredByUser.setStatus("mandatory")
_BesSysHealthMsgFilteredByGlobal_Type = Integer32
_BesSysHealthMsgFilteredByGlobal_Object = MibTableColumn
besSysHealthMsgFilteredByGlobal = _BesSysHealthMsgFilteredByGlobal_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 24),
    _BesSysHealthMsgFilteredByGlobal_Type()
)
besSysHealthMsgFilteredByGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgFilteredByGlobal.setStatus("mandatory")
_BesSysHealthMsgPending_Type = Integer32
_BesSysHealthMsgPending_Object = MibTableColumn
besSysHealthMsgPending = _BesSysHealthMsgPending_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 25),
    _BesSysHealthMsgPending_Type()
)
besSysHealthMsgPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgPending.setStatus("mandatory")
_BesSysHealthMsgExpired_Type = Integer32
_BesSysHealthMsgExpired_Object = MibTableColumn
besSysHealthMsgExpired = _BesSysHealthMsgExpired_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 26),
    _BesSysHealthMsgExpired_Type()
)
besSysHealthMsgExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgExpired.setStatus("mandatory")
_BesSysHealthMsgErrors_Type = Integer32
_BesSysHealthMsgErrors_Object = MibTableColumn
besSysHealthMsgErrors = _BesSysHealthMsgErrors_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 27),
    _BesSysHealthMsgErrors_Type()
)
besSysHealthMsgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgErrors.setStatus("mandatory")
_BesSysHealthMsgMoreRequests_Type = Integer32
_BesSysHealthMsgMoreRequests_Object = MibTableColumn
besSysHealthMsgMoreRequests = _BesSysHealthMsgMoreRequests_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 28),
    _BesSysHealthMsgMoreRequests_Type()
)
besSysHealthMsgMoreRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgMoreRequests.setStatus("mandatory")
_BesSysHealthCalUsersOTACEnabled_Type = Integer32
_BesSysHealthCalUsersOTACEnabled_Object = MibTableColumn
besSysHealthCalUsersOTACEnabled = _BesSysHealthCalUsersOTACEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 40),
    _BesSysHealthCalUsersOTACEnabled_Type()
)
besSysHealthCalUsersOTACEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthCalUsersOTACEnabled.setStatus("mandatory")
_BesSysHealthCalEventToHandheld_Type = Integer32
_BesSysHealthCalEventToHandheld_Object = MibTableColumn
besSysHealthCalEventToHandheld = _BesSysHealthCalEventToHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 41),
    _BesSysHealthCalEventToHandheld_Type()
)
besSysHealthCalEventToHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthCalEventToHandheld.setStatus("mandatory")
_BesSysHealthCalEventFromHandheld_Type = Integer32
_BesSysHealthCalEventFromHandheld_Object = MibTableColumn
besSysHealthCalEventFromHandheld = _BesSysHealthCalEventFromHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 42),
    _BesSysHealthCalEventFromHandheld_Type()
)
besSysHealthCalEventFromHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthCalEventFromHandheld.setStatus("mandatory")
_BesSysHealthWERUsersEnabled_Type = Integer32
_BesSysHealthWERUsersEnabled_Object = MibTableColumn
besSysHealthWERUsersEnabled = _BesSysHealthWERUsersEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 50),
    _BesSysHealthWERUsersEnabled_Type()
)
besSysHealthWERUsersEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthWERUsersEnabled.setStatus("mandatory")
_BesSysHealthWERRequestsToHandheld_Type = Integer32
_BesSysHealthWERRequestsToHandheld_Object = MibTableColumn
besSysHealthWERRequestsToHandheld = _BesSysHealthWERRequestsToHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 51),
    _BesSysHealthWERRequestsToHandheld_Type()
)
besSysHealthWERRequestsToHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthWERRequestsToHandheld.setStatus("mandatory")
_BesSysHealthWERRequestsFromHandheld_Type = Integer32
_BesSysHealthWERRequestsFromHandheld_Object = MibTableColumn
besSysHealthWERRequestsFromHandheld = _BesSysHealthWERRequestsFromHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 52),
    _BesSysHealthWERRequestsFromHandheld_Type()
)
besSysHealthWERRequestsFromHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthWERRequestsFromHandheld.setStatus("mandatory")
_BesSysHealthMdsDeviceConnections_Type = Integer32
_BesSysHealthMdsDeviceConnections_Object = MibTableColumn
besSysHealthMdsDeviceConnections = _BesSysHealthMdsDeviceConnections_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 60),
    _BesSysHealthMdsDeviceConnections_Type()
)
besSysHealthMdsDeviceConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsDeviceConnections.setStatus("mandatory")
_BesSysHealthMdsPushConnections_Type = Integer32
_BesSysHealthMdsPushConnections_Object = MibTableColumn
besSysHealthMdsPushConnections = _BesSysHealthMdsPushConnections_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 61),
    _BesSysHealthMdsPushConnections_Type()
)
besSysHealthMdsPushConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsPushConnections.setStatus("mandatory")
_BesSysHealthMdsTotalBytesFromDevices_Type = Integer32
_BesSysHealthMdsTotalBytesFromDevices_Object = MibTableColumn
besSysHealthMdsTotalBytesFromDevices = _BesSysHealthMdsTotalBytesFromDevices_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 62),
    _BesSysHealthMdsTotalBytesFromDevices_Type()
)
besSysHealthMdsTotalBytesFromDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsTotalBytesFromDevices.setStatus("mandatory")
_BesSysHealthMdsMaxPacketSizeFromDevice_Type = Integer32
_BesSysHealthMdsMaxPacketSizeFromDevice_Object = MibTableColumn
besSysHealthMdsMaxPacketSizeFromDevice = _BesSysHealthMdsMaxPacketSizeFromDevice_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 63),
    _BesSysHealthMdsMaxPacketSizeFromDevice_Type()
)
besSysHealthMdsMaxPacketSizeFromDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsMaxPacketSizeFromDevice.setStatus("mandatory")
_BesSysHealthMdsAvgPacketSizeFromDevice_Type = Integer32
_BesSysHealthMdsAvgPacketSizeFromDevice_Object = MibTableColumn
besSysHealthMdsAvgPacketSizeFromDevice = _BesSysHealthMdsAvgPacketSizeFromDevice_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 64),
    _BesSysHealthMdsAvgPacketSizeFromDevice_Type()
)
besSysHealthMdsAvgPacketSizeFromDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsAvgPacketSizeFromDevice.setStatus("mandatory")
_BesSysHealthMdsTotalBytesToDevice_Type = Integer32
_BesSysHealthMdsTotalBytesToDevice_Object = MibTableColumn
besSysHealthMdsTotalBytesToDevice = _BesSysHealthMdsTotalBytesToDevice_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 65),
    _BesSysHealthMdsTotalBytesToDevice_Type()
)
besSysHealthMdsTotalBytesToDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsTotalBytesToDevice.setStatus("mandatory")
_BesSysHealthMdsMaxPacketSizeToDevice_Type = Integer32
_BesSysHealthMdsMaxPacketSizeToDevice_Object = MibTableColumn
besSysHealthMdsMaxPacketSizeToDevice = _BesSysHealthMdsMaxPacketSizeToDevice_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 66),
    _BesSysHealthMdsMaxPacketSizeToDevice_Type()
)
besSysHealthMdsMaxPacketSizeToDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsMaxPacketSizeToDevice.setStatus("mandatory")
_BesSysHealthMdsAvgPacketSizeToDevice_Type = Integer32
_BesSysHealthMdsAvgPacketSizeToDevice_Object = MibTableColumn
besSysHealthMdsAvgPacketSizeToDevice = _BesSysHealthMdsAvgPacketSizeToDevice_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 67),
    _BesSysHealthMdsAvgPacketSizeToDevice_Type()
)
besSysHealthMdsAvgPacketSizeToDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsAvgPacketSizeToDevice.setStatus("mandatory")
_BesSysHealthMdsRefusedPackets_Type = Integer32
_BesSysHealthMdsRefusedPackets_Object = MibTableColumn
besSysHealthMdsRefusedPackets = _BesSysHealthMdsRefusedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 68),
    _BesSysHealthMdsRefusedPackets_Type()
)
besSysHealthMdsRefusedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsRefusedPackets.setStatus("mandatory")
_BesSysHealthMdsInvalidPackets_Type = Integer32
_BesSysHealthMdsInvalidPackets_Object = MibTableColumn
besSysHealthMdsInvalidPackets = _BesSysHealthMdsInvalidPackets_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 69),
    _BesSysHealthMdsInvalidPackets_Type()
)
besSysHealthMdsInvalidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsInvalidPackets.setStatus("mandatory")
_BesSysHealthMdsConnectionSuccess_Type = Integer32
_BesSysHealthMdsConnectionSuccess_Object = MibTableColumn
besSysHealthMdsConnectionSuccess = _BesSysHealthMdsConnectionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 70),
    _BesSysHealthMdsConnectionSuccess_Type()
)
besSysHealthMdsConnectionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsConnectionSuccess.setStatus("mandatory")
_BesSysHealthMdsConnectionFailure_Type = Integer32
_BesSysHealthMdsConnectionFailure_Object = MibTableColumn
besSysHealthMdsConnectionFailure = _BesSysHealthMdsConnectionFailure_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 71),
    _BesSysHealthMdsConnectionFailure_Type()
)
besSysHealthMdsConnectionFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsConnectionFailure.setStatus("mandatory")
_BesSysHealthMdsConnectionTruncated_Type = Integer32
_BesSysHealthMdsConnectionTruncated_Object = MibTableColumn
besSysHealthMdsConnectionTruncated = _BesSysHealthMdsConnectionTruncated_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 72),
    _BesSysHealthMdsConnectionTruncated_Type()
)
besSysHealthMdsConnectionTruncated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsConnectionTruncated.setStatus("mandatory")
_BesSysHealthV1MsgsPending_Type = Integer32
_BesSysHealthV1MsgsPending_Object = MibTableColumn
besSysHealthV1MsgsPending = _BesSysHealthV1MsgsPending_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 202),
    _BesSysHealthV1MsgsPending_Type()
)
besSysHealthV1MsgsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthV1MsgsPending.setStatus("mandatory")
_BesSysHealthV1TotalMsgsSent_Type = Integer32
_BesSysHealthV1TotalMsgsSent_Object = MibTableColumn
besSysHealthV1TotalMsgsSent = _BesSysHealthV1TotalMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 203),
    _BesSysHealthV1TotalMsgsSent_Type()
)
besSysHealthV1TotalMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthV1TotalMsgsSent.setStatus("mandatory")
_BesSysHealthV1TotalMsgsReceived_Type = Integer32
_BesSysHealthV1TotalMsgsReceived_Object = MibTableColumn
besSysHealthV1TotalMsgsReceived = _BesSysHealthV1TotalMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 204),
    _BesSysHealthV1TotalMsgsReceived_Type()
)
besSysHealthV1TotalMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthV1TotalMsgsReceived.setStatus("mandatory")
_BesSysHealthV1TotalMsgsExpired_Type = Integer32
_BesSysHealthV1TotalMsgsExpired_Object = MibTableColumn
besSysHealthV1TotalMsgsExpired = _BesSysHealthV1TotalMsgsExpired_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 205),
    _BesSysHealthV1TotalMsgsExpired_Type()
)
besSysHealthV1TotalMsgsExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthV1TotalMsgsExpired.setStatus("mandatory")
_BesSysHealthV1TotalMsgsFiltered_Type = Integer32
_BesSysHealthV1TotalMsgsFiltered_Object = MibTableColumn
besSysHealthV1TotalMsgsFiltered = _BesSysHealthV1TotalMsgsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 206),
    _BesSysHealthV1TotalMsgsFiltered_Type()
)
besSysHealthV1TotalMsgsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthV1TotalMsgsFiltered.setStatus("mandatory")
_BesSysHealthV1MsgsSentPerMin_Type = Integer32
_BesSysHealthV1MsgsSentPerMin_Object = MibTableColumn
besSysHealthV1MsgsSentPerMin = _BesSysHealthV1MsgsSentPerMin_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 207),
    _BesSysHealthV1MsgsSentPerMin_Type()
)
besSysHealthV1MsgsSentPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthV1MsgsSentPerMin.setStatus("mandatory")
_BesSysHealthV1MsgsRecvdPerMin_Type = Integer32
_BesSysHealthV1MsgsRecvdPerMin_Object = MibTableColumn
besSysHealthV1MsgsRecvdPerMin = _BesSysHealthV1MsgsRecvdPerMin_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 208),
    _BesSysHealthV1MsgsRecvdPerMin_Type()
)
besSysHealthV1MsgsRecvdPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthV1MsgsRecvdPerMin.setStatus("mandatory")


class _BesSysHealthV1SRPConnectState_Type(Integer32):
    """Custom type besSysHealthV1SRPConnectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BesSysHealthV1SRPConnectState_Type.__name__ = "Integer32"
_BesSysHealthV1SRPConnectState_Object = MibTableColumn
besSysHealthV1SRPConnectState = _BesSysHealthV1SRPConnectState_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 209),
    _BesSysHealthV1SRPConnectState_Type()
)
besSysHealthV1SRPConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthV1SRPConnectState.setStatus("mandatory")
_BesMailServerHealthTable_Object = MibTable
besMailServerHealthTable = _BesMailServerHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 26)
)
if mibBuilder.loadTexts:
    besMailServerHealthTable.setStatus("mandatory")
_BesMailServerHealthEntry_Object = MibTableRow
besMailServerHealthEntry = _BesMailServerHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 26, 1)
)
besMailServerHealthEntry.setIndexNames(
    (0, "BLACKBERRYSERVER-MIB", "besMailServerHealthServerInstance"),
    (0, "BLACKBERRYSERVER-MIB", "besMailServerHealthServerId"),
)
if mibBuilder.loadTexts:
    besMailServerHealthEntry.setStatus("mandatory")
_BesMailServerHealthServerInstance_Type = Integer32
_BesMailServerHealthServerInstance_Object = MibTableColumn
besMailServerHealthServerInstance = _BesMailServerHealthServerInstance_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 26, 1, 1),
    _BesMailServerHealthServerInstance_Type()
)
besMailServerHealthServerInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besMailServerHealthServerInstance.setStatus("mandatory")
_BesMailServerHealthServerId_Type = Integer32
_BesMailServerHealthServerId_Object = MibTableColumn
besMailServerHealthServerId = _BesMailServerHealthServerId_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 26, 1, 2),
    _BesMailServerHealthServerId_Type()
)
besMailServerHealthServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besMailServerHealthServerId.setStatus("mandatory")
_BesMailServerHealthServerName_Type = DisplayString
_BesMailServerHealthServerName_Object = MibTableColumn
besMailServerHealthServerName = _BesMailServerHealthServerName_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 26, 1, 3),
    _BesMailServerHealthServerName_Type()
)
besMailServerHealthServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besMailServerHealthServerName.setStatus("mandatory")
_BesMailServerHealthTotalUsers_Type = Integer32
_BesMailServerHealthTotalUsers_Object = MibTableColumn
besMailServerHealthTotalUsers = _BesMailServerHealthTotalUsers_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 26, 1, 10),
    _BesMailServerHealthTotalUsers_Type()
)
besMailServerHealthTotalUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besMailServerHealthTotalUsers.setStatus("mandatory")
_BesMailServerHealthAvgResponceTime10min_Type = Integer32
_BesMailServerHealthAvgResponceTime10min_Object = MibTableColumn
besMailServerHealthAvgResponceTime10min = _BesMailServerHealthAvgResponceTime10min_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 26, 1, 11),
    _BesMailServerHealthAvgResponceTime10min_Type()
)
besMailServerHealthAvgResponceTime10min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besMailServerHealthAvgResponceTime10min.setStatus("mandatory")
_BesMailServerHealthFailedConn10min_Type = Integer32
_BesMailServerHealthFailedConn10min_Object = MibTableColumn
besMailServerHealthFailedConn10min = _BesMailServerHealthFailedConn10min_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 26, 1, 12),
    _BesMailServerHealthFailedConn10min_Type()
)
besMailServerHealthFailedConn10min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besMailServerHealthFailedConn10min.setStatus("mandatory")
_BesUserHealthTable_Object = MibTable
besUserHealthTable = _BesUserHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30)
)
if mibBuilder.loadTexts:
    besUserHealthTable.setStatus("mandatory")
_BesUserHealthEntry_Object = MibTableRow
besUserHealthEntry = _BesUserHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1)
)
besUserHealthEntry.setIndexNames(
    (0, "BLACKBERRYSERVER-MIB", "besUserHealthServerInstance"),
    (0, "BLACKBERRYSERVER-MIB", "besUserHealthUserId"),
)
if mibBuilder.loadTexts:
    besUserHealthEntry.setStatus("mandatory")
_BesUserHealthServerInstance_Type = Integer32
_BesUserHealthServerInstance_Object = MibTableColumn
besUserHealthServerInstance = _BesUserHealthServerInstance_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 1),
    _BesUserHealthServerInstance_Type()
)
besUserHealthServerInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthServerInstance.setStatus("mandatory")
_BesUserHealthUserId_Type = Integer32
_BesUserHealthUserId_Object = MibTableColumn
besUserHealthUserId = _BesUserHealthUserId_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 2),
    _BesUserHealthUserId_Type()
)
besUserHealthUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthUserId.setStatus("mandatory")
_BesUserHealthUserName_Type = DisplayString
_BesUserHealthUserName_Object = MibTableColumn
besUserHealthUserName = _BesUserHealthUserName_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 3),
    _BesUserHealthUserName_Type()
)
besUserHealthUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthUserName.setStatus("mandatory")
_BesUserHealthLastErrorText_Type = DisplayString
_BesUserHealthLastErrorText_Object = MibTableColumn
besUserHealthLastErrorText = _BesUserHealthLastErrorText_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 10),
    _BesUserHealthLastErrorText_Type()
)
besUserHealthLastErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthLastErrorText.setStatus("mandatory")
_BesUserHealthLastErrorTime_Type = DisplayString
_BesUserHealthLastErrorTime_Object = MibTableColumn
besUserHealthLastErrorTime = _BesUserHealthLastErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 11),
    _BesUserHealthLastErrorTime_Type()
)
besUserHealthLastErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthLastErrorTime.setStatus("mandatory")
_BesUserHealthDeviceNetwork_Type = DisplayString
_BesUserHealthDeviceNetwork_Object = MibTableColumn
besUserHealthDeviceNetwork = _BesUserHealthDeviceNetwork_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 20),
    _BesUserHealthDeviceNetwork_Type()
)
besUserHealthDeviceNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthDeviceNetwork.setStatus("mandatory")
_BesUserHealthDevicePIN_Type = DisplayString
_BesUserHealthDevicePIN_Object = MibTableColumn
besUserHealthDevicePIN = _BesUserHealthDevicePIN_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 21),
    _BesUserHealthDevicePIN_Type()
)
besUserHealthDevicePIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthDevicePIN.setStatus("mandatory")
_BesUserHealthDeviceInCradle_Type = Integer32
_BesUserHealthDeviceInCradle_Object = MibTableColumn
besUserHealthDeviceInCradle = _BesUserHealthDeviceInCradle_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 22),
    _BesUserHealthDeviceInCradle_Type()
)
besUserHealthDeviceInCradle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthDeviceInCradle.setStatus("mandatory")
_BesUserHealthNumRedirectedFolders_Type = Integer32
_BesUserHealthNumRedirectedFolders_Object = MibTableColumn
besUserHealthNumRedirectedFolders = _BesUserHealthNumRedirectedFolders_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 30),
    _BesUserHealthNumRedirectedFolders_Type()
)
besUserHealthNumRedirectedFolders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthNumRedirectedFolders.setStatus("mandatory")


class _BesUserHealthSaveInSent_Type(Integer32):
    """Custom type besUserHealthSaveInSent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BesUserHealthSaveInSent_Type.__name__ = "Integer32"
_BesUserHealthSaveInSent_Object = MibTableColumn
besUserHealthSaveInSent = _BesUserHealthSaveInSent_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 31),
    _BesUserHealthSaveInSent_Type()
)
besUserHealthSaveInSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthSaveInSent.setStatus("mandatory")


class _BesUserHealthRedirectEnabledOnDesktop_Type(Integer32):
    """Custom type besUserHealthRedirectEnabledOnDesktop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BesUserHealthRedirectEnabledOnDesktop_Type.__name__ = "Integer32"
_BesUserHealthRedirectEnabledOnDesktop_Object = MibTableColumn
besUserHealthRedirectEnabledOnDesktop = _BesUserHealthRedirectEnabledOnDesktop_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 32),
    _BesUserHealthRedirectEnabledOnDesktop_Type()
)
besUserHealthRedirectEnabledOnDesktop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthRedirectEnabledOnDesktop.setStatus("mandatory")


class _BesUserHealthDisableWhileInCradle_Type(Integer32):
    """Custom type besUserHealthDisableWhileInCradle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BesUserHealthDisableWhileInCradle_Type.__name__ = "Integer32"
_BesUserHealthDisableWhileInCradle_Object = MibTableColumn
besUserHealthDisableWhileInCradle = _BesUserHealthDisableWhileInCradle_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 33),
    _BesUserHealthDisableWhileInCradle_Type()
)
besUserHealthDisableWhileInCradle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthDisableWhileInCradle.setStatus("mandatory")
_BesUserHealthFullyConfigured_Type = Integer32
_BesUserHealthFullyConfigured_Object = MibTableColumn
besUserHealthFullyConfigured = _BesUserHealthFullyConfigured_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 34),
    _BesUserHealthFullyConfigured_Type()
)
besUserHealthFullyConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthFullyConfigured.setStatus("mandatory")
_BesUserHealthEnabled_Type = Integer32
_BesUserHealthEnabled_Object = MibTableColumn
besUserHealthEnabled = _BesUserHealthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 35),
    _BesUserHealthEnabled_Type()
)
besUserHealthEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthEnabled.setStatus("mandatory")
_BesUserHealthMsgTotalProc_Type = Integer32
_BesUserHealthMsgTotalProc_Object = MibTableColumn
besUserHealthMsgTotalProc = _BesUserHealthMsgTotalProc_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 40),
    _BesUserHealthMsgTotalProc_Type()
)
besUserHealthMsgTotalProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgTotalProc.setStatus("mandatory")
_BesUserHealthMsgToHandheld_Type = Integer32
_BesUserHealthMsgToHandheld_Object = MibTableColumn
besUserHealthMsgToHandheld = _BesUserHealthMsgToHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 41),
    _BesUserHealthMsgToHandheld_Type()
)
besUserHealthMsgToHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgToHandheld.setStatus("mandatory")
_BesUserHealthMsgFromHandheld_Type = Integer32
_BesUserHealthMsgFromHandheld_Object = MibTableColumn
besUserHealthMsgFromHandheld = _BesUserHealthMsgFromHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 42),
    _BesUserHealthMsgFromHandheld_Type()
)
besUserHealthMsgFromHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgFromHandheld.setStatus("mandatory")
_BesUserHealthMsgFiltered_Type = Integer32
_BesUserHealthMsgFiltered_Object = MibTableColumn
besUserHealthMsgFiltered = _BesUserHealthMsgFiltered_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 43),
    _BesUserHealthMsgFiltered_Type()
)
besUserHealthMsgFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgFiltered.setStatus("mandatory")
_BesUserHealthMsgPending_Type = Integer32
_BesUserHealthMsgPending_Object = MibTableColumn
besUserHealthMsgPending = _BesUserHealthMsgPending_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 44),
    _BesUserHealthMsgPending_Type()
)
besUserHealthMsgPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgPending.setStatus("mandatory")
_BesUserHealthMsgExpired_Type = Integer32
_BesUserHealthMsgExpired_Object = MibTableColumn
besUserHealthMsgExpired = _BesUserHealthMsgExpired_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 45),
    _BesUserHealthMsgExpired_Type()
)
besUserHealthMsgExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgExpired.setStatus("mandatory")
_BesUserHealthMsgErrors_Type = Integer32
_BesUserHealthMsgErrors_Object = MibTableColumn
besUserHealthMsgErrors = _BesUserHealthMsgErrors_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 46),
    _BesUserHealthMsgErrors_Type()
)
besUserHealthMsgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgErrors.setStatus("mandatory")
_BesUserHealthMsgMoreRequests_Type = Integer32
_BesUserHealthMsgMoreRequests_Object = MibTableColumn
besUserHealthMsgMoreRequests = _BesUserHealthMsgMoreRequests_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 47),
    _BesUserHealthMsgMoreRequests_Type()
)
besUserHealthMsgMoreRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgMoreRequests.setStatus("mandatory")
_BesUserHealthMsgForwardedFromDevice_Type = Integer32
_BesUserHealthMsgForwardedFromDevice_Object = MibTableColumn
besUserHealthMsgForwardedFromDevice = _BesUserHealthMsgForwardedFromDevice_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 48),
    _BesUserHealthMsgForwardedFromDevice_Type()
)
besUserHealthMsgForwardedFromDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgForwardedFromDevice.setStatus("mandatory")
_BesUserHealthMsgRepliedToWithText_Type = Integer32
_BesUserHealthMsgRepliedToWithText_Object = MibTableColumn
besUserHealthMsgRepliedToWithText = _BesUserHealthMsgRepliedToWithText_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 49),
    _BesUserHealthMsgRepliedToWithText_Type()
)
besUserHealthMsgRepliedToWithText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgRepliedToWithText.setStatus("mandatory")
_BesUserHealthLastTimeInCradle_Type = DisplayString
_BesUserHealthLastTimeInCradle_Object = MibTableColumn
besUserHealthLastTimeInCradle = _BesUserHealthLastTimeInCradle_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 60),
    _BesUserHealthLastTimeInCradle_Type()
)
besUserHealthLastTimeInCradle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthLastTimeInCradle.setStatus("mandatory")
_BesUserHealthLastInteractionWithDevice_Type = DisplayString
_BesUserHealthLastInteractionWithDevice_Object = MibTableColumn
besUserHealthLastInteractionWithDevice = _BesUserHealthLastInteractionWithDevice_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 61),
    _BesUserHealthLastInteractionWithDevice_Type()
)
besUserHealthLastInteractionWithDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthLastInteractionWithDevice.setStatus("mandatory")
_BesUserHealthLastMessageForwarded_Type = DisplayString
_BesUserHealthLastMessageForwarded_Object = MibTableColumn
besUserHealthLastMessageForwarded = _BesUserHealthLastMessageForwarded_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 62),
    _BesUserHealthLastMessageForwarded_Type()
)
besUserHealthLastMessageForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthLastMessageForwarded.setStatus("mandatory")
_BesUserHealthLastKeyDateGenerated_Type = DisplayString
_BesUserHealthLastKeyDateGenerated_Object = MibTableColumn
besUserHealthLastKeyDateGenerated = _BesUserHealthLastKeyDateGenerated_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 63),
    _BesUserHealthLastKeyDateGenerated_Type()
)
besUserHealthLastKeyDateGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthLastKeyDateGenerated.setStatus("mandatory")
_BesUserHealthAvgKBForwarded_Type = Integer32
_BesUserHealthAvgKBForwarded_Object = MibTableColumn
besUserHealthAvgKBForwarded = _BesUserHealthAvgKBForwarded_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 70),
    _BesUserHealthAvgKBForwarded_Type()
)
besUserHealthAvgKBForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthAvgKBForwarded.setStatus("mandatory")
_BesUserHealthAvgKBReplyWithText_Type = Integer32
_BesUserHealthAvgKBReplyWithText_Object = MibTableColumn
besUserHealthAvgKBReplyWithText = _BesUserHealthAvgKBReplyWithText_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 71),
    _BesUserHealthAvgKBReplyWithText_Type()
)
besUserHealthAvgKBReplyWithText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthAvgKBReplyWithText.setStatus("mandatory")
_BesUserHealthAvgLatencyInSecLast10Msg_Type = Integer32
_BesUserHealthAvgLatencyInSecLast10Msg_Object = MibTableColumn
besUserHealthAvgLatencyInSecLast10Msg = _BesUserHealthAvgLatencyInSecLast10Msg_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 72),
    _BesUserHealthAvgLatencyInSecLast10Msg_Type()
)
besUserHealthAvgLatencyInSecLast10Msg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthAvgLatencyInSecLast10Msg.setStatus("mandatory")


class _BesUserHealthCalOTAEnabled_Type(Integer32):
    """Custom type besUserHealthCalOTAEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BesUserHealthCalOTAEnabled_Type.__name__ = "Integer32"
_BesUserHealthCalOTAEnabled_Object = MibTableColumn
besUserHealthCalOTAEnabled = _BesUserHealthCalOTAEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 80),
    _BesUserHealthCalOTAEnabled_Type()
)
besUserHealthCalOTAEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthCalOTAEnabled.setStatus("mandatory")
_BesUserHealthCalEventToHandheld_Type = Integer32
_BesUserHealthCalEventToHandheld_Object = MibTableColumn
besUserHealthCalEventToHandheld = _BesUserHealthCalEventToHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 81),
    _BesUserHealthCalEventToHandheld_Type()
)
besUserHealthCalEventToHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthCalEventToHandheld.setStatus("mandatory")
_BesUserHealthCalEventFromHandheld_Type = Integer32
_BesUserHealthCalEventFromHandheld_Object = MibTableColumn
besUserHealthCalEventFromHandheld = _BesUserHealthCalEventFromHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 82),
    _BesUserHealthCalEventFromHandheld_Type()
)
besUserHealthCalEventFromHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthCalEventFromHandheld.setStatus("mandatory")


class _BesUserHealthWirelessEmailRecoEnabled_Type(Integer32):
    """Custom type besUserHealthWirelessEmailRecoEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BesUserHealthWirelessEmailRecoEnabled_Type.__name__ = "Integer32"
_BesUserHealthWirelessEmailRecoEnabled_Object = MibTableColumn
besUserHealthWirelessEmailRecoEnabled = _BesUserHealthWirelessEmailRecoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 90),
    _BesUserHealthWirelessEmailRecoEnabled_Type()
)
besUserHealthWirelessEmailRecoEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthWirelessEmailRecoEnabled.setStatus("mandatory")
_BesUserHealthWERRequestsToHandheld_Type = Integer32
_BesUserHealthWERRequestsToHandheld_Object = MibTableColumn
besUserHealthWERRequestsToHandheld = _BesUserHealthWERRequestsToHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 91),
    _BesUserHealthWERRequestsToHandheld_Type()
)
besUserHealthWERRequestsToHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthWERRequestsToHandheld.setStatus("mandatory")
_BesUserHealthWERRequestsFromHandheld_Type = Integer32
_BesUserHealthWERRequestsFromHandheld_Object = MibTableColumn
besUserHealthWERRequestsFromHandheld = _BesUserHealthWERRequestsFromHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 92),
    _BesUserHealthWERRequestsFromHandheld_Type()
)
besUserHealthWERRequestsFromHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthWERRequestsFromHandheld.setStatus("mandatory")

# Managed Objects groups


# Notification objects

besSRPConnectEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 0, 1)
)
besSRPConnectEvent.setObjects(
    ("BLACKBERRYSERVER-MIB", "besSRPConnectState")
)
if mibBuilder.loadTexts:
    besSRPConnectEvent.setStatus(
        ""
    )

besHungThreadEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 0, 3)
)
if mibBuilder.loadTexts:
    besHungThreadEvent.setStatus(
        ""
    )

besMailServerDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 0, 5)
)
if mibBuilder.loadTexts:
    besMailServerDownEvent.setStatus(
        ""
    )

besMDStoBESConnectionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 0, 7)
)
if mibBuilder.loadTexts:
    besMDStoBESConnectionEvent.setStatus(
        ""
    )

besMDSStartStopEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 0, 11)
)
if mibBuilder.loadTexts:
    besMDSStartStopEvent.setStatus(
        ""
    )

besMDStoDBConnectionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 0, 13)
)
if mibBuilder.loadTexts:
    besMDStoDBConnectionEvent.setStatus(
        ""
    )

besCriticalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 0, 21)
)
if mibBuilder.loadTexts:
    besCriticalEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLACKBERRYSERVER-MIB",
    **{"rim": rim,
       "blackBerryServer": blackBerryServer,
       "besSRPConnectEvent": besSRPConnectEvent,
       "besHungThreadEvent": besHungThreadEvent,
       "besMailServerDownEvent": besMailServerDownEvent,
       "besMDStoBESConnectionEvent": besMDStoBESConnectionEvent,
       "besMDSStartStopEvent": besMDSStartStopEvent,
       "besMDStoDBConnectionEvent": besMDStoDBConnectionEvent,
       "besCriticalEvent": besCriticalEvent,
       "version": version,
       "besTotMsgsPending": besTotMsgsPending,
       "besTotMsgsSent": besTotMsgsSent,
       "besTotMsgsRecvd": besTotMsgsRecvd,
       "besTotMsgsXpired": besTotMsgsXpired,
       "besTotMsgsFiltered": besTotMsgsFiltered,
       "besTotMsgsSentPerMin": besTotMsgsSentPerMin,
       "besTotMsgsRecvdPerMin": besTotMsgsRecvdPerMin,
       "besTrapVariables": besTrapVariables,
       "besSRPConnectState": besSRPConnectState,
       "besNumServerInfoAvailable": besNumServerInfoAvailable,
       "besConfigTable": besConfigTable,
       "besConfigEntry": besConfigEntry,
       "besConfigServerInstance": besConfigServerInstance,
       "besConfigServerName": besConfigServerName,
       "besConfigVersionString": besConfigVersionString,
       "besConfigReleaseMaj": besConfigReleaseMaj,
       "besConfigReleaseMin": besConfigReleaseMin,
       "besConfigReleaseServicePack": besConfigReleaseServicePack,
       "besConfigReleaseBuild": besConfigReleaseBuild,
       "besConfigLicenceTotal": besConfigLicenceTotal,
       "besConfigLicenceUsed": besConfigLicenceUsed,
       "besConfigLicenceRemaining": besConfigLicenceRemaining,
       "besConfigServerUID": besConfigServerUID,
       "besConfigSystemAttendant": besConfigSystemAttendant,
       "besConfigSRPHost": besConfigSRPHost,
       "besConfigSRPPort": besConfigSRPPort,
       "besConfigAutoBCCEnabled": besConfigAutoBCCEnabled,
       "besConfigAutoBCCAddress": besConfigAutoBCCAddress,
       "besConfigForceSaveInSentEnabled": besConfigForceSaveInSentEnabled,
       "besConfigWirelessEmailRecoEnabled": besConfigWirelessEmailRecoEnabled,
       "besSysHealthTable": besSysHealthTable,
       "besSysHealthEntry": besSysHealthEntry,
       "besSysHealthServerInstance": besSysHealthServerInstance,
       "besSysHealthSrpConnectedState": besSysHealthSrpConnectedState,
       "besSysHealthSrpLastConnectDate": besSysHealthSrpLastConnectDate,
       "besSysHealthSrpReconnectSuccess": besSysHealthSrpReconnectSuccess,
       "besSysHealthSrpReconnectsFail": besSysHealthSrpReconnectsFail,
       "besSysHealthSrpTotalSecNotConnected": besSysHealthSrpTotalSecNotConnected,
       "besSysHealthSrpLastErrorText": besSysHealthSrpLastErrorText,
       "besSysHealthSrpLastErrorTime": besSysHealthSrpLastErrorTime,
       "besSysHealthMsgTotalProc": besSysHealthMsgTotalProc,
       "besSysHealthMsgToHandheld": besSysHealthMsgToHandheld,
       "besSysHealthMsgFromHandheld": besSysHealthMsgFromHandheld,
       "besSysHealthMsgFilteredByUser": besSysHealthMsgFilteredByUser,
       "besSysHealthMsgFilteredByGlobal": besSysHealthMsgFilteredByGlobal,
       "besSysHealthMsgPending": besSysHealthMsgPending,
       "besSysHealthMsgExpired": besSysHealthMsgExpired,
       "besSysHealthMsgErrors": besSysHealthMsgErrors,
       "besSysHealthMsgMoreRequests": besSysHealthMsgMoreRequests,
       "besSysHealthCalUsersOTACEnabled": besSysHealthCalUsersOTACEnabled,
       "besSysHealthCalEventToHandheld": besSysHealthCalEventToHandheld,
       "besSysHealthCalEventFromHandheld": besSysHealthCalEventFromHandheld,
       "besSysHealthWERUsersEnabled": besSysHealthWERUsersEnabled,
       "besSysHealthWERRequestsToHandheld": besSysHealthWERRequestsToHandheld,
       "besSysHealthWERRequestsFromHandheld": besSysHealthWERRequestsFromHandheld,
       "besSysHealthMdsDeviceConnections": besSysHealthMdsDeviceConnections,
       "besSysHealthMdsPushConnections": besSysHealthMdsPushConnections,
       "besSysHealthMdsTotalBytesFromDevices": besSysHealthMdsTotalBytesFromDevices,
       "besSysHealthMdsMaxPacketSizeFromDevice": besSysHealthMdsMaxPacketSizeFromDevice,
       "besSysHealthMdsAvgPacketSizeFromDevice": besSysHealthMdsAvgPacketSizeFromDevice,
       "besSysHealthMdsTotalBytesToDevice": besSysHealthMdsTotalBytesToDevice,
       "besSysHealthMdsMaxPacketSizeToDevice": besSysHealthMdsMaxPacketSizeToDevice,
       "besSysHealthMdsAvgPacketSizeToDevice": besSysHealthMdsAvgPacketSizeToDevice,
       "besSysHealthMdsRefusedPackets": besSysHealthMdsRefusedPackets,
       "besSysHealthMdsInvalidPackets": besSysHealthMdsInvalidPackets,
       "besSysHealthMdsConnectionSuccess": besSysHealthMdsConnectionSuccess,
       "besSysHealthMdsConnectionFailure": besSysHealthMdsConnectionFailure,
       "besSysHealthMdsConnectionTruncated": besSysHealthMdsConnectionTruncated,
       "besSysHealthV1MsgsPending": besSysHealthV1MsgsPending,
       "besSysHealthV1TotalMsgsSent": besSysHealthV1TotalMsgsSent,
       "besSysHealthV1TotalMsgsReceived": besSysHealthV1TotalMsgsReceived,
       "besSysHealthV1TotalMsgsExpired": besSysHealthV1TotalMsgsExpired,
       "besSysHealthV1TotalMsgsFiltered": besSysHealthV1TotalMsgsFiltered,
       "besSysHealthV1MsgsSentPerMin": besSysHealthV1MsgsSentPerMin,
       "besSysHealthV1MsgsRecvdPerMin": besSysHealthV1MsgsRecvdPerMin,
       "besSysHealthV1SRPConnectState": besSysHealthV1SRPConnectState,
       "besMailServerHealthTable": besMailServerHealthTable,
       "besMailServerHealthEntry": besMailServerHealthEntry,
       "besMailServerHealthServerInstance": besMailServerHealthServerInstance,
       "besMailServerHealthServerId": besMailServerHealthServerId,
       "besMailServerHealthServerName": besMailServerHealthServerName,
       "besMailServerHealthTotalUsers": besMailServerHealthTotalUsers,
       "besMailServerHealthAvgResponceTime10min": besMailServerHealthAvgResponceTime10min,
       "besMailServerHealthFailedConn10min": besMailServerHealthFailedConn10min,
       "besUserHealthTable": besUserHealthTable,
       "besUserHealthEntry": besUserHealthEntry,
       "besUserHealthServerInstance": besUserHealthServerInstance,
       "besUserHealthUserId": besUserHealthUserId,
       "besUserHealthUserName": besUserHealthUserName,
       "besUserHealthLastErrorText": besUserHealthLastErrorText,
       "besUserHealthLastErrorTime": besUserHealthLastErrorTime,
       "besUserHealthDeviceNetwork": besUserHealthDeviceNetwork,
       "besUserHealthDevicePIN": besUserHealthDevicePIN,
       "besUserHealthDeviceInCradle": besUserHealthDeviceInCradle,
       "besUserHealthNumRedirectedFolders": besUserHealthNumRedirectedFolders,
       "besUserHealthSaveInSent": besUserHealthSaveInSent,
       "besUserHealthRedirectEnabledOnDesktop": besUserHealthRedirectEnabledOnDesktop,
       "besUserHealthDisableWhileInCradle": besUserHealthDisableWhileInCradle,
       "besUserHealthFullyConfigured": besUserHealthFullyConfigured,
       "besUserHealthEnabled": besUserHealthEnabled,
       "besUserHealthMsgTotalProc": besUserHealthMsgTotalProc,
       "besUserHealthMsgToHandheld": besUserHealthMsgToHandheld,
       "besUserHealthMsgFromHandheld": besUserHealthMsgFromHandheld,
       "besUserHealthMsgFiltered": besUserHealthMsgFiltered,
       "besUserHealthMsgPending": besUserHealthMsgPending,
       "besUserHealthMsgExpired": besUserHealthMsgExpired,
       "besUserHealthMsgErrors": besUserHealthMsgErrors,
       "besUserHealthMsgMoreRequests": besUserHealthMsgMoreRequests,
       "besUserHealthMsgForwardedFromDevice": besUserHealthMsgForwardedFromDevice,
       "besUserHealthMsgRepliedToWithText": besUserHealthMsgRepliedToWithText,
       "besUserHealthLastTimeInCradle": besUserHealthLastTimeInCradle,
       "besUserHealthLastInteractionWithDevice": besUserHealthLastInteractionWithDevice,
       "besUserHealthLastMessageForwarded": besUserHealthLastMessageForwarded,
       "besUserHealthLastKeyDateGenerated": besUserHealthLastKeyDateGenerated,
       "besUserHealthAvgKBForwarded": besUserHealthAvgKBForwarded,
       "besUserHealthAvgKBReplyWithText": besUserHealthAvgKBReplyWithText,
       "besUserHealthAvgLatencyInSecLast10Msg": besUserHealthAvgLatencyInSecLast10Msg,
       "besUserHealthCalOTAEnabled": besUserHealthCalOTAEnabled,
       "besUserHealthCalEventToHandheld": besUserHealthCalEventToHandheld,
       "besUserHealthCalEventFromHandheld": besUserHealthCalEventFromHandheld,
       "besUserHealthWirelessEmailRecoEnabled": besUserHealthWirelessEmailRecoEnabled,
       "besUserHealthWERRequestsToHandheld": besUserHealthWERRequestsToHandheld,
       "besUserHealthWERRequestsFromHandheld": besUserHealthWERRequestsFromHandheld}
)
