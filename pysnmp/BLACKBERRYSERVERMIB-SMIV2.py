# SNMP MIB module (BLACKBERRYSERVERMIB-SMIV2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLACKBERRYSERVERMIB-SMIV2
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:58 2024
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

blackBerryServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3530, 5)
)
blackBerryServer.setRevisions(
        ("2005-08-18 16:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rim_ObjectIdentity = ObjectIdentity
rim = _Rim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3530)
)
_Version_Type = Integer32
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 1),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_BesTotMsgsPending_Type = Integer32
_BesTotMsgsPending_Object = MibScalar
besTotMsgsPending = _BesTotMsgsPending_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 2),
    _BesTotMsgsPending_Type()
)
besTotMsgsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTotMsgsPending.setStatus("current")
_BesTotMsgsSent_Type = Integer32
_BesTotMsgsSent_Object = MibScalar
besTotMsgsSent = _BesTotMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 3),
    _BesTotMsgsSent_Type()
)
besTotMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTotMsgsSent.setStatus("current")
_BesTotMsgsRecvd_Type = Integer32
_BesTotMsgsRecvd_Object = MibScalar
besTotMsgsRecvd = _BesTotMsgsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 4),
    _BesTotMsgsRecvd_Type()
)
besTotMsgsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTotMsgsRecvd.setStatus("current")
_BesTotMsgsXpired_Type = Integer32
_BesTotMsgsXpired_Object = MibScalar
besTotMsgsXpired = _BesTotMsgsXpired_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 5),
    _BesTotMsgsXpired_Type()
)
besTotMsgsXpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTotMsgsXpired.setStatus("current")
_BesTotMsgsFiltered_Type = Integer32
_BesTotMsgsFiltered_Object = MibScalar
besTotMsgsFiltered = _BesTotMsgsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 6),
    _BesTotMsgsFiltered_Type()
)
besTotMsgsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTotMsgsFiltered.setStatus("current")
_BesTotMsgsSentPerMin_Type = Integer32
_BesTotMsgsSentPerMin_Object = MibScalar
besTotMsgsSentPerMin = _BesTotMsgsSentPerMin_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 7),
    _BesTotMsgsSentPerMin_Type()
)
besTotMsgsSentPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTotMsgsSentPerMin.setStatus("current")
_BesTotMsgsRecvdPerMin_Type = Integer32
_BesTotMsgsRecvdPerMin_Object = MibScalar
besTotMsgsRecvdPerMin = _BesTotMsgsRecvdPerMin_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 8),
    _BesTotMsgsRecvdPerMin_Type()
)
besTotMsgsRecvdPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTotMsgsRecvdPerMin.setStatus("current")
_BesTrapVariables_ObjectIdentity = ObjectIdentity
besTrapVariables = _BesTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3530, 5, 9)
)
_BlackBerryServerTraps_ObjectIdentity = ObjectIdentity
blackBerryServerTraps = _BlackBerryServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3530, 5, 10)
)
_BesNumServerInfoAvailable_Type = Integer32
_BesNumServerInfoAvailable_Object = MibScalar
besNumServerInfoAvailable = _BesNumServerInfoAvailable_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 15),
    _BesNumServerInfoAvailable_Type()
)
besNumServerInfoAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besNumServerInfoAvailable.setStatus("current")
_BesConfigTable_Object = MibTable
besConfigTable = _BesConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20)
)
if mibBuilder.loadTexts:
    besConfigTable.setStatus("current")
_BesConfigEntry_Object = MibTableRow
besConfigEntry = _BesConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1)
)
besConfigEntry.setIndexNames(
    (0, "BLACKBERRYSERVERMIB-SMIV2", "besConfigServerInstance"),
)
if mibBuilder.loadTexts:
    besConfigEntry.setStatus("current")


class _BesConfigServerInstance_Type(Integer32):
    """Custom type besConfigServerInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_BesConfigServerInstance_Type.__name__ = "Integer32"
_BesConfigServerInstance_Object = MibTableColumn
besConfigServerInstance = _BesConfigServerInstance_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 1),
    _BesConfigServerInstance_Type()
)
besConfigServerInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigServerInstance.setStatus("current")
_BesConfigServerName_Type = DisplayString
_BesConfigServerName_Object = MibTableColumn
besConfigServerName = _BesConfigServerName_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 2),
    _BesConfigServerName_Type()
)
besConfigServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigServerName.setStatus("current")
_BesConfigVersionString_Type = DisplayString
_BesConfigVersionString_Object = MibTableColumn
besConfigVersionString = _BesConfigVersionString_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 10),
    _BesConfigVersionString_Type()
)
besConfigVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigVersionString.setStatus("current")
_BesConfigReleaseMaj_Type = Integer32
_BesConfigReleaseMaj_Object = MibTableColumn
besConfigReleaseMaj = _BesConfigReleaseMaj_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 11),
    _BesConfigReleaseMaj_Type()
)
besConfigReleaseMaj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigReleaseMaj.setStatus("current")
_BesConfigReleaseMin_Type = Integer32
_BesConfigReleaseMin_Object = MibTableColumn
besConfigReleaseMin = _BesConfigReleaseMin_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 12),
    _BesConfigReleaseMin_Type()
)
besConfigReleaseMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigReleaseMin.setStatus("current")
_BesConfigReleaseServicePack_Type = Integer32
_BesConfigReleaseServicePack_Object = MibTableColumn
besConfigReleaseServicePack = _BesConfigReleaseServicePack_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 13),
    _BesConfigReleaseServicePack_Type()
)
besConfigReleaseServicePack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigReleaseServicePack.setStatus("current")
_BesConfigReleaseBuild_Type = Integer32
_BesConfigReleaseBuild_Object = MibTableColumn
besConfigReleaseBuild = _BesConfigReleaseBuild_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 14),
    _BesConfigReleaseBuild_Type()
)
besConfigReleaseBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigReleaseBuild.setStatus("current")
_BesConfigLicenceTotal_Type = Integer32
_BesConfigLicenceTotal_Object = MibTableColumn
besConfigLicenceTotal = _BesConfigLicenceTotal_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 20),
    _BesConfigLicenceTotal_Type()
)
besConfigLicenceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigLicenceTotal.setStatus("obsolete")
_BesConfigLicenceUsed_Type = Integer32
_BesConfigLicenceUsed_Object = MibTableColumn
besConfigLicenceUsed = _BesConfigLicenceUsed_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 21),
    _BesConfigLicenceUsed_Type()
)
besConfigLicenceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigLicenceUsed.setStatus("current")
_BesConfigLicenceRemaining_Type = Integer32
_BesConfigLicenceRemaining_Object = MibTableColumn
besConfigLicenceRemaining = _BesConfigLicenceRemaining_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 22),
    _BesConfigLicenceRemaining_Type()
)
besConfigLicenceRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigLicenceRemaining.setStatus("obsolete")
_BesConfigServerUID_Type = DisplayString
_BesConfigServerUID_Object = MibTableColumn
besConfigServerUID = _BesConfigServerUID_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 30),
    _BesConfigServerUID_Type()
)
besConfigServerUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigServerUID.setStatus("current")
_BesConfigSystemAttendant_Type = DisplayString
_BesConfigSystemAttendant_Object = MibTableColumn
besConfigSystemAttendant = _BesConfigSystemAttendant_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 40),
    _BesConfigSystemAttendant_Type()
)
besConfigSystemAttendant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigSystemAttendant.setStatus("current")
_BesConfigSRPHost_Type = DisplayString
_BesConfigSRPHost_Object = MibTableColumn
besConfigSRPHost = _BesConfigSRPHost_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 50),
    _BesConfigSRPHost_Type()
)
besConfigSRPHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigSRPHost.setStatus("current")
_BesConfigSRPPort_Type = Integer32
_BesConfigSRPPort_Object = MibTableColumn
besConfigSRPPort = _BesConfigSRPPort_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 51),
    _BesConfigSRPPort_Type()
)
besConfigSRPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigSRPPort.setStatus("current")


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
    besConfigAutoBCCEnabled.setStatus("current")
_BesConfigAutoBCCAddress_Type = DisplayString
_BesConfigAutoBCCAddress_Object = MibTableColumn
besConfigAutoBCCAddress = _BesConfigAutoBCCAddress_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 61),
    _BesConfigAutoBCCAddress_Type()
)
besConfigAutoBCCAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigAutoBCCAddress.setStatus("current")


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
    besConfigForceSaveInSentEnabled.setStatus("current")


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
    besConfigWirelessEmailRecoEnabled.setStatus("current")
_BesConfigLastModified_Type = Integer32
_BesConfigLastModified_Object = MibTableColumn
besConfigLastModified = _BesConfigLastModified_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 20, 1, 301),
    _BesConfigLastModified_Type()
)
besConfigLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigLastModified.setStatus("current")
_BesSysHealthTable_Object = MibTable
besSysHealthTable = _BesSysHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25)
)
if mibBuilder.loadTexts:
    besSysHealthTable.setStatus("current")
_BesSysHealthEntry_Object = MibTableRow
besSysHealthEntry = _BesSysHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1)
)
besSysHealthEntry.setIndexNames(
    (0, "BLACKBERRYSERVERMIB-SMIV2", "besSysHealthServerInstance"),
)
if mibBuilder.loadTexts:
    besSysHealthEntry.setStatus("current")


class _BesSysHealthServerInstance_Type(Integer32):
    """Custom type besSysHealthServerInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_BesSysHealthServerInstance_Type.__name__ = "Integer32"
