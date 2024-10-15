# SNMP MIB module (CISCO-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:28 2024
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

(CiscoPort,
 TimeIntervalMin,
 TimeIntervalSec) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort",
    "TimeIntervalMin",
    "TimeIntervalSec")

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

ciscoRadiusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 288)
)
ciscoRadiusMIB.setRevisions(
        ("2009-02-06 00:00",
         "2007-07-22 00:00",
         "2007-01-03 00:00",
         "2004-03-03 00:00",
         "2002-11-09 00:00",
         "2002-10-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoRadiusAuthKey(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )



class CiscoRadiusRoundTripTimePercent(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class CiscoRadiusRetransPercent(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoRadiusMIBObjects_ObjectIdentity = ObjectIdentity
ciscoRadiusMIBObjects = _CiscoRadiusMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1)
)
_CrRadiusGenericConfig_ObjectIdentity = ObjectIdentity
crRadiusGenericConfig = _CrRadiusGenericConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 1)
)


class _CrRadiusLoginAuthentication_Type(Bits):
    """Custom type crRadiusLoginAuthentication based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("console", 1),
          ("http", 2),
          ("telnet", 0))
    )

_CrRadiusLoginAuthentication_Type.__name__ = "Bits"
_CrRadiusLoginAuthentication_Object = MibScalar
crRadiusLoginAuthentication = _CrRadiusLoginAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 1, 1),
    _CrRadiusLoginAuthentication_Type()
)
crRadiusLoginAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusLoginAuthentication.setStatus("current")


class _CrRadiusDeadtime_Type(TimeIntervalMin):
    """Custom type crRadiusDeadtime based on TimeIntervalMin"""
    defaultValue = 0

    subtypeSpec = TimeIntervalMin.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CrRadiusDeadtime_Type.__name__ = "TimeIntervalMin"
_CrRadiusDeadtime_Object = MibScalar
crRadiusDeadtime = _CrRadiusDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 1, 2),
    _CrRadiusDeadtime_Type()
)
crRadiusDeadtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusDeadtime.setStatus("current")
if mibBuilder.loadTexts:
    crRadiusDeadtime.setUnits("minutes")
_CrRadiusAuthKey_Type = CiscoRadiusAuthKey
_CrRadiusAuthKey_Object = MibScalar
crRadiusAuthKey = _CrRadiusAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 1, 3),
    _CrRadiusAuthKey_Type()
)
crRadiusAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusAuthKey.setStatus("current")


class _CrRadiusTimeout_Type(TimeIntervalSec):
    """Custom type crRadiusTimeout based on TimeIntervalSec"""
    defaultValue = 1

    subtypeSpec = TimeIntervalSec.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CrRadiusTimeout_Type.__name__ = "TimeIntervalSec"
_CrRadiusTimeout_Object = MibScalar
crRadiusTimeout = _CrRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 1, 4),
    _CrRadiusTimeout_Type()
)
crRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusTimeout.setStatus("current")
if mibBuilder.loadTexts:
    crRadiusTimeout.setUnits("seconds")


class _CrRadiusRetransmits_Type(Unsigned32):
    """Custom type crRadiusRetransmits based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CrRadiusRetransmits_Type.__name__ = "Unsigned32"
_CrRadiusRetransmits_Object = MibScalar
crRadiusRetransmits = _CrRadiusRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 1, 5),
    _CrRadiusRetransmits_Type()
)
crRadiusRetransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusRetransmits.setStatus("current")
if mibBuilder.loadTexts:
    crRadiusRetransmits.setUnits("retransmits")


class _CrRadiusAccountingLogMaxSize_Type(Unsigned32):
    """Custom type crRadiusAccountingLogMaxSize based on Unsigned32"""
    defaultValue = 30000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_CrRadiusAccountingLogMaxSize_Type.__name__ = "Unsigned32"
_CrRadiusAccountingLogMaxSize_Object = MibScalar
crRadiusAccountingLogMaxSize = _CrRadiusAccountingLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 1, 6),
    _CrRadiusAccountingLogMaxSize_Type()
)
crRadiusAccountingLogMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusAccountingLogMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    crRadiusAccountingLogMaxSize.setUnits("bytes")


class _CrRadiusAccountingMethod_Type(Bits):
    """Custom type crRadiusAccountingMethod based on Bits"""
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 0))
    )

