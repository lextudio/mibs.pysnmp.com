# SNMP MIB module (ADTRAN-AOS-DESKTOP-AUDITING) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOS-DESKTOP-AUDITING
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:04 2024
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

(adGenAOSConformance,
 adGenAOSSwitch) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSConformance",
    "adGenAOSSwitch")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

adGenAOSDesktopAuditingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenDesktopAuditing_ObjectIdentity = ObjectIdentity
adGenDesktopAuditing = _AdGenDesktopAuditing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2)
)
_AdGenNapClients_ObjectIdentity = ObjectIdentity
adGenNapClients = _AdGenNapClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0)
)
_AdGenNapClientsTable_Object = MibTable
adGenNapClientsTable = _AdGenNapClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1)
)
if mibBuilder.loadTexts:
    adGenNapClientsTable.setStatus("current")
_AdGenNapClientsEntry_Object = MibTableRow
adGenNapClientsEntry = _AdGenNapClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1)
)
adGenNapClientsEntry.setIndexNames(
    (0, "ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientMac"),
    (0, "ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientVlanId"),
)
if mibBuilder.loadTexts:
    adGenNapClientsEntry.setStatus("current")
_AdNapClientMac_Type = DisplayString
_AdNapClientMac_Object = MibTableColumn
adNapClientMac = _AdNapClientMac_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 1),
    _AdNapClientMac_Type()
)
adNapClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientMac.setStatus("current")
_AdNapClientVlanId_Type = Unsigned32
_AdNapClientVlanId_Object = MibTableColumn
adNapClientVlanId = _AdNapClientVlanId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 2),
    _AdNapClientVlanId_Type()
)
adNapClientVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientVlanId.setStatus("current")
_AdNapClientIp_Type = DisplayString
_AdNapClientIp_Object = MibTableColumn
adNapClientIp = _AdNapClientIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 3),
    _AdNapClientIp_Type()
)
adNapClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientIp.setStatus("current")
_AdNapClientHostname_Type = DisplayString
_AdNapClientHostname_Object = MibTableColumn
adNapClientHostname = _AdNapClientHostname_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 4),
    _AdNapClientHostname_Type()
)
adNapClientHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientHostname.setStatus("current")
_AdNapClientSrcPortIfId_Type = Unsigned32
_AdNapClientSrcPortIfId_Object = MibTableColumn
adNapClientSrcPortIfId = _AdNapClientSrcPortIfId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 5),
    _AdNapClientSrcPortIfId_Type()
)
adNapClientSrcPortIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientSrcPortIfId.setStatus("current")
_AdNapClientSrcPortIfType_Type = Unsigned32
_AdNapClientSrcPortIfType_Object = MibTableColumn
adNapClientSrcPortIfType = _AdNapClientSrcPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 6),
    _AdNapClientSrcPortIfType_Type()
)
adNapClientSrcPortIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientSrcPortIfType.setStatus("current")
_AdNapServerMac_Type = DisplayString
_AdNapServerMac_Object = MibTableColumn
adNapServerMac = _AdNapServerMac_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 7),
    _AdNapServerMac_Type()
)
adNapServerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapServerMac.setStatus("current")
_AdNapServerIp_Type = DisplayString
_AdNapServerIp_Object = MibTableColumn
adNapServerIp = _AdNapServerIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 8),
    _AdNapServerIp_Type()
)
adNapServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapServerIp.setStatus("current")
_AdNapCollectionMethod_Type = Unsigned32
_AdNapCollectionMethod_Object = MibTableColumn
adNapCollectionMethod = _AdNapCollectionMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 9),
    _AdNapCollectionMethod_Type()
)
adNapCollectionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapCollectionMethod.setStatus("current")
_AdNapCollectionTime_Type = DisplayString
_AdNapCollectionTime_Object = MibTableColumn
adNapCollectionTime = _AdNapCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 10),
    _AdNapCollectionTime_Type()
)
adNapCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapCollectionTime.setStatus("current")
_AdNapCapableClient_Type = TruthValue
_AdNapCapableClient_Object = MibTableColumn
adNapCapableClient = _AdNapCapableClient_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 11),
    _AdNapCapableClient_Type()
)
adNapCapableClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapCapableClient.setStatus("current")
_AdNapCapableServer_Type = TruthValue
_AdNapCapableServer_Object = MibTableColumn
adNapCapableServer = _AdNapCapableServer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 12),
    _AdNapCapableServer_Type()
)
adNapCapableServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapCapableServer.setStatus("current")
_AdNapClientOsVersion_Type = DisplayString
_AdNapClientOsVersion_Object = MibTableColumn
adNapClientOsVersion = _AdNapClientOsVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 13),
    _AdNapClientOsVersion_Type()
)
adNapClientOsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientOsVersion.setStatus("current")
_AdNapClientOsServicePk_Type = DisplayString
_AdNapClientOsServicePk_Object = MibTableColumn
adNapClientOsServicePk = _AdNapClientOsServicePk_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 14),
    _AdNapClientOsServicePk_Type()
)
adNapClientOsServicePk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientOsServicePk.setStatus("current")
_AdNapClientOsProcessorArc_Type = DisplayString
_AdNapClientOsProcessorArc_Object = MibTableColumn
adNapClientOsProcessorArc = _AdNapClientOsProcessorArc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 15),
    _AdNapClientOsProcessorArc_Type()
)
adNapClientOsProcessorArc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientOsProcessorArc.setStatus("current")
_AdNapClientLastSecurityUpdate_Type = DisplayString
_AdNapClientLastSecurityUpdate_Object = MibTableColumn
adNapClientLastSecurityUpdate = _AdNapClientLastSecurityUpdate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 16),
    _AdNapClientLastSecurityUpdate_Type()
)
adNapClientLastSecurityUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientLastSecurityUpdate.setStatus("current")
_AdNapClientSecurityUpdateServer_Type = DisplayString
_AdNapClientSecurityUpdateServer_Object = MibTableColumn
adNapClientSecurityUpdateServer = _AdNapClientSecurityUpdateServer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 17),
    _AdNapClientSecurityUpdateServer_Type()
)
adNapClientSecurityUpdateServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientSecurityUpdateServer.setStatus("current")


