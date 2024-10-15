# SNMP MIB module (DCS3RMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DCS3RMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:27 2024
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



class DellObjectRange(Integer32):
    """Custom type DellObjectRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )





class DellUnsigned8BitRange(Integer32):
    """Custom type DellUnsigned8BitRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class DellUnsigned16BitRange(Integer32):
    """Custom type DellUnsigned16BitRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class DellUnsigned32BitRange(Integer32):
    """Custom type DellUnsigned32BitRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )





class DellBoolean(Integer32):
    """Custom type DellBoolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )





class DellStateCapabilities(Integer32):
    """Custom type DellStateCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("enableAndNotReadyCapable", 6),
          ("enableCapable", 2),
          ("notReadyCapable", 4),
          ("unknownCapabilities", 1))
    )





class DellStateSettings(Integer32):
    """Custom type DellStateSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("enabledAndNotReady", 6),
          ("notReady", 4),
          ("unknown", 1))
    )





class DellStatus(Integer32):
    """Custom type DellStatus based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )





class DellRemoteAccessType(Integer32):
    """Custom type DellRemoteAccessType based on Integer32"""
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
        *(("remoteAccessTypeIsDRAC4", 5),
          ("remoteAccessTypeIsDRAC5", 6),
          ("remoteAccessTypeIsDRACIII", 3),
          ("remoteAccessTypeIsERA", 4),
          ("remoteAccessTypeIsOther", 1),
          ("remoteAccessTypeIsUnknown", 2))
    )





class DellRemoteAccessControlCapabilities(Integer32):
    """Custom type DellRemoteAccessControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              62,
              64,
              126)
        )
    )
    namedValues = NamedValues(
        *(("allResetAndShutdownCapable", 126),
          ("allResetCapable", 62),
          ("defaultConfigResetCapable", 32),
          ("gracefulResetCapable", 16),
          ("hardResetCapable", 4),
          ("logResetCapable", 2),
          ("shutdownCapable", 64),
          ("softResetCapable", 8),
          ("unknownCapabilities", 1))
    )





class DellRemoteAccessControlSettings(Integer32):
    """Custom type DellRemoteAccessControlSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("defaultConfigReset", 32),
          ("gracefulReset", 16),
          ("hardReset", 4),
          ("logReset", 2),
          ("shutdown", 64),
          ("softReset", 8),
          ("unknown", 1))
    )





class DellRemoteAccessMonitorCapabilities(Integer32):
    """Custom type DellRemoteAccessMonitorCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("extPwrSupplyMonitorAlwaysEnabledCapable", 4),
          ("extPwrSupplyMonitorIfConnectedAndAlwaysEnabledCapable", 6),
          ("extPwrSupplyMonitorIfConnectedCapable", 2),
          ("unknownCapabilities", 1))
    )





class DellRemoteAccessMonitorSettings(Integer32):
    """Custom type DellRemoteAccessMonitorSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("extPwrSupplyMonitorAlwaysEnabledEnabled", 4),
          ("extPwrSupplyMonitorIfConnectedEnabled", 2),
          ("unknown", 1))
    )





class DellRemoteAccessLANCapabilities(Integer32):
    """Custom type DellRemoteAccessLANCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nicAndNicDHCPCapable", 6),
          ("nicCapable", 2),
          ("nicDHCPCapable", 4),
          ("unknownCapabilities", 1))
    )





class DellRemoteAccessLANSettings(Integer32):
    """Custom type DellRemoteAccessLANSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nicAndNicDHCPEnabled", 6),
          ("nicDHCPEnabled", 4),
          ("nicEnabled", 2),
          ("unknown", 1))
    )





class DellRemoteAccessHostCapabilities(Integer32):
    """Custom type DellRemoteAccessHostCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              10,
              12,
              14)
        )
    )
    namedValues = NamedValues(
        *(("smtpEmailAndTftpRemoteFloppyAndFwUpdateCapable", 14),
          ("smtpEmailAndTftpRemoteFloppyCapable", 6),
          ("smtpEmailAndTftpRemoteFwUpdateCapable", 10),
          ("smtpEmailCapable", 2),
          ("tftpRemoteFloppyAndFwUpdateCapable", 12),
          ("tftpRemoteFloppyCapable", 4),
          ("tftpRemoteFwUpdateCapable", 8),
          ("unknownCapabilities", 1))
    )





class DellRemoteAccessHostSettings(Integer32):
    """Custom type DellRemoteAccessHostSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              10,
              12,
              14)
        )
    )
    namedValues = NamedValues(
        *(("smtpEmailAndTftpRemoteFloppyAndFwUpdateEnabled", 14),
          ("smtpEmailAndTftpRemoteFloppyEnabled", 6),
          ("smtpEmailAndTftpRemoteFwUpdateEnabled", 10),
          ("smtpEmailEnabled", 2),
          ("tftpRemoteFloppyAndFwUpdateEnabled", 12),
          ("tftpRemoteFloppyEnabled", 4),
          ("tftpRemoteFwUpdateEnabled", 8),
          ("unknown", 1))
    )





class DellRemoteAccessOutOfBandSNMPCapabilities(Integer32):
    """Custom type DellRemoteAccessOutOfBandSNMPCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("oobSNMPAgentAndTrapsCapable", 6),
          ("oobSNMPAgentCapable", 2),
          ("oobSNMPTrapsCapable", 4),
          ("unknownCapabilities", 1))
    )





class DellRemoteAccessOutOfBandSNMPSettings(Integer32):
    """Custom type DellRemoteAccessOutOfBandSNMPSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("oobSNMPAgentAndTrapsEnabled", 6),
          ("oobSNMPAgentEnabled", 2),
          ("oobSNMPTrapsEnabled", 4),
          ("unknown", 1))
    )





class DellRemoteUserAdminStateCapabilities(Integer32):
    """Custom type DellRemoteUserAdminStateCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              24,
              32,
              56,
              64,
              120)
        )
    )
    namedValues = NamedValues(
        *(("alphaPagerCapable", 16),
          ("emailCapable", 32),
          ("enableCapable", 2),
          ("notReadyCapable", 4),
          ("numericPagerAlphaPagerAndEmailCapable", 56),
          ("numericPagerAlphaPagerEmailAndPrivilegeCapable", 120),
          ("numericPagerAndAlphaPagerCapable", 24),
          ("numericPagerCapable", 8),
          ("privilegeCapable", 64),
          ("unknownCapabilities", 1))
    )





class DellRemoteUserAdminStateSettings(Integer32):
    """Custom type DellRemoteUserAdminStateSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              16,
              18,
              26,
              32,
              34,
              42,
              50,
              58)
        )
    )
    namedValues = NamedValues(
        *(("alphaPagerEnabled", 16),
          ("emailEnabled", 32),
          ("enabled", 2),
          ("enabledAndAlphaPagerAndEmailEnabled", 50),
          ("enabledAndAlphaPagerEnabled", 18),
          ("enabledAndEmailEnabled", 34),
          ("enabledAndNumericPagerAlphaPagerAndEmailEnabled", 58),
          ("enabledAndNumericPagerAndAlphaPagerEnabled", 26),
          ("enabledAndNumericPagerAndEmailEnabled", 42),
          ("enabledAndNumericPagerEnabled", 10),
          ("notReady", 4),
          ("numericPagerEnabled", 8),
          ("unknown", 1))
    )





class DellRemoteUserAdminControlCapabilities(Integer32):
    """Custom type DellRemoteUserAdminControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              14)
        )
    )
    namedValues = NamedValues(
        *(("alphaPagerTestCapable", 4),
          ("emailTestCapable", 8),
          ("numericPagerTestAlphaPagerTestAndEmailTestCapable", 14),
          ("numericPagerTestAndAlphaPagerTestCapable", 6),
          ("numericPagerTestCapable", 2),
          ("unknownCapabilities", 1))
    )





class DellRemoteUserAdminControlSettings(Integer32):
    """Custom type DellRemoteUserAdminControlSettings based on Integer32"""
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
        *(("alphaPagerTest", 4),
          ("emailTest", 8),
          ("numericPagerTest", 2),
          ("unknown", 1))
    )





class DellRemoteUserAdminAlphaProtocolType(Integer32):
    """Custom type DellRemoteUserAdminAlphaProtocolType based on Integer32"""
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
        *(("alpha7E0", 3),
          ("alpha8N1", 4),
          ("other", 1),
          ("unknown", 2))
    )





class DellRemoteUserAdminAlphaBaudType(Integer32):
    """Custom type DellRemoteUserAdminAlphaBaudType based on Integer32"""
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
        *(("alphaBaud1200", 4),
          ("alphaBaud300", 3),
          ("other", 1),
          ("unknown", 2))
    )





class DellRemoteSNMPTrapStateCapabilities(Integer32):
    """Custom type DellRemoteSNMPTrapStateCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("enableAndNotReadyCapable", 6),
          ("enableCapable", 2),
          ("notReadyCapable", 4),
          ("unknownCapabilities", 1))
    )





class DellRemoteSNMPTrapStateSettings(Integer32):
    """Custom type DellRemoteSNMPTrapStateSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("enabledAndNotReady", 6),
          ("notReady", 4),
          ("unknown", 1))
    )





class DellRemoteSNMPTrapControlCapabilities(Integer32):
    """Custom type DellRemoteSNMPTrapControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapTestCapable", 2),
          ("unknownCapabilities", 1))
    )