_CrRadiusAccountingMethod_Type.__name__ = "Bits"
_CrRadiusAccountingMethod_Object = MibScalar
crRadiusAccountingMethod = _CrRadiusAccountingMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 1, 7),
    _CrRadiusAccountingMethod_Type()
)
crRadiusAccountingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusAccountingMethod.setStatus("current")
_CrRadiusServerConfig_ObjectIdentity = ObjectIdentity
crRadiusServerConfig = _CrRadiusServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2)
)


class _CrRadiusServerTableMaxEntries_Type(Unsigned32):
    """Custom type crRadiusServerTableMaxEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CrRadiusServerTableMaxEntries_Type.__name__ = "Unsigned32"
_CrRadiusServerTableMaxEntries_Object = MibScalar
crRadiusServerTableMaxEntries = _CrRadiusServerTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2, 1),
    _CrRadiusServerTableMaxEntries_Type()
)
crRadiusServerTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crRadiusServerTableMaxEntries.setStatus("current")
_CrRadiusServerTable_Object = MibTable
crRadiusServerTable = _CrRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2, 2)
)
if mibBuilder.loadTexts:
    crRadiusServerTable.setStatus("current")
_CrRadiusServerEntry_Object = MibTableRow
crRadiusServerEntry = _CrRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2, 2, 1)
)
crRadiusServerEntry.setIndexNames(
    (0, "CISCO-RADIUS-MIB", "crRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    crRadiusServerEntry.setStatus("current")


class _CrRadiusServerIndex_Type(Unsigned32):
    """Custom type crRadiusServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CrRadiusServerIndex_Type.__name__ = "Unsigned32"
_CrRadiusServerIndex_Object = MibTableColumn
crRadiusServerIndex = _CrRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2, 2, 1, 1),
    _CrRadiusServerIndex_Type()
)
crRadiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crRadiusServerIndex.setStatus("current")


class _CrRadiusServerAddrType_Type(InetAddressType):
    """Custom type crRadiusServerAddrType based on InetAddressType"""


_CrRadiusServerAddrType_Object = MibTableColumn
crRadiusServerAddrType = _CrRadiusServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2, 2, 1, 2),
    _CrRadiusServerAddrType_Type()
)
crRadiusServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crRadiusServerAddrType.setStatus("current")
_CrRadiusServerAddr_Type = InetAddress
_CrRadiusServerAddr_Object = MibTableColumn
crRadiusServerAddr = _CrRadiusServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2, 2, 1, 3),
    _CrRadiusServerAddr_Type()
)
crRadiusServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crRadiusServerAddr.setStatus("current")


class _CrRadiusServerAuthPort_Type(CiscoPort):
    """Custom type crRadiusServerAuthPort based on CiscoPort"""
    defaultValue = 1812


_CrRadiusServerAuthPort_Object = MibTableColumn
crRadiusServerAuthPort = _CrRadiusServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2, 2, 1, 4),
    _CrRadiusServerAuthPort_Type()
)
crRadiusServerAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crRadiusServerAuthPort.setStatus("current")


class _CrRadiusServerAcctPort_Type(CiscoPort):
    """Custom type crRadiusServerAcctPort based on CiscoPort"""
    defaultValue = 1813


_CrRadiusServerAcctPort_Object = MibTableColumn
crRadiusServerAcctPort = _CrRadiusServerAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2, 2, 1, 5),
    _CrRadiusServerAcctPort_Type()
)
crRadiusServerAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crRadiusServerAcctPort.setStatus("current")


class _CrRadiusServerKey_Type(CiscoRadiusAuthKey):
    """Custom type crRadiusServerKey based on CiscoRadiusAuthKey"""
    defaultHexValue = "00000000"


_CrRadiusServerKey_Object = MibTableColumn
crRadiusServerKey = _CrRadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2, 2, 1, 6),
    _CrRadiusServerKey_Type()
)
crRadiusServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crRadiusServerKey.setStatus("current")