class _AdNapClientRequiresRemediation_Type(Integer32):
    """Custom type adNapClientRequiresRemediation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("true", 2),
          ("unknown", 1))
    )


_AdNapClientRequiresRemediation_Type.__name__ = "Integer32"
_AdNapClientRequiresRemediation_Object = MibTableColumn
adNapClientRequiresRemediation = _AdNapClientRequiresRemediation_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 18),
    _AdNapClientRequiresRemediation_Type()
)
adNapClientRequiresRemediation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientRequiresRemediation.setStatus("current")
_AdNapClientLocalPolicyViolator_Type = TruthValue
_AdNapClientLocalPolicyViolator_Object = MibTableColumn
adNapClientLocalPolicyViolator = _AdNapClientLocalPolicyViolator_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 19),
    _AdNapClientLocalPolicyViolator_Type()
)
adNapClientLocalPolicyViolator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientLocalPolicyViolator.setStatus("current")


class _AdNapClientFirewallState_Type(Integer32):
    """Custom type adNapClientFirewallState based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("enaNotUTDNotSn", 11),
          ("enaNotUTDSn", 9),
          ("enaUTDNotSn", 15),
          ("enaUTDSn", 13),
          ("micsftEnaNotUTDNotSn", 12),
          ("micsftEnaNotUTDSn", 10),
          ("micsftEnaUTDNotSn", 16),
          ("micsftEnaUTDSn", 14),
          ("micsftNotEnaNotUTD", 6),
          ("micsftNotEnaUTD", 8),
          ("notEnaNotUTD", 5),
          ("notEnaUTD", 7),
          ("notInstalled", 2),
          ("unknown", 1),
          ("wscNotStarted", 4),
          ("wscServiceDown", 3))
    )


_AdNapClientFirewallState_Type.__name__ = "Integer32"
_AdNapClientFirewallState_Object = MibTableColumn
adNapClientFirewallState = _AdNapClientFirewallState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 20),
    _AdNapClientFirewallState_Type()
)
adNapClientFirewallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientFirewallState.setStatus("current")
_AdNapClientFirewall_Type = DisplayString
_AdNapClientFirewall_Object = MibTableColumn
adNapClientFirewall = _AdNapClientFirewall_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 21),
    _AdNapClientFirewall_Type()
)
adNapClientFirewall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientFirewall.setStatus("current")


