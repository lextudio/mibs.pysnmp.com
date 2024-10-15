# SNMP MIB module (CISCO-PSD-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PSD-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:13 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoPsdClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 495)
)
ciscoPsdClientMIB.setRevisions(
        ("2005-08-24 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoPsdClientMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoPsdClientMIBNotifs = _CiscoPsdClientMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 0)
)
_CiscoPsdClientMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPsdClientMIBObjects = _CiscoPsdClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1)
)
_CiscoPsdClientStatistics_ObjectIdentity = ObjectIdentity
ciscoPsdClientStatistics = _CiscoPsdClientStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 1)
)
_CPsdClientDSWriteReq_Type = Counter32
_CPsdClientDSWriteReq_Object = MibScalar
cPsdClientDSWriteReq = _CPsdClientDSWriteReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 1, 1),
    _CPsdClientDSWriteReq_Type()
)
cPsdClientDSWriteReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPsdClientDSWriteReq.setStatus("current")
_CPsdClientDSReadReq_Type = Counter32
_CPsdClientDSReadReq_Object = MibScalar
cPsdClientDSReadReq = _CPsdClientDSReadReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 1, 2),
    _CPsdClientDSReadReq_Type()
)
cPsdClientDSReadReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPsdClientDSReadReq.setStatus("current")
_CPsdClientDSRdWrRetrans_Type = Counter32
_CPsdClientDSRdWrRetrans_Object = MibScalar
cPsdClientDSRdWrRetrans = _CPsdClientDSRdWrRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 1, 3),
    _CPsdClientDSRdWrRetrans_Type()
)
cPsdClientDSRdWrRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPsdClientDSRdWrRetrans.setStatus("current")
_CPsdClientDSDiskFullTrans_Type = Counter32
_CPsdClientDSDiskFullTrans_Object = MibScalar
cPsdClientDSDiskFullTrans = _CPsdClientDSDiskFullTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 1, 4),
    _CPsdClientDSDiskFullTrans_Type()
)
cPsdClientDSDiskFullTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPsdClientDSDiskFullTrans.setStatus("current")
_CiscoPsdClientNotifMgmt_ObjectIdentity = ObjectIdentity
ciscoPsdClientNotifMgmt = _CiscoPsdClientNotifMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 2)
)


class _CPsdClientNotifEnable_Type(TruthValue):
    """Custom type cPsdClientNotifEnable based on TruthValue"""


_CPsdClientNotifEnable_Object = MibScalar
cPsdClientNotifEnable = _CPsdClientNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 2, 1),
    _CPsdClientNotifEnable_Type()
)
cPsdClientNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPsdClientNotifEnable.setStatus("current")
_CiscoPsdClientConfigurations_ObjectIdentity = ObjectIdentity
ciscoPsdClientConfigurations = _CiscoPsdClientConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 3)
)
_CPsdClientDSTable_Object = MibTable
cPsdClientDSTable = _CPsdClientDSTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cPsdClientDSTable.setStatus("current")
_CPsdClientDSEntry_Object = MibTableRow
cPsdClientDSEntry = _CPsdClientDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 3, 1, 1)
)
cPsdClientDSEntry.setIndexNames(
    (0, "CISCO-PSD-CLIENT-MIB", "cPsdClientDSName"),
)
if mibBuilder.loadTexts:
    cPsdClientDSEntry.setStatus("current")


class _CPsdClientDSName_Type(SnmpAdminString):
    """Custom type cPsdClientDSName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CPsdClientDSName_Type.__name__ = "SnmpAdminString"
_CPsdClientDSName_Object = MibTableColumn
cPsdClientDSName = _CPsdClientDSName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 3, 1, 1, 1),
    _CPsdClientDSName_Type()
)
cPsdClientDSName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPsdClientDSName.setStatus("current")


class _CPsdClientDSAutoRetrieve_Type(TruthValue):
    """Custom type cPsdClientDSAutoRetrieve based on TruthValue"""


_CPsdClientDSAutoRetrieve_Object = MibTableColumn
cPsdClientDSAutoRetrieve = _CPsdClientDSAutoRetrieve_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 3, 1, 1, 2),
    _CPsdClientDSAutoRetrieve_Type()
)
cPsdClientDSAutoRetrieve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPsdClientDSAutoRetrieve.setStatus("current")


class _CPsdClientDSMaxRetrieve_Type(Integer32):
    """Custom type cPsdClientDSMaxRetrieve based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6000),
    )