class _CrRadiusServerType_Type(Integer32):
    """Custom type crRadiusServerType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("primary", 2))
    )


_CrRadiusServerType_Type.__name__ = "Integer32"
_CrRadiusServerType_Object = MibTableColumn
crRadiusServerType = _CrRadiusServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2, 2, 1, 7),
    _CrRadiusServerType_Type()
)
crRadiusServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crRadiusServerType.setStatus("current")


class _CrRadiusServerMode_Type(Integer32):
    """Custom type crRadiusServerMode based on Integer32"""
    defaultValue = 2

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
        *(("acctOnly", 4),
          ("authAndAcct", 2),
          ("authOnly", 3),
          ("none", 1))
    )


_CrRadiusServerMode_Type.__name__ = "Integer32"
_CrRadiusServerMode_Object = MibTableColumn
crRadiusServerMode = _CrRadiusServerMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2, 2, 1, 8),
    _CrRadiusServerMode_Type()
)
crRadiusServerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crRadiusServerMode.setStatus("current")
_CrRadiusServerRowStatus_Type = RowStatus
_CrRadiusServerRowStatus_Object = MibTableColumn
crRadiusServerRowStatus = _CrRadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2, 2, 1, 9),
    _CrRadiusServerRowStatus_Type()
)
crRadiusServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crRadiusServerRowStatus.setStatus("current")
_CrRadiusServerRTTThldNorm_Type = CiscoRadiusRoundTripTimePercent
_CrRadiusServerRTTThldNorm_Object = MibTableColumn
crRadiusServerRTTThldNorm = _CrRadiusServerRTTThldNorm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2, 2, 1, 10),
    _CrRadiusServerRTTThldNorm_Type()
)
crRadiusServerRTTThldNorm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crRadiusServerRTTThldNorm.setStatus("current")
if mibBuilder.loadTexts:
    crRadiusServerRTTThldNorm.setUnits("percent")
_CrRadiusServerRTTThldHi_Type = CiscoRadiusRoundTripTimePercent
_CrRadiusServerRTTThldHi_Object = MibTableColumn
crRadiusServerRTTThldHi = _CrRadiusServerRTTThldHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2, 2, 1, 11),
    _CrRadiusServerRTTThldHi_Type()
)
crRadiusServerRTTThldHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crRadiusServerRTTThldHi.setStatus("current")
if mibBuilder.loadTexts:
    crRadiusServerRTTThldHi.setUnits("percent")
_CrRadiusServerRetransThldNorm_Type = CiscoRadiusRetransPercent
_CrRadiusServerRetransThldNorm_Object = MibTableColumn
crRadiusServerRetransThldNorm = _CrRadiusServerRetransThldNorm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2, 2, 1, 12),
    _CrRadiusServerRetransThldNorm_Type()
)
crRadiusServerRetransThldNorm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crRadiusServerRetransThldNorm.setStatus("current")
if mibBuilder.loadTexts:
    crRadiusServerRetransThldNorm.setUnits("percent")
_CrRadiusServerRetransThldHi_Type = CiscoRadiusRetransPercent
_CrRadiusServerRetransThldHi_Object = MibTableColumn
crRadiusServerRetransThldHi = _CrRadiusServerRetransThldHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 2, 2, 1, 13),
    _CrRadiusServerRetransThldHi_Type()
)
crRadiusServerRetransThldHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crRadiusServerRetransThldHi.setStatus("current")
if mibBuilder.loadTexts:
    crRadiusServerRetransThldHi.setUnits("percent")
_CrRadiusAttributesConfig_ObjectIdentity = ObjectIdentity
crRadiusAttributesConfig = _CrRadiusAttributesConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 3)
)
_CrRadiusFramedIpAddrIncluded_Type = TruthValue
_CrRadiusFramedIpAddrIncluded_Object = MibScalar
crRadiusFramedIpAddrIncluded = _CrRadiusFramedIpAddrIncluded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 3, 1),
    _CrRadiusFramedIpAddrIncluded_Type()
)
crRadiusFramedIpAddrIncluded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusFramedIpAddrIncluded.setStatus("current")
_CrRadiusFramedMtu_Type = Unsigned32
_CrRadiusFramedMtu_Object = MibScalar
crRadiusFramedMtu = _CrRadiusFramedMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 3, 2),
    _CrRadiusFramedMtu_Type()
)
crRadiusFramedMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusFramedMtu.setStatus("current")
_CrRadiusVlanConfigGroup_ObjectIdentity = ObjectIdentity
crRadiusVlanConfigGroup = _CrRadiusVlanConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 4)
)
_CrRadiusVlanAssignmentEnabled_Type = TruthValue
_CrRadiusVlanAssignmentEnabled_Object = MibScalar
crRadiusVlanAssignmentEnabled = _CrRadiusVlanAssignmentEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 4, 1),
    _CrRadiusVlanAssignmentEnabled_Type()
)
crRadiusVlanAssignmentEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusVlanAssignmentEnabled.setStatus("current")
_CrVlanGroupTable_Object = MibTable
crVlanGroupTable = _CrVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 4, 2)
)
if mibBuilder.loadTexts:
    crVlanGroupTable.setStatus("current")
_CrVlanGroupEntry_Object = MibTableRow
crVlanGroupEntry = _CrVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 4, 2, 1)
)
crVlanGroupEntry.setIndexNames(
    (0, "CISCO-RADIUS-MIB", "crVlanGroupName"),
)
if mibBuilder.loadTexts:
    crVlanGroupEntry.setStatus("current")
_CrVlanGroupName_Type = SnmpAdminString
_CrVlanGroupName_Object = MibTableColumn
crVlanGroupName = _CrVlanGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 4, 2, 1, 1),
    _CrVlanGroupName_Type()
)
crVlanGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crVlanGroupName.setStatus("current")


class _CrVlanGroupVlansLow_Type(OctetString):
    """Custom type crVlanGroupVlansLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CrVlanGroupVlansLow_Type.__name__ = "OctetString"