_BesSysHealthServerInstance_Object = MibTableColumn
besSysHealthServerInstance = _BesSysHealthServerInstance_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 1),
    _BesSysHealthServerInstance_Type()
)
besSysHealthServerInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthServerInstance.setStatus("current")
_BesSysHealthSrpConnectedState_Type = Integer32
_BesSysHealthSrpConnectedState_Object = MibTableColumn
besSysHealthSrpConnectedState = _BesSysHealthSrpConnectedState_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 10),
    _BesSysHealthSrpConnectedState_Type()
)
besSysHealthSrpConnectedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthSrpConnectedState.setStatus("current")
_BesSysHealthSrpLastConnectDate_Type = DisplayString
_BesSysHealthSrpLastConnectDate_Object = MibTableColumn
besSysHealthSrpLastConnectDate = _BesSysHealthSrpLastConnectDate_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 11),
    _BesSysHealthSrpLastConnectDate_Type()
)
besSysHealthSrpLastConnectDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthSrpLastConnectDate.setStatus("current")
_BesSysHealthSrpReconnectSuccess_Type = Integer32
_BesSysHealthSrpReconnectSuccess_Object = MibTableColumn
besSysHealthSrpReconnectSuccess = _BesSysHealthSrpReconnectSuccess_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 12),
    _BesSysHealthSrpReconnectSuccess_Type()
)
besSysHealthSrpReconnectSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthSrpReconnectSuccess.setStatus("current")
_BesSysHealthSrpReconnectsFail_Type = Integer32
_BesSysHealthSrpReconnectsFail_Object = MibTableColumn
besSysHealthSrpReconnectsFail = _BesSysHealthSrpReconnectsFail_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 13),
    _BesSysHealthSrpReconnectsFail_Type()
)
besSysHealthSrpReconnectsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthSrpReconnectsFail.setStatus("current")
_BesSysHealthSrpTotalSecNotConnected_Type = Integer32
_BesSysHealthSrpTotalSecNotConnected_Object = MibTableColumn
besSysHealthSrpTotalSecNotConnected = _BesSysHealthSrpTotalSecNotConnected_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 14),
    _BesSysHealthSrpTotalSecNotConnected_Type()
)
besSysHealthSrpTotalSecNotConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthSrpTotalSecNotConnected.setStatus("current")
_BesSysHealthSrpLastErrorText_Type = DisplayString
_BesSysHealthSrpLastErrorText_Object = MibTableColumn
besSysHealthSrpLastErrorText = _BesSysHealthSrpLastErrorText_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 15),
    _BesSysHealthSrpLastErrorText_Type()
)
besSysHealthSrpLastErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthSrpLastErrorText.setStatus("current")
_BesSysHealthSrpLastErrorTime_Type = DisplayString
_BesSysHealthSrpLastErrorTime_Object = MibTableColumn
besSysHealthSrpLastErrorTime = _BesSysHealthSrpLastErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 16),
    _BesSysHealthSrpLastErrorTime_Type()
)
besSysHealthSrpLastErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthSrpLastErrorTime.setStatus("current")
_BesSysHealthMsgTotalProc_Type = Integer32
_BesSysHealthMsgTotalProc_Object = MibTableColumn
besSysHealthMsgTotalProc = _BesSysHealthMsgTotalProc_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 20),
    _BesSysHealthMsgTotalProc_Type()
)
besSysHealthMsgTotalProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgTotalProc.setStatus("current")
_BesSysHealthMsgToHandheld_Type = Integer32
_BesSysHealthMsgToHandheld_Object = MibTableColumn
besSysHealthMsgToHandheld = _BesSysHealthMsgToHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 21),
    _BesSysHealthMsgToHandheld_Type()
)
besSysHealthMsgToHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgToHandheld.setStatus("current")
_BesSysHealthMsgFromHandheld_Type = Integer32
_BesSysHealthMsgFromHandheld_Object = MibTableColumn
besSysHealthMsgFromHandheld = _BesSysHealthMsgFromHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 22),
    _BesSysHealthMsgFromHandheld_Type()
)
besSysHealthMsgFromHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgFromHandheld.setStatus("current")
_BesSysHealthMsgFilteredByUser_Type = Integer32
_BesSysHealthMsgFilteredByUser_Object = MibTableColumn
besSysHealthMsgFilteredByUser = _BesSysHealthMsgFilteredByUser_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 23),
    _BesSysHealthMsgFilteredByUser_Type()
)
besSysHealthMsgFilteredByUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgFilteredByUser.setStatus("current")
_BesSysHealthMsgFilteredByGlobal_Type = Integer32
_BesSysHealthMsgFilteredByGlobal_Object = MibTableColumn
besSysHealthMsgFilteredByGlobal = _BesSysHealthMsgFilteredByGlobal_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 24),
    _BesSysHealthMsgFilteredByGlobal_Type()
)
besSysHealthMsgFilteredByGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgFilteredByGlobal.setStatus("current")
_BesSysHealthMsgPending_Type = Integer32
_BesSysHealthMsgPending_Object = MibTableColumn
besSysHealthMsgPending = _BesSysHealthMsgPending_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 25),
    _BesSysHealthMsgPending_Type()
)
besSysHealthMsgPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgPending.setStatus("current")
_BesSysHealthMsgExpired_Type = Integer32
_BesSysHealthMsgExpired_Object = MibTableColumn
besSysHealthMsgExpired = _BesSysHealthMsgExpired_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 26),
    _BesSysHealthMsgExpired_Type()
)
besSysHealthMsgExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgExpired.setStatus("current")
_BesSysHealthMsgErrors_Type = Integer32
_BesSysHealthMsgErrors_Object = MibTableColumn
besSysHealthMsgErrors = _BesSysHealthMsgErrors_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 27),
    _BesSysHealthMsgErrors_Type()
)
besSysHealthMsgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgErrors.setStatus("current")
_BesSysHealthMsgMoreRequests_Type = Integer32
_BesSysHealthMsgMoreRequests_Object = MibTableColumn
besSysHealthMsgMoreRequests = _BesSysHealthMsgMoreRequests_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 28),
    _BesSysHealthMsgMoreRequests_Type()
)
besSysHealthMsgMoreRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMsgMoreRequests.setStatus("current")
_BesSysHealthCalUsersOTACEnabled_Type = Integer32
_BesSysHealthCalUsersOTACEnabled_Object = MibTableColumn
besSysHealthCalUsersOTACEnabled = _BesSysHealthCalUsersOTACEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 40),
    _BesSysHealthCalUsersOTACEnabled_Type()
)
besSysHealthCalUsersOTACEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthCalUsersOTACEnabled.setStatus("current")
_BesSysHealthCalEventToHandheld_Type = Integer32
_BesSysHealthCalEventToHandheld_Object = MibTableColumn
besSysHealthCalEventToHandheld = _BesSysHealthCalEventToHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 41),
    _BesSysHealthCalEventToHandheld_Type()
)
besSysHealthCalEventToHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthCalEventToHandheld.setStatus("current")
_BesSysHealthCalEventFromHandheld_Type = Integer32
_BesSysHealthCalEventFromHandheld_Object = MibTableColumn
besSysHealthCalEventFromHandheld = _BesSysHealthCalEventFromHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 42),
    _BesSysHealthCalEventFromHandheld_Type()
)
besSysHealthCalEventFromHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthCalEventFromHandheld.setStatus("current")
_BesSysHealthWERUsersEnabled_Type = Integer32
_BesSysHealthWERUsersEnabled_Object = MibTableColumn
besSysHealthWERUsersEnabled = _BesSysHealthWERUsersEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 50),
    _BesSysHealthWERUsersEnabled_Type()
)
besSysHealthWERUsersEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthWERUsersEnabled.setStatus("current")
_BesSysHealthWERRequestsToHandheld_Type = Integer32
_BesSysHealthWERRequestsToHandheld_Object = MibTableColumn
besSysHealthWERRequestsToHandheld = _BesSysHealthWERRequestsToHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 51),
    _BesSysHealthWERRequestsToHandheld_Type()
)
besSysHealthWERRequestsToHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthWERRequestsToHandheld.setStatus("current")
_BesSysHealthWERRequestsFromHandheld_Type = Integer32
_BesSysHealthWERRequestsFromHandheld_Object = MibTableColumn
besSysHealthWERRequestsFromHandheld = _BesSysHealthWERRequestsFromHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 52),
    _BesSysHealthWERRequestsFromHandheld_Type()
)
besSysHealthWERRequestsFromHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthWERRequestsFromHandheld.setStatus("current")
_BesSysHealthMdsDeviceConnections_Type = Integer32
_BesSysHealthMdsDeviceConnections_Object = MibTableColumn
besSysHealthMdsDeviceConnections = _BesSysHealthMdsDeviceConnections_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 60),
    _BesSysHealthMdsDeviceConnections_Type()
)
besSysHealthMdsDeviceConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsDeviceConnections.setStatus("current")
_BesSysHealthMdsPushConnections_Type = Integer32
_BesSysHealthMdsPushConnections_Object = MibTableColumn
besSysHealthMdsPushConnections = _BesSysHealthMdsPushConnections_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 61),
    _BesSysHealthMdsPushConnections_Type()
)
besSysHealthMdsPushConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsPushConnections.setStatus("current")
_BesSysHealthMdsTotalBytesFromDevices_Type = Integer32
_BesSysHealthMdsTotalBytesFromDevices_Object = MibTableColumn
besSysHealthMdsTotalBytesFromDevices = _BesSysHealthMdsTotalBytesFromDevices_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 62),
    _BesSysHealthMdsTotalBytesFromDevices_Type()
)
besSysHealthMdsTotalBytesFromDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsTotalBytesFromDevices.setStatus("current")
_BesSysHealthMdsMaxPacketSizeFromDevice_Type = Integer32
_BesSysHealthMdsMaxPacketSizeFromDevice_Object = MibTableColumn
besSysHealthMdsMaxPacketSizeFromDevice = _BesSysHealthMdsMaxPacketSizeFromDevice_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 63),
    _BesSysHealthMdsMaxPacketSizeFromDevice_Type()
)
besSysHealthMdsMaxPacketSizeFromDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsMaxPacketSizeFromDevice.setStatus("current")
_BesSysHealthMdsAvgPacketSizeFromDevice_Type = Integer32
_BesSysHealthMdsAvgPacketSizeFromDevice_Object = MibTableColumn
besSysHealthMdsAvgPacketSizeFromDevice = _BesSysHealthMdsAvgPacketSizeFromDevice_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 64),
    _BesSysHealthMdsAvgPacketSizeFromDevice_Type()
)
besSysHealthMdsAvgPacketSizeFromDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsAvgPacketSizeFromDevice.setStatus("current")
_BesSysHealthMdsTotalBytesToDevice_Type = Integer32
_BesSysHealthMdsTotalBytesToDevice_Object = MibTableColumn
besSysHealthMdsTotalBytesToDevice = _BesSysHealthMdsTotalBytesToDevice_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 65),
    _BesSysHealthMdsTotalBytesToDevice_Type()
)
besSysHealthMdsTotalBytesToDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsTotalBytesToDevice.setStatus("current")
_BesSysHealthMdsMaxPacketSizeToDevice_Type = Integer32
_BesSysHealthMdsMaxPacketSizeToDevice_Object = MibTableColumn
besSysHealthMdsMaxPacketSizeToDevice = _BesSysHealthMdsMaxPacketSizeToDevice_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 66),
    _BesSysHealthMdsMaxPacketSizeToDevice_Type()
)
besSysHealthMdsMaxPacketSizeToDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsMaxPacketSizeToDevice.setStatus("current")
_BesSysHealthMdsAvgPacketSizeToDevice_Type = Integer32
_BesSysHealthMdsAvgPacketSizeToDevice_Object = MibTableColumn
besSysHealthMdsAvgPacketSizeToDevice = _BesSysHealthMdsAvgPacketSizeToDevice_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 67),
    _BesSysHealthMdsAvgPacketSizeToDevice_Type()
)
besSysHealthMdsAvgPacketSizeToDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsAvgPacketSizeToDevice.setStatus("current")
_BesSysHealthMdsRefusedPackets_Type = Integer32
_BesSysHealthMdsRefusedPackets_Object = MibTableColumn
besSysHealthMdsRefusedPackets = _BesSysHealthMdsRefusedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 68),
    _BesSysHealthMdsRefusedPackets_Type()
)
besSysHealthMdsRefusedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsRefusedPackets.setStatus("current")
_BesSysHealthMdsInvalidPackets_Type = Integer32
_BesSysHealthMdsInvalidPackets_Object = MibTableColumn
besSysHealthMdsInvalidPackets = _BesSysHealthMdsInvalidPackets_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 69),
    _BesSysHealthMdsInvalidPackets_Type()
)
besSysHealthMdsInvalidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsInvalidPackets.setStatus("current")
_BesSysHealthMdsConnectionSuccess_Type = Integer32
_BesSysHealthMdsConnectionSuccess_Object = MibTableColumn
besSysHealthMdsConnectionSuccess = _BesSysHealthMdsConnectionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 70),
    _BesSysHealthMdsConnectionSuccess_Type()
)
besSysHealthMdsConnectionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsConnectionSuccess.setStatus("current")
_BesSysHealthMdsConnectionFailure_Type = Integer32
_BesSysHealthMdsConnectionFailure_Object = MibTableColumn
besSysHealthMdsConnectionFailure = _BesSysHealthMdsConnectionFailure_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 71),
    _BesSysHealthMdsConnectionFailure_Type()
)
besSysHealthMdsConnectionFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsConnectionFailure.setStatus("current")
_BesSysHealthMdsConnectionTruncated_Type = Integer32
_BesSysHealthMdsConnectionTruncated_Object = MibTableColumn
besSysHealthMdsConnectionTruncated = _BesSysHealthMdsConnectionTruncated_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 72),
    _BesSysHealthMdsConnectionTruncated_Type()
)
besSysHealthMdsConnectionTruncated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthMdsConnectionTruncated.setStatus("current")
_BesSysHealthV1MsgsPending_Type = Integer32
_BesSysHealthV1MsgsPending_Object = MibTableColumn
besSysHealthV1MsgsPending = _BesSysHealthV1MsgsPending_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 202),
    _BesSysHealthV1MsgsPending_Type()
)
besSysHealthV1MsgsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthV1MsgsPending.setStatus("current")
_BesSysHealthV1TotalMsgsSent_Type = Integer32
_BesSysHealthV1TotalMsgsSent_Object = MibTableColumn
besSysHealthV1TotalMsgsSent = _BesSysHealthV1TotalMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 203),
    _BesSysHealthV1TotalMsgsSent_Type()
)
besSysHealthV1TotalMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthV1TotalMsgsSent.setStatus("current")
_BesSysHealthV1TotalMsgsReceived_Type = Integer32
_BesSysHealthV1TotalMsgsReceived_Object = MibTableColumn
besSysHealthV1TotalMsgsReceived = _BesSysHealthV1TotalMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 204),
    _BesSysHealthV1TotalMsgsReceived_Type()
)
besSysHealthV1TotalMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthV1TotalMsgsReceived.setStatus("current")
_BesSysHealthV1TotalMsgsExpired_Type = Integer32
_BesSysHealthV1TotalMsgsExpired_Object = MibTableColumn
besSysHealthV1TotalMsgsExpired = _BesSysHealthV1TotalMsgsExpired_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 205),
    _BesSysHealthV1TotalMsgsExpired_Type()
)
besSysHealthV1TotalMsgsExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthV1TotalMsgsExpired.setStatus("current")
_BesSysHealthV1TotalMsgsFiltered_Type = Integer32
_BesSysHealthV1TotalMsgsFiltered_Object = MibTableColumn
besSysHealthV1TotalMsgsFiltered = _BesSysHealthV1TotalMsgsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 206),
    _BesSysHealthV1TotalMsgsFiltered_Type()
)
besSysHealthV1TotalMsgsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthV1TotalMsgsFiltered.setStatus("current")
_BesSysHealthV1MsgsSentPerMin_Type = Integer32
_BesSysHealthV1MsgsSentPerMin_Object = MibTableColumn
besSysHealthV1MsgsSentPerMin = _BesSysHealthV1MsgsSentPerMin_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 207),
    _BesSysHealthV1MsgsSentPerMin_Type()
)
besSysHealthV1MsgsSentPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthV1MsgsSentPerMin.setStatus("current")
_BesSysHealthV1MsgsRecvdPerMin_Type = Integer32
_BesSysHealthV1MsgsRecvdPerMin_Object = MibTableColumn
besSysHealthV1MsgsRecvdPerMin = _BesSysHealthV1MsgsRecvdPerMin_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 208),
    _BesSysHealthV1MsgsRecvdPerMin_Type()
)
besSysHealthV1MsgsRecvdPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthV1MsgsRecvdPerMin.setStatus("current")


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
    besSysHealthV1SRPConnectState.setStatus("current")