class DellRemoteSNMPTrapControlSettings(Integer32):
    """Custom type DellRemoteSNMPTrapControlSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapTest", 2),
          ("unknown", 1))
    )





class DellRemoteDialUpStateCapabilities(Integer32):
    """Custom type DellRemoteDialUpStateCapabilities based on Integer32"""
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
              120,
              128,
              248,
              256,
              504)
        )
    )
    namedValues = NamedValues(
        *(("dialInAndOutAndDialInDHCPAndAllAuthCapable", 504),
          ("dialInAndOutAndDialInDHCPAndAuthAnyAndEncryptedCapable", 248),
          ("dialInAndOutAndDialInDHCPAndAuthAnyCapable", 120),
          ("dialInAuthAnyCapable", 64),
          ("dialInAuthEncryptedCapable", 128),
          ("dialInAuthMschapCapable", 256),
          ("dialInCapable", 8),
          ("dialInDHCPCapable", 32),
          ("dialOutCapable", 16),
          ("enableCapable", 2),
          ("notReadyCapable", 4),
          ("unknownCapabilities", 1))
    )





class DellRemoteDialUpStateSettings(Integer32):
    """Custom type DellRemoteDialUpStateSettings based on Integer32"""
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
              90,
              122,
              128,
              154,
              186,
              256,
              282,
              314)
        )
    )
    namedValues = NamedValues(
        *(("dialInAuthAnyEnabled", 64),
          ("dialInAuthEncryptedEnabled", 128),
          ("dialInAuthMschapEnabled", 256),
          ("dialInDHCPEnabled", 32),
          ("dialInEnabled", 8),
          ("dialOutEnabled", 16),
          ("enabled", 2),
          ("enabledDialInAndOutAndDialInAuthAnyEnabled", 90),
          ("enabledDialInAndOutAndDialInAuthEncryptedEnabled", 154),
          ("enabledDialInAndOutAndDialInAuthMschapEnabled", 282),
          ("enabledDialInAndOutAndDialInDHCPAndAuthAnyEnabled", 122),
          ("enabledDialInAndOutAndDialInDHCPAndAuthEncryptedEnabled", 186),
          ("enabledDialInAndOutAndDialInDHCPAndAuthMschapEnabled", 314),
          ("notReady", 4),
          ("unknown", 1))
    )





class DellRemoteDialUpModemDialType(Integer32):
    """Custom type DellRemoteDialUpModemDialType based on Integer32"""
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
        *(("remoteDialUpIsOther", 1),
          ("remoteDialUpIsPulse", 4),
          ("remoteDialUpIsTone", 3),
          ("remoteDialUpIsUnknown", 2))
    )





class DellRemoteUserDialInStateCapabilities(Integer32):
    """Custom type DellRemoteUserDialInStateCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              16,
              18,
              24,
              26)
        )
    )
    namedValues = NamedValues(
        *(("dialInCallbackPresetNumberAndUserSpecifiedCapable", 24),
          ("dialInCallbackPresetNumberCapable", 8),
          ("dialInCallbackUserSpecifiedCapable", 16),
          ("enableAndDialInCallbackPresetNumberAndUserSpecifiedCapable", 26),
          ("enableAndDialInCallbackPresetNumberCapable", 10),
          ("enableAndDialInCallbackUserSpecifiedCapable", 18),
          ("enableCapable", 2),
          ("notReadyCapable", 4),
          ("unknownCapabilities", 1))
    )





class DellRemoteUserDialInStateSettings(Integer32):
    """Custom type DellRemoteUserDialInStateSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              16,
              18)
        )
    )
    namedValues = NamedValues(
        *(("dialInCallbackPresetNumberEnabled", 8),
          ("dialInCallbackUserSpecifiedEnabled", 16),
          ("enabled", 2),
          ("enabledAndDialInCallbackPresetNumberEnabled", 10),
          ("enabledAndDialInCallbackUserSpecifiedEnabled", 18),
          ("notReady", 4),
          ("unknown", 1))
    )





class DellRemoteDialOutStateCapabilities(Integer32):
    """Custom type DellRemoteDialOutStateCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              24,
              32,
              40,
              48,
              56)
        )
    )
    namedValues = NamedValues(
        *(("dialOutPPPAuthAnyAndEncryptedCapable", 24),
          ("dialOutPPPAuthAnyAndMschapCapable", 40),
          ("dialOutPPPAuthAnyCapable", 8),
          ("dialOutPPPAuthAnyEncryptedAndMschapCapable", 56),
          ("dialOutPPPAuthEncryptedAndMschapCapable", 48),
          ("dialOutPPPAuthEncryptedCapable", 16),
          ("dialOutPPPAuthMschapCapable", 32),
          ("enableCapable", 2),
          ("notReadyCapable", 4),
          ("unknownCapabilities", 1))
    )





class DellRemoteDialOutStateSettings(Integer32):
    """Custom type DellRemoteDialOutStateSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              16,
              18,
              32,
              34)
        )
    )
    namedValues = NamedValues(
        *(("dialOutPPPAuthAnyEnabled", 8),
          ("dialOutPPPAuthEncryptedEnabled", 16),
          ("dialOutPPPAuthMschapEnabled", 32),
          ("enabled", 2),
          ("enabledAnddialOutPPPAuthAnyEnabled", 10),
          ("enabledAnddialOutPPPAuthEncryptedEnabled", 18),
          ("enabledAnddialOutPPPAuthMschapEnabled", 34),
          ("notReady", 4),
          ("unknown", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Server3_ObjectIdentity = ObjectIdentity
server3 = _Server3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892)
)
_BaseboardGroup_ObjectIdentity = ObjectIdentity
baseboardGroup = _BaseboardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1)
)
_RemoteAccessGroup_ObjectIdentity = ObjectIdentity
remoteAccessGroup = _RemoteAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700)
)
_RemoteAccessTable_Object = MibTable
remoteAccessTable = _RemoteAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10)
)
if mibBuilder.loadTexts:
    remoteAccessTable.setStatus("mandatory")
_RemoteAccessTableEntry_Object = MibTableRow
remoteAccessTableEntry = _RemoteAccessTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1)
)
remoteAccessTableEntry.setIndexNames(
    (0, "DCS3RMT-MIB", "remoteAccessChassisIndex"),
    (0, "DCS3RMT-MIB", "remoteAccessAdapterIndex"),
)
if mibBuilder.loadTexts:
    remoteAccessTableEntry.setStatus("mandatory")
_RemoteAccessChassisIndex_Type = DellObjectRange
_RemoteAccessChassisIndex_Object = MibTableColumn
remoteAccessChassisIndex = _RemoteAccessChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 1),
    _RemoteAccessChassisIndex_Type()
)
remoteAccessChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessChassisIndex.setStatus("mandatory")
_RemoteAccessAdapterIndex_Type = DellObjectRange
_RemoteAccessAdapterIndex_Object = MibTableColumn
remoteAccessAdapterIndex = _RemoteAccessAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 2),
    _RemoteAccessAdapterIndex_Type()
)
remoteAccessAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessAdapterIndex.setStatus("mandatory")
_RemoteAccessType_Type = DellRemoteAccessType
_RemoteAccessType_Object = MibTableColumn
remoteAccessType = _RemoteAccessType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 3),
    _RemoteAccessType_Type()
)
remoteAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessType.setStatus("mandatory")
_RemoteAccessStateCapabilities_Type = DellStateCapabilities
_RemoteAccessStateCapabilities_Object = MibTableColumn
remoteAccessStateCapabilities = _RemoteAccessStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 4),
    _RemoteAccessStateCapabilities_Type()
)
remoteAccessStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessStateCapabilities.setStatus("mandatory")
_RemoteAccessStateSettings_Type = DellStateSettings
_RemoteAccessStateSettings_Object = MibTableColumn
remoteAccessStateSettings = _RemoteAccessStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 5),
    _RemoteAccessStateSettings_Type()
)
remoteAccessStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessStateSettings.setStatus("mandatory")
_RemoteAccessStatus_Type = DellStatus
_RemoteAccessStatus_Object = MibTableColumn
remoteAccessStatus = _RemoteAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 6),
    _RemoteAccessStatus_Type()
)
remoteAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessStatus.setStatus("mandatory")


class _RemoteAccessProductInfoName_Type(DisplayString):
    """Custom type remoteAccessProductInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteAccessProductInfoName_Type.__name__ = "DisplayString"
_RemoteAccessProductInfoName_Object = MibTableColumn
remoteAccessProductInfoName = _RemoteAccessProductInfoName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 7),
    _RemoteAccessProductInfoName_Type()
)
remoteAccessProductInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessProductInfoName.setStatus("mandatory")


class _RemoteAccessDescriptionInfoName_Type(DisplayString):
    """Custom type remoteAccessDescriptionInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RemoteAccessDescriptionInfoName_Type.__name__ = "DisplayString"
_RemoteAccessDescriptionInfoName_Object = MibTableColumn
remoteAccessDescriptionInfoName = _RemoteAccessDescriptionInfoName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 8),
    _RemoteAccessDescriptionInfoName_Type()
)
remoteAccessDescriptionInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessDescriptionInfoName.setStatus("mandatory")


class _RemoteAccessVersionInfoName_Type(DisplayString):
    """Custom type remoteAccessVersionInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteAccessVersionInfoName_Type.__name__ = "DisplayString"