_CrVlanGroupVlansLow_Object = MibTableColumn
crVlanGroupVlansLow = _CrVlanGroupVlansLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 4, 2, 1, 2),
    _CrVlanGroupVlansLow_Type()
)
crVlanGroupVlansLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crVlanGroupVlansLow.setStatus("current")


class _CrVlanGroupVlansHigh_Type(OctetString):
    """Custom type crVlanGroupVlansHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CrVlanGroupVlansHigh_Type.__name__ = "OctetString"
_CrVlanGroupVlansHigh_Object = MibTableColumn
crVlanGroupVlansHigh = _CrVlanGroupVlansHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 4, 2, 1, 3),
    _CrVlanGroupVlansHigh_Type()
)
crVlanGroupVlansHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crVlanGroupVlansHigh.setStatus("current")
_CrVlanGroupRowStatus_Type = RowStatus
_CrVlanGroupRowStatus_Object = MibTableColumn
crVlanGroupRowStatus = _CrVlanGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 4, 2, 1, 4),
    _CrVlanGroupRowStatus_Type()
)
crVlanGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crVlanGroupRowStatus.setStatus("current")
_CrRadiusKeepAliveConfig_ObjectIdentity = ObjectIdentity
crRadiusKeepAliveConfig = _CrRadiusKeepAliveConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 5)
)
_CrRadiusKeepAliveEnabled_Type = TruthValue
_CrRadiusKeepAliveEnabled_Object = MibScalar
crRadiusKeepAliveEnabled = _CrRadiusKeepAliveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 5, 1),
    _CrRadiusKeepAliveEnabled_Type()
)
crRadiusKeepAliveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusKeepAliveEnabled.setStatus("current")
_CrRadiusKeepAliveInterval_Type = Unsigned32
_CrRadiusKeepAliveInterval_Object = MibScalar
crRadiusKeepAliveInterval = _CrRadiusKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 5, 2),
    _CrRadiusKeepAliveInterval_Type()
)
crRadiusKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    crRadiusKeepAliveInterval.setUnits("seconds")
_CrRadiusKeepAliveServerTable_Object = MibTable
crRadiusKeepAliveServerTable = _CrRadiusKeepAliveServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 5, 3)
)
if mibBuilder.loadTexts:
    crRadiusKeepAliveServerTable.setStatus("current")
_CrRadiusKeepAliveServerEntry_Object = MibTableRow
crRadiusKeepAliveServerEntry = _CrRadiusKeepAliveServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 5, 3, 1)
)
crRadiusKeepAliveServerEntry.setIndexNames(
    (0, "CISCO-RADIUS-MIB", "crRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    crRadiusKeepAliveServerEntry.setStatus("current")


class _CrRadiusKeepAliveServerStatus_Type(Integer32):
    """Custom type crRadiusKeepAliveServerStatus based on Integer32"""
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
        *(("active", 3),
          ("checkup", 4),
          ("dead", 5),
          ("init", 2),
          ("other", 1))
    )


_CrRadiusKeepAliveServerStatus_Type.__name__ = "Integer32"
_CrRadiusKeepAliveServerStatus_Object = MibTableColumn
crRadiusKeepAliveServerStatus = _CrRadiusKeepAliveServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 5, 3, 1, 1),
    _CrRadiusKeepAliveServerStatus_Type()
)
crRadiusKeepAliveServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crRadiusKeepAliveServerStatus.setStatus("current")
_CrRadiusPortAutoInitialize_Type = TruthValue
_CrRadiusPortAutoInitialize_Object = MibScalar
crRadiusPortAutoInitialize = _CrRadiusPortAutoInitialize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 5, 4),
    _CrRadiusPortAutoInitialize_Type()
)
crRadiusPortAutoInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusPortAutoInitialize.setStatus("current")
_CrRadiusKeepAliveUserName_Type = SnmpAdminString
_CrRadiusKeepAliveUserName_Object = MibScalar
crRadiusKeepAliveUserName = _CrRadiusKeepAliveUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 5, 5),
    _CrRadiusKeepAliveUserName_Type()
)
crRadiusKeepAliveUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusKeepAliveUserName.setStatus("current")
_CrRadiusServerNotifCntl_ObjectIdentity = ObjectIdentity
crRadiusServerNotifCntl = _CrRadiusServerNotifCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 6)
)


class _CrRadiusServerRTTNormNotifEnable_Type(TruthValue):
    """Custom type crRadiusServerRTTNormNotifEnable based on TruthValue"""


_CrRadiusServerRTTNormNotifEnable_Object = MibScalar
crRadiusServerRTTNormNotifEnable = _CrRadiusServerRTTNormNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 6, 1),
    _CrRadiusServerRTTNormNotifEnable_Type()
)
crRadiusServerRTTNormNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusServerRTTNormNotifEnable.setStatus("current")


class _CrRadiusServerRTTHiNotifEnable_Type(TruthValue):
    """Custom type crRadiusServerRTTHiNotifEnable based on TruthValue"""


_CrRadiusServerRTTHiNotifEnable_Object = MibScalar
crRadiusServerRTTHiNotifEnable = _CrRadiusServerRTTHiNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 6, 2),
    _CrRadiusServerRTTHiNotifEnable_Type()
)
crRadiusServerRTTHiNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusServerRTTHiNotifEnable.setStatus("current")


class _CrRadiusServerRetransNormNotifEnable_Type(TruthValue):
    """Custom type crRadiusServerRetransNormNotifEnable based on TruthValue"""


_CrRadiusServerRetransNormNotifEnable_Object = MibScalar
crRadiusServerRetransNormNotifEnable = _CrRadiusServerRetransNormNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 6, 3),
    _CrRadiusServerRetransNormNotifEnable_Type()
)
crRadiusServerRetransNormNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusServerRetransNormNotifEnable.setStatus("current")


class _CrRadiusServerRetransHiNotifEnable_Type(TruthValue):
    """Custom type crRadiusServerRetransHiNotifEnable based on TruthValue"""


_CrRadiusServerRetransHiNotifEnable_Object = MibScalar
crRadiusServerRetransHiNotifEnable = _CrRadiusServerRetransHiNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 1, 6, 4),
    _CrRadiusServerRetransHiNotifEnable_Type()
)
crRadiusServerRetransHiNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crRadiusServerRetransHiNotifEnable.setStatus("current")
_CiscoRadiusMIBConformance_ObjectIdentity = ObjectIdentity
ciscoRadiusMIBConformance = _CiscoRadiusMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2)
)
_CiscoRadiusMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoRadiusMIBCompliances = _CiscoRadiusMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2, 1)
)
_CiscoRadiusMIBGroups_ObjectIdentity = ObjectIdentity
ciscoRadiusMIBGroups = _CiscoRadiusMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2, 2)
)
_CiscoRadiusMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoRadiusMIBNotifications = _CiscoRadiusMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 3)
)

# Managed Objects groups

crmConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2, 2, 1)
)
crmConfigurationGroup.setObjects(
      *(("CISCO-RADIUS-MIB", "crRadiusLoginAuthentication"),
        ("CISCO-RADIUS-MIB", "crRadiusAuthKey"),
        ("CISCO-RADIUS-MIB", "crRadiusTimeout"),
        ("CISCO-RADIUS-MIB", "crRadiusRetransmits"),
        ("CISCO-RADIUS-MIB", "crRadiusDeadtime"),
        ("CISCO-RADIUS-MIB", "crRadiusAccountingLogMaxSize"),
        ("CISCO-RADIUS-MIB", "crRadiusAccountingMethod"),
        ("CISCO-RADIUS-MIB", "crRadiusServerTableMaxEntries"),
        ("CISCO-RADIUS-MIB", "crRadiusServerAddrType"),
        ("CISCO-RADIUS-MIB", "crRadiusServerAddr"),
        ("CISCO-RADIUS-MIB", "crRadiusServerAuthPort"),
        ("CISCO-RADIUS-MIB", "crRadiusServerAcctPort"),
        ("CISCO-RADIUS-MIB", "crRadiusServerKey"),
        ("CISCO-RADIUS-MIB", "crRadiusServerType"),
        ("CISCO-RADIUS-MIB", "crRadiusServerMode"),
        ("CISCO-RADIUS-MIB", "crRadiusServerRowStatus"))
)
if mibBuilder.loadTexts:
    crmConfigurationGroup.setStatus("current")

crmAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2, 2, 2)
)
crmAttributesGroup.setObjects(
    ("CISCO-RADIUS-MIB", "crRadiusFramedIpAddrIncluded")
)
if mibBuilder.loadTexts:
    crmAttributesGroup.setStatus("current")

crmVlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2, 2, 3)
)
crmVlanConfigGroup.setObjects(
      *(("CISCO-RADIUS-MIB", "crRadiusVlanAssignmentEnabled"),
        ("CISCO-RADIUS-MIB", "crVlanGroupVlansLow"),
        ("CISCO-RADIUS-MIB", "crVlanGroupVlansHigh"),
        ("CISCO-RADIUS-MIB", "crVlanGroupRowStatus"))
)
if mibBuilder.loadTexts:
    crmVlanConfigGroup.setStatus("current")

crmKeepAliveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2, 2, 4)
)
crmKeepAliveGroup.setObjects(
      *(("CISCO-RADIUS-MIB", "crRadiusKeepAliveEnabled"),
        ("CISCO-RADIUS-MIB", "crRadiusKeepAliveInterval"),
        ("CISCO-RADIUS-MIB", "crRadiusKeepAliveServerStatus"))
)
if mibBuilder.loadTexts:
    crmKeepAliveGroup.setStatus("current")

crmAutoInitializeConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2, 2, 5)
)
crmAutoInitializeConfigGroup.setObjects(
    ("CISCO-RADIUS-MIB", "crRadiusPortAutoInitialize")
)
if mibBuilder.loadTexts:
    crmAutoInitializeConfigGroup.setStatus("current")

crmAttributesGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2, 2, 6)
)
crmAttributesGroup2.setObjects(
    ("CISCO-RADIUS-MIB", "crRadiusFramedMtu")
)
if mibBuilder.loadTexts:
    crmAttributesGroup2.setStatus("current")

crmRadiusKeepAliveUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2, 2, 7)
)
crmRadiusKeepAliveUserGroup.setObjects(
    ("CISCO-RADIUS-MIB", "crRadiusKeepAliveUserName")
)
if mibBuilder.loadTexts:
    crmRadiusKeepAliveUserGroup.setStatus("current")

crmConfigurationGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2, 2, 9)
)
crmConfigurationGroupSup1.setObjects(
      *(("CISCO-RADIUS-MIB", "crRadiusServerRTTThldNorm"),
        ("CISCO-RADIUS-MIB", "crRadiusServerRTTThldHi"),
        ("CISCO-RADIUS-MIB", "crRadiusServerRetransThldNorm"),
        ("CISCO-RADIUS-MIB", "crRadiusServerRetransThldHi"))
)
if mibBuilder.loadTexts:
    crmConfigurationGroupSup1.setStatus("current")

crmRadiusServerNotifCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2, 2, 10)
)
crmRadiusServerNotifCntlGroup.setObjects(
      *(("CISCO-RADIUS-MIB", "crRadiusServerRTTNormNotifEnable"),
        ("CISCO-RADIUS-MIB", "crRadiusServerRTTHiNotifEnable"),
        ("CISCO-RADIUS-MIB", "crRadiusServerRetransNormNotifEnable"),
        ("CISCO-RADIUS-MIB", "crRadiusServerRetransHiNotifEnable"))
)
if mibBuilder.loadTexts:
    crmRadiusServerNotifCntlGroup.setStatus("current")


# Notification objects

crRadiusServerRTTNormNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 3, 1)
)
crRadiusServerRTTNormNotif.setObjects(
      *(("CISCO-RADIUS-MIB", "crRadiusServerRTTThldNorm"),
        ("CISCO-RADIUS-MIB", "crRadiusServerAddr"),
        ("CISCO-RADIUS-MIB", "crRadiusServerAuthPort"))
)
if mibBuilder.loadTexts:
    crRadiusServerRTTNormNotif.setStatus(
        "current"
    )

crRadiusServerRTTHiNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 3, 2)
)
crRadiusServerRTTHiNotif.setObjects(
      *(("CISCO-RADIUS-MIB", "crRadiusServerRTTThldHi"),
        ("CISCO-RADIUS-MIB", "crRadiusServerAddr"),
        ("CISCO-RADIUS-MIB", "crRadiusServerAuthPort"))
)
if mibBuilder.loadTexts:
    crRadiusServerRTTHiNotif.setStatus(
        "current"
    )

crRadiusServerRetransNormNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 3, 3)
)
crRadiusServerRetransNormNotif.setObjects(
      *(("CISCO-RADIUS-MIB", "crRadiusServerRetransThldNorm"),
        ("CISCO-RADIUS-MIB", "crRadiusServerAddr"),
        ("CISCO-RADIUS-MIB", "crRadiusServerAuthPort"))
)
if mibBuilder.loadTexts:
    crRadiusServerRetransNormNotif.setStatus(
        "current"
    )

crRadiusServerRetransHiNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 3, 4)
)
crRadiusServerRetransHiNotif.setObjects(
      *(("CISCO-RADIUS-MIB", "crRadiusServerRetransThldHi"),
        ("CISCO-RADIUS-MIB", "crRadiusServerAddr"),
        ("CISCO-RADIUS-MIB", "crRadiusServerAuthPort"))
)
if mibBuilder.loadTexts:
    crRadiusServerRetransHiNotif.setStatus(
        "current"
    )


# Notifications groups

crmRadiusServerNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2, 2, 8)
)
crmRadiusServerNotifGroup.setObjects(
      *(("CISCO-RADIUS-MIB", "crRadiusServerRTTNormNotif"),
        ("CISCO-RADIUS-MIB", "crRadiusServerRTTHiNotif"),
        ("CISCO-RADIUS-MIB", "crRadiusServerRetransNormNotif"),
        ("CISCO-RADIUS-MIB", "crRadiusServerRetransHiNotif"))
)
if mibBuilder.loadTexts:
    crmRadiusServerNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoRadiusMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoRadiusMIBCompliance.setStatus(
        "deprecated"
    )

ciscoRadiusMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoRadiusMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoRadiusMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoRadiusMIBCompliance3.setStatus(
        "deprecated"
    )

ciscoRadiusMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 288, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoRadiusMIBCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RADIUS-MIB",
    **{"CiscoRadiusAuthKey": CiscoRadiusAuthKey,
       "CiscoRadiusRoundTripTimePercent": CiscoRadiusRoundTripTimePercent,
       "CiscoRadiusRetransPercent": CiscoRadiusRetransPercent,
       "ciscoRadiusMIB": ciscoRadiusMIB,
       "ciscoRadiusMIBObjects": ciscoRadiusMIBObjects,
       "crRadiusGenericConfig": crRadiusGenericConfig,
       "crRadiusLoginAuthentication": crRadiusLoginAuthentication,
       "crRadiusDeadtime": crRadiusDeadtime,
       "crRadiusAuthKey": crRadiusAuthKey,
       "crRadiusTimeout": crRadiusTimeout,
       "crRadiusRetransmits": crRadiusRetransmits,
       "crRadiusAccountingLogMaxSize": crRadiusAccountingLogMaxSize,
       "crRadiusAccountingMethod": crRadiusAccountingMethod,
       "crRadiusServerConfig": crRadiusServerConfig,
       "crRadiusServerTableMaxEntries": crRadiusServerTableMaxEntries,
       "crRadiusServerTable": crRadiusServerTable,
       "crRadiusServerEntry": crRadiusServerEntry,
       "crRadiusServerIndex": crRadiusServerIndex,
       "crRadiusServerAddrType": crRadiusServerAddrType,
       "crRadiusServerAddr": crRadiusServerAddr,
       "crRadiusServerAuthPort": crRadiusServerAuthPort,
       "crRadiusServerAcctPort": crRadiusServerAcctPort,
       "crRadiusServerKey": crRadiusServerKey,
       "crRadiusServerType": crRadiusServerType,
       "crRadiusServerMode": crRadiusServerMode,
       "crRadiusServerRowStatus": crRadiusServerRowStatus,
       "crRadiusServerRTTThldNorm": crRadiusServerRTTThldNorm,
       "crRadiusServerRTTThldHi": crRadiusServerRTTThldHi,
       "crRadiusServerRetransThldNorm": crRadiusServerRetransThldNorm,
       "crRadiusServerRetransThldHi": crRadiusServerRetransThldHi,
       "crRadiusAttributesConfig": crRadiusAttributesConfig,
       "crRadiusFramedIpAddrIncluded": crRadiusFramedIpAddrIncluded,
       "crRadiusFramedMtu": crRadiusFramedMtu,
       "crRadiusVlanConfigGroup": crRadiusVlanConfigGroup,
       "crRadiusVlanAssignmentEnabled": crRadiusVlanAssignmentEnabled,
       "crVlanGroupTable": crVlanGroupTable,
       "crVlanGroupEntry": crVlanGroupEntry,
       "crVlanGroupName": crVlanGroupName,
       "crVlanGroupVlansLow": crVlanGroupVlansLow,
       "crVlanGroupVlansHigh": crVlanGroupVlansHigh,
       "crVlanGroupRowStatus": crVlanGroupRowStatus,
       "crRadiusKeepAliveConfig": crRadiusKeepAliveConfig,
       "crRadiusKeepAliveEnabled": crRadiusKeepAliveEnabled,
       "crRadiusKeepAliveInterval": crRadiusKeepAliveInterval,
       "crRadiusKeepAliveServerTable": crRadiusKeepAliveServerTable,
       "crRadiusKeepAliveServerEntry": crRadiusKeepAliveServerEntry,
       "crRadiusKeepAliveServerStatus": crRadiusKeepAliveServerStatus,
       "crRadiusPortAutoInitialize": crRadiusPortAutoInitialize,
       "crRadiusKeepAliveUserName": crRadiusKeepAliveUserName,
       "crRadiusServerNotifCntl": crRadiusServerNotifCntl,
       "crRadiusServerRTTNormNotifEnable": crRadiusServerRTTNormNotifEnable,
       "crRadiusServerRTTHiNotifEnable": crRadiusServerRTTHiNotifEnable,
       "crRadiusServerRetransNormNotifEnable": crRadiusServerRetransNormNotifEnable,
       "crRadiusServerRetransHiNotifEnable": crRadiusServerRetransHiNotifEnable,
       "ciscoRadiusMIBConformance": ciscoRadiusMIBConformance,
       "ciscoRadiusMIBCompliances": ciscoRadiusMIBCompliances,
       "ciscoRadiusMIBCompliance": ciscoRadiusMIBCompliance,
       "ciscoRadiusMIBCompliance2": ciscoRadiusMIBCompliance2,
       "ciscoRadiusMIBCompliance3": ciscoRadiusMIBCompliance3,
       "ciscoRadiusMIBCompliance4": ciscoRadiusMIBCompliance4,
       "ciscoRadiusMIBGroups": ciscoRadiusMIBGroups,
       "crmConfigurationGroup": crmConfigurationGroup,
       "crmAttributesGroup": crmAttributesGroup,
       "crmVlanConfigGroup": crmVlanConfigGroup,
       "crmKeepAliveGroup": crmKeepAliveGroup,
       "crmAutoInitializeConfigGroup": crmAutoInitializeConfigGroup,
       "crmAttributesGroup2": crmAttributesGroup2,
       "crmRadiusKeepAliveUserGroup": crmRadiusKeepAliveUserGroup,
       "crmRadiusServerNotifGroup": crmRadiusServerNotifGroup,
       "crmConfigurationGroupSup1": crmConfigurationGroupSup1,
       "crmRadiusServerNotifCntlGroup": crmRadiusServerNotifCntlGroup,
       "ciscoRadiusMIBNotifications": ciscoRadiusMIBNotifications,
       "crRadiusServerRTTNormNotif": crRadiusServerRTTNormNotif,
       "crRadiusServerRTTHiNotif": crRadiusServerRTTHiNotif,
       "crRadiusServerRetransNormNotif": crRadiusServerRetransNormNotif,
       "crRadiusServerRetransHiNotif": crRadiusServerRetransHiNotif}
)