_BesSysHealthSrpLastErrorTimeSec_Type = Integer32
_BesSysHealthSrpLastErrorTimeSec_Object = MibTableColumn
besSysHealthSrpLastErrorTimeSec = _BesSysHealthSrpLastErrorTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 301),
    _BesSysHealthSrpLastErrorTimeSec_Type()
)
besSysHealthSrpLastErrorTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthSrpLastErrorTimeSec.setStatus("current")
_BesSysHealthFailedUsers_Type = Integer32
_BesSysHealthFailedUsers_Object = MibTableColumn
besSysHealthFailedUsers = _BesSysHealthFailedUsers_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 25, 1, 302),
    _BesSysHealthFailedUsers_Type()
)
besSysHealthFailedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besSysHealthFailedUsers.setStatus("current")
_BesMailServerHealthTable_Object = MibTable
besMailServerHealthTable = _BesMailServerHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 26)
)
if mibBuilder.loadTexts:
    besMailServerHealthTable.setStatus("current")
_BesMailServerHealthEntry_Object = MibTableRow
besMailServerHealthEntry = _BesMailServerHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 26, 1)
)
besMailServerHealthEntry.setIndexNames(
    (0, "BLACKBERRYSERVERMIB-SMIV2", "besMailServerHealthServerInstance"),
    (0, "BLACKBERRYSERVERMIB-SMIV2", "besMailServerHealthServerId"),
)
if mibBuilder.loadTexts:
    besMailServerHealthEntry.setStatus("current")


