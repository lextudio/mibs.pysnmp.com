# SNMP MIB module (ACTONA-ACTASTOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACTONA-ACTASTOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:40 2024
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

actona = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17471)
)
actona.setRevisions(
        ("2010-07-30 00:00",
         "2004-12-23 00:00",
         "2003-11-24 16:10")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcNotifications_ObjectIdentity = ObjectIdentity
acNotifications = _AcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 0)
)
_Actastor_ObjectIdentity = ObjectIdentity
actastor = _Actastor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1)
)
if mibBuilder.loadTexts:
    actastor.setStatus("current")
_GeneralInformation_ObjectIdentity = ObjectIdentity
generalInformation = _GeneralInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 1)
)
if mibBuilder.loadTexts:
    generalInformation.setStatus("current")
_ActastorVersion_Type = OctetString
_ActastorVersion_Object = MibScalar
actastorVersion = _ActastorVersion_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 1, 1),
    _ActastorVersion_Type()
)
actastorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actastorVersion.setStatus("current")
_BuildString_Type = OctetString
_BuildString_Object = MibScalar
buildString = _BuildString_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 1, 2),
    _BuildString_Type()
)
buildString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buildString.setStatus("current")
_Support_ObjectIdentity = ObjectIdentity
support = _Support_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 1, 3)
)
if mibBuilder.loadTexts:
    support.setStatus("current")
_Email_Type = OctetString
_Email_Object = MibScalar
email = _Email_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 1, 3, 1),
    _Email_Type()
)
email.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    email.setStatus("current")
_License_ObjectIdentity = ObjectIdentity
license = _License_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 1, 4)
)
if mibBuilder.loadTexts:
    license.setStatus("current")


class _IsValid_Type(Integer32):
    """Custom type isValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_IsValid_Type.__name__ = "Integer32"
_IsValid_Object = MibScalar
isValid = _IsValid_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 1, 4, 1),
    _IsValid_Type()
)
isValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isValid.setStatus("current")


class _DaysLeft_Type(Integer32):
    """Custom type daysLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_DaysLeft_Type.__name__ = "Integer32"
_DaysLeft_Object = MibScalar
daysLeft = _DaysLeft_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 1, 4, 2),
    _DaysLeft_Type()
)
daysLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daysLeft.setStatus("current")
if mibBuilder.loadTexts:
    daysLeft.setUnits("days (99999 is unlimited license)")
_Manager_ObjectIdentity = ObjectIdentity
manager = _Manager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 2)
)
if mibBuilder.loadTexts:
    manager.setStatus("current")
_MgrCentralServerHost_Type = OctetString
_MgrCentralServerHost_Object = MibScalar
mgrCentralServerHost = _MgrCentralServerHost_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 2, 1),
    _MgrCentralServerHost_Type()
)
mgrCentralServerHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgrCentralServerHost.setStatus("current")
_CoreServer_ObjectIdentity = ObjectIdentity
coreServer = _CoreServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3)
)
if mibBuilder.loadTexts:
    coreServer.setStatus("current")
_CsGeneral_ObjectIdentity = ObjectIdentity
csGeneral = _CsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 1)
)
if mibBuilder.loadTexts:
    csGeneral.setStatus("current")


class _CsIsConfigured_Type(Integer32):
    """Custom type csIsConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CsIsConfigured_Type.__name__ = "Integer32"
_CsIsConfigured_Object = MibScalar
csIsConfigured = _CsIsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 1, 1),
    _CsIsConfigured_Type()
)
csIsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csIsConfigured.setStatus("current")


class _CsIsAlive_Type(Integer32):
    """Custom type csIsAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CsIsAlive_Type.__name__ = "Integer32"
_CsIsAlive_Object = MibScalar
csIsAlive = _CsIsAlive_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 1, 2),
    _CsIsAlive_Type()
)
csIsAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csIsAlive.setStatus("current")
_CsUpTime_Type = TimeTicks
_CsUpTime_Object = MibScalar
csUpTime = _CsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 1, 3),
    _CsUpTime_Type()
)
csUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csUpTime.setStatus("current")
_CsState_ObjectIdentity = ObjectIdentity
csState = _CsState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2)
)
if mibBuilder.loadTexts:
    csState.setStatus("current")
_CsConnectivityTable_Object = MibTable
csConnectivityTable = _CsConnectivityTable_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    csConnectivityTable.setStatus("current")
_CsConnectivityEntry_Object = MibTableRow
csConnectivityEntry = _CsConnectivityEntry_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 1, 1)
)
csConnectivityEntry.setIndexNames(
    (0, "ACTONA-ACTASTOR-MIB", "csConTabIndex"),
)
if mibBuilder.loadTexts:
    csConnectivityEntry.setStatus("current")


class _CsConTabIndex_Type(Integer32):
    """Custom type csConTabIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CsConTabIndex_Type.__name__ = "Integer32"
_CsConTabIndex_Object = MibTableColumn
csConTabIndex = _CsConTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 1, 1, 1),
    _CsConTabIndex_Type()
)
csConTabIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csConTabIndex.setStatus("current")


class _CsConTabClusterID_Type(Integer32):
    """Custom type csConTabClusterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CsConTabClusterID_Type.__name__ = "Integer32"
_CsConTabClusterID_Object = MibTableColumn
csConTabClusterID = _CsConTabClusterID_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 1, 1, 2),
    _CsConTabClusterID_Type()
)
csConTabClusterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csConTabClusterID.setStatus("current")
_CsConTabClusterName_Type = OctetString
_CsConTabClusterName_Object = MibTableColumn
csConTabClusterName = _CsConTabClusterName_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 1, 1, 3),
    _CsConTabClusterName_Type()
)
csConTabClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csConTabClusterName.setStatus("current")


class _CsConTabIsConnected_Type(Integer32):
    """Custom type csConTabIsConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CsConTabIsConnected_Type.__name__ = "Integer32"
_CsConTabIsConnected_Object = MibTableColumn
csConTabIsConnected = _CsConTabIsConnected_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 1, 1, 4),
    _CsConTabIsConnected_Type()
)
csConTabIsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csConTabIsConnected.setStatus("current")
_CsConTabTotalSentMessages_Type = Counter32
_CsConTabTotalSentMessages_Object = MibTableColumn
csConTabTotalSentMessages = _CsConTabTotalSentMessages_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 1, 1, 5),
    _CsConTabTotalSentMessages_Type()
)
csConTabTotalSentMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csConTabTotalSentMessages.setStatus("current")


class _CsConTabSentCompressionRatio_Type(Integer32):
    """Custom type csConTabSentCompressionRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CsConTabSentCompressionRatio_Type.__name__ = "Integer32"
_CsConTabSentCompressionRatio_Object = MibTableColumn
csConTabSentCompressionRatio = _CsConTabSentCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 1, 1, 6),
    _CsConTabSentCompressionRatio_Type()
)
csConTabSentCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csConTabSentCompressionRatio.setStatus("current")
if mibBuilder.loadTexts:
    csConTabSentCompressionRatio.setUnits("%")