_RemoteAccessVersionInfoName_Object = MibTableColumn
remoteAccessVersionInfoName = _RemoteAccessVersionInfoName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 9),
    _RemoteAccessVersionInfoName_Type()
)
remoteAccessVersionInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessVersionInfoName.setStatus("mandatory")
_RemoteAccessControlCapabilities_Type = DellRemoteAccessControlCapabilities
_RemoteAccessControlCapabilities_Object = MibTableColumn
remoteAccessControlCapabilities = _RemoteAccessControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 10),
    _RemoteAccessControlCapabilities_Type()
)
remoteAccessControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessControlCapabilities.setStatus("mandatory")
_RemoteAccessControlSettings_Type = DellRemoteAccessControlSettings
_RemoteAccessControlSettings_Object = MibTableColumn
remoteAccessControlSettings = _RemoteAccessControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 11),
    _RemoteAccessControlSettings_Type()
)
remoteAccessControlSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessControlSettings.setStatus("mandatory")
_RemoteAccessMonitorCapabilities_Type = DellRemoteAccessMonitorCapabilities
_RemoteAccessMonitorCapabilities_Object = MibTableColumn
remoteAccessMonitorCapabilities = _RemoteAccessMonitorCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 12),
    _RemoteAccessMonitorCapabilities_Type()
)
remoteAccessMonitorCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessMonitorCapabilities.setStatus("mandatory")
_RemoteAccessMonitorSettings_Type = DellRemoteAccessMonitorSettings
_RemoteAccessMonitorSettings_Object = MibTableColumn
remoteAccessMonitorSettings = _RemoteAccessMonitorSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 13),
    _RemoteAccessMonitorSettings_Type()
)
remoteAccessMonitorSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessMonitorSettings.setStatus("mandatory")
_RemoteAccessLANCapabilities_Type = DellRemoteAccessLANCapabilities
_RemoteAccessLANCapabilities_Object = MibTableColumn
remoteAccessLANCapabilities = _RemoteAccessLANCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 14),
    _RemoteAccessLANCapabilities_Type()
)
remoteAccessLANCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessLANCapabilities.setStatus("mandatory")
_RemoteAccessLANSettings_Type = DellRemoteAccessLANSettings
_RemoteAccessLANSettings_Object = MibTableColumn
remoteAccessLANSettings = _RemoteAccessLANSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 15),
    _RemoteAccessLANSettings_Type()
)
remoteAccessLANSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessLANSettings.setStatus("mandatory")
_RemoteAccessHostCapabilities_Type = DellRemoteAccessHostCapabilities
_RemoteAccessHostCapabilities_Object = MibTableColumn
remoteAccessHostCapabilities = _RemoteAccessHostCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 16),
    _RemoteAccessHostCapabilities_Type()
)
remoteAccessHostCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessHostCapabilities.setStatus("mandatory")
_RemoteAccessHostSettings_Type = DellRemoteAccessHostSettings
_RemoteAccessHostSettings_Object = MibTableColumn
remoteAccessHostSettings = _RemoteAccessHostSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 17),
    _RemoteAccessHostSettings_Type()
)
remoteAccessHostSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessHostSettings.setStatus("mandatory")
_RemoteAccessOutOfBandSNMPCapabilities_Type = DellRemoteAccessOutOfBandSNMPCapabilities
_RemoteAccessOutOfBandSNMPCapabilities_Object = MibTableColumn
remoteAccessOutOfBandSNMPCapabilities = _RemoteAccessOutOfBandSNMPCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 18),
    _RemoteAccessOutOfBandSNMPCapabilities_Type()
)
remoteAccessOutOfBandSNMPCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessOutOfBandSNMPCapabilities.setStatus("mandatory")
_RemoteAccessOutOfBandSNMPSettings_Type = DellRemoteAccessOutOfBandSNMPSettings
_RemoteAccessOutOfBandSNMPSettings_Object = MibTableColumn
remoteAccessOutOfBandSNMPSettings = _RemoteAccessOutOfBandSNMPSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 19),
    _RemoteAccessOutOfBandSNMPSettings_Type()
)
remoteAccessOutOfBandSNMPSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessOutOfBandSNMPSettings.setStatus("mandatory")
_RemoteAccessSMTPServerIPAddress_Type = IpAddress
_RemoteAccessSMTPServerIPAddress_Object = MibTableColumn
remoteAccessSMTPServerIPAddress = _RemoteAccessSMTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 20),
    _RemoteAccessSMTPServerIPAddress_Type()
)
remoteAccessSMTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessSMTPServerIPAddress.setStatus("mandatory")
_RemoteAccessFloppyTFTPIPAddress_Type = IpAddress
_RemoteAccessFloppyTFTPIPAddress_Object = MibTableColumn
remoteAccessFloppyTFTPIPAddress = _RemoteAccessFloppyTFTPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 21),
    _RemoteAccessFloppyTFTPIPAddress_Type()
)
remoteAccessFloppyTFTPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessFloppyTFTPIPAddress.setStatus("mandatory")


class _RemoteAccessFloppyTFTPPathName_Type(DisplayString):
    """Custom type remoteAccessFloppyTFTPPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RemoteAccessFloppyTFTPPathName_Type.__name__ = "DisplayString"
_RemoteAccessFloppyTFTPPathName_Object = MibTableColumn
remoteAccessFloppyTFTPPathName = _RemoteAccessFloppyTFTPPathName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 22),
    _RemoteAccessFloppyTFTPPathName_Type()
)
remoteAccessFloppyTFTPPathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessFloppyTFTPPathName.setStatus("mandatory")
_RemoteAccessFirmwareUpdateIPAddress_Type = IpAddress
_RemoteAccessFirmwareUpdateIPAddress_Object = MibTableColumn
remoteAccessFirmwareUpdateIPAddress = _RemoteAccessFirmwareUpdateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 23),
    _RemoteAccessFirmwareUpdateIPAddress_Type()
)
remoteAccessFirmwareUpdateIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessFirmwareUpdateIPAddress.setStatus("mandatory")


class _RemoteAccessFirmwareUpdatePathName_Type(DisplayString):
    """Custom type remoteAccessFirmwareUpdatePathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RemoteAccessFirmwareUpdatePathName_Type.__name__ = "DisplayString"
_RemoteAccessFirmwareUpdatePathName_Object = MibTableColumn
remoteAccessFirmwareUpdatePathName = _RemoteAccessFirmwareUpdatePathName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 24),
    _RemoteAccessFirmwareUpdatePathName_Type()
)
remoteAccessFirmwareUpdatePathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessFirmwareUpdatePathName.setStatus("mandatory")
_RemoteAccessNICStaticIPAddress_Type = IpAddress
_RemoteAccessNICStaticIPAddress_Object = MibTableColumn
remoteAccessNICStaticIPAddress = _RemoteAccessNICStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 25),
    _RemoteAccessNICStaticIPAddress_Type()
)
remoteAccessNICStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessNICStaticIPAddress.setStatus("mandatory")
_RemoteAccessNICStaticNetmaskAddress_Type = IpAddress
_RemoteAccessNICStaticNetmaskAddress_Object = MibTableColumn
remoteAccessNICStaticNetmaskAddress = _RemoteAccessNICStaticNetmaskAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 26),
    _RemoteAccessNICStaticNetmaskAddress_Type()
)
remoteAccessNICStaticNetmaskAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessNICStaticNetmaskAddress.setStatus("mandatory")
_RemoteAccessNICStaticGatewayAddress_Type = IpAddress
_RemoteAccessNICStaticGatewayAddress_Object = MibTableColumn
remoteAccessNICStaticGatewayAddress = _RemoteAccessNICStaticGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 27),
    _RemoteAccessNICStaticGatewayAddress_Type()
)
remoteAccessNICStaticGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessNICStaticGatewayAddress.setStatus("mandatory")


class _RemoteAccessPCMCIAInfoName_Type(DisplayString):
    """Custom type remoteAccessPCMCIAInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteAccessPCMCIAInfoName_Type.__name__ = "DisplayString"
_RemoteAccessPCMCIAInfoName_Object = MibTableColumn
remoteAccessPCMCIAInfoName = _RemoteAccessPCMCIAInfoName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 28),
    _RemoteAccessPCMCIAInfoName_Type()
)
remoteAccessPCMCIAInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessPCMCIAInfoName.setStatus("mandatory")


class _RemoteAccessMiscInfoName_Type(DisplayString):
    """Custom type remoteAccessMiscInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteAccessMiscInfoName_Type.__name__ = "DisplayString"
_RemoteAccessMiscInfoName_Object = MibTableColumn
remoteAccessMiscInfoName = _RemoteAccessMiscInfoName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 29),
    _RemoteAccessMiscInfoName_Type()
)
remoteAccessMiscInfoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessMiscInfoName.setStatus("mandatory")
_RemoteAccessNICCurrentIPAddress_Type = IpAddress
_RemoteAccessNICCurrentIPAddress_Object = MibTableColumn
remoteAccessNICCurrentIPAddress = _RemoteAccessNICCurrentIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 30),
    _RemoteAccessNICCurrentIPAddress_Type()
)
remoteAccessNICCurrentIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessNICCurrentIPAddress.setStatus("mandatory")
_RemoteAccessNICCurrentNetmaskAddress_Type = IpAddress
_RemoteAccessNICCurrentNetmaskAddress_Object = MibTableColumn
remoteAccessNICCurrentNetmaskAddress = _RemoteAccessNICCurrentNetmaskAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 31),
    _RemoteAccessNICCurrentNetmaskAddress_Type()
)
remoteAccessNICCurrentNetmaskAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessNICCurrentNetmaskAddress.setStatus("mandatory")
_RemoteAccessNICCurrentGatewayAddress_Type = IpAddress
_RemoteAccessNICCurrentGatewayAddress_Object = MibTableColumn
remoteAccessNICCurrentGatewayAddress = _RemoteAccessNICCurrentGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 32),
    _RemoteAccessNICCurrentGatewayAddress_Type()
)
remoteAccessNICCurrentGatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessNICCurrentGatewayAddress.setStatus("mandatory")
_RemoteAccessNICCurrentInfoFromDHCP_Type = DellBoolean
_RemoteAccessNICCurrentInfoFromDHCP_Object = MibTableColumn
remoteAccessNICCurrentInfoFromDHCP = _RemoteAccessNICCurrentInfoFromDHCP_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 33),
    _RemoteAccessNICCurrentInfoFromDHCP_Type()
)
remoteAccessNICCurrentInfoFromDHCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessNICCurrentInfoFromDHCP.setStatus("mandatory")


class _RemoteAccessRemoteConnectURL_Type(DisplayString):
    """Custom type remoteAccessRemoteConnectURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteAccessRemoteConnectURL_Type.__name__ = "DisplayString"
_RemoteAccessRemoteConnectURL_Object = MibTableColumn
remoteAccessRemoteConnectURL = _RemoteAccessRemoteConnectURL_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 34),
    _RemoteAccessRemoteConnectURL_Type()
)
remoteAccessRemoteConnectURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessRemoteConnectURL.setStatus("mandatory")
_RemoteUserAdminTable_Object = MibTable
remoteUserAdminTable = _RemoteUserAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20)
)
if mibBuilder.loadTexts:
    remoteUserAdminTable.setStatus("mandatory")
_RemoteUserAdminTableEntry_Object = MibTableRow
remoteUserAdminTableEntry = _RemoteUserAdminTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1)
)
remoteUserAdminTableEntry.setIndexNames(
    (0, "DCS3RMT-MIB", "remoteUserAdminChassisIndex"),
    (0, "DCS3RMT-MIB", "remoteUserAdminAdapterIndex"),
    (0, "DCS3RMT-MIB", "remoteUserAdminUserIndex"),
)
if mibBuilder.loadTexts:
    remoteUserAdminTableEntry.setStatus("mandatory")
_RemoteUserAdminChassisIndex_Type = DellObjectRange
_RemoteUserAdminChassisIndex_Object = MibTableColumn
remoteUserAdminChassisIndex = _RemoteUserAdminChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 1),
    _RemoteUserAdminChassisIndex_Type()
)
remoteUserAdminChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminChassisIndex.setStatus("mandatory")
_RemoteUserAdminAdapterIndex_Type = DellObjectRange
_RemoteUserAdminAdapterIndex_Object = MibTableColumn
remoteUserAdminAdapterIndex = _RemoteUserAdminAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 2),
    _RemoteUserAdminAdapterIndex_Type()
)
remoteUserAdminAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminAdapterIndex.setStatus("mandatory")
_RemoteUserAdminUserIndex_Type = DellObjectRange
_RemoteUserAdminUserIndex_Object = MibTableColumn
remoteUserAdminUserIndex = _RemoteUserAdminUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 3),
    _RemoteUserAdminUserIndex_Type()
)
remoteUserAdminUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminUserIndex.setStatus("mandatory")
_RemoteUserAdminStateCapabilities_Type = DellRemoteUserAdminStateCapabilities
_RemoteUserAdminStateCapabilities_Object = MibTableColumn
remoteUserAdminStateCapabilities = _RemoteUserAdminStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 4),
    _RemoteUserAdminStateCapabilities_Type()
)
remoteUserAdminStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminStateCapabilities.setStatus("mandatory")
_RemoteUserAdminStateSettings_Type = DellRemoteUserAdminStateSettings
_RemoteUserAdminStateSettings_Object = MibTableColumn
remoteUserAdminStateSettings = _RemoteUserAdminStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 5),
    _RemoteUserAdminStateSettings_Type()
)
remoteUserAdminStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminStateSettings.setStatus("mandatory")
_RemoteUserAdminStatus_Type = DellStatus
_RemoteUserAdminStatus_Object = MibTableColumn
remoteUserAdminStatus = _RemoteUserAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 6),
    _RemoteUserAdminStatus_Type()
)
remoteUserAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminStatus.setStatus("mandatory")


class _RemoteUserAdminUserName_Type(DisplayString):
    """Custom type remoteUserAdminUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RemoteUserAdminUserName_Type.__name__ = "DisplayString"