class _BesMailServerHealthServerInstance_Type(Integer32):
    """Custom type besMailServerHealthServerInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_BesMailServerHealthServerInstance_Type.__name__ = "Integer32"
_BesMailServerHealthServerInstance_Object = MibTableColumn
besMailServerHealthServerInstance = _BesMailServerHealthServerInstance_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 26, 1, 1),
    _BesMailServerHealthServerInstance_Type()
)
besMailServerHealthServerInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besMailServerHealthServerInstance.setStatus("current")


class _BesMailServerHealthServerId_Type(Integer32):
    """Custom type besMailServerHealthServerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_BesMailServerHealthServerId_Type.__name__ = "Integer32"
_BesMailServerHealthServerId_Object = MibTableColumn
besMailServerHealthServerId = _BesMailServerHealthServerId_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 26, 1, 2),
    _BesMailServerHealthServerId_Type()
)
besMailServerHealthServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besMailServerHealthServerId.setStatus("current")
_BesMailServerHealthServerName_Type = DisplayString
_BesMailServerHealthServerName_Object = MibTableColumn
besMailServerHealthServerName = _BesMailServerHealthServerName_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 26, 1, 3),
    _BesMailServerHealthServerName_Type()
)
besMailServerHealthServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besMailServerHealthServerName.setStatus("current")
_BesMailServerHealthTotalUsers_Type = Integer32
_BesMailServerHealthTotalUsers_Object = MibTableColumn
besMailServerHealthTotalUsers = _BesMailServerHealthTotalUsers_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 26, 1, 10),
    _BesMailServerHealthTotalUsers_Type()
)
besMailServerHealthTotalUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besMailServerHealthTotalUsers.setStatus("current")
_BesMailServerHealthAvgResponceTime10min_Type = Integer32
_BesMailServerHealthAvgResponceTime10min_Object = MibTableColumn
besMailServerHealthAvgResponceTime10min = _BesMailServerHealthAvgResponceTime10min_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 26, 1, 11),
    _BesMailServerHealthAvgResponceTime10min_Type()
)
besMailServerHealthAvgResponceTime10min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besMailServerHealthAvgResponceTime10min.setStatus("current")
_BesMailServerHealthFailedConn10min_Type = Integer32
_BesMailServerHealthFailedConn10min_Object = MibTableColumn
besMailServerHealthFailedConn10min = _BesMailServerHealthFailedConn10min_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 26, 1, 12),
    _BesMailServerHealthFailedConn10min_Type()
)
besMailServerHealthFailedConn10min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besMailServerHealthFailedConn10min.setStatus("current")
_BesUserHealthTable_Object = MibTable
besUserHealthTable = _BesUserHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30)
)
if mibBuilder.loadTexts:
    besUserHealthTable.setStatus("current")
_BesUserHealthEntry_Object = MibTableRow
besUserHealthEntry = _BesUserHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1)
)
besUserHealthEntry.setIndexNames(
    (0, "BLACKBERRYSERVERMIB-SMIV2", "besUserHealthServerInstance"),
    (0, "BLACKBERRYSERVERMIB-SMIV2", "besUserHealthUserId"),
)
if mibBuilder.loadTexts:
    besUserHealthEntry.setStatus("current")


class _BesUserHealthServerInstance_Type(Integer32):
    """Custom type besUserHealthServerInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_BesUserHealthServerInstance_Type.__name__ = "Integer32"
_BesUserHealthServerInstance_Object = MibTableColumn
besUserHealthServerInstance = _BesUserHealthServerInstance_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 1),
    _BesUserHealthServerInstance_Type()
)
besUserHealthServerInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthServerInstance.setStatus("current")


class _BesUserHealthUserId_Type(Integer32):
    """Custom type besUserHealthUserId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_BesUserHealthUserId_Type.__name__ = "Integer32"
_BesUserHealthUserId_Object = MibTableColumn
besUserHealthUserId = _BesUserHealthUserId_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 2),
    _BesUserHealthUserId_Type()
)
besUserHealthUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthUserId.setStatus("current")
_BesUserHealthUserName_Type = DisplayString
_BesUserHealthUserName_Object = MibTableColumn
besUserHealthUserName = _BesUserHealthUserName_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 3),
    _BesUserHealthUserName_Type()
)
besUserHealthUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthUserName.setStatus("current")
_BesUserHealthLastErrorText_Type = DisplayString
_BesUserHealthLastErrorText_Object = MibTableColumn
besUserHealthLastErrorText = _BesUserHealthLastErrorText_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 10),
    _BesUserHealthLastErrorText_Type()
)
besUserHealthLastErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthLastErrorText.setStatus("current")
_BesUserHealthLastErrorTime_Type = DisplayString
_BesUserHealthLastErrorTime_Object = MibTableColumn
besUserHealthLastErrorTime = _BesUserHealthLastErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 11),
    _BesUserHealthLastErrorTime_Type()
)
besUserHealthLastErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthLastErrorTime.setStatus("current")
_BesUserHealthDeviceNetwork_Type = DisplayString
_BesUserHealthDeviceNetwork_Object = MibTableColumn
besUserHealthDeviceNetwork = _BesUserHealthDeviceNetwork_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 20),
    _BesUserHealthDeviceNetwork_Type()
)
besUserHealthDeviceNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthDeviceNetwork.setStatus("current")
_BesUserHealthDevicePIN_Type = DisplayString
_BesUserHealthDevicePIN_Object = MibTableColumn
besUserHealthDevicePIN = _BesUserHealthDevicePIN_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 21),
    _BesUserHealthDevicePIN_Type()
)
besUserHealthDevicePIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthDevicePIN.setStatus("current")
_BesUserHealthDeviceInCradle_Type = Integer32
_BesUserHealthDeviceInCradle_Object = MibTableColumn
besUserHealthDeviceInCradle = _BesUserHealthDeviceInCradle_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 22),
    _BesUserHealthDeviceInCradle_Type()
)
besUserHealthDeviceInCradle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthDeviceInCradle.setStatus("current")
_BesUserHealthNumRedirectedFolders_Type = Integer32
_BesUserHealthNumRedirectedFolders_Object = MibTableColumn
besUserHealthNumRedirectedFolders = _BesUserHealthNumRedirectedFolders_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 30),
    _BesUserHealthNumRedirectedFolders_Type()
)
besUserHealthNumRedirectedFolders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthNumRedirectedFolders.setStatus("current")


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
    besUserHealthSaveInSent.setStatus("current")


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
    besUserHealthRedirectEnabledOnDesktop.setStatus("current")


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
    besUserHealthDisableWhileInCradle.setStatus("current")