_CsConTabTotalReceivedMessages_Type = Counter32
_CsConTabTotalReceivedMessages_Object = MibTableColumn
csConTabTotalReceivedMessages = _CsConTabTotalReceivedMessages_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 1, 1, 7),
    _CsConTabTotalReceivedMessages_Type()
)
csConTabTotalReceivedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csConTabTotalReceivedMessages.setStatus("current")


class _CsConTabReceivedCompressionRatio_Type(Integer32):
    """Custom type csConTabReceivedCompressionRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CsConTabReceivedCompressionRatio_Type.__name__ = "Integer32"
_CsConTabReceivedCompressionRatio_Object = MibTableColumn
csConTabReceivedCompressionRatio = _CsConTabReceivedCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 1, 1, 8),
    _CsConTabReceivedCompressionRatio_Type()
)
csConTabReceivedCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csConTabReceivedCompressionRatio.setStatus("current")
if mibBuilder.loadTexts:
    csConTabReceivedCompressionRatio.setUnits("%")
_CsConTabTotalSentKBytes_Type = Unsigned32
_CsConTabTotalSentKBytes_Object = MibTableColumn
csConTabTotalSentKBytes = _CsConTabTotalSentKBytes_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 1, 1, 9),
    _CsConTabTotalSentKBytes_Type()
)
csConTabTotalSentKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csConTabTotalSentKBytes.setStatus("current")
if mibBuilder.loadTexts:
    csConTabTotalSentKBytes.setUnits("KB")
_CsConTabTotalReceivedKBytes_Type = Unsigned32
_CsConTabTotalReceivedKBytes_Object = MibTableColumn
csConTabTotalReceivedKBytes = _CsConTabTotalReceivedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 1, 1, 10),
    _CsConTabTotalReceivedKBytes_Type()
)
csConTabTotalReceivedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csConTabTotalReceivedKBytes.setStatus("current")
if mibBuilder.loadTexts:
    csConTabTotalReceivedKBytes.setUnits("KB")
_CsDeviceName_Type = OctetString
_CsDeviceName_Object = MibScalar
csDeviceName = _CsDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 2),
    _CsDeviceName_Type()
)
csDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csDeviceName.setStatus("current")
_CsWINS_Type = OctetString
_CsWINS_Object = MibScalar
csWINS = _CsWINS_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 3),
    _CsWINS_Type()
)
csWINS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csWINS.setStatus("current")
_CsCIFSServersTable_Object = MibTable
csCIFSServersTable = _CsCIFSServersTable_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    csCIFSServersTable.setStatus("current")
_CsCIFSServersEntry_Object = MibTableRow
csCIFSServersEntry = _CsCIFSServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 4, 1)
)
csCIFSServersEntry.setIndexNames(
    (0, "ACTONA-ACTASTOR-MIB", "csCIFSServersTabIndex"),
)
if mibBuilder.loadTexts:
    csCIFSServersEntry.setStatus("current")


class _CsCIFSServersTabIndex_Type(Integer32):
    """Custom type csCIFSServersTabIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CsCIFSServersTabIndex_Type.__name__ = "Integer32"
_CsCIFSServersTabIndex_Object = MibTableColumn
csCIFSServersTabIndex = _CsCIFSServersTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 4, 1, 1),
    _CsCIFSServersTabIndex_Type()
)
csCIFSServersTabIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csCIFSServersTabIndex.setStatus("current")
_CsCIFSServersTabServerName_Type = OctetString
_CsCIFSServersTabServerName_Object = MibTableColumn
csCIFSServersTabServerName = _CsCIFSServersTabServerName_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 4, 1, 2),
    _CsCIFSServersTabServerName_Type()
)
csCIFSServersTabServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csCIFSServersTabServerName.setStatus("current")
_CsNFSServersTable_Object = MibTable
csNFSServersTable = _CsNFSServersTable_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    csNFSServersTable.setStatus("current")
_CsNFSServersEntry_Object = MibTableRow
csNFSServersEntry = _CsNFSServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 5, 1)
)
csNFSServersEntry.setIndexNames(
    (0, "ACTONA-ACTASTOR-MIB", "csNFSServersTabIndex"),
)
if mibBuilder.loadTexts:
    csNFSServersEntry.setStatus("current")


class _CsNFSServersTabIndex_Type(Integer32):
    """Custom type csNFSServersTabIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CsNFSServersTabIndex_Type.__name__ = "Integer32"
_CsNFSServersTabIndex_Object = MibTableColumn
csNFSServersTabIndex = _CsNFSServersTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 5, 1, 1),
    _CsNFSServersTabIndex_Type()
)
csNFSServersTabIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csNFSServersTabIndex.setStatus("current")
_CsNFSServersTabServerName_Type = OctetString
_CsNFSServersTabServerName_Object = MibTableColumn
csNFSServersTabServerName = _CsNFSServersTabServerName_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 5, 1, 2),
    _CsNFSServersTabServerName_Type()
)
csNFSServersTabServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csNFSServersTabServerName.setStatus("current")


class _CsNFSServersTabUseTCP_Type(Integer32):
    """Custom type csNFSServersTabUseTCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CsNFSServersTabUseTCP_Type.__name__ = "Integer32"
_CsNFSServersTabUseTCP_Object = MibTableColumn
csNFSServersTabUseTCP = _CsNFSServersTabUseTCP_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 5, 1, 3),
    _CsNFSServersTabUseTCP_Type()
)
csNFSServersTabUseTCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csNFSServersTabUseTCP.setStatus("current")


class _CsNFSServersTabUseUDP_Type(Integer32):
    """Custom type csNFSServersTabUseUDP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CsNFSServersTabUseUDP_Type.__name__ = "Integer32"
_CsNFSServersTabUseUDP_Object = MibTableColumn
csNFSServersTabUseUDP = _CsNFSServersTabUseUDP_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 2, 5, 1, 4),
    _CsNFSServersTabUseUDP_Type()
)
csNFSServersTabUseUDP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csNFSServersTabUseUDP.setStatus("current")
_EdgeServer_ObjectIdentity = ObjectIdentity
edgeServer = _EdgeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4)
)
if mibBuilder.loadTexts:
    edgeServer.setStatus("current")
_EsGeneral_ObjectIdentity = ObjectIdentity
esGeneral = _EsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 1)
)
if mibBuilder.loadTexts:
    esGeneral.setStatus("current")


class _EsIsConfigured_Type(Integer32):
    """Custom type esIsConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_EsIsConfigured_Type.__name__ = "Integer32"
_EsIsConfigured_Object = MibScalar
esIsConfigured = _EsIsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 1, 1),
    _EsIsConfigured_Type()
)
esIsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIsConfigured.setStatus("current")