_RemoteUserAdminUserName_Object = MibTableColumn
remoteUserAdminUserName = _RemoteUserAdminUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 7),
    _RemoteUserAdminUserName_Type()
)
remoteUserAdminUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminUserName.setStatus("mandatory")


class _RemoteUserAdminUserPasswordName_Type(DisplayString):
    """Custom type remoteUserAdminUserPasswordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RemoteUserAdminUserPasswordName_Type.__name__ = "DisplayString"
_RemoteUserAdminUserPasswordName_Object = MibTableColumn
remoteUserAdminUserPasswordName = _RemoteUserAdminUserPasswordName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 8),
    _RemoteUserAdminUserPasswordName_Type()
)
remoteUserAdminUserPasswordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminUserPasswordName.setStatus("mandatory")


class _RemoteUserAdminUserPrivilege_Type(DisplayString):
    """Custom type remoteUserAdminUserPrivilege based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteUserAdminUserPrivilege_Type.__name__ = "DisplayString"
_RemoteUserAdminUserPrivilege_Object = MibTableColumn
remoteUserAdminUserPrivilege = _RemoteUserAdminUserPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 9),
    _RemoteUserAdminUserPrivilege_Type()
)
remoteUserAdminUserPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminUserPrivilege.setStatus("mandatory")


class _RemoteUserAdminUserPrivilegeCapabilities_Type(DisplayString):
    """Custom type remoteUserAdminUserPrivilegeCapabilities based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteUserAdminUserPrivilegeCapabilities_Type.__name__ = "DisplayString"
_RemoteUserAdminUserPrivilegeCapabilities_Object = MibTableColumn
remoteUserAdminUserPrivilegeCapabilities = _RemoteUserAdminUserPrivilegeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 10),
    _RemoteUserAdminUserPrivilegeCapabilities_Type()
)
remoteUserAdminUserPrivilegeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminUserPrivilegeCapabilities.setStatus("mandatory")
_RemoteUserAdminAlertFilterDrsEventsMask_Type = DellUnsigned32BitRange
_RemoteUserAdminAlertFilterDrsEventsMask_Object = MibTableColumn
remoteUserAdminAlertFilterDrsEventsMask = _RemoteUserAdminAlertFilterDrsEventsMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 11),
    _RemoteUserAdminAlertFilterDrsEventsMask_Type()
)
remoteUserAdminAlertFilterDrsEventsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminAlertFilterDrsEventsMask.setStatus("mandatory")
_RemoteUserAdminAlertFilterSysEventsMask_Type = DellUnsigned32BitRange
_RemoteUserAdminAlertFilterSysEventsMask_Object = MibTableColumn
remoteUserAdminAlertFilterSysEventsMask = _RemoteUserAdminAlertFilterSysEventsMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 12),
    _RemoteUserAdminAlertFilterSysEventsMask_Type()
)
remoteUserAdminAlertFilterSysEventsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminAlertFilterSysEventsMask.setStatus("mandatory")
_RemoteUserAdminAlertFilterDrsCapabilities_Type = DellUnsigned32BitRange
_RemoteUserAdminAlertFilterDrsCapabilities_Object = MibTableColumn
remoteUserAdminAlertFilterDrsCapabilities = _RemoteUserAdminAlertFilterDrsCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 13),
    _RemoteUserAdminAlertFilterDrsCapabilities_Type()
)
remoteUserAdminAlertFilterDrsCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminAlertFilterDrsCapabilities.setStatus("mandatory")
_RemoteUserAdminAlertFilterSysCapabilities_Type = DellUnsigned32BitRange
_RemoteUserAdminAlertFilterSysCapabilities_Object = MibTableColumn
remoteUserAdminAlertFilterSysCapabilities = _RemoteUserAdminAlertFilterSysCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 14),
    _RemoteUserAdminAlertFilterSysCapabilities_Type()
)
remoteUserAdminAlertFilterSysCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminAlertFilterSysCapabilities.setStatus("mandatory")


class _RemoteUserAdminPagerNumericNumberName_Type(DisplayString):
    """Custom type remoteUserAdminPagerNumericNumberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_RemoteUserAdminPagerNumericNumberName_Type.__name__ = "DisplayString"
_RemoteUserAdminPagerNumericNumberName_Object = MibTableColumn
remoteUserAdminPagerNumericNumberName = _RemoteUserAdminPagerNumericNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 15),
    _RemoteUserAdminPagerNumericNumberName_Type()
)
remoteUserAdminPagerNumericNumberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerNumericNumberName.setStatus("mandatory")


class _RemoteUserAdminPagerNumericMessageName_Type(DisplayString):
    """Custom type remoteUserAdminPagerNumericMessageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteUserAdminPagerNumericMessageName_Type.__name__ = "DisplayString"
_RemoteUserAdminPagerNumericMessageName_Object = MibTableColumn
remoteUserAdminPagerNumericMessageName = _RemoteUserAdminPagerNumericMessageName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 16),
    _RemoteUserAdminPagerNumericMessageName_Type()
)
remoteUserAdminPagerNumericMessageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerNumericMessageName.setStatus("mandatory")
_RemoteUserAdminPagerNumericHangupDelay_Type = DellUnsigned32BitRange
_RemoteUserAdminPagerNumericHangupDelay_Object = MibTableColumn
remoteUserAdminPagerNumericHangupDelay = _RemoteUserAdminPagerNumericHangupDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 17),
    _RemoteUserAdminPagerNumericHangupDelay_Type()
)
remoteUserAdminPagerNumericHangupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerNumericHangupDelay.setStatus("mandatory")


class _RemoteUserAdminPagerAlphaPhoneNumberName_Type(DisplayString):
    """Custom type remoteUserAdminPagerAlphaPhoneNumberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_RemoteUserAdminPagerAlphaPhoneNumberName_Type.__name__ = "DisplayString"
_RemoteUserAdminPagerAlphaPhoneNumberName_Object = MibTableColumn
remoteUserAdminPagerAlphaPhoneNumberName = _RemoteUserAdminPagerAlphaPhoneNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 18),
    _RemoteUserAdminPagerAlphaPhoneNumberName_Type()
)
remoteUserAdminPagerAlphaPhoneNumberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaPhoneNumberName.setStatus("mandatory")
_RemoteUserAdminPagerAlphaProtocol_Type = DellRemoteUserAdminAlphaProtocolType
_RemoteUserAdminPagerAlphaProtocol_Object = MibTableColumn
remoteUserAdminPagerAlphaProtocol = _RemoteUserAdminPagerAlphaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 19),
    _RemoteUserAdminPagerAlphaProtocol_Type()
)
remoteUserAdminPagerAlphaProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaProtocol.setStatus("mandatory")
_RemoteUserAdminPagerAlphaBaudRate_Type = DellRemoteUserAdminAlphaBaudType
_RemoteUserAdminPagerAlphaBaudRate_Object = MibTableColumn
remoteUserAdminPagerAlphaBaudRate = _RemoteUserAdminPagerAlphaBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 20),
    _RemoteUserAdminPagerAlphaBaudRate_Type()
)
remoteUserAdminPagerAlphaBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaBaudRate.setStatus("mandatory")


class _RemoteUserAdminPagerAlphaCustomMessageName_Type(DisplayString):
    """Custom type remoteUserAdminPagerAlphaCustomMessageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteUserAdminPagerAlphaCustomMessageName_Type.__name__ = "DisplayString"
_RemoteUserAdminPagerAlphaCustomMessageName_Object = MibTableColumn
remoteUserAdminPagerAlphaCustomMessageName = _RemoteUserAdminPagerAlphaCustomMessageName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 21),
    _RemoteUserAdminPagerAlphaCustomMessageName_Type()
)
remoteUserAdminPagerAlphaCustomMessageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaCustomMessageName.setStatus("mandatory")
_RemoteUserAdminPagerAlphaModemConnectTimeout_Type = DellUnsigned32BitRange
_RemoteUserAdminPagerAlphaModemConnectTimeout_Object = MibTableColumn
remoteUserAdminPagerAlphaModemConnectTimeout = _RemoteUserAdminPagerAlphaModemConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 22),
    _RemoteUserAdminPagerAlphaModemConnectTimeout_Type()
)
remoteUserAdminPagerAlphaModemConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaModemConnectTimeout.setStatus("mandatory")


class _RemoteUserAdminPagerAlphaPagerIdName_Type(DisplayString):
    """Custom type remoteUserAdminPagerAlphaPagerIdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteUserAdminPagerAlphaPagerIdName_Type.__name__ = "DisplayString"
_RemoteUserAdminPagerAlphaPagerIdName_Object = MibTableColumn
remoteUserAdminPagerAlphaPagerIdName = _RemoteUserAdminPagerAlphaPagerIdName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 23),
    _RemoteUserAdminPagerAlphaPagerIdName_Type()
)
remoteUserAdminPagerAlphaPagerIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaPagerIdName.setStatus("mandatory")