class _AdNapClientAntivirusState_Type(Integer32):
    """Custom type adNapClientAntivirusState based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("enaNotUTDNotSn", 11),
          ("enaNotUTDSn", 9),
          ("enaUTDNotSn", 15),
          ("enaUTDSn", 13),
          ("micsftEnaNotUTDNotSn", 12),
          ("micsftEnaNotUTDSn", 10),
          ("micsftEnaUTDNotSn", 16),
          ("micsftEnaUTDSn", 14),
          ("micsftNotEnaNotUTD", 6),
          ("micsftNotEnaUTD", 8),
          ("notEnaNotUTD", 5),
          ("notEnaUTD", 7),
          ("notInstalled", 2),
          ("unknown", 1),
          ("wscNotStarted", 4),
          ("wscServiceDown", 3))
    )


_AdNapClientAntivirusState_Type.__name__ = "Integer32"
_AdNapClientAntivirusState_Object = MibTableColumn
adNapClientAntivirusState = _AdNapClientAntivirusState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 22),
    _AdNapClientAntivirusState_Type()
)
adNapClientAntivirusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientAntivirusState.setStatus("current")
_AdNapClientAntivirus_Type = DisplayString
_AdNapClientAntivirus_Object = MibTableColumn
adNapClientAntivirus = _AdNapClientAntivirus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 23),
    _AdNapClientAntivirus_Type()
)
adNapClientAntivirus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientAntivirus.setStatus("current")


class _AdNapClientAntispywareState_Type(Integer32):
    """Custom type adNapClientAntispywareState based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("enaNotUTDNotSn", 11),
          ("enaNotUTDSn", 9),
          ("enaUTDNotSn", 15),
          ("enaUTDSn", 13),
          ("micsftEnaNotUTDNotSn", 12),
          ("micsftEnaNotUTDSn", 10),
          ("micsftEnaUTDNotSn", 16),
          ("micsftEnaUTDSn", 14),
          ("micsftNotEnaNotUTD", 6),
          ("micsftNotEnaUTD", 8),
          ("notEnaNotUTD", 5),
          ("notEnaUTD", 7),
          ("notInstalled", 2),
          ("unknown", 1),
          ("wscNotStarted", 4),
          ("wscServiceDown", 3))
    )


_AdNapClientAntispywareState_Type.__name__ = "Integer32"
_AdNapClientAntispywareState_Object = MibTableColumn
adNapClientAntispywareState = _AdNapClientAntispywareState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 24),
    _AdNapClientAntispywareState_Type()
)
adNapClientAntispywareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientAntispywareState.setStatus("current")
_AdNapClientAntispyware_Type = DisplayString
_AdNapClientAntispyware_Object = MibTableColumn
adNapClientAntispyware = _AdNapClientAntispyware_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 25),
    _AdNapClientAntispyware_Type()
)
adNapClientAntispyware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientAntispyware.setStatus("current")


class _AdNapClientAutoupdateState_Type(Integer32):
    """Custom type adNapClientAutoupdateState based on Integer32"""
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
        *(("enaCkUpdateOnly", 6),
          ("enaDownload", 7),
          ("enaDownloadInstall", 8),
          ("neverConfigured", 9),
          ("notEna", 5),
          ("notInstalled", 2),
          ("unknown", 1),
          ("wscNotStarted", 4),
          ("wscServiceDown", 3))
    )


_AdNapClientAutoupdateState_Type.__name__ = "Integer32"
_AdNapClientAutoupdateState_Object = MibTableColumn
adNapClientAutoupdateState = _AdNapClientAutoupdateState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 26),
    _AdNapClientAutoupdateState_Type()
)
adNapClientAutoupdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientAutoupdateState.setStatus("current")


class _AdNapClientSecurityupdateState_Type(Integer32):
    """Custom type adNapClientSecurityupdateState based on Integer32"""
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
        *(("missingUpdate", 3),
          ("noClientID", 5),
          ("noMissingUpdate", 2),
          ("noWUS", 4),
          ("unknown", 1),
          ("updateInsNeedReboot", 8),
          ("wuaCommFailed", 7),
          ("wuaNotStarted", 9),
          ("wuaServiceDisabled", 6))
    )


_AdNapClientSecurityupdateState_Type.__name__ = "Integer32"
_AdNapClientSecurityupdateState_Object = MibTableColumn
adNapClientSecurityupdateState = _AdNapClientSecurityupdateState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 27),
    _AdNapClientSecurityupdateState_Type()
)
adNapClientSecurityupdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientSecurityupdateState.setStatus("current")


class _AdNapClientSecuritySeverity_Type(Integer32):
    """Custom type adNapClientSecuritySeverity based on Integer32"""
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
        *(("critical", 6),
          ("important", 5),
          ("low", 3),
          ("moderate", 4),
          ("unknown", 1),
          ("unspecified", 2))
    )


_AdNapClientSecuritySeverity_Type.__name__ = "Integer32"
_AdNapClientSecuritySeverity_Object = MibTableColumn
adNapClientSecuritySeverity = _AdNapClientSecuritySeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 28),
    _AdNapClientSecuritySeverity_Type()
)
adNapClientSecuritySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientSecuritySeverity.setStatus("current")


class _AdNapClientConnectionState_Type(Integer32):
    """Custom type adNapClientConnectionState based on Integer32"""
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
        *(("notResMaybeLater", 3),
          ("notRestricted", 2),
          ("restricted", 4),
          ("unknown", 1))
    )