class _EsIsAlive_Type(Integer32):
    """Custom type esIsAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_EsIsAlive_Type.__name__ = "Integer32"
_EsIsAlive_Object = MibScalar
esIsAlive = _EsIsAlive_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 1, 2),
    _EsIsAlive_Type()
)
esIsAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIsAlive.setStatus("current")
_EsUpTime_Type = TimeTicks
_EsUpTime_Object = MibScalar
esUpTime = _EsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 1, 3),
    _EsUpTime_Type()
)
esUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esUpTime.setStatus("current")
_EsState_ObjectIdentity = ObjectIdentity
esState = _EsState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2)
)
if mibBuilder.loadTexts:
    esState.setStatus("current")
_EsConnectivityTable_Object = MibTable
esConnectivityTable = _EsConnectivityTable_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    esConnectivityTable.setStatus("current")
_EsConnectivityEntry_Object = MibTableRow
esConnectivityEntry = _EsConnectivityEntry_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 1, 1)
)
esConnectivityEntry.setIndexNames(
    (0, "ACTONA-ACTASTOR-MIB", "esConTabIndex"),
)
if mibBuilder.loadTexts:
    esConnectivityEntry.setStatus("current")


class _EsConTabIndex_Type(Integer32):
    """Custom type esConTabIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_EsConTabIndex_Type.__name__ = "Integer32"
_EsConTabIndex_Object = MibTableColumn
esConTabIndex = _EsConTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 1, 1, 1),
    _EsConTabIndex_Type()
)
esConTabIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    esConTabIndex.setStatus("current")


class _EsConTabClusterID_Type(Integer32):
    """Custom type esConTabClusterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EsConTabClusterID_Type.__name__ = "Integer32"
_EsConTabClusterID_Object = MibTableColumn
esConTabClusterID = _EsConTabClusterID_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 1, 1, 2),
    _EsConTabClusterID_Type()
)
esConTabClusterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esConTabClusterID.setStatus("current")
_EsConTabClusterName_Type = OctetString
_EsConTabClusterName_Object = MibTableColumn
esConTabClusterName = _EsConTabClusterName_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 1, 1, 3),
    _EsConTabClusterName_Type()
)
esConTabClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esConTabClusterName.setStatus("current")


class _EsConTabIsConnected_Type(Integer32):
    """Custom type esConTabIsConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_EsConTabIsConnected_Type.__name__ = "Integer32"
_EsConTabIsConnected_Object = MibTableColumn
esConTabIsConnected = _EsConTabIsConnected_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 1, 1, 4),
    _EsConTabIsConnected_Type()
)
esConTabIsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esConTabIsConnected.setStatus("current")
_EsConTabTotalSentMessages_Type = Counter32
_EsConTabTotalSentMessages_Object = MibTableColumn
esConTabTotalSentMessages = _EsConTabTotalSentMessages_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 1, 1, 5),
    _EsConTabTotalSentMessages_Type()
)
esConTabTotalSentMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esConTabTotalSentMessages.setStatus("current")


class _EsConTabSentCompressionRatio_Type(Integer32):
    """Custom type esConTabSentCompressionRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EsConTabSentCompressionRatio_Type.__name__ = "Integer32"
_EsConTabSentCompressionRatio_Object = MibTableColumn
esConTabSentCompressionRatio = _EsConTabSentCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 1, 1, 6),
    _EsConTabSentCompressionRatio_Type()
)
esConTabSentCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esConTabSentCompressionRatio.setStatus("current")
if mibBuilder.loadTexts:
    esConTabSentCompressionRatio.setUnits("%")
_EsConTabTotalReceivedMessages_Type = Counter32
_EsConTabTotalReceivedMessages_Object = MibTableColumn
esConTabTotalReceivedMessages = _EsConTabTotalReceivedMessages_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 1, 1, 7),
    _EsConTabTotalReceivedMessages_Type()
)
esConTabTotalReceivedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esConTabTotalReceivedMessages.setStatus("current")


class _EsConTabReceivedCompressionRatio_Type(Integer32):
    """Custom type esConTabReceivedCompressionRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EsConTabReceivedCompressionRatio_Type.__name__ = "Integer32"
_EsConTabReceivedCompressionRatio_Object = MibTableColumn
esConTabReceivedCompressionRatio = _EsConTabReceivedCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 1, 1, 8),
    _EsConTabReceivedCompressionRatio_Type()
)
esConTabReceivedCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esConTabReceivedCompressionRatio.setStatus("current")
if mibBuilder.loadTexts:
    esConTabReceivedCompressionRatio.setUnits("%")
_EsConTabTotalSentKBytes_Type = Unsigned32
_EsConTabTotalSentKBytes_Object = MibTableColumn
esConTabTotalSentKBytes = _EsConTabTotalSentKBytes_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 1, 1, 9),
    _EsConTabTotalSentKBytes_Type()
)
esConTabTotalSentKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esConTabTotalSentKBytes.setStatus("current")
if mibBuilder.loadTexts:
    esConTabTotalSentKBytes.setUnits("KB")
_EsConTabTotalReceivedKBytes_Type = Unsigned32
_EsConTabTotalReceivedKBytes_Object = MibTableColumn
esConTabTotalReceivedKBytes = _EsConTabTotalReceivedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 1, 1, 10),
    _EsConTabTotalReceivedKBytes_Type()
)
esConTabTotalReceivedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esConTabTotalReceivedKBytes.setStatus("current")
if mibBuilder.loadTexts:
    esConTabTotalReceivedKBytes.setUnits("KB")
_EsCIFSInfo_ObjectIdentity = ObjectIdentity
esCIFSInfo = _EsCIFSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    esCIFSInfo.setStatus("current")
_EsTotalBytesRead_Type = Unsigned32
_EsTotalBytesRead_Object = MibScalar
esTotalBytesRead = _EsTotalBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 2, 1),
    _EsTotalBytesRead_Type()
)
esTotalBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esTotalBytesRead.setStatus("current")
if mibBuilder.loadTexts:
    esTotalBytesRead.setUnits("KB")
_EsTotalWrittenBytes_Type = Unsigned32
_EsTotalWrittenBytes_Object = MibScalar
esTotalWrittenBytes = _EsTotalWrittenBytes_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 2, 2),
    _EsTotalWrittenBytes_Type()
)
esTotalWrittenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esTotalWrittenBytes.setStatus("current")
if mibBuilder.loadTexts:
    esTotalWrittenBytes.setUnits("KB")