_BesUserHealthFullyConfigured_Type = Integer32
_BesUserHealthFullyConfigured_Object = MibTableColumn
besUserHealthFullyConfigured = _BesUserHealthFullyConfigured_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 34),
    _BesUserHealthFullyConfigured_Type()
)
besUserHealthFullyConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthFullyConfigured.setStatus("current")
_BesUserHealthEnabled_Type = Integer32
_BesUserHealthEnabled_Object = MibTableColumn
besUserHealthEnabled = _BesUserHealthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 35),
    _BesUserHealthEnabled_Type()
)
besUserHealthEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthEnabled.setStatus("current")
_BesUserHealthMsgTotalProc_Type = Integer32
_BesUserHealthMsgTotalProc_Object = MibTableColumn
besUserHealthMsgTotalProc = _BesUserHealthMsgTotalProc_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 40),
    _BesUserHealthMsgTotalProc_Type()
)
besUserHealthMsgTotalProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgTotalProc.setStatus("current")
_BesUserHealthMsgToHandheld_Type = Integer32
_BesUserHealthMsgToHandheld_Object = MibTableColumn
besUserHealthMsgToHandheld = _BesUserHealthMsgToHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 41),
    _BesUserHealthMsgToHandheld_Type()
)
besUserHealthMsgToHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgToHandheld.setStatus("current")
_BesUserHealthMsgFromHandheld_Type = Integer32
_BesUserHealthMsgFromHandheld_Object = MibTableColumn
besUserHealthMsgFromHandheld = _BesUserHealthMsgFromHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 42),
    _BesUserHealthMsgFromHandheld_Type()
)
besUserHealthMsgFromHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgFromHandheld.setStatus("current")
_BesUserHealthMsgFiltered_Type = Integer32
_BesUserHealthMsgFiltered_Object = MibTableColumn
besUserHealthMsgFiltered = _BesUserHealthMsgFiltered_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 43),
    _BesUserHealthMsgFiltered_Type()
)
besUserHealthMsgFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgFiltered.setStatus("current")
_BesUserHealthMsgPending_Type = Integer32
_BesUserHealthMsgPending_Object = MibTableColumn
besUserHealthMsgPending = _BesUserHealthMsgPending_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 44),
    _BesUserHealthMsgPending_Type()
)
besUserHealthMsgPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgPending.setStatus("current")
_BesUserHealthMsgExpired_Type = Integer32
_BesUserHealthMsgExpired_Object = MibTableColumn
besUserHealthMsgExpired = _BesUserHealthMsgExpired_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 45),
    _BesUserHealthMsgExpired_Type()
)
besUserHealthMsgExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgExpired.setStatus("current")
_BesUserHealthMsgErrors_Type = Integer32
_BesUserHealthMsgErrors_Object = MibTableColumn
besUserHealthMsgErrors = _BesUserHealthMsgErrors_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 46),
    _BesUserHealthMsgErrors_Type()
)
besUserHealthMsgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgErrors.setStatus("current")
_BesUserHealthMsgMoreRequests_Type = Integer32
_BesUserHealthMsgMoreRequests_Object = MibTableColumn
besUserHealthMsgMoreRequests = _BesUserHealthMsgMoreRequests_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 47),
    _BesUserHealthMsgMoreRequests_Type()
)
besUserHealthMsgMoreRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgMoreRequests.setStatus("current")
_BesUserHealthMsgForwardedFromDevice_Type = Integer32
_BesUserHealthMsgForwardedFromDevice_Object = MibTableColumn
besUserHealthMsgForwardedFromDevice = _BesUserHealthMsgForwardedFromDevice_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 48),
    _BesUserHealthMsgForwardedFromDevice_Type()
)
besUserHealthMsgForwardedFromDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgForwardedFromDevice.setStatus("current")
_BesUserHealthMsgRepliedToWithText_Type = Integer32
_BesUserHealthMsgRepliedToWithText_Object = MibTableColumn
besUserHealthMsgRepliedToWithText = _BesUserHealthMsgRepliedToWithText_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 49),
    _BesUserHealthMsgRepliedToWithText_Type()
)
besUserHealthMsgRepliedToWithText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMsgRepliedToWithText.setStatus("current")
_BesUserHealthLastTimeInCradle_Type = DisplayString
_BesUserHealthLastTimeInCradle_Object = MibTableColumn
besUserHealthLastTimeInCradle = _BesUserHealthLastTimeInCradle_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 60),
    _BesUserHealthLastTimeInCradle_Type()
)
besUserHealthLastTimeInCradle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthLastTimeInCradle.setStatus("current")
_BesUserHealthLastInteractionWithDevice_Type = DisplayString
_BesUserHealthLastInteractionWithDevice_Object = MibTableColumn
besUserHealthLastInteractionWithDevice = _BesUserHealthLastInteractionWithDevice_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 61),
    _BesUserHealthLastInteractionWithDevice_Type()
)
besUserHealthLastInteractionWithDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthLastInteractionWithDevice.setStatus("current")
_BesUserHealthLastMessageForwarded_Type = DisplayString
_BesUserHealthLastMessageForwarded_Object = MibTableColumn
besUserHealthLastMessageForwarded = _BesUserHealthLastMessageForwarded_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 62),
    _BesUserHealthLastMessageForwarded_Type()
)
besUserHealthLastMessageForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthLastMessageForwarded.setStatus("current")
_BesUserHealthLastKeyDateGenerated_Type = DisplayString
_BesUserHealthLastKeyDateGenerated_Object = MibTableColumn
besUserHealthLastKeyDateGenerated = _BesUserHealthLastKeyDateGenerated_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 63),
    _BesUserHealthLastKeyDateGenerated_Type()
)
besUserHealthLastKeyDateGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthLastKeyDateGenerated.setStatus("current")
_BesUserHealthAvgKBForwarded_Type = Integer32
_BesUserHealthAvgKBForwarded_Object = MibTableColumn
besUserHealthAvgKBForwarded = _BesUserHealthAvgKBForwarded_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 70),
    _BesUserHealthAvgKBForwarded_Type()
)
besUserHealthAvgKBForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthAvgKBForwarded.setStatus("current")
_BesUserHealthAvgKBReplyWithText_Type = Integer32
_BesUserHealthAvgKBReplyWithText_Object = MibTableColumn
besUserHealthAvgKBReplyWithText = _BesUserHealthAvgKBReplyWithText_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 71),
    _BesUserHealthAvgKBReplyWithText_Type()
)
besUserHealthAvgKBReplyWithText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthAvgKBReplyWithText.setStatus("current")
_BesUserHealthAvgLatencyInSecLast10Msg_Type = Integer32
_BesUserHealthAvgLatencyInSecLast10Msg_Object = MibTableColumn
besUserHealthAvgLatencyInSecLast10Msg = _BesUserHealthAvgLatencyInSecLast10Msg_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 72),
    _BesUserHealthAvgLatencyInSecLast10Msg_Type()
)
besUserHealthAvgLatencyInSecLast10Msg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthAvgLatencyInSecLast10Msg.setStatus("current")


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
    besUserHealthCalOTAEnabled.setStatus("current")
_BesUserHealthCalEventToHandheld_Type = Integer32
_BesUserHealthCalEventToHandheld_Object = MibTableColumn
besUserHealthCalEventToHandheld = _BesUserHealthCalEventToHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 81),
    _BesUserHealthCalEventToHandheld_Type()
)
besUserHealthCalEventToHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthCalEventToHandheld.setStatus("current")
_BesUserHealthCalEventFromHandheld_Type = Integer32
_BesUserHealthCalEventFromHandheld_Object = MibTableColumn
besUserHealthCalEventFromHandheld = _BesUserHealthCalEventFromHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 82),
    _BesUserHealthCalEventFromHandheld_Type()
)
besUserHealthCalEventFromHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthCalEventFromHandheld.setStatus("current")


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
    besUserHealthWirelessEmailRecoEnabled.setStatus("current")