class _RemoteUserAdminPagerAlphaPasswordName_Type(DisplayString):
    """Custom type remoteUserAdminPagerAlphaPasswordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteUserAdminPagerAlphaPasswordName_Type.__name__ = "DisplayString"
_RemoteUserAdminPagerAlphaPasswordName_Object = MibTableColumn
remoteUserAdminPagerAlphaPasswordName = _RemoteUserAdminPagerAlphaPasswordName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 24),
    _RemoteUserAdminPagerAlphaPasswordName_Type()
)
remoteUserAdminPagerAlphaPasswordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaPasswordName.setStatus("mandatory")


class _RemoteUserAdminPagerModemInitStringName_Type(DisplayString):
    """Custom type remoteUserAdminPagerModemInitStringName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteUserAdminPagerModemInitStringName_Type.__name__ = "DisplayString"
_RemoteUserAdminPagerModemInitStringName_Object = MibTableColumn
remoteUserAdminPagerModemInitStringName = _RemoteUserAdminPagerModemInitStringName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 25),
    _RemoteUserAdminPagerModemInitStringName_Type()
)
remoteUserAdminPagerModemInitStringName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerModemInitStringName.setStatus("mandatory")
_RemoteUserAdminPagerModemPort_Type = DellUnsigned32BitRange
_RemoteUserAdminPagerModemPort_Object = MibTableColumn
remoteUserAdminPagerModemPort = _RemoteUserAdminPagerModemPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 26),
    _RemoteUserAdminPagerModemPort_Type()
)
remoteUserAdminPagerModemPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerModemPort.setStatus("mandatory")


class _RemoteUserAdminEmailAddressName_Type(DisplayString):
    """Custom type remoteUserAdminEmailAddressName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteUserAdminEmailAddressName_Type.__name__ = "DisplayString"
_RemoteUserAdminEmailAddressName_Object = MibTableColumn
remoteUserAdminEmailAddressName = _RemoteUserAdminEmailAddressName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 27),
    _RemoteUserAdminEmailAddressName_Type()
)
remoteUserAdminEmailAddressName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminEmailAddressName.setStatus("mandatory")


class _RemoteUserAdminEmailCustomMessageName_Type(DisplayString):
    """Custom type remoteUserAdminEmailCustomMessageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteUserAdminEmailCustomMessageName_Type.__name__ = "DisplayString"
_RemoteUserAdminEmailCustomMessageName_Object = MibTableColumn
remoteUserAdminEmailCustomMessageName = _RemoteUserAdminEmailCustomMessageName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 28),
    _RemoteUserAdminEmailCustomMessageName_Type()
)
remoteUserAdminEmailCustomMessageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminEmailCustomMessageName.setStatus("mandatory")
_RemoteUserAdminControlCapabilities_Type = DellRemoteUserAdminControlCapabilities
_RemoteUserAdminControlCapabilities_Object = MibTableColumn
remoteUserAdminControlCapabilities = _RemoteUserAdminControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 29),
    _RemoteUserAdminControlCapabilities_Type()
)
remoteUserAdminControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminControlCapabilities.setStatus("mandatory")
_RemoteUserAdminControlSettings_Type = DellRemoteUserAdminControlSettings
_RemoteUserAdminControlSettings_Object = MibTableColumn
remoteUserAdminControlSettings = _RemoteUserAdminControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 30),
    _RemoteUserAdminControlSettings_Type()
)
remoteUserAdminControlSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminControlSettings.setStatus("mandatory")
_RemoteUserAdminUserType_Type = DellUnsigned8BitRange
_RemoteUserAdminUserType_Object = MibTableColumn
remoteUserAdminUserType = _RemoteUserAdminUserType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 31),
    _RemoteUserAdminUserType_Type()
)
remoteUserAdminUserType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminUserType.setStatus("mandatory")
_RemoteSNMPTrapTable_Object = MibTable
remoteSNMPTrapTable = _RemoteSNMPTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30)
)
if mibBuilder.loadTexts:
    remoteSNMPTrapTable.setStatus("mandatory")
_RemoteSNMPTrapTableEntry_Object = MibTableRow
remoteSNMPTrapTableEntry = _RemoteSNMPTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1)
)
remoteSNMPTrapTableEntry.setIndexNames(
    (0, "DCS3RMT-MIB", "remoteSNMPTrapChassisIndex"),
    (0, "DCS3RMT-MIB", "remoteSNMPTrapAdapterIndex"),
    (0, "DCS3RMT-MIB", "remoteSNMPTrapIndex"),
)
if mibBuilder.loadTexts:
    remoteSNMPTrapTableEntry.setStatus("mandatory")
_RemoteSNMPTrapChassisIndex_Type = DellObjectRange
_RemoteSNMPTrapChassisIndex_Object = MibTableColumn
remoteSNMPTrapChassisIndex = _RemoteSNMPTrapChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 1),
    _RemoteSNMPTrapChassisIndex_Type()
)
remoteSNMPTrapChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSNMPTrapChassisIndex.setStatus("mandatory")
_RemoteSNMPTrapAdapterIndex_Type = DellObjectRange
_RemoteSNMPTrapAdapterIndex_Object = MibTableColumn
remoteSNMPTrapAdapterIndex = _RemoteSNMPTrapAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 2),
    _RemoteSNMPTrapAdapterIndex_Type()
)
remoteSNMPTrapAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSNMPTrapAdapterIndex.setStatus("mandatory")
_RemoteSNMPTrapIndex_Type = DellObjectRange
_RemoteSNMPTrapIndex_Object = MibTableColumn
remoteSNMPTrapIndex = _RemoteSNMPTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 3),
    _RemoteSNMPTrapIndex_Type()
)
remoteSNMPTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSNMPTrapIndex.setStatus("mandatory")
_RemoteSNMPTrapStateCapabilities_Type = DellRemoteSNMPTrapStateCapabilities
_RemoteSNMPTrapStateCapabilities_Object = MibTableColumn
remoteSNMPTrapStateCapabilities = _RemoteSNMPTrapStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 4),
    _RemoteSNMPTrapStateCapabilities_Type()
)
remoteSNMPTrapStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSNMPTrapStateCapabilities.setStatus("mandatory")
_RemoteSNMPTrapStateSettings_Type = DellRemoteSNMPTrapStateSettings
_RemoteSNMPTrapStateSettings_Object = MibTableColumn
remoteSNMPTrapStateSettings = _RemoteSNMPTrapStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 5),
    _RemoteSNMPTrapStateSettings_Type()
)
remoteSNMPTrapStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteSNMPTrapStateSettings.setStatus("mandatory")
_RemoteSNMPTrapStatus_Type = DellStatus
_RemoteSNMPTrapStatus_Object = MibTableColumn
remoteSNMPTrapStatus = _RemoteSNMPTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 6),
    _RemoteSNMPTrapStatus_Type()
)
remoteSNMPTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSNMPTrapStatus.setStatus("mandatory")
_RemoteSNMPTrapDestinationIPAddress_Type = IpAddress
_RemoteSNMPTrapDestinationIPAddress_Object = MibTableColumn
remoteSNMPTrapDestinationIPAddress = _RemoteSNMPTrapDestinationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 7),
    _RemoteSNMPTrapDestinationIPAddress_Type()
)
remoteSNMPTrapDestinationIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteSNMPTrapDestinationIPAddress.setStatus("mandatory")