_EsRemoteRequestCount_Type = Counter32
_EsRemoteRequestCount_Object = MibScalar
esRemoteRequestCount = _EsRemoteRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 2, 3),
    _EsRemoteRequestCount_Type()
)
esRemoteRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esRemoteRequestCount.setStatus("current")
_EsLocalRequestCount_Type = Counter32
_EsLocalRequestCount_Object = MibScalar
esLocalRequestCount = _EsLocalRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 2, 4),
    _EsLocalRequestCount_Type()
)
esLocalRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esLocalRequestCount.setStatus("current")
_EsTotalRemoteTime_Type = TimeTicks
_EsTotalRemoteTime_Object = MibScalar
esTotalRemoteTime = _EsTotalRemoteTime_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 2, 5),
    _EsTotalRemoteTime_Type()
)
esTotalRemoteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esTotalRemoteTime.setStatus("current")
_EsTotalLocalTime_Type = TimeTicks
_EsTotalLocalTime_Object = MibScalar
esTotalLocalTime = _EsTotalLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 2, 6),
    _EsTotalLocalTime_Type()
)
esTotalLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esTotalLocalTime.setStatus("current")


class _EsConnectedSessionCount_Type(Integer32):
    """Custom type esConnectedSessionCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_EsConnectedSessionCount_Type.__name__ = "Integer32"
_EsConnectedSessionCount_Object = MibScalar
esConnectedSessionCount = _EsConnectedSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 2, 7),
    _EsConnectedSessionCount_Type()
)
esConnectedSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esConnectedSessionCount.setStatus("current")


class _EsCifsOpenFiles_Type(Integer32):
    """Custom type esCifsOpenFiles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_EsCifsOpenFiles_Type.__name__ = "Integer32"
_EsCifsOpenFiles_Object = MibScalar
esCifsOpenFiles = _EsCifsOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 2, 8),
    _EsCifsOpenFiles_Type()
)
esCifsOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCifsOpenFiles.setStatus("current")
_EsCacheInfo_ObjectIdentity = ObjectIdentity
esCacheInfo = _EsCacheInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    esCacheInfo.setStatus("current")
_EsMaxCacheVolume_Type = Unsigned32
_EsMaxCacheVolume_Object = MibScalar
esMaxCacheVolume = _EsMaxCacheVolume_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 4, 1),
    _EsMaxCacheVolume_Type()
)
esMaxCacheVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esMaxCacheVolume.setStatus("current")
if mibBuilder.loadTexts:
    esMaxCacheVolume.setUnits("KB")
_EsCurrentCacheVolume_Type = Unsigned32
_EsCurrentCacheVolume_Object = MibScalar
esCurrentCacheVolume = _EsCurrentCacheVolume_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 4, 2),
    _EsCurrentCacheVolume_Type()
)
esCurrentCacheVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCurrentCacheVolume.setStatus("current")
if mibBuilder.loadTexts:
    esCurrentCacheVolume.setUnits("KB")


class _EsMaxCacheResources_Type(Integer32):
    """Custom type esMaxCacheResources based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EsMaxCacheResources_Type.__name__ = "Integer32"
_EsMaxCacheResources_Object = MibScalar
esMaxCacheResources = _EsMaxCacheResources_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 4, 3),
    _EsMaxCacheResources_Type()
)
esMaxCacheResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esMaxCacheResources.setStatus("current")


class _EsCurrentCacheResources_Type(Integer32):
    """Custom type esCurrentCacheResources based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EsCurrentCacheResources_Type.__name__ = "Integer32"
_EsCurrentCacheResources_Object = MibScalar
esCurrentCacheResources = _EsCurrentCacheResources_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 4, 4),
    _EsCurrentCacheResources_Type()
)
esCurrentCacheResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCurrentCacheResources.setStatus("current")
_EsResourceEvictedNum_Type = Counter32
_EsResourceEvictedNum_Object = MibScalar
esResourceEvictedNum = _EsResourceEvictedNum_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 4, 5),
    _EsResourceEvictedNum_Type()
)
esResourceEvictedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esResourceEvictedNum.setStatus("current")
_EsLastEvictedTime_Type = TimeTicks
_EsLastEvictedTime_Object = MibScalar
esLastEvictedTime = _EsLastEvictedTime_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 4, 6),
    _EsLastEvictedTime_Type()
)
esLastEvictedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esLastEvictedTime.setStatus("current")


class _EsVolHiWatermark_Type(Integer32):
    """Custom type esVolHiWatermark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EsVolHiWatermark_Type.__name__ = "Integer32"
_EsVolHiWatermark_Object = MibScalar
esVolHiWatermark = _EsVolHiWatermark_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 4, 7),
    _EsVolHiWatermark_Type()
)
esVolHiWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esVolHiWatermark.setStatus("current")
if mibBuilder.loadTexts:
    esVolHiWatermark.setUnits("%")


class _EsVolLoWatermark_Type(Integer32):
    """Custom type esVolLoWatermark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EsVolLoWatermark_Type.__name__ = "Integer32"
_EsVolLoWatermark_Object = MibScalar
esVolLoWatermark = _EsVolLoWatermark_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 4, 8),
    _EsVolLoWatermark_Type()
)
esVolLoWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esVolLoWatermark.setStatus("current")
if mibBuilder.loadTexts:
    esVolLoWatermark.setUnits("%")


class _EsAmntHiWatermark_Type(Integer32):
    """Custom type esAmntHiWatermark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EsAmntHiWatermark_Type.__name__ = "Integer32"
_EsAmntHiWatermark_Object = MibScalar
esAmntHiWatermark = _EsAmntHiWatermark_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 4, 9),
    _EsAmntHiWatermark_Type()
)
esAmntHiWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAmntHiWatermark.setStatus("current")
if mibBuilder.loadTexts:
    esAmntHiWatermark.setUnits("%")


class _EsAmntLoWatermark_Type(Integer32):
    """Custom type esAmntLoWatermark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EsAmntLoWatermark_Type.__name__ = "Integer32"
_EsAmntLoWatermark_Object = MibScalar
esAmntLoWatermark = _EsAmntLoWatermark_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 4, 10),
    _EsAmntLoWatermark_Type()
)
esAmntLoWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAmntLoWatermark.setStatus("current")
if mibBuilder.loadTexts:
    esAmntLoWatermark.setUnits("%")
_EsEvictedAge_Type = TimeTicks
_EsEvictedAge_Object = MibScalar
esEvictedAge = _EsEvictedAge_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 4, 11),
    _EsEvictedAge_Type()
)
esEvictedAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esEvictedAge.setStatus("current")
_EsEvictedLastAccess_Type = OctetString
_EsEvictedLastAccess_Object = MibScalar
esEvictedLastAccess = _EsEvictedLastAccess_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 2, 4, 12),
    _EsEvictedLastAccess_Type()
)
esEvictedLastAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esEvictedLastAccess.setStatus("current")
_NotificationsInfo_ObjectIdentity = ObjectIdentity
notificationsInfo = _NotificationsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 5)
)
if mibBuilder.loadTexts:
    notificationsInfo.setStatus("current")


class _AcLogSeverity_Type(Integer32):
    """Custom type acLogSeverity based on Integer32"""
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
        *(("debug", 5),
          ("error", 2),
          ("fatal", 1),
          ("info", 4),
          ("warning", 3))
    )