_BesUserHealthWERRequestsToHandheld_Type = Integer32
_BesUserHealthWERRequestsToHandheld_Object = MibTableColumn
besUserHealthWERRequestsToHandheld = _BesUserHealthWERRequestsToHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 91),
    _BesUserHealthWERRequestsToHandheld_Type()
)
besUserHealthWERRequestsToHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthWERRequestsToHandheld.setStatus("current")
_BesUserHealthWERRequestsFromHandheld_Type = Integer32
_BesUserHealthWERRequestsFromHandheld_Object = MibTableColumn
besUserHealthWERRequestsFromHandheld = _BesUserHealthWERRequestsFromHandheld_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 92),
    _BesUserHealthWERRequestsFromHandheld_Type()
)
besUserHealthWERRequestsFromHandheld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthWERRequestsFromHandheld.setStatus("current")
_BesUserHealthLastErrorTimeSec_Type = Integer32
_BesUserHealthLastErrorTimeSec_Object = MibTableColumn
besUserHealthLastErrorTimeSec = _BesUserHealthLastErrorTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 301),
    _BesUserHealthLastErrorTimeSec_Type()
)
besUserHealthLastErrorTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthLastErrorTimeSec.setStatus("current")
_BesUserHealthSMTP_Type = DisplayString
_BesUserHealthSMTP_Object = MibTableColumn
besUserHealthSMTP = _BesUserHealthSMTP_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 302),
    _BesUserHealthSMTP_Type()
)
besUserHealthSMTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthSMTP.setStatus("current")
_BesUserHealthLastTimeInCradleSec_Type = Integer32
_BesUserHealthLastTimeInCradleSec_Object = MibTableColumn
besUserHealthLastTimeInCradleSec = _BesUserHealthLastTimeInCradleSec_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 303),
    _BesUserHealthLastTimeInCradleSec_Type()
)
besUserHealthLastTimeInCradleSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthLastTimeInCradleSec.setStatus("current")
_BesUserHealthMailServer_Type = DisplayString
_BesUserHealthMailServer_Object = MibTableColumn
besUserHealthMailServer = _BesUserHealthMailServer_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 30, 1, 304),
    _BesUserHealthMailServer_Type()
)
besUserHealthMailServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besUserHealthMailServer.setStatus("current")
_BlackBerryDispatcher_ObjectIdentity = ObjectIdentity
blackBerryDispatcher = _BlackBerryDispatcher_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50)
)
_DispConfigVariables_ObjectIdentity = ObjectIdentity
dispConfigVariables = _DispConfigVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1)
)
_DispConfigServerName_Type = DisplayString
_DispConfigServerName_Object = MibScalar
dispConfigServerName = _DispConfigServerName_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 2),
    _DispConfigServerName_Type()
)
dispConfigServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigServerName.setStatus("current")
_DispConfigServerId_Type = Integer32
_DispConfigServerId_Object = MibScalar
dispConfigServerId = _DispConfigServerId_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 3),
    _DispConfigServerId_Type()
)
dispConfigServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigServerId.setStatus("current")
_DispConfigVersionString_Type = DisplayString
_DispConfigVersionString_Object = MibScalar
dispConfigVersionString = _DispConfigVersionString_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 10),
    _DispConfigVersionString_Type()
)
dispConfigVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigVersionString.setStatus("current")
_DispConfigReleaseMaj_Type = Integer32
_DispConfigReleaseMaj_Object = MibScalar
dispConfigReleaseMaj = _DispConfigReleaseMaj_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 11),
    _DispConfigReleaseMaj_Type()
)
dispConfigReleaseMaj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigReleaseMaj.setStatus("current")
_DispConfigReleaseMin_Type = Integer32
_DispConfigReleaseMin_Object = MibScalar
dispConfigReleaseMin = _DispConfigReleaseMin_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 12),
    _DispConfigReleaseMin_Type()
)
dispConfigReleaseMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigReleaseMin.setStatus("current")
_DispConfigReleaseServicePack_Type = Integer32
_DispConfigReleaseServicePack_Object = MibScalar
dispConfigReleaseServicePack = _DispConfigReleaseServicePack_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 13),
    _DispConfigReleaseServicePack_Type()
)
dispConfigReleaseServicePack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigReleaseServicePack.setStatus("current")
_DispConfigReleaseBuild_Type = Integer32
_DispConfigReleaseBuild_Object = MibScalar
dispConfigReleaseBuild = _DispConfigReleaseBuild_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 14),
    _DispConfigReleaseBuild_Type()
)
dispConfigReleaseBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigReleaseBuild.setStatus("current")
_DispConfigSRPId_Type = DisplayString
_DispConfigSRPId_Object = MibScalar
dispConfigSRPId = _DispConfigSRPId_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 20),
    _DispConfigSRPId_Type()
)
dispConfigSRPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigSRPId.setStatus("current")
_DispConfigSRPHost_Type = DisplayString
_DispConfigSRPHost_Object = MibScalar
dispConfigSRPHost = _DispConfigSRPHost_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 21),
    _DispConfigSRPHost_Type()
)
dispConfigSRPHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigSRPHost.setStatus("current")
_DispConfigSRPPort_Type = Integer32
_DispConfigSRPPort_Object = MibScalar
dispConfigSRPPort = _DispConfigSRPPort_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 22),
    _DispConfigSRPPort_Type()
)
dispConfigSRPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigSRPPort.setStatus("current")
_DispConfigBIPPPort_Type = Integer32
_DispConfigBIPPPort_Object = MibScalar
dispConfigBIPPPort = _DispConfigBIPPPort_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 23),
    _DispConfigBIPPPort_Type()
)
dispConfigBIPPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigBIPPPort.setStatus("current")
_DispConfigHRT_Type = DisplayString
_DispConfigHRT_Object = MibScalar
dispConfigHRT = _DispConfigHRT_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 24),
    _DispConfigHRT_Type()
)
dispConfigHRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigHRT.setStatus("current")
_DispConfigDBConnectingString_Type = DisplayString
_DispConfigDBConnectingString_Object = MibScalar
dispConfigDBConnectingString = _DispConfigDBConnectingString_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 30),
    _DispConfigDBConnectingString_Type()
)
dispConfigDBConnectingString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigDBConnectingString.setStatus("current")
_DispConfigMaxNumberOfAgents_Type = Integer32
_DispConfigMaxNumberOfAgents_Object = MibScalar
dispConfigMaxNumberOfAgents = _DispConfigMaxNumberOfAgents_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 31),
    _DispConfigMaxNumberOfAgents_Type()
)
dispConfigMaxNumberOfAgents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigMaxNumberOfAgents.setStatus("current")
_DispConfigActualNumberOfAgents_Type = Integer32
_DispConfigActualNumberOfAgents_Object = MibScalar
dispConfigActualNumberOfAgents = _DispConfigActualNumberOfAgents_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 32),
    _DispConfigActualNumberOfAgents_Type()
)
dispConfigActualNumberOfAgents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigActualNumberOfAgents.setStatus("current")
_DispConfigExternalServicesAllowed_Type = Integer32
_DispConfigExternalServicesAllowed_Object = MibScalar
dispConfigExternalServicesAllowed = _DispConfigExternalServicesAllowed_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 33),
    _DispConfigExternalServicesAllowed_Type()
)
dispConfigExternalServicesAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigExternalServicesAllowed.setStatus("current")
_DispConfigExternalServicesPort_Type = Integer32
_DispConfigExternalServicesPort_Object = MibScalar
dispConfigExternalServicesPort = _DispConfigExternalServicesPort_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 34),
    _DispConfigExternalServicesPort_Type()
)
dispConfigExternalServicesPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigExternalServicesPort.setStatus("current")
_DispConfigEnabledEncryptionAlgorithm_Type = Integer32
_DispConfigEnabledEncryptionAlgorithm_Object = MibScalar
dispConfigEnabledEncryptionAlgorithm = _DispConfigEnabledEncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 35),
    _DispConfigEnabledEncryptionAlgorithm_Type()
)
dispConfigEnabledEncryptionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigEnabledEncryptionAlgorithm.setStatus("current")
_DispConfigLicenceTotal_Type = Integer32
_DispConfigLicenceTotal_Object = MibScalar
dispConfigLicenceTotal = _DispConfigLicenceTotal_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 36),
    _DispConfigLicenceTotal_Type()
)
dispConfigLicenceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigLicenceTotal.setStatus("current")
_DispConfigLicenceRemaining_Type = Integer32
_DispConfigLicenceRemaining_Object = MibScalar
dispConfigLicenceRemaining = _DispConfigLicenceRemaining_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 37),
    _DispConfigLicenceRemaining_Type()
)
dispConfigLicenceRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigLicenceRemaining.setStatus("current")
_DispConfigLicenceUsed_Type = Integer32
_DispConfigLicenceUsed_Object = MibScalar
dispConfigLicenceUsed = _DispConfigLicenceUsed_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 38),
    _DispConfigLicenceUsed_Type()
)
dispConfigLicenceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigLicenceUsed.setStatus("current")
_DispConfigLastModified_Type = Integer32
_DispConfigLastModified_Object = MibScalar
dispConfigLastModified = _DispConfigLastModified_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 1, 301),
    _DispConfigLastModified_Type()
)
dispConfigLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispConfigLastModified.setStatus("current")
_DispHealthVariables_ObjectIdentity = ObjectIdentity
dispHealthVariables = _DispHealthVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 2)
)
_DispSysHealthSRPConnectedState_Type = Integer32
_DispSysHealthSRPConnectedState_Object = MibScalar
dispSysHealthSRPConnectedState = _DispSysHealthSRPConnectedState_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 2, 10),
    _DispSysHealthSRPConnectedState_Type()
)
dispSysHealthSRPConnectedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispSysHealthSRPConnectedState.setStatus("current")
_DispSysHealthSRPLastConnectDate_Type = DisplayString
_DispSysHealthSRPLastConnectDate_Object = MibScalar
dispSysHealthSRPLastConnectDate = _DispSysHealthSRPLastConnectDate_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 2, 11),
    _DispSysHealthSRPLastConnectDate_Type()
)
dispSysHealthSRPLastConnectDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispSysHealthSRPLastConnectDate.setStatus("current")
_DispSysHealthSRPReconnectSuccess_Type = Integer32
_DispSysHealthSRPReconnectSuccess_Object = MibScalar
dispSysHealthSRPReconnectSuccess = _DispSysHealthSRPReconnectSuccess_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 2, 12),
    _DispSysHealthSRPReconnectSuccess_Type()
)
dispSysHealthSRPReconnectSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispSysHealthSRPReconnectSuccess.setStatus("current")
_DispSysHealthSRPReconnectsFail_Type = Integer32
_DispSysHealthSRPReconnectsFail_Object = MibScalar
dispSysHealthSRPReconnectsFail = _DispSysHealthSRPReconnectsFail_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 2, 13),
    _DispSysHealthSRPReconnectsFail_Type()
)
dispSysHealthSRPReconnectsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispSysHealthSRPReconnectsFail.setStatus("current")
_DispSysHealthSRPTotalSecNotConnected_Type = Integer32
_DispSysHealthSRPTotalSecNotConnected_Object = MibScalar
dispSysHealthSRPTotalSecNotConnected = _DispSysHealthSRPTotalSecNotConnected_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 2, 14),
    _DispSysHealthSRPTotalSecNotConnected_Type()
)
dispSysHealthSRPTotalSecNotConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispSysHealthSRPTotalSecNotConnected.setStatus("current")
_DispSysHealthSRPLastErrorText_Type = DisplayString
_DispSysHealthSRPLastErrorText_Object = MibScalar
dispSysHealthSRPLastErrorText = _DispSysHealthSRPLastErrorText_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 2, 15),
    _DispSysHealthSRPLastErrorText_Type()
)
dispSysHealthSRPLastErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispSysHealthSRPLastErrorText.setStatus("current")
_DispSysHealthSRPLastErrorTime_Type = DisplayString
_DispSysHealthSRPLastErrorTime_Object = MibScalar
dispSysHealthSRPLastErrorTime = _DispSysHealthSRPLastErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 2, 16),
    _DispSysHealthSRPLastErrorTime_Type()
)
dispSysHealthSRPLastErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dispSysHealthSRPLastErrorTime.setStatus("current")
_DispTrapVariables_ObjectIdentity = ObjectIdentity
dispTrapVariables = _DispTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 10)
)
_BlackBerryRouter_ObjectIdentity = ObjectIdentity
blackBerryRouter = _BlackBerryRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55)
)
_RoutConfigVariables_ObjectIdentity = ObjectIdentity
routConfigVariables = _RoutConfigVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 1)
)
_RoutConfigServerName_Type = DisplayString
_RoutConfigServerName_Object = MibScalar
routConfigServerName = _RoutConfigServerName_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 1, 2),
    _RoutConfigServerName_Type()
)
routConfigServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routConfigServerName.setStatus("current")
_RoutConfigVersionString_Type = DisplayString
_RoutConfigVersionString_Object = MibScalar
routConfigVersionString = _RoutConfigVersionString_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 1, 10),
    _RoutConfigVersionString_Type()
)
routConfigVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routConfigVersionString.setStatus("current")
_RoutConfigReleaseMaj_Type = Integer32
_RoutConfigReleaseMaj_Object = MibScalar
routConfigReleaseMaj = _RoutConfigReleaseMaj_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 1, 11),
    _RoutConfigReleaseMaj_Type()
)
routConfigReleaseMaj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routConfigReleaseMaj.setStatus("current")
_RoutConfigReleaseMin_Type = Integer32
_RoutConfigReleaseMin_Object = MibScalar
routConfigReleaseMin = _RoutConfigReleaseMin_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 1, 12),
    _RoutConfigReleaseMin_Type()
)
routConfigReleaseMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routConfigReleaseMin.setStatus("current")
_RoutConfigReleaseServicePack_Type = Integer32
_RoutConfigReleaseServicePack_Object = MibScalar
routConfigReleaseServicePack = _RoutConfigReleaseServicePack_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 1, 13),
    _RoutConfigReleaseServicePack_Type()
)
routConfigReleaseServicePack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routConfigReleaseServicePack.setStatus("current")
_RoutConfigReleaseBuild_Type = Integer32
_RoutConfigReleaseBuild_Object = MibScalar
routConfigReleaseBuild = _RoutConfigReleaseBuild_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 1, 14),
    _RoutConfigReleaseBuild_Type()
)
routConfigReleaseBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routConfigReleaseBuild.setStatus("current")
_RoutConfigSRPHost_Type = DisplayString
_RoutConfigSRPHost_Object = MibScalar
routConfigSRPHost = _RoutConfigSRPHost_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 1, 21),
    _RoutConfigSRPHost_Type()
)
routConfigSRPHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routConfigSRPHost.setStatus("current")
_RoutConfigSRPPort_Type = Integer32
_RoutConfigSRPPort_Object = MibScalar
routConfigSRPPort = _RoutConfigSRPPort_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 1, 22),
    _RoutConfigSRPPort_Type()
)
routConfigSRPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routConfigSRPPort.setStatus("current")
_RoutConfigServicePort_Type = Integer32
_RoutConfigServicePort_Object = MibScalar
routConfigServicePort = _RoutConfigServicePort_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 1, 24),
    _RoutConfigServicePort_Type()
)
routConfigServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routConfigServicePort.setStatus("current")
_RoutConfigDevicePort_Type = Integer32
_RoutConfigDevicePort_Object = MibScalar
routConfigDevicePort = _RoutConfigDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 1, 25),
    _RoutConfigDevicePort_Type()
)
routConfigDevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routConfigDevicePort.setStatus("current")
_RoutConfigMaxServiceConnections_Type = Integer32
_RoutConfigMaxServiceConnections_Object = MibScalar
routConfigMaxServiceConnections = _RoutConfigMaxServiceConnections_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 1, 26),
    _RoutConfigMaxServiceConnections_Type()
)
routConfigMaxServiceConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routConfigMaxServiceConnections.setStatus("current")
_RoutConfigMaxDeviceConnections_Type = Integer32
_RoutConfigMaxDeviceConnections_Object = MibScalar
routConfigMaxDeviceConnections = _RoutConfigMaxDeviceConnections_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 1, 27),
    _RoutConfigMaxDeviceConnections_Type()
)
routConfigMaxDeviceConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routConfigMaxDeviceConnections.setStatus("current")
_RoutConfigAllowRemoteServices_Type = Integer32
_RoutConfigAllowRemoteServices_Object = MibScalar
routConfigAllowRemoteServices = _RoutConfigAllowRemoteServices_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 1, 28),
    _RoutConfigAllowRemoteServices_Type()
)
routConfigAllowRemoteServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routConfigAllowRemoteServices.setStatus("current")
_RoutConfigLastModified_Type = Integer32
_RoutConfigLastModified_Object = MibScalar
routConfigLastModified = _RoutConfigLastModified_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 1, 301),
    _RoutConfigLastModified_Type()
)
routConfigLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routConfigLastModified.setStatus("current")
_RoutHealthVariables_ObjectIdentity = ObjectIdentity
routHealthVariables = _RoutHealthVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 2)
)
_RoutSysHealthServicesConnected_Type = Integer32
_RoutSysHealthServicesConnected_Object = MibScalar
routSysHealthServicesConnected = _RoutSysHealthServicesConnected_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 2, 10),
    _RoutSysHealthServicesConnected_Type()
)
routSysHealthServicesConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routSysHealthServicesConnected.setStatus("current")
_RoutSysHealthDevicesConnected_Type = Integer32
_RoutSysHealthDevicesConnected_Object = MibScalar
routSysHealthDevicesConnected = _RoutSysHealthDevicesConnected_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 2, 11),
    _RoutSysHealthDevicesConnected_Type()
)
routSysHealthDevicesConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routSysHealthDevicesConnected.setStatus("current")
_RoutSysHealthLastConfigCheck_Type = Integer32
_RoutSysHealthLastConfigCheck_Object = MibScalar
routSysHealthLastConfigCheck = _RoutSysHealthLastConfigCheck_Object(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 2, 12),
    _RoutSysHealthLastConfigCheck_Type()
)
routSysHealthLastConfigCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routSysHealthLastConfigCheck.setStatus("current")
_RoutTrapVariables_ObjectIdentity = ObjectIdentity
routTrapVariables = _RoutTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 10)
)