_CPsdClientDSMaxRetrieve_Type.__name__ = "Integer32"
_CPsdClientDSMaxRetrieve_Object = MibTableColumn
cPsdClientDSMaxRetrieve = _CPsdClientDSMaxRetrieve_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 3, 1, 1, 3),
    _CPsdClientDSMaxRetrieve_Type()
)
cPsdClientDSMaxRetrieve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPsdClientDSMaxRetrieve.setStatus("current")
if mibBuilder.loadTexts:
    cPsdClientDSMaxRetrieve.setUnits("messages/minute")
_CPsdClientDSRowStatus_Type = RowStatus
_CPsdClientDSRowStatus_Object = MibTableColumn
cPsdClientDSRowStatus = _CPsdClientDSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 3, 1, 1, 4),
    _CPsdClientDSRowStatus_Type()
)
cPsdClientDSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPsdClientDSRowStatus.setStatus("current")
_CPsdClientDSServerTable_Object = MibTable
cPsdClientDSServerTable = _CPsdClientDSServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cPsdClientDSServerTable.setStatus("current")
_CPsdClientDSServerEntry_Object = MibTableRow
cPsdClientDSServerEntry = _CPsdClientDSServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 3, 2, 1)
)
cPsdClientDSServerEntry.setIndexNames(
    (0, "CISCO-PSD-CLIENT-MIB", "cPsdClientDSName"),
    (0, "CISCO-PSD-CLIENT-MIB", "cPsdClientDSServerAddressType"),
    (0, "CISCO-PSD-CLIENT-MIB", "cPsdClientDSServerAddress"),
)
if mibBuilder.loadTexts:
    cPsdClientDSServerEntry.setStatus("current")
_CPsdClientDSServerAddressType_Type = InetAddressType
_CPsdClientDSServerAddressType_Object = MibTableColumn
cPsdClientDSServerAddressType = _CPsdClientDSServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 3, 2, 1, 1),
    _CPsdClientDSServerAddressType_Type()
)
cPsdClientDSServerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPsdClientDSServerAddressType.setStatus("current")