_AcLogSeverity_Type.__name__ = "Integer32"
_AcLogSeverity_Object = MibScalar
acLogSeverity = _AcLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 5, 1),
    _AcLogSeverity_Type()
)
acLogSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogSeverity.setStatus("current")


class _AcLogMsgText_Type(DisplayString):
    """Custom type acLogMsgText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcLogMsgText_Type.__name__ = "DisplayString"
_AcLogMsgText_Object = MibScalar
acLogMsgText = _AcLogMsgText_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 5, 2),
    _AcLogMsgText_Type()
)
acLogMsgText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogMsgText.setStatus("current")
_CifsAO_ObjectIdentity = ObjectIdentity
cifsAO = _CifsAO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6)
)
if mibBuilder.loadTexts:
    cifsAO.setStatus("current")
_CfGeneral_ObjectIdentity = ObjectIdentity
cfGeneral = _CfGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cfGeneral.setStatus("current")


class _CfIsConfigured_Type(Integer32):
    """Custom type cfIsConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CfIsConfigured_Type.__name__ = "Integer32"
_CfIsConfigured_Object = MibScalar
cfIsConfigured = _CfIsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 1, 1),
    _CfIsConfigured_Type()
)
cfIsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfIsConfigured.setStatus("current")


class _CfIsAlive_Type(Integer32):
    """Custom type cfIsAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CfIsAlive_Type.__name__ = "Integer32"
_CfIsAlive_Object = MibScalar
cfIsAlive = _CfIsAlive_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 1, 2),
    _CfIsAlive_Type()
)
cfIsAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfIsAlive.setStatus("current")
_CfUpTime_Type = TimeTicks
_CfUpTime_Object = MibScalar
cfUpTime = _CfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 1, 3),
    _CfUpTime_Type()
)
cfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfUpTime.setStatus("current")
_CfState_ObjectIdentity = ObjectIdentity
cfState = _CfState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cfState.setStatus("current")
_CfCIFSInfo_ObjectIdentity = ObjectIdentity
cfCIFSInfo = _CfCIFSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    cfCIFSInfo.setStatus("current")
_CfTotalBytesRead_Type = Unsigned32
_CfTotalBytesRead_Object = MibScalar
cfTotalBytesRead = _CfTotalBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 1, 1),
    _CfTotalBytesRead_Type()
)
cfTotalBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfTotalBytesRead.setStatus("current")
if mibBuilder.loadTexts:
    cfTotalBytesRead.setUnits("KB")
_CfTotalWrittenBytes_Type = Unsigned32
_CfTotalWrittenBytes_Object = MibScalar
cfTotalWrittenBytes = _CfTotalWrittenBytes_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 1, 2),
    _CfTotalWrittenBytes_Type()
)
cfTotalWrittenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfTotalWrittenBytes.setStatus("current")
if mibBuilder.loadTexts:
    cfTotalWrittenBytes.setUnits("KB")
_CfRemoteRequestCount_Type = Counter32
_CfRemoteRequestCount_Object = MibScalar
cfRemoteRequestCount = _CfRemoteRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 1, 3),
    _CfRemoteRequestCount_Type()
)
cfRemoteRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfRemoteRequestCount.setStatus("current")
_CfLocalRequestCount_Type = Counter32
_CfLocalRequestCount_Object = MibScalar
cfLocalRequestCount = _CfLocalRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 1, 4),
    _CfLocalRequestCount_Type()
)
cfLocalRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfLocalRequestCount.setStatus("current")
_CfTotalRemoteTime_Type = TimeTicks
_CfTotalRemoteTime_Object = MibScalar
cfTotalRemoteTime = _CfTotalRemoteTime_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 1, 5),
    _CfTotalRemoteTime_Type()
)
cfTotalRemoteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfTotalRemoteTime.setStatus("current")
_CfTotalLocalTime_Type = TimeTicks
_CfTotalLocalTime_Object = MibScalar
cfTotalLocalTime = _CfTotalLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 1, 6),
    _CfTotalLocalTime_Type()
)
cfTotalLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfTotalLocalTime.setStatus("current")


class _CfConnectedSessionCount_Type(Integer32):
    """Custom type cfConnectedSessionCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CfConnectedSessionCount_Type.__name__ = "Integer32"
_CfConnectedSessionCount_Object = MibScalar
cfConnectedSessionCount = _CfConnectedSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 1, 7),
    _CfConnectedSessionCount_Type()
)
cfConnectedSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfConnectedSessionCount.setStatus("current")


class _CfCifsOpenFiles_Type(Integer32):
    """Custom type cfCifsOpenFiles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CfCifsOpenFiles_Type.__name__ = "Integer32"
_CfCifsOpenFiles_Object = MibScalar
cfCifsOpenFiles = _CfCifsOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 1, 8),
    _CfCifsOpenFiles_Type()
)
cfCifsOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfCifsOpenFiles.setStatus("current")
_CfCacheInfo_ObjectIdentity = ObjectIdentity
cfCacheInfo = _CfCacheInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    cfCacheInfo.setStatus("current")
_CfMaxCacheVolume_Type = Unsigned32
_CfMaxCacheVolume_Object = MibScalar
cfMaxCacheVolume = _CfMaxCacheVolume_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 2, 1),
    _CfMaxCacheVolume_Type()
)
cfMaxCacheVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfMaxCacheVolume.setStatus("current")
if mibBuilder.loadTexts:
    cfMaxCacheVolume.setUnits("KB")
_CfCurrentCacheVolume_Type = Unsigned32
_CfCurrentCacheVolume_Object = MibScalar
cfCurrentCacheVolume = _CfCurrentCacheVolume_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 2, 2),
    _CfCurrentCacheVolume_Type()
)
cfCurrentCacheVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfCurrentCacheVolume.setStatus("current")
if mibBuilder.loadTexts:
    cfCurrentCacheVolume.setUnits("KB")


class _CfMaxCacheResources_Type(Integer32):
    """Custom type cfMaxCacheResources based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CfMaxCacheResources_Type.__name__ = "Integer32"
_CfMaxCacheResources_Object = MibScalar
cfMaxCacheResources = _CfMaxCacheResources_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 2, 3),
    _CfMaxCacheResources_Type()
)
cfMaxCacheResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfMaxCacheResources.setStatus("current")


class _CfCurrentCacheResources_Type(Integer32):
    """Custom type cfCurrentCacheResources based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CfCurrentCacheResources_Type.__name__ = "Integer32"
_CfCurrentCacheResources_Object = MibScalar
cfCurrentCacheResources = _CfCurrentCacheResources_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 2, 4),
    _CfCurrentCacheResources_Type()
)
cfCurrentCacheResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfCurrentCacheResources.setStatus("current")
_CfResourceEvictedNum_Type = Counter32
_CfResourceEvictedNum_Object = MibScalar
cfResourceEvictedNum = _CfResourceEvictedNum_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 2, 5),
    _CfResourceEvictedNum_Type()
)
cfResourceEvictedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfResourceEvictedNum.setStatus("current")
_CfLastEvictedTime_Type = TimeTicks
_CfLastEvictedTime_Object = MibScalar
cfLastEvictedTime = _CfLastEvictedTime_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 2, 6),
    _CfLastEvictedTime_Type()
)
cfLastEvictedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfLastEvictedTime.setStatus("current")


class _CfVolHiWatermark_Type(Integer32):
    """Custom type cfVolHiWatermark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfVolHiWatermark_Type.__name__ = "Integer32"