class _RemoteSNMPTrapSNMPCommunityName_Type(DisplayString):
    """Custom type remoteSNMPTrapSNMPCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteSNMPTrapSNMPCommunityName_Type.__name__ = "DisplayString"
_RemoteSNMPTrapSNMPCommunityName_Object = MibTableColumn
remoteSNMPTrapSNMPCommunityName = _RemoteSNMPTrapSNMPCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 8),
    _RemoteSNMPTrapSNMPCommunityName_Type()
)
remoteSNMPTrapSNMPCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteSNMPTrapSNMPCommunityName.setStatus("mandatory")
_RemoteSNMPTrapFilterDrsEventsMask_Type = DellUnsigned32BitRange
_RemoteSNMPTrapFilterDrsEventsMask_Object = MibTableColumn
remoteSNMPTrapFilterDrsEventsMask = _RemoteSNMPTrapFilterDrsEventsMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 9),
    _RemoteSNMPTrapFilterDrsEventsMask_Type()
)
remoteSNMPTrapFilterDrsEventsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteSNMPTrapFilterDrsEventsMask.setStatus("mandatory")
_RemoteSNMPTrapFilterSysEventsMask_Type = DellUnsigned32BitRange
_RemoteSNMPTrapFilterSysEventsMask_Object = MibTableColumn
remoteSNMPTrapFilterSysEventsMask = _RemoteSNMPTrapFilterSysEventsMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 10),
    _RemoteSNMPTrapFilterSysEventsMask_Type()
)
remoteSNMPTrapFilterSysEventsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteSNMPTrapFilterSysEventsMask.setStatus("mandatory")
_RemoteSNMPTrapFilterDrsCapabilities_Type = DellUnsigned32BitRange
_RemoteSNMPTrapFilterDrsCapabilities_Object = MibTableColumn
remoteSNMPTrapFilterDrsCapabilities = _RemoteSNMPTrapFilterDrsCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 11),
    _RemoteSNMPTrapFilterDrsCapabilities_Type()
)
remoteSNMPTrapFilterDrsCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSNMPTrapFilterDrsCapabilities.setStatus("mandatory")
_RemoteSNMPTrapFilterSysCapabilities_Type = DellUnsigned32BitRange
_RemoteSNMPTrapFilterSysCapabilities_Object = MibTableColumn
remoteSNMPTrapFilterSysCapabilities = _RemoteSNMPTrapFilterSysCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 12),
    _RemoteSNMPTrapFilterSysCapabilities_Type()
)
remoteSNMPTrapFilterSysCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSNMPTrapFilterSysCapabilities.setStatus("mandatory")
_RemoteSNMPTrapControlCapabilities_Type = DellRemoteSNMPTrapControlCapabilities
_RemoteSNMPTrapControlCapabilities_Object = MibTableColumn
remoteSNMPTrapControlCapabilities = _RemoteSNMPTrapControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 13),
    _RemoteSNMPTrapControlCapabilities_Type()
)
remoteSNMPTrapControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSNMPTrapControlCapabilities.setStatus("mandatory")
_RemoteSNMPTrapControlSettings_Type = DellRemoteSNMPTrapControlSettings
_RemoteSNMPTrapControlSettings_Object = MibTableColumn
remoteSNMPTrapControlSettings = _RemoteSNMPTrapControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 14),
    _RemoteSNMPTrapControlSettings_Type()
)
remoteSNMPTrapControlSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteSNMPTrapControlSettings.setStatus("mandatory")
_RemoteDialUpTable_Object = MibTable
remoteDialUpTable = _RemoteDialUpTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40)
)
if mibBuilder.loadTexts:
    remoteDialUpTable.setStatus("mandatory")
_RemoteDialUpTableEntry_Object = MibTableRow
remoteDialUpTableEntry = _RemoteDialUpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1)
)
remoteDialUpTableEntry.setIndexNames(
    (0, "DCS3RMT-MIB", "remoteDialUpChassisIndex"),
    (0, "DCS3RMT-MIB", "remoteDialUpAdapterIndex"),
    (0, "DCS3RMT-MIB", "remoteDialUpIndex"),
)
if mibBuilder.loadTexts:
    remoteDialUpTableEntry.setStatus("mandatory")
_RemoteDialUpChassisIndex_Type = DellObjectRange
_RemoteDialUpChassisIndex_Object = MibTableColumn
remoteDialUpChassisIndex = _RemoteDialUpChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 1),
    _RemoteDialUpChassisIndex_Type()
)
remoteDialUpChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialUpChassisIndex.setStatus("mandatory")
_RemoteDialUpAdapterIndex_Type = DellObjectRange
_RemoteDialUpAdapterIndex_Object = MibTableColumn
remoteDialUpAdapterIndex = _RemoteDialUpAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 2),
    _RemoteDialUpAdapterIndex_Type()
)
remoteDialUpAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialUpAdapterIndex.setStatus("mandatory")
_RemoteDialUpIndex_Type = DellObjectRange
_RemoteDialUpIndex_Object = MibTableColumn
remoteDialUpIndex = _RemoteDialUpIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 3),
    _RemoteDialUpIndex_Type()
)
remoteDialUpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialUpIndex.setStatus("mandatory")
_RemoteDialUpStateCapabilities_Type = DellRemoteDialUpStateCapabilities
_RemoteDialUpStateCapabilities_Object = MibTableColumn
remoteDialUpStateCapabilities = _RemoteDialUpStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 4),
    _RemoteDialUpStateCapabilities_Type()
)
remoteDialUpStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialUpStateCapabilities.setStatus("mandatory")
_RemoteDialUpStateSettings_Type = DellRemoteDialUpStateSettings
_RemoteDialUpStateSettings_Object = MibTableColumn
remoteDialUpStateSettings = _RemoteDialUpStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 5),
    _RemoteDialUpStateSettings_Type()
)
remoteDialUpStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpStateSettings.setStatus("mandatory")
_RemoteDialUpStatus_Type = DellStatus
_RemoteDialUpStatus_Object = MibTableColumn
remoteDialUpStatus = _RemoteDialUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 6),
    _RemoteDialUpStatus_Type()
)
remoteDialUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialUpStatus.setStatus("mandatory")
_RemoteDialUpPPPDialInBaseIPAddress_Type = IpAddress
_RemoteDialUpPPPDialInBaseIPAddress_Object = MibTableColumn
remoteDialUpPPPDialInBaseIPAddress = _RemoteDialUpPPPDialInBaseIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 7),
    _RemoteDialUpPPPDialInBaseIPAddress_Type()
)
remoteDialUpPPPDialInBaseIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpPPPDialInBaseIPAddress.setStatus("mandatory")
_RemoteDialUpPPPDialInIdleTimeout_Type = DellUnsigned32BitRange
_RemoteDialUpPPPDialInIdleTimeout_Object = MibTableColumn
remoteDialUpPPPDialInIdleTimeout = _RemoteDialUpPPPDialInIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 8),
    _RemoteDialUpPPPDialInIdleTimeout_Type()
)
remoteDialUpPPPDialInIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpPPPDialInIdleTimeout.setStatus("mandatory")
_RemoteDialUpPPPDialInMaxConnectTimeout_Type = DellUnsigned32BitRange
_RemoteDialUpPPPDialInMaxConnectTimeout_Object = MibTableColumn
remoteDialUpPPPDialInMaxConnectTimeout = _RemoteDialUpPPPDialInMaxConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 9),
    _RemoteDialUpPPPDialInMaxConnectTimeout_Type()
)
remoteDialUpPPPDialInMaxConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpPPPDialInMaxConnectTimeout.setStatus("mandatory")
_RemoteDialUpDialOutModemConnectTimeout_Type = DellUnsigned32BitRange
_RemoteDialUpDialOutModemConnectTimeout_Object = MibTableColumn
remoteDialUpDialOutModemConnectTimeout = _RemoteDialUpDialOutModemConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 10),
    _RemoteDialUpDialOutModemConnectTimeout_Type()
)
remoteDialUpDialOutModemConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpDialOutModemConnectTimeout.setStatus("mandatory")
_RemoteDialUpModemDialType_Type = DellRemoteDialUpModemDialType
_RemoteDialUpModemDialType_Object = MibTableColumn
remoteDialUpModemDialType = _RemoteDialUpModemDialType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 11),
    _RemoteDialUpModemDialType_Type()
)
remoteDialUpModemDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpModemDialType.setStatus("mandatory")


class _RemoteDialUpModemInitStringName_Type(DisplayString):
    """Custom type remoteDialUpModemInitStringName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteDialUpModemInitStringName_Type.__name__ = "DisplayString"
_RemoteDialUpModemInitStringName_Object = MibTableColumn
remoteDialUpModemInitStringName = _RemoteDialUpModemInitStringName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 12),
    _RemoteDialUpModemInitStringName_Type()
)
remoteDialUpModemInitStringName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpModemInitStringName.setStatus("mandatory")
_RemoteDialUpModemBaudRate_Type = DellUnsigned32BitRange
_RemoteDialUpModemBaudRate_Object = MibTableColumn
remoteDialUpModemBaudRate = _RemoteDialUpModemBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 13),
    _RemoteDialUpModemBaudRate_Type()
)
remoteDialUpModemBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpModemBaudRate.setStatus("mandatory")
_RemoteDialUpModemPort_Type = DellUnsigned32BitRange
_RemoteDialUpModemPort_Object = MibTableColumn
remoteDialUpModemPort = _RemoteDialUpModemPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 14),
    _RemoteDialUpModemPort_Type()
)
remoteDialUpModemPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpModemPort.setStatus("mandatory")
_RemoteUserDialInCfgTable_Object = MibTable
remoteUserDialInCfgTable = _RemoteUserDialInCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50)
)
if mibBuilder.loadTexts:
    remoteUserDialInCfgTable.setStatus("mandatory")
_RemoteUserDialInCfgTableEntry_Object = MibTableRow
remoteUserDialInCfgTableEntry = _RemoteUserDialInCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1)
)
remoteUserDialInCfgTableEntry.setIndexNames(
    (0, "DCS3RMT-MIB", "remoteUserDialInCfgChassisIndex"),
    (0, "DCS3RMT-MIB", "remoteUserDialInCfgAdapterIndex"),
    (0, "DCS3RMT-MIB", "remoteUserDialInCfgUserIndex"),
)
if mibBuilder.loadTexts:
    remoteUserDialInCfgTableEntry.setStatus("mandatory")
_RemoteUserDialInCfgChassisIndex_Type = DellObjectRange
_RemoteUserDialInCfgChassisIndex_Object = MibTableColumn
remoteUserDialInCfgChassisIndex = _RemoteUserDialInCfgChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 1),
    _RemoteUserDialInCfgChassisIndex_Type()
)
remoteUserDialInCfgChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserDialInCfgChassisIndex.setStatus("mandatory")
_RemoteUserDialInCfgAdapterIndex_Type = DellObjectRange
_RemoteUserDialInCfgAdapterIndex_Object = MibTableColumn
remoteUserDialInCfgAdapterIndex = _RemoteUserDialInCfgAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 2),
    _RemoteUserDialInCfgAdapterIndex_Type()
)
remoteUserDialInCfgAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserDialInCfgAdapterIndex.setStatus("mandatory")
_RemoteUserDialInCfgUserIndex_Type = DellObjectRange
_RemoteUserDialInCfgUserIndex_Object = MibTableColumn
remoteUserDialInCfgUserIndex = _RemoteUserDialInCfgUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 3),
    _RemoteUserDialInCfgUserIndex_Type()
)
remoteUserDialInCfgUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserDialInCfgUserIndex.setStatus("mandatory")
_RemoteUserDialInCfgStateCapabilities_Type = DellRemoteUserDialInStateCapabilities
_RemoteUserDialInCfgStateCapabilities_Object = MibTableColumn
remoteUserDialInCfgStateCapabilities = _RemoteUserDialInCfgStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 4),
    _RemoteUserDialInCfgStateCapabilities_Type()
)
remoteUserDialInCfgStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserDialInCfgStateCapabilities.setStatus("mandatory")
_RemoteUserDialInCfgStateSettings_Type = DellRemoteUserDialInStateSettings
_RemoteUserDialInCfgStateSettings_Object = MibTableColumn
remoteUserDialInCfgStateSettings = _RemoteUserDialInCfgStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 5),
    _RemoteUserDialInCfgStateSettings_Type()
)
remoteUserDialInCfgStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserDialInCfgStateSettings.setStatus("mandatory")
_RemoteUserDialInCfgStatus_Type = DellStatus
_RemoteUserDialInCfgStatus_Object = MibTableColumn
remoteUserDialInCfgStatus = _RemoteUserDialInCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 6),
    _RemoteUserDialInCfgStatus_Type()
)
remoteUserDialInCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserDialInCfgStatus.setStatus("mandatory")