_AdNapClientConnectionState_Type.__name__ = "Integer32"
_AdNapClientConnectionState_Object = MibTableColumn
adNapClientConnectionState = _AdNapClientConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 29),
    _AdNapClientConnectionState_Type()
)
adNapClientConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNapClientConnectionState.setStatus("current")
_AdGenAOSDesktopAuditingConformance_ObjectIdentity = ObjectIdentity
adGenAOSDesktopAuditingConformance = _AdGenAOSDesktopAuditingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10)
)
_AdGenAOSDesktopAuditingGroups_ObjectIdentity = ObjectIdentity
adGenAOSDesktopAuditingGroups = _AdGenAOSDesktopAuditingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 1)
)
_AdGenAOSDesktopAuditingCompliances_ObjectIdentity = ObjectIdentity
adGenAOSDesktopAuditingCompliances = _AdGenAOSDesktopAuditingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 2)
)

# Managed Objects groups

adGenNapClientsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 1, 1)
)
adGenNapClientsGroup.setObjects(
      *(("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientMac"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientVlanId"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientIp"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientHostname"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientSrcPortIfId"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientSrcPortIfType"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapServerMac"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapServerIp"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapCollectionMethod"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapCollectionTime"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapCapableClient"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapCapableServer"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientOsVersion"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientOsServicePk"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientOsProcessorArc"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientLastSecurityUpdate"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientSecurityUpdateServer"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientRequiresRemediation"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientLocalPolicyViolator"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientFirewallState"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientFirewall"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientAntivirusState"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientAntivirus"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientAntispywareState"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientAntispyware"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientAutoupdateState"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientSecurityupdateState"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientSecuritySeverity"),
        ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientConnectionState"))
)
if mibBuilder.loadTexts:
    adGenNapClientsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenAOSDesktopAuditingFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAOSDesktopAuditingFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-DESKTOP-AUDITING",
    **{"adGenDesktopAuditing": adGenDesktopAuditing,
       "adGenNapClients": adGenNapClients,
       "adGenNapClientsTable": adGenNapClientsTable,
       "adGenNapClientsEntry": adGenNapClientsEntry,
       "adNapClientMac": adNapClientMac,
       "adNapClientVlanId": adNapClientVlanId,
       "adNapClientIp": adNapClientIp,
       "adNapClientHostname": adNapClientHostname,
       "adNapClientSrcPortIfId": adNapClientSrcPortIfId,
       "adNapClientSrcPortIfType": adNapClientSrcPortIfType,
       "adNapServerMac": adNapServerMac,
       "adNapServerIp": adNapServerIp,
       "adNapCollectionMethod": adNapCollectionMethod,
       "adNapCollectionTime": adNapCollectionTime,
       "adNapCapableClient": adNapCapableClient,
       "adNapCapableServer": adNapCapableServer,
       "adNapClientOsVersion": adNapClientOsVersion,
       "adNapClientOsServicePk": adNapClientOsServicePk,
       "adNapClientOsProcessorArc": adNapClientOsProcessorArc,
       "adNapClientLastSecurityUpdate": adNapClientLastSecurityUpdate,
       "adNapClientSecurityUpdateServer": adNapClientSecurityUpdateServer,
       "adNapClientRequiresRemediation": adNapClientRequiresRemediation,
       "adNapClientLocalPolicyViolator": adNapClientLocalPolicyViolator,
       "adNapClientFirewallState": adNapClientFirewallState,
       "adNapClientFirewall": adNapClientFirewall,
       "adNapClientAntivirusState": adNapClientAntivirusState,
       "adNapClientAntivirus": adNapClientAntivirus,
       "adNapClientAntispywareState": adNapClientAntispywareState,
       "adNapClientAntispyware": adNapClientAntispyware,
       "adNapClientAutoupdateState": adNapClientAutoupdateState,
       "adNapClientSecurityupdateState": adNapClientSecurityupdateState,
       "adNapClientSecuritySeverity": adNapClientSecuritySeverity,
       "adNapClientConnectionState": adNapClientConnectionState,
       "adGenAOSDesktopAuditingConformance": adGenAOSDesktopAuditingConformance,
       "adGenAOSDesktopAuditingGroups": adGenAOSDesktopAuditingGroups,
       "adGenNapClientsGroup": adGenNapClientsGroup,
       "adGenAOSDesktopAuditingCompliances": adGenAOSDesktopAuditingCompliances,
       "adGenAOSDesktopAuditingFullCompliance": adGenAOSDesktopAuditingFullCompliance,
       "adGenAOSDesktopAuditingMib": adGenAOSDesktopAuditingMib}
)