_CfVolHiWatermark_Object = MibScalar
cfVolHiWatermark = _CfVolHiWatermark_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 2, 7),
    _CfVolHiWatermark_Type()
)
cfVolHiWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfVolHiWatermark.setStatus("current")
if mibBuilder.loadTexts:
    cfVolHiWatermark.setUnits("%")


class _CfVolLoWatermark_Type(Integer32):
    """Custom type cfVolLoWatermark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfVolLoWatermark_Type.__name__ = "Integer32"
_CfVolLoWatermark_Object = MibScalar
cfVolLoWatermark = _CfVolLoWatermark_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 2, 8),
    _CfVolLoWatermark_Type()
)
cfVolLoWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfVolLoWatermark.setStatus("current")
if mibBuilder.loadTexts:
    cfVolLoWatermark.setUnits("%")


class _CfAmntHiWatermark_Type(Integer32):
    """Custom type cfAmntHiWatermark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfAmntHiWatermark_Type.__name__ = "Integer32"
_CfAmntHiWatermark_Object = MibScalar
cfAmntHiWatermark = _CfAmntHiWatermark_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 2, 9),
    _CfAmntHiWatermark_Type()
)
cfAmntHiWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfAmntHiWatermark.setStatus("current")
if mibBuilder.loadTexts:
    cfAmntHiWatermark.setUnits("%")