class _RemoteUserDialInCfgPPPUserName_Type(DisplayString):
    """Custom type remoteUserDialInCfgPPPUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RemoteUserDialInCfgPPPUserName_Type.__name__ = "DisplayString"
_RemoteUserDialInCfgPPPUserName_Object = MibTableColumn
remoteUserDialInCfgPPPUserName = _RemoteUserDialInCfgPPPUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 7),
    _RemoteUserDialInCfgPPPUserName_Type()
)
remoteUserDialInCfgPPPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserDialInCfgPPPUserName.setStatus("mandatory")


class _RemoteUserDialInCfgPPPUserPasswordName_Type(DisplayString):
    """Custom type remoteUserDialInCfgPPPUserPasswordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RemoteUserDialInCfgPPPUserPasswordName_Type.__name__ = "DisplayString"
_RemoteUserDialInCfgPPPUserPasswordName_Object = MibTableColumn
remoteUserDialInCfgPPPUserPasswordName = _RemoteUserDialInCfgPPPUserPasswordName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 8),
    _RemoteUserDialInCfgPPPUserPasswordName_Type()
)
remoteUserDialInCfgPPPUserPasswordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserDialInCfgPPPUserPasswordName.setStatus("mandatory")


class _RemoteUserDialInCfgCallbackPhoneNumberName_Type(DisplayString):
    """Custom type remoteUserDialInCfgCallbackPhoneNumberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_RemoteUserDialInCfgCallbackPhoneNumberName_Type.__name__ = "DisplayString"
_RemoteUserDialInCfgCallbackPhoneNumberName_Object = MibTableColumn
remoteUserDialInCfgCallbackPhoneNumberName = _RemoteUserDialInCfgCallbackPhoneNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 9),
    _RemoteUserDialInCfgCallbackPhoneNumberName_Type()
)
remoteUserDialInCfgCallbackPhoneNumberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserDialInCfgCallbackPhoneNumberName.setStatus("mandatory")
_RemoteDialOutTable_Object = MibTable
remoteDialOutTable = _RemoteDialOutTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60)
)
if mibBuilder.loadTexts:
    remoteDialOutTable.setStatus("mandatory")
_RemoteDialOutTableEntry_Object = MibTableRow
remoteDialOutTableEntry = _RemoteDialOutTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1)
)
remoteDialOutTableEntry.setIndexNames(
    (0, "DCS3RMT-MIB", "remoteDialOutChassisIndex"),
    (0, "DCS3RMT-MIB", "remoteDialOutAdapterIndex"),
    (0, "DCS3RMT-MIB", "remoteDialOutDialOutIndex"),
)
if mibBuilder.loadTexts:
    remoteDialOutTableEntry.setStatus("mandatory")
_RemoteDialOutChassisIndex_Type = DellObjectRange
_RemoteDialOutChassisIndex_Object = MibTableColumn
remoteDialOutChassisIndex = _RemoteDialOutChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 1),
    _RemoteDialOutChassisIndex_Type()
)
remoteDialOutChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialOutChassisIndex.setStatus("mandatory")
_RemoteDialOutAdapterIndex_Type = DellObjectRange
_RemoteDialOutAdapterIndex_Object = MibTableColumn
remoteDialOutAdapterIndex = _RemoteDialOutAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 2),
    _RemoteDialOutAdapterIndex_Type()
)
remoteDialOutAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialOutAdapterIndex.setStatus("mandatory")
_RemoteDialOutDialOutIndex_Type = DellObjectRange
_RemoteDialOutDialOutIndex_Object = MibTableColumn
remoteDialOutDialOutIndex = _RemoteDialOutDialOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 3),
    _RemoteDialOutDialOutIndex_Type()
)
remoteDialOutDialOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialOutDialOutIndex.setStatus("mandatory")
_RemoteDialOutStateCapabilities_Type = DellRemoteDialOutStateCapabilities
_RemoteDialOutStateCapabilities_Object = MibTableColumn
remoteDialOutStateCapabilities = _RemoteDialOutStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 4),
    _RemoteDialOutStateCapabilities_Type()
)
remoteDialOutStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialOutStateCapabilities.setStatus("mandatory")
_RemoteDialOutStateSettings_Type = DellRemoteDialOutStateSettings
_RemoteDialOutStateSettings_Object = MibTableColumn
remoteDialOutStateSettings = _RemoteDialOutStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 5),
    _RemoteDialOutStateSettings_Type()
)
remoteDialOutStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialOutStateSettings.setStatus("mandatory")
_RemoteDialOutStatus_Type = DellStatus
_RemoteDialOutStatus_Object = MibTableColumn
remoteDialOutStatus = _RemoteDialOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 6),
    _RemoteDialOutStatus_Type()
)
remoteDialOutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialOutStatus.setStatus("mandatory")
_RemoteDialOutIPAddress_Type = IpAddress
_RemoteDialOutIPAddress_Object = MibTableColumn
remoteDialOutIPAddress = _RemoteDialOutIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 7),
    _RemoteDialOutIPAddress_Type()
)
remoteDialOutIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialOutIPAddress.setStatus("mandatory")


class _RemoteDialOutPhoneNumberName_Type(DisplayString):
    """Custom type remoteDialOutPhoneNumberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_RemoteDialOutPhoneNumberName_Type.__name__ = "DisplayString"
_RemoteDialOutPhoneNumberName_Object = MibTableColumn
remoteDialOutPhoneNumberName = _RemoteDialOutPhoneNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 8),
    _RemoteDialOutPhoneNumberName_Type()
)
remoteDialOutPhoneNumberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialOutPhoneNumberName.setStatus("mandatory")


class _RemoteDialOutPPPUserName_Type(DisplayString):
    """Custom type remoteDialOutPPPUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteDialOutPPPUserName_Type.__name__ = "DisplayString"
_RemoteDialOutPPPUserName_Object = MibTableColumn
remoteDialOutPPPUserName = _RemoteDialOutPPPUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 9),
    _RemoteDialOutPPPUserName_Type()
)
remoteDialOutPPPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialOutPPPUserName.setStatus("mandatory")


class _RemoteDialOutPPPPasswordName_Type(DisplayString):
    """Custom type remoteDialOutPPPPasswordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteDialOutPPPPasswordName_Type.__name__ = "DisplayString"