class _CPsdClientDSServerAddress_Type(InetAddress):
    """Custom type cPsdClientDSServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_CPsdClientDSServerAddress_Type.__name__ = "InetAddress"
_CPsdClientDSServerAddress_Object = MibTableColumn
cPsdClientDSServerAddress = _CPsdClientDSServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 3, 2, 1, 2),
    _CPsdClientDSServerAddress_Type()
)
cPsdClientDSServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPsdClientDSServerAddress.setStatus("current")
_CPsdClientDSRetrieveOnly_Type = TruthValue
_CPsdClientDSRetrieveOnly_Object = MibTableColumn
cPsdClientDSRetrieveOnly = _CPsdClientDSRetrieveOnly_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 3, 2, 1, 3),
    _CPsdClientDSRetrieveOnly_Type()
)
cPsdClientDSRetrieveOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPsdClientDSRetrieveOnly.setStatus("current")
_CPsdClientDSServerRowStatus_Type = RowStatus
_CPsdClientDSServerRowStatus_Object = MibTableColumn
cPsdClientDSServerRowStatus = _CPsdClientDSServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 3, 2, 1, 4),
    _CPsdClientDSServerRowStatus_Type()
)
cPsdClientDSServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPsdClientDSServerRowStatus.setStatus("current")
_CiscoPsdClientNotifInfo_ObjectIdentity = ObjectIdentity
ciscoPsdClientNotifInfo = _CiscoPsdClientNotifInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 4)
)
_CPsdClientNotifDSServerAddrType_Type = InetAddressType
_CPsdClientNotifDSServerAddrType_Object = MibScalar
cPsdClientNotifDSServerAddrType = _CPsdClientNotifDSServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 4, 1),
    _CPsdClientNotifDSServerAddrType_Type()
)
cPsdClientNotifDSServerAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cPsdClientNotifDSServerAddrType.setStatus("current")
_CPsdClientNotifDSServerAddress_Type = InetAddress
_CPsdClientNotifDSServerAddress_Object = MibScalar
cPsdClientNotifDSServerAddress = _CPsdClientNotifDSServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 1, 4, 2),
    _CPsdClientNotifDSServerAddress_Type()
)
cPsdClientNotifDSServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cPsdClientNotifDSServerAddress.setStatus("current")
_CiscoPsdClientMIBConform_ObjectIdentity = ObjectIdentity
ciscoPsdClientMIBConform = _CiscoPsdClientMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 2)
)
_CPsdClientMIBCompliances_ObjectIdentity = ObjectIdentity
cPsdClientMIBCompliances = _CPsdClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 2, 1)
)
_CPsdClientMIBGroups_ObjectIdentity = ObjectIdentity
cPsdClientMIBGroups = _CPsdClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 2, 2)
)

# Managed Objects groups

cPsdClientMIBStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 2, 2, 1)
)
cPsdClientMIBStatisticsGroup.setObjects(
      *(("CISCO-PSD-CLIENT-MIB", "cPsdClientDSWriteReq"),
        ("CISCO-PSD-CLIENT-MIB", "cPsdClientDSReadReq"),
        ("CISCO-PSD-CLIENT-MIB", "cPsdClientDSRdWrRetrans"),
        ("CISCO-PSD-CLIENT-MIB", "cPsdClientDSDiskFullTrans"))
)
if mibBuilder.loadTexts:
    cPsdClientMIBStatisticsGroup.setStatus("current")

cPsdClientMIBConfigurationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 2, 2, 2)
)
cPsdClientMIBConfigurationsGroup.setObjects(
      *(("CISCO-PSD-CLIENT-MIB", "cPsdClientDSRowStatus"),
        ("CISCO-PSD-CLIENT-MIB", "cPsdClientDSAutoRetrieve"),
        ("CISCO-PSD-CLIENT-MIB", "cPsdClientDSMaxRetrieve"),
        ("CISCO-PSD-CLIENT-MIB", "cPsdClientDSServerRowStatus"),
        ("CISCO-PSD-CLIENT-MIB", "cPsdClientDSRetrieveOnly"))
)
if mibBuilder.loadTexts:
    cPsdClientMIBConfigurationsGroup.setStatus("current")

cPsdClientMIBNotifInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 2, 2, 4)
)
cPsdClientMIBNotifInfoGroup.setObjects(
      *(("CISCO-PSD-CLIENT-MIB", "cPsdClientNotifDSServerAddrType"),
        ("CISCO-PSD-CLIENT-MIB", "cPsdClientNotifDSServerAddress"))
)
if mibBuilder.loadTexts:
    cPsdClientMIBNotifInfoGroup.setStatus("current")

cPsdClientMIBNotifMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 2, 2, 5)
)
cPsdClientMIBNotifMgmtGroup.setObjects(
    ("CISCO-PSD-CLIENT-MIB", "cPsdClientNotifEnable")
)
if mibBuilder.loadTexts:
    cPsdClientMIBNotifMgmtGroup.setStatus("current")


# Notification objects

cPsdClientDownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 0, 1)
)
cPsdClientDownNotif.setObjects(
      *(("CISCO-PSD-CLIENT-MIB", "cPsdClientNotifDSServerAddrType"),
        ("CISCO-PSD-CLIENT-MIB", "cPsdClientNotifDSServerAddress"))
)
if mibBuilder.loadTexts:
    cPsdClientDownNotif.setStatus(
        "current"
    )

cPsdClientUpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 0, 2)
)
cPsdClientUpNotif.setObjects(
      *(("CISCO-PSD-CLIENT-MIB", "cPsdClientNotifDSServerAddrType"),
        ("CISCO-PSD-CLIENT-MIB", "cPsdClientNotifDSServerAddress"))
)
if mibBuilder.loadTexts:
    cPsdClientUpNotif.setStatus(
        "current"
    )

cPsdClientDiskFullNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 0, 3)
)
cPsdClientDiskFullNotif.setObjects(
      *(("CISCO-PSD-CLIENT-MIB", "cPsdClientNotifDSServerAddrType"),
        ("CISCO-PSD-CLIENT-MIB", "cPsdClientNotifDSServerAddress"))
)
if mibBuilder.loadTexts:
    cPsdClientDiskFullNotif.setStatus(
        "current"
    )


# Notifications groups

cPsdClientMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 2, 2, 3)
)
cPsdClientMIBNotifGroup.setObjects(
      *(("CISCO-PSD-CLIENT-MIB", "cPsdClientDownNotif"),
        ("CISCO-PSD-CLIENT-MIB", "cPsdClientUpNotif"),
        ("CISCO-PSD-CLIENT-MIB", "cPsdClientDiskFullNotif"))
)
if mibBuilder.loadTexts:
    cPsdClientMIBNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cPsdClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 495, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cPsdClientMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PSD-CLIENT-MIB",
    **{"ciscoPsdClientMIB": ciscoPsdClientMIB,
       "ciscoPsdClientMIBNotifs": ciscoPsdClientMIBNotifs,
       "cPsdClientDownNotif": cPsdClientDownNotif,
       "cPsdClientUpNotif": cPsdClientUpNotif,
       "cPsdClientDiskFullNotif": cPsdClientDiskFullNotif,
       "ciscoPsdClientMIBObjects": ciscoPsdClientMIBObjects,
       "ciscoPsdClientStatistics": ciscoPsdClientStatistics,
       "cPsdClientDSWriteReq": cPsdClientDSWriteReq,
       "cPsdClientDSReadReq": cPsdClientDSReadReq,
       "cPsdClientDSRdWrRetrans": cPsdClientDSRdWrRetrans,
       "cPsdClientDSDiskFullTrans": cPsdClientDSDiskFullTrans,
       "ciscoPsdClientNotifMgmt": ciscoPsdClientNotifMgmt,
       "cPsdClientNotifEnable": cPsdClientNotifEnable,
       "ciscoPsdClientConfigurations": ciscoPsdClientConfigurations,
       "cPsdClientDSTable": cPsdClientDSTable,
       "cPsdClientDSEntry": cPsdClientDSEntry,
       "cPsdClientDSName": cPsdClientDSName,
       "cPsdClientDSAutoRetrieve": cPsdClientDSAutoRetrieve,
       "cPsdClientDSMaxRetrieve": cPsdClientDSMaxRetrieve,
       "cPsdClientDSRowStatus": cPsdClientDSRowStatus,
       "cPsdClientDSServerTable": cPsdClientDSServerTable,
       "cPsdClientDSServerEntry": cPsdClientDSServerEntry,
       "cPsdClientDSServerAddressType": cPsdClientDSServerAddressType,
       "cPsdClientDSServerAddress": cPsdClientDSServerAddress,
       "cPsdClientDSRetrieveOnly": cPsdClientDSRetrieveOnly,
       "cPsdClientDSServerRowStatus": cPsdClientDSServerRowStatus,
       "ciscoPsdClientNotifInfo": ciscoPsdClientNotifInfo,
       "cPsdClientNotifDSServerAddrType": cPsdClientNotifDSServerAddrType,
       "cPsdClientNotifDSServerAddress": cPsdClientNotifDSServerAddress,
       "ciscoPsdClientMIBConform": ciscoPsdClientMIBConform,
       "cPsdClientMIBCompliances": cPsdClientMIBCompliances,
       "cPsdClientMIBCompliance": cPsdClientMIBCompliance,
       "cPsdClientMIBGroups": cPsdClientMIBGroups,
       "cPsdClientMIBStatisticsGroup": cPsdClientMIBStatisticsGroup,
       "cPsdClientMIBConfigurationsGroup": cPsdClientMIBConfigurationsGroup,
       "cPsdClientMIBNotifGroup": cPsdClientMIBNotifGroup,
       "cPsdClientMIBNotifInfoGroup": cPsdClientMIBNotifInfoGroup,
       "cPsdClientMIBNotifMgmtGroup": cPsdClientMIBNotifMgmtGroup}
)