# Managed Objects groups


# Notification objects

besSRPConnectEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 9, 1)
)
if mibBuilder.loadTexts:
    besSRPConnectEvent.setStatus(
        "current"
    )

besHungThreadEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 9, 3)
)
if mibBuilder.loadTexts:
    besHungThreadEvent.setStatus(
        "current"
    )

besMailServerDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 9, 5)
)
if mibBuilder.loadTexts:
    besMailServerDownEvent.setStatus(
        "current"
    )

besMDStoBESConnectionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 9, 7)
)
if mibBuilder.loadTexts:
    besMDStoBESConnectionEvent.setStatus(
        "current"
    )

besMDSStartStopEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 9, 11)
)
if mibBuilder.loadTexts:
    besMDSStartStopEvent.setStatus(
        "current"
    )

besMDStoDBConnectionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 9, 13)
)
if mibBuilder.loadTexts:
    besMDStoDBConnectionEvent.setStatus(
        "current"
    )

besCriticalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 9, 21)
)
if mibBuilder.loadTexts:
    besCriticalEvent.setStatus(
        "current"
    )

besSRPConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 10, 3001)
)
if mibBuilder.loadTexts:
    besSRPConnectionEstablished.setStatus(
        "obsolete"
    )

besSRPConnectionDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 10, 3002)
)
if mibBuilder.loadTexts:
    besSRPConnectionDropped.setStatus(
        "obsolete"
    )

besMailServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 10, 3005)
)
if mibBuilder.loadTexts:
    besMailServerUp.setStatus(
        "current"
    )

besMailServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 10, 3006)
)
if mibBuilder.loadTexts:
    besMailServerDown.setStatus(
        "current"
    )

besMDStoBESConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 10, 3007)
)
if mibBuilder.loadTexts:
    besMDStoBESConnectionEstablished.setStatus(
        "current"
    )

besMDStoBESConnectionDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 10, 3008)
)
if mibBuilder.loadTexts:
    besMDStoBESConnectionDropped.setStatus(
        "current"
    )

mdsStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 10, 3011)
)
if mibBuilder.loadTexts:
    mdsStarted.setStatus(
        "current"
    )

mdsStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 10, 3012)
)
if mibBuilder.loadTexts:
    mdsStopped.setStatus(
        "current"
    )

mdsDBConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 10, 3013)
)
if mibBuilder.loadTexts:
    mdsDBConnectionEstablished.setStatus(
        "current"
    )

mdsDBConnectionDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 10, 3014)
)
if mibBuilder.loadTexts:
    mdsDBConnectionDropped.setStatus(
        "current"
    )

besMailAgentStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 10, 3015)
)
if mibBuilder.loadTexts:
    besMailAgentStarted.setStatus(
        "current"
    )

besMailAgentStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 10, 3016)
)
if mibBuilder.loadTexts:
    besMailAgentStopped.setStatus(
        "current"
    )

besFailedUsers = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 10, 3017)
)
if mibBuilder.loadTexts:
    besFailedUsers.setStatus(
        "current"
    )

dispSRPConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 10, 3101)
)
if mibBuilder.loadTexts:
    dispSRPConnectionEstablished.setStatus(
        "current"
    )

dispSRPConnectionDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 10, 3102)
)
if mibBuilder.loadTexts:
    dispSRPConnectionDropped.setStatus(
        "current"
    )

dispStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 10, 3103)
)
if mibBuilder.loadTexts:
    dispStarted.setStatus(
        "current"
    )

dispStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 10, 3104)
)
if mibBuilder.loadTexts:
    dispStopped.setStatus(
        "current"
    )

dispDBConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 10, 3105)
)
if mibBuilder.loadTexts:
    dispDBConnectionEstablished.setStatus(
        "current"
    )

dispDBConnectionDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 50, 10, 3106)
)
if mibBuilder.loadTexts:
    dispDBConnectionDropped.setStatus(
        "current"
    )

routSRPConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 10, 3201)
)
if mibBuilder.loadTexts:
    routSRPConnectionEstablished.setStatus(
        "current"
    )

routSRPConnectionDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 10, 3202)
)
if mibBuilder.loadTexts:
    routSRPConnectionDropped.setStatus(
        "current"
    )

routStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 10, 3203)
)
if mibBuilder.loadTexts:
    routStarted.setStatus(
        "current"
    )

routStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3530, 5, 55, 10, 3204)
)
if mibBuilder.loadTexts:
    routStopped.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLACKBERRYSERVERMIB-SMIV2",
    **{"rim": rim,
       "blackBerryServer": blackBerryServer,
       "version": version,
       "besTotMsgsPending": besTotMsgsPending,
       "besTotMsgsSent": besTotMsgsSent,
       "besTotMsgsRecvd": besTotMsgsRecvd,
       "besTotMsgsXpired": besTotMsgsXpired,
       "besTotMsgsFiltered": besTotMsgsFiltered,
       "besTotMsgsSentPerMin": besTotMsgsSentPerMin,
       "besTotMsgsRecvdPerMin": besTotMsgsRecvdPerMin,
       "besTrapVariables": besTrapVariables,
       "besSRPConnectEvent": besSRPConnectEvent,
       "besHungThreadEvent": besHungThreadEvent,
       "besMailServerDownEvent": besMailServerDownEvent,
       "besMDStoBESConnectionEvent": besMDStoBESConnectionEvent,
       "besMDSStartStopEvent": besMDSStartStopEvent,
       "besMDStoDBConnectionEvent": besMDStoDBConnectionEvent,
       "besCriticalEvent": besCriticalEvent,
       "blackBerryServerTraps": blackBerryServerTraps,
       "besSRPConnectionEstablished": besSRPConnectionEstablished,
       "besSRPConnectionDropped": besSRPConnectionDropped,
       "besMailServerUp": besMailServerUp,
       "besMailServerDown": besMailServerDown,
       "besMDStoBESConnectionEstablished": besMDStoBESConnectionEstablished,
       "besMDStoBESConnectionDropped": besMDStoBESConnectionDropped,
       "mdsStarted": mdsStarted,
       "mdsStopped": mdsStopped,
       "mdsDBConnectionEstablished": mdsDBConnectionEstablished,
       "mdsDBConnectionDropped": mdsDBConnectionDropped,
       "besMailAgentStarted": besMailAgentStarted,
       "besMailAgentStopped": besMailAgentStopped,
       "besFailedUsers": besFailedUsers,
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
       "besConfigLastModified": besConfigLastModified,
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
       "besSysHealthSrpLastErrorTimeSec": besSysHealthSrpLastErrorTimeSec,
       "besSysHealthFailedUsers": besSysHealthFailedUsers,
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
       "besUserHealthWERRequestsFromHandheld": besUserHealthWERRequestsFromHandheld,
       "besUserHealthLastErrorTimeSec": besUserHealthLastErrorTimeSec,
       "besUserHealthSMTP": besUserHealthSMTP,
       "besUserHealthLastTimeInCradleSec": besUserHealthLastTimeInCradleSec,
       "besUserHealthMailServer": besUserHealthMailServer,
       "blackBerryDispatcher": blackBerryDispatcher,
       "dispConfigVariables": dispConfigVariables,
       "dispConfigServerName": dispConfigServerName,
       "dispConfigServerId": dispConfigServerId,
       "dispConfigVersionString": dispConfigVersionString,
       "dispConfigReleaseMaj": dispConfigReleaseMaj,
       "dispConfigReleaseMin": dispConfigReleaseMin,
       "dispConfigReleaseServicePack": dispConfigReleaseServicePack,
       "dispConfigReleaseBuild": dispConfigReleaseBuild,
       "dispConfigSRPId": dispConfigSRPId,
       "dispConfigSRPHost": dispConfigSRPHost,
       "dispConfigSRPPort": dispConfigSRPPort,
       "dispConfigBIPPPort": dispConfigBIPPPort,
       "dispConfigHRT": dispConfigHRT,
       "dispConfigDBConnectingString": dispConfigDBConnectingString,
       "dispConfigMaxNumberOfAgents": dispConfigMaxNumberOfAgents,
       "dispConfigActualNumberOfAgents": dispConfigActualNumberOfAgents,
       "dispConfigExternalServicesAllowed": dispConfigExternalServicesAllowed,
       "dispConfigExternalServicesPort": dispConfigExternalServicesPort,
       "dispConfigEnabledEncryptionAlgorithm": dispConfigEnabledEncryptionAlgorithm,
       "dispConfigLicenceTotal": dispConfigLicenceTotal,
       "dispConfigLicenceRemaining": dispConfigLicenceRemaining,
       "dispConfigLicenceUsed": dispConfigLicenceUsed,
       "dispConfigLastModified": dispConfigLastModified,
       "dispHealthVariables": dispHealthVariables,
       "dispSysHealthSRPConnectedState": dispSysHealthSRPConnectedState,
       "dispSysHealthSRPLastConnectDate": dispSysHealthSRPLastConnectDate,
       "dispSysHealthSRPReconnectSuccess": dispSysHealthSRPReconnectSuccess,
       "dispSysHealthSRPReconnectsFail": dispSysHealthSRPReconnectsFail,
       "dispSysHealthSRPTotalSecNotConnected": dispSysHealthSRPTotalSecNotConnected,
       "dispSysHealthSRPLastErrorText": dispSysHealthSRPLastErrorText,
       "dispSysHealthSRPLastErrorTime": dispSysHealthSRPLastErrorTime,
       "dispTrapVariables": dispTrapVariables,
       "dispSRPConnectionEstablished": dispSRPConnectionEstablished,
       "dispSRPConnectionDropped": dispSRPConnectionDropped,
       "dispStarted": dispStarted,
       "dispStopped": dispStopped,
       "dispDBConnectionEstablished": dispDBConnectionEstablished,
       "dispDBConnectionDropped": dispDBConnectionDropped,
       "blackBerryRouter": blackBerryRouter,
       "routConfigVariables": routConfigVariables,
       "routConfigServerName": routConfigServerName,
       "routConfigVersionString": routConfigVersionString,
       "routConfigReleaseMaj": routConfigReleaseMaj,
       "routConfigReleaseMin": routConfigReleaseMin,
       "routConfigReleaseServicePack": routConfigReleaseServicePack,
       "routConfigReleaseBuild": routConfigReleaseBuild,
       "routConfigSRPHost": routConfigSRPHost,
       "routConfigSRPPort": routConfigSRPPort,
       "routConfigServicePort": routConfigServicePort,
       "routConfigDevicePort": routConfigDevicePort,
       "routConfigMaxServiceConnections": routConfigMaxServiceConnections,
       "routConfigMaxDeviceConnections": routConfigMaxDeviceConnections,
       "routConfigAllowRemoteServices": routConfigAllowRemoteServices,
       "routConfigLastModified": routConfigLastModified,
       "routHealthVariables": routHealthVariables,
       "routSysHealthServicesConnected": routSysHealthServicesConnected,
       "routSysHealthDevicesConnected": routSysHealthDevicesConnected,
       "routSysHealthLastConfigCheck": routSysHealthLastConfigCheck,
       "routTrapVariables": routTrapVariables,
       "routSRPConnectionEstablished": routSRPConnectionEstablished,
       "routSRPConnectionDropped": routSRPConnectionDropped,
       "routStarted": routStarted,
       "routStopped": routStopped}
)