_RemoteDialOutPPPPasswordName_Object = MibTableColumn
remoteDialOutPPPPasswordName = _RemoteDialOutPPPPasswordName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 10),
    _RemoteDialOutPPPPasswordName_Type()
)
remoteDialOutPPPPasswordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialOutPPPPasswordName.setStatus("mandatory")
_DrsOutOfBandGroup_ObjectIdentity = ObjectIdentity
drsOutOfBandGroup = _DrsOutOfBandGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DCS3RMT-MIB",
    **{"DellObjectRange": DellObjectRange,
       "DellUnsigned8BitRange": DellUnsigned8BitRange,
       "DellUnsigned16BitRange": DellUnsigned16BitRange,
       "DellUnsigned32BitRange": DellUnsigned32BitRange,
       "DellBoolean": DellBoolean,
       "DellStateCapabilities": DellStateCapabilities,
       "DellStateSettings": DellStateSettings,
       "DellStatus": DellStatus,
       "DellRemoteAccessType": DellRemoteAccessType,
       "DellRemoteAccessControlCapabilities": DellRemoteAccessControlCapabilities,
       "DellRemoteAccessControlSettings": DellRemoteAccessControlSettings,
       "DellRemoteAccessMonitorCapabilities": DellRemoteAccessMonitorCapabilities,
       "DellRemoteAccessMonitorSettings": DellRemoteAccessMonitorSettings,
       "DellRemoteAccessLANCapabilities": DellRemoteAccessLANCapabilities,
       "DellRemoteAccessLANSettings": DellRemoteAccessLANSettings,
       "DellRemoteAccessHostCapabilities": DellRemoteAccessHostCapabilities,
       "DellRemoteAccessHostSettings": DellRemoteAccessHostSettings,
       "DellRemoteAccessOutOfBandSNMPCapabilities": DellRemoteAccessOutOfBandSNMPCapabilities,
       "DellRemoteAccessOutOfBandSNMPSettings": DellRemoteAccessOutOfBandSNMPSettings,
       "DellRemoteUserAdminStateCapabilities": DellRemoteUserAdminStateCapabilities,
       "DellRemoteUserAdminStateSettings": DellRemoteUserAdminStateSettings,
       "DellRemoteUserAdminControlCapabilities": DellRemoteUserAdminControlCapabilities,
       "DellRemoteUserAdminControlSettings": DellRemoteUserAdminControlSettings,
       "DellRemoteUserAdminAlphaProtocolType": DellRemoteUserAdminAlphaProtocolType,
       "DellRemoteUserAdminAlphaBaudType": DellRemoteUserAdminAlphaBaudType,
       "DellRemoteSNMPTrapStateCapabilities": DellRemoteSNMPTrapStateCapabilities,
       "DellRemoteSNMPTrapStateSettings": DellRemoteSNMPTrapStateSettings,
       "DellRemoteSNMPTrapControlCapabilities": DellRemoteSNMPTrapControlCapabilities,
       "DellRemoteSNMPTrapControlSettings": DellRemoteSNMPTrapControlSettings,
       "DellRemoteDialUpStateCapabilities": DellRemoteDialUpStateCapabilities,
       "DellRemoteDialUpStateSettings": DellRemoteDialUpStateSettings,
       "DellRemoteDialUpModemDialType": DellRemoteDialUpModemDialType,
       "DellRemoteUserDialInStateCapabilities": DellRemoteUserDialInStateCapabilities,
       "DellRemoteUserDialInStateSettings": DellRemoteUserDialInStateSettings,
       "DellRemoteDialOutStateCapabilities": DellRemoteDialOutStateCapabilities,
       "DellRemoteDialOutStateSettings": DellRemoteDialOutStateSettings,
       "dell": dell,
       "server3": server3,
       "baseboardGroup": baseboardGroup,
       "remoteAccessGroup": remoteAccessGroup,
       "remoteAccessTable": remoteAccessTable,
       "remoteAccessTableEntry": remoteAccessTableEntry,
       "remoteAccessChassisIndex": remoteAccessChassisIndex,
       "remoteAccessAdapterIndex": remoteAccessAdapterIndex,
       "remoteAccessType": remoteAccessType,
       "remoteAccessStateCapabilities": remoteAccessStateCapabilities,
       "remoteAccessStateSettings": remoteAccessStateSettings,
       "remoteAccessStatus": remoteAccessStatus,
       "remoteAccessProductInfoName": remoteAccessProductInfoName,
       "remoteAccessDescriptionInfoName": remoteAccessDescriptionInfoName,
       "remoteAccessVersionInfoName": remoteAccessVersionInfoName,
       "remoteAccessControlCapabilities": remoteAccessControlCapabilities,
       "remoteAccessControlSettings": remoteAccessControlSettings,
       "remoteAccessMonitorCapabilities": remoteAccessMonitorCapabilities,
       "remoteAccessMonitorSettings": remoteAccessMonitorSettings,
       "remoteAccessLANCapabilities": remoteAccessLANCapabilities,
       "remoteAccessLANSettings": remoteAccessLANSettings,
       "remoteAccessHostCapabilities": remoteAccessHostCapabilities,
       "remoteAccessHostSettings": remoteAccessHostSettings,
       "remoteAccessOutOfBandSNMPCapabilities": remoteAccessOutOfBandSNMPCapabilities,
       "remoteAccessOutOfBandSNMPSettings": remoteAccessOutOfBandSNMPSettings,
       "remoteAccessSMTPServerIPAddress": remoteAccessSMTPServerIPAddress,
       "remoteAccessFloppyTFTPIPAddress": remoteAccessFloppyTFTPIPAddress,
       "remoteAccessFloppyTFTPPathName": remoteAccessFloppyTFTPPathName,
       "remoteAccessFirmwareUpdateIPAddress": remoteAccessFirmwareUpdateIPAddress,
       "remoteAccessFirmwareUpdatePathName": remoteAccessFirmwareUpdatePathName,
       "remoteAccessNICStaticIPAddress": remoteAccessNICStaticIPAddress,
       "remoteAccessNICStaticNetmaskAddress": remoteAccessNICStaticNetmaskAddress,
       "remoteAccessNICStaticGatewayAddress": remoteAccessNICStaticGatewayAddress,
       "remoteAccessPCMCIAInfoName": remoteAccessPCMCIAInfoName,
       "remoteAccessMiscInfoName": remoteAccessMiscInfoName,
       "remoteAccessNICCurrentIPAddress": remoteAccessNICCurrentIPAddress,
       "remoteAccessNICCurrentNetmaskAddress": remoteAccessNICCurrentNetmaskAddress,
       "remoteAccessNICCurrentGatewayAddress": remoteAccessNICCurrentGatewayAddress,
       "remoteAccessNICCurrentInfoFromDHCP": remoteAccessNICCurrentInfoFromDHCP,
       "remoteAccessRemoteConnectURL": remoteAccessRemoteConnectURL,
       "remoteUserAdminTable": remoteUserAdminTable,
       "remoteUserAdminTableEntry": remoteUserAdminTableEntry,
       "remoteUserAdminChassisIndex": remoteUserAdminChassisIndex,
       "remoteUserAdminAdapterIndex": remoteUserAdminAdapterIndex,
       "remoteUserAdminUserIndex": remoteUserAdminUserIndex,
       "remoteUserAdminStateCapabilities": remoteUserAdminStateCapabilities,
       "remoteUserAdminStateSettings": remoteUserAdminStateSettings,
       "remoteUserAdminStatus": remoteUserAdminStatus,
       "remoteUserAdminUserName": remoteUserAdminUserName,
       "remoteUserAdminUserPasswordName": remoteUserAdminUserPasswordName,
       "remoteUserAdminUserPrivilege": remoteUserAdminUserPrivilege,
       "remoteUserAdminUserPrivilegeCapabilities": remoteUserAdminUserPrivilegeCapabilities,
       "remoteUserAdminAlertFilterDrsEventsMask": remoteUserAdminAlertFilterDrsEventsMask,
       "remoteUserAdminAlertFilterSysEventsMask": remoteUserAdminAlertFilterSysEventsMask,
       "remoteUserAdminAlertFilterDrsCapabilities": remoteUserAdminAlertFilterDrsCapabilities,
       "remoteUserAdminAlertFilterSysCapabilities": remoteUserAdminAlertFilterSysCapabilities,
       "remoteUserAdminPagerNumericNumberName": remoteUserAdminPagerNumericNumberName,
       "remoteUserAdminPagerNumericMessageName": remoteUserAdminPagerNumericMessageName,
       "remoteUserAdminPagerNumericHangupDelay": remoteUserAdminPagerNumericHangupDelay,
       "remoteUserAdminPagerAlphaPhoneNumberName": remoteUserAdminPagerAlphaPhoneNumberName,
       "remoteUserAdminPagerAlphaProtocol": remoteUserAdminPagerAlphaProtocol,
       "remoteUserAdminPagerAlphaBaudRate": remoteUserAdminPagerAlphaBaudRate,
       "remoteUserAdminPagerAlphaCustomMessageName": remoteUserAdminPagerAlphaCustomMessageName,
       "remoteUserAdminPagerAlphaModemConnectTimeout": remoteUserAdminPagerAlphaModemConnectTimeout,
       "remoteUserAdminPagerAlphaPagerIdName": remoteUserAdminPagerAlphaPagerIdName,
       "remoteUserAdminPagerAlphaPasswordName": remoteUserAdminPagerAlphaPasswordName,
       "remoteUserAdminPagerModemInitStringName": remoteUserAdminPagerModemInitStringName,
       "remoteUserAdminPagerModemPort": remoteUserAdminPagerModemPort,
       "remoteUserAdminEmailAddressName": remoteUserAdminEmailAddressName,
       "remoteUserAdminEmailCustomMessageName": remoteUserAdminEmailCustomMessageName,
       "remoteUserAdminControlCapabilities": remoteUserAdminControlCapabilities,
       "remoteUserAdminControlSettings": remoteUserAdminControlSettings,
       "remoteUserAdminUserType": remoteUserAdminUserType,
       "remoteSNMPTrapTable": remoteSNMPTrapTable,
       "remoteSNMPTrapTableEntry": remoteSNMPTrapTableEntry,
       "remoteSNMPTrapChassisIndex": remoteSNMPTrapChassisIndex,
       "remoteSNMPTrapAdapterIndex": remoteSNMPTrapAdapterIndex,
       "remoteSNMPTrapIndex": remoteSNMPTrapIndex,
       "remoteSNMPTrapStateCapabilities": remoteSNMPTrapStateCapabilities,
       "remoteSNMPTrapStateSettings": remoteSNMPTrapStateSettings,
       "remoteSNMPTrapStatus": remoteSNMPTrapStatus,
       "remoteSNMPTrapDestinationIPAddress": remoteSNMPTrapDestinationIPAddress,
       "remoteSNMPTrapSNMPCommunityName": remoteSNMPTrapSNMPCommunityName,
       "remoteSNMPTrapFilterDrsEventsMask": remoteSNMPTrapFilterDrsEventsMask,
       "remoteSNMPTrapFilterSysEventsMask": remoteSNMPTrapFilterSysEventsMask,
       "remoteSNMPTrapFilterDrsCapabilities": remoteSNMPTrapFilterDrsCapabilities,
       "remoteSNMPTrapFilterSysCapabilities": remoteSNMPTrapFilterSysCapabilities,
       "remoteSNMPTrapControlCapabilities": remoteSNMPTrapControlCapabilities,
       "remoteSNMPTrapControlSettings": remoteSNMPTrapControlSettings,
       "remoteDialUpTable": remoteDialUpTable,
       "remoteDialUpTableEntry": remoteDialUpTableEntry,
       "remoteDialUpChassisIndex": remoteDialUpChassisIndex,
       "remoteDialUpAdapterIndex": remoteDialUpAdapterIndex,
       "remoteDialUpIndex": remoteDialUpIndex,
       "remoteDialUpStateCapabilities": remoteDialUpStateCapabilities,
       "remoteDialUpStateSettings": remoteDialUpStateSettings,
       "remoteDialUpStatus": remoteDialUpStatus,
       "remoteDialUpPPPDialInBaseIPAddress": remoteDialUpPPPDialInBaseIPAddress,
       "remoteDialUpPPPDialInIdleTimeout": remoteDialUpPPPDialInIdleTimeout,
       "remoteDialUpPPPDialInMaxConnectTimeout": remoteDialUpPPPDialInMaxConnectTimeout,
       "remoteDialUpDialOutModemConnectTimeout": remoteDialUpDialOutModemConnectTimeout,
       "remoteDialUpModemDialType": remoteDialUpModemDialType,
       "remoteDialUpModemInitStringName": remoteDialUpModemInitStringName,
       "remoteDialUpModemBaudRate": remoteDialUpModemBaudRate,
       "remoteDialUpModemPort": remoteDialUpModemPort,
       "remoteUserDialInCfgTable": remoteUserDialInCfgTable,
       "remoteUserDialInCfgTableEntry": remoteUserDialInCfgTableEntry,
       "remoteUserDialInCfgChassisIndex": remoteUserDialInCfgChassisIndex,
       "remoteUserDialInCfgAdapterIndex": remoteUserDialInCfgAdapterIndex,
       "remoteUserDialInCfgUserIndex": remoteUserDialInCfgUserIndex,
       "remoteUserDialInCfgStateCapabilities": remoteUserDialInCfgStateCapabilities,
       "remoteUserDialInCfgStateSettings": remoteUserDialInCfgStateSettings,
       "remoteUserDialInCfgStatus": remoteUserDialInCfgStatus,
       "remoteUserDialInCfgPPPUserName": remoteUserDialInCfgPPPUserName,
       "remoteUserDialInCfgPPPUserPasswordName": remoteUserDialInCfgPPPUserPasswordName,
       "remoteUserDialInCfgCallbackPhoneNumberName": remoteUserDialInCfgCallbackPhoneNumberName,
       "remoteDialOutTable": remoteDialOutTable,
       "remoteDialOutTableEntry": remoteDialOutTableEntry,
       "remoteDialOutChassisIndex": remoteDialOutChassisIndex,
       "remoteDialOutAdapterIndex": remoteDialOutAdapterIndex,
       "remoteDialOutDialOutIndex": remoteDialOutDialOutIndex,
       "remoteDialOutStateCapabilities": remoteDialOutStateCapabilities,
       "remoteDialOutStateSettings": remoteDialOutStateSettings,
       "remoteDialOutStatus": remoteDialOutStatus,
       "remoteDialOutIPAddress": remoteDialOutIPAddress,
       "remoteDialOutPhoneNumberName": remoteDialOutPhoneNumberName,
       "remoteDialOutPPPUserName": remoteDialOutPPPUserName,
       "remoteDialOutPPPPasswordName": remoteDialOutPPPPasswordName,
       "drsOutOfBandGroup": drsOutOfBandGroup}
)