class _CfAmntLoWatermark_Type(Integer32):
    """Custom type cfAmntLoWatermark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfAmntLoWatermark_Type.__name__ = "Integer32"
_CfAmntLoWatermark_Object = MibScalar
cfAmntLoWatermark = _CfAmntLoWatermark_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 2, 10),
    _CfAmntLoWatermark_Type()
)
cfAmntLoWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfAmntLoWatermark.setStatus("current")
if mibBuilder.loadTexts:
    cfAmntLoWatermark.setUnits("%")
_CfEvictedAge_Type = TimeTicks
_CfEvictedAge_Object = MibScalar
cfEvictedAge = _CfEvictedAge_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 2, 11),
    _CfEvictedAge_Type()
)
cfEvictedAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfEvictedAge.setStatus("current")
_CfEvictedLastAccess_Type = OctetString
_CfEvictedLastAccess_Object = MibScalar
cfEvictedLastAccess = _CfEvictedLastAccess_Object(
    (1, 3, 6, 1, 4, 1, 17471, 1, 6, 2, 2, 12),
    _CfEvictedLastAccess_Type()
)
cfEvictedLastAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfEvictedLastAccess.setStatus("current")
_ActastorGroups_ObjectIdentity = ObjectIdentity
actastorGroups = _ActastorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17471, 2)
)
if mibBuilder.loadTexts:
    actastorGroups.setStatus("current")

# Managed Objects groups

generalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17471, 2, 1)
)
generalGroup.setObjects(
      *(("ACTONA-ACTASTOR-MIB", "actastorVersion"),
        ("ACTONA-ACTASTOR-MIB", "buildString"),
        ("ACTONA-ACTASTOR-MIB", "email"),
        ("ACTONA-ACTASTOR-MIB", "isValid"),
        ("ACTONA-ACTASTOR-MIB", "daysLeft"))
)
if mibBuilder.loadTexts:
    generalGroup.setStatus("current")

managerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17471, 2, 2)
)
managerGroup.setObjects(
    ("ACTONA-ACTASTOR-MIB", "mgrCentralServerHost")
)
if mibBuilder.loadTexts:
    managerGroup.setStatus("current")

coreServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17471, 2, 3)
)
coreServerGroup.setObjects(
      *(("ACTONA-ACTASTOR-MIB", "csDeviceName"),
        ("ACTONA-ACTASTOR-MIB", "csIsConfigured"),
        ("ACTONA-ACTASTOR-MIB", "csIsAlive"),
        ("ACTONA-ACTASTOR-MIB", "csUpTime"),
        ("ACTONA-ACTASTOR-MIB", "csWINS"),
        ("ACTONA-ACTASTOR-MIB", "csConTabClusterID"),
        ("ACTONA-ACTASTOR-MIB", "csConTabClusterName"),
        ("ACTONA-ACTASTOR-MIB", "csConTabIsConnected"),
        ("ACTONA-ACTASTOR-MIB", "csConTabTotalSentMessages"),
        ("ACTONA-ACTASTOR-MIB", "csConTabSentCompressionRatio"),
        ("ACTONA-ACTASTOR-MIB", "csConTabTotalReceivedMessages"),
        ("ACTONA-ACTASTOR-MIB", "csConTabReceivedCompressionRatio"),
        ("ACTONA-ACTASTOR-MIB", "csConTabTotalSentKBytes"),
        ("ACTONA-ACTASTOR-MIB", "csConTabTotalReceivedKBytes"),
        ("ACTONA-ACTASTOR-MIB", "csCIFSServersTabServerName"),
        ("ACTONA-ACTASTOR-MIB", "csNFSServersTabServerName"),
        ("ACTONA-ACTASTOR-MIB", "csNFSServersTabUseTCP"),
        ("ACTONA-ACTASTOR-MIB", "csNFSServersTabUseUDP"))
)
if mibBuilder.loadTexts:
    coreServerGroup.setStatus("current")

edgeServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17471, 2, 4)
)
edgeServerGroup.setObjects(
      *(("ACTONA-ACTASTOR-MIB", "esIsConfigured"),
        ("ACTONA-ACTASTOR-MIB", "esIsAlive"),
        ("ACTONA-ACTASTOR-MIB", "esUpTime"),
        ("ACTONA-ACTASTOR-MIB", "esTotalBytesRead"),
        ("ACTONA-ACTASTOR-MIB", "esTotalWrittenBytes"),
        ("ACTONA-ACTASTOR-MIB", "esRemoteRequestCount"),
        ("ACTONA-ACTASTOR-MIB", "esLocalRequestCount"),
        ("ACTONA-ACTASTOR-MIB", "esConnectedSessionCount"),
        ("ACTONA-ACTASTOR-MIB", "esCifsOpenFiles"),
        ("ACTONA-ACTASTOR-MIB", "esMaxCacheVolume"),
        ("ACTONA-ACTASTOR-MIB", "esCurrentCacheVolume"),
        ("ACTONA-ACTASTOR-MIB", "esMaxCacheResources"),
        ("ACTONA-ACTASTOR-MIB", "esCurrentCacheResources"),
        ("ACTONA-ACTASTOR-MIB", "esTotalRemoteTime"),
        ("ACTONA-ACTASTOR-MIB", "esTotalLocalTime"),
        ("ACTONA-ACTASTOR-MIB", "esConTabClusterID"),
        ("ACTONA-ACTASTOR-MIB", "esConTabClusterName"),
        ("ACTONA-ACTASTOR-MIB", "esConTabIsConnected"),
        ("ACTONA-ACTASTOR-MIB", "esConTabTotalSentMessages"),
        ("ACTONA-ACTASTOR-MIB", "esConTabSentCompressionRatio"),
        ("ACTONA-ACTASTOR-MIB", "esConTabTotalReceivedMessages"),
        ("ACTONA-ACTASTOR-MIB", "esConTabReceivedCompressionRatio"),
        ("ACTONA-ACTASTOR-MIB", "esConTabTotalSentKBytes"),
        ("ACTONA-ACTASTOR-MIB", "esConTabTotalReceivedKBytes"),
        ("ACTONA-ACTASTOR-MIB", "esResourceEvictedNum"),
        ("ACTONA-ACTASTOR-MIB", "esLastEvictedTime"),
        ("ACTONA-ACTASTOR-MIB", "esVolHiWatermark"),
        ("ACTONA-ACTASTOR-MIB", "esVolLoWatermark"),
        ("ACTONA-ACTASTOR-MIB", "esAmntHiWatermark"),
        ("ACTONA-ACTASTOR-MIB", "esAmntLoWatermark"),
        ("ACTONA-ACTASTOR-MIB", "esEvictedAge"),
        ("ACTONA-ACTASTOR-MIB", "esEvictedLastAccess"))
)
if mibBuilder.loadTexts:
    edgeServerGroup.setStatus("current")

acNotificationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17471, 2, 7)
)
acNotificationInfoGroup.setObjects(
      *(("ACTONA-ACTASTOR-MIB", "acLogSeverity"),
        ("ACTONA-ACTASTOR-MIB", "acLogMsgText"))
)
if mibBuilder.loadTexts:
    acNotificationInfoGroup.setStatus("current")

cifsAOGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17471, 2, 9)
)
cifsAOGroup.setObjects(
      *(("ACTONA-ACTASTOR-MIB", "cfIsConfigured"),
        ("ACTONA-ACTASTOR-MIB", "cfIsAlive"),
        ("ACTONA-ACTASTOR-MIB", "cfUpTime"),
        ("ACTONA-ACTASTOR-MIB", "cfTotalBytesRead"),
        ("ACTONA-ACTASTOR-MIB", "cfTotalWrittenBytes"),
        ("ACTONA-ACTASTOR-MIB", "cfRemoteRequestCount"),
        ("ACTONA-ACTASTOR-MIB", "cfLocalRequestCount"),
        ("ACTONA-ACTASTOR-MIB", "cfTotalRemoteTime"),
        ("ACTONA-ACTASTOR-MIB", "cfTotalLocalTime"),
        ("ACTONA-ACTASTOR-MIB", "cfConnectedSessionCount"),
        ("ACTONA-ACTASTOR-MIB", "cfCifsOpenFiles"),
        ("ACTONA-ACTASTOR-MIB", "cfMaxCacheVolume"),
        ("ACTONA-ACTASTOR-MIB", "cfCurrentCacheVolume"),
        ("ACTONA-ACTASTOR-MIB", "cfMaxCacheResources"),
        ("ACTONA-ACTASTOR-MIB", "cfCurrentCacheResources"),
        ("ACTONA-ACTASTOR-MIB", "cfResourceEvictedNum"),
        ("ACTONA-ACTASTOR-MIB", "cfLastEvictedTime"),
        ("ACTONA-ACTASTOR-MIB", "cfVolHiWatermark"),
        ("ACTONA-ACTASTOR-MIB", "cfVolLoWatermark"),
        ("ACTONA-ACTASTOR-MIB", "cfAmntHiWatermark"),
        ("ACTONA-ACTASTOR-MIB", "cfAmntLoWatermark"),
        ("ACTONA-ACTASTOR-MIB", "cfEvictedAge"),
        ("ACTONA-ACTASTOR-MIB", "cfEvictedLastAccess"))
)
if mibBuilder.loadTexts:
    cifsAOGroup.setStatus("current")


# Notification objects

acCsLogsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17471, 0, 0)
)
acCsLogsTrap.setObjects(
      *(("ACTONA-ACTASTOR-MIB", "acLogSeverity"),
        ("ACTONA-ACTASTOR-MIB", "acLogMsgText"))
)
if mibBuilder.loadTexts:
    acCsLogsTrap.setStatus(
        "current"
    )

acMgrLogsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17471, 0, 1)
)
acMgrLogsTrap.setObjects(
      *(("ACTONA-ACTASTOR-MIB", "acLogSeverity"),
        ("ACTONA-ACTASTOR-MIB", "acLogMsgText"))
)
if mibBuilder.loadTexts:
    acMgrLogsTrap.setStatus(
        "current"
    )

acEsLogsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17471, 0, 2)
)
acEsLogsTrap.setObjects(
      *(("ACTONA-ACTASTOR-MIB", "acLogSeverity"),
        ("ACTONA-ACTASTOR-MIB", "acLogMsgText"))
)
if mibBuilder.loadTexts:
    acEsLogsTrap.setStatus(
        "current"
    )

mgrLogsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17471, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mgrLogsTrap.setStatus(
        "deprecated"
    )

csLogsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17471, 1, 3, 3)
)
if mibBuilder.loadTexts:
    csLogsTrap.setStatus(
        "deprecated"
    )

esLogsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17471, 1, 4, 3)
)
if mibBuilder.loadTexts:
    esLogsTrap.setStatus(
        "deprecated"
    )


# Notifications groups

logNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 17471, 2, 5)
)
logNotificationsGroup.setObjects(
      *(("ACTONA-ACTASTOR-MIB", "csLogsTrap"),
        ("ACTONA-ACTASTOR-MIB", "esLogsTrap"),
        ("ACTONA-ACTASTOR-MIB", "mgrLogsTrap"))
)
if mibBuilder.loadTexts:
    logNotificationsGroup.setStatus(
        "deprecated"
    )

logNotificationsGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 17471, 2, 6)
)
logNotificationsGroupRev1.setObjects(
      *(("ACTONA-ACTASTOR-MIB", "acCsLogsTrap"),
        ("ACTONA-ACTASTOR-MIB", "acEsLogsTrap"),
        ("ACTONA-ACTASTOR-MIB", "acMgrLogsTrap"))
)
if mibBuilder.loadTexts:
    logNotificationsGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACTONA-ACTASTOR-MIB",
    **{"actona": actona,
       "acNotifications": acNotifications,
       "acCsLogsTrap": acCsLogsTrap,
       "acMgrLogsTrap": acMgrLogsTrap,
       "acEsLogsTrap": acEsLogsTrap,
       "actastor": actastor,
       "generalInformation": generalInformation,
       "actastorVersion": actastorVersion,
       "buildString": buildString,
       "support": support,
       "email": email,
       "license": license,
       "isValid": isValid,
       "daysLeft": daysLeft,
       "manager": manager,
       "mgrCentralServerHost": mgrCentralServerHost,
       "mgrLogsTrap": mgrLogsTrap,
       "coreServer": coreServer,
       "csGeneral": csGeneral,
       "csIsConfigured": csIsConfigured,
       "csIsAlive": csIsAlive,
       "csUpTime": csUpTime,
       "csState": csState,
       "csConnectivityTable": csConnectivityTable,
       "csConnectivityEntry": csConnectivityEntry,
       "csConTabIndex": csConTabIndex,
       "csConTabClusterID": csConTabClusterID,
       "csConTabClusterName": csConTabClusterName,
       "csConTabIsConnected": csConTabIsConnected,
       "csConTabTotalSentMessages": csConTabTotalSentMessages,
       "csConTabSentCompressionRatio": csConTabSentCompressionRatio,
       "csConTabTotalReceivedMessages": csConTabTotalReceivedMessages,
       "csConTabReceivedCompressionRatio": csConTabReceivedCompressionRatio,
       "csConTabTotalSentKBytes": csConTabTotalSentKBytes,
       "csConTabTotalReceivedKBytes": csConTabTotalReceivedKBytes,
       "csDeviceName": csDeviceName,
       "csWINS": csWINS,
       "csCIFSServersTable": csCIFSServersTable,
       "csCIFSServersEntry": csCIFSServersEntry,
       "csCIFSServersTabIndex": csCIFSServersTabIndex,
       "csCIFSServersTabServerName": csCIFSServersTabServerName,
       "csNFSServersTable": csNFSServersTable,
       "csNFSServersEntry": csNFSServersEntry,
       "csNFSServersTabIndex": csNFSServersTabIndex,
       "csNFSServersTabServerName": csNFSServersTabServerName,
       "csNFSServersTabUseTCP": csNFSServersTabUseTCP,
       "csNFSServersTabUseUDP": csNFSServersTabUseUDP,
       "csLogsTrap": csLogsTrap,
       "edgeServer": edgeServer,
       "esGeneral": esGeneral,
       "esIsConfigured": esIsConfigured,
       "esIsAlive": esIsAlive,
       "esUpTime": esUpTime,
       "esState": esState,
       "esConnectivityTable": esConnectivityTable,
       "esConnectivityEntry": esConnectivityEntry,
       "esConTabIndex": esConTabIndex,
       "esConTabClusterID": esConTabClusterID,
       "esConTabClusterName": esConTabClusterName,
       "esConTabIsConnected": esConTabIsConnected,
       "esConTabTotalSentMessages": esConTabTotalSentMessages,
       "esConTabSentCompressionRatio": esConTabSentCompressionRatio,
       "esConTabTotalReceivedMessages": esConTabTotalReceivedMessages,
       "esConTabReceivedCompressionRatio": esConTabReceivedCompressionRatio,
       "esConTabTotalSentKBytes": esConTabTotalSentKBytes,
       "esConTabTotalReceivedKBytes": esConTabTotalReceivedKBytes,
       "esCIFSInfo": esCIFSInfo,
       "esTotalBytesRead": esTotalBytesRead,
       "esTotalWrittenBytes": esTotalWrittenBytes,
       "esRemoteRequestCount": esRemoteRequestCount,
       "esLocalRequestCount": esLocalRequestCount,
       "esTotalRemoteTime": esTotalRemoteTime,
       "esTotalLocalTime": esTotalLocalTime,
       "esConnectedSessionCount": esConnectedSessionCount,
       "esCifsOpenFiles": esCifsOpenFiles,
       "esCacheInfo": esCacheInfo,
       "esMaxCacheVolume": esMaxCacheVolume,
       "esCurrentCacheVolume": esCurrentCacheVolume,
       "esMaxCacheResources": esMaxCacheResources,
       "esCurrentCacheResources": esCurrentCacheResources,
       "esResourceEvictedNum": esResourceEvictedNum,
       "esLastEvictedTime": esLastEvictedTime,
       "esVolHiWatermark": esVolHiWatermark,
       "esVolLoWatermark": esVolLoWatermark,
       "esAmntHiWatermark": esAmntHiWatermark,
       "esAmntLoWatermark": esAmntLoWatermark,
       "esEvictedAge": esEvictedAge,
       "esEvictedLastAccess": esEvictedLastAccess,
       "esLogsTrap": esLogsTrap,
       "notificationsInfo": notificationsInfo,
       "acLogSeverity": acLogSeverity,
       "acLogMsgText": acLogMsgText,
       "cifsAO": cifsAO,
       "cfGeneral": cfGeneral,
       "cfIsConfigured": cfIsConfigured,
       "cfIsAlive": cfIsAlive,
       "cfUpTime": cfUpTime,
       "cfState": cfState,
       "cfCIFSInfo": cfCIFSInfo,
       "cfTotalBytesRead": cfTotalBytesRead,
       "cfTotalWrittenBytes": cfTotalWrittenBytes,
       "cfRemoteRequestCount": cfRemoteRequestCount,
       "cfLocalRequestCount": cfLocalRequestCount,
       "cfTotalRemoteTime": cfTotalRemoteTime,
       "cfTotalLocalTime": cfTotalLocalTime,
       "cfConnectedSessionCount": cfConnectedSessionCount,
       "cfCifsOpenFiles": cfCifsOpenFiles,
       "cfCacheInfo": cfCacheInfo,
       "cfMaxCacheVolume": cfMaxCacheVolume,
       "cfCurrentCacheVolume": cfCurrentCacheVolume,
       "cfMaxCacheResources": cfMaxCacheResources,
       "cfCurrentCacheResources": cfCurrentCacheResources,
       "cfResourceEvictedNum": cfResourceEvictedNum,
       "cfLastEvictedTime": cfLastEvictedTime,
       "cfVolHiWatermark": cfVolHiWatermark,
       "cfVolLoWatermark": cfVolLoWatermark,
       "cfAmntHiWatermark": cfAmntHiWatermark,
       "cfAmntLoWatermark": cfAmntLoWatermark,
       "cfEvictedAge": cfEvictedAge,
       "cfEvictedLastAccess": cfEvictedLastAccess,
       "actastorGroups": actastorGroups,
       "generalGroup": generalGroup,
       "managerGroup": managerGroup,
       "coreServerGroup": coreServerGroup,
       "edgeServerGroup": edgeServerGroup,
       "logNotificationsGroup": logNotificationsGroup,
       "logNotificationsGroupRev1": logNotificationsGroupRev1,
       "acNotificationInfoGroup": acNotificationInfoGroup,
       "cifsAOGroup": cifsAOGroup}
)
