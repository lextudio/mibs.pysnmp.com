# SNMP MIB module (RBN-SUBSCRIBER-ACTIVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-SUBSCRIBER-ACTIVE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:02 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnCircuitHandle,
 RbnPercentage,
 RbnPortMediumType) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnCircuitHandle",
    "RbnPercentage",
    "RbnPortMediumType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(vacmContextName,) = mibBuilder.importSymbols(
    "SNMP-VIEW-BASED-ACM-MIB",
    "vacmContextName")

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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "zeroDotZero")

(DateAndTime,
 DisplayString,
 RowPointer,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rbnSubscriberActiveMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27)
)
rbnSubscriberActiveMib.setRevisions(
        ("2013-02-27 00:00",
         "2012-09-04 00:00",
         "2010-02-01 00:00",
         "2009-01-19 18:00",
         "2008-12-03 18:00",
         "2007-05-24 18:00",
         "2007-05-09 18:00",
         "2004-06-28 18:00",
         "2004-02-02 18:00",
         "2003-11-01 18:00",
         "2003-06-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnSubsActiveObjects_ObjectIdentity = ObjectIdentity
rbnSubsActiveObjects = _RbnSubsActiveObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1)
)
_RbnSubsActive_ObjectIdentity = ObjectIdentity
rbnSubsActive = _RbnSubsActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1)
)
_RbnSubsActiveTable_Object = MibTable
rbnSubsActiveTable = _RbnSubsActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbnSubsActiveTable.setStatus("current")
_RbnSubsActiveEntry_Object = MibTableRow
rbnSubsActiveEntry = _RbnSubsActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 1, 1)
)
rbnSubsActiveEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveName"),
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveSessionId"),
)
if mibBuilder.loadTexts:
    rbnSubsActiveEntry.setStatus("current")


class _RbnSubsActiveName_Type(SnmpAdminString):
    """Custom type rbnSubsActiveName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RbnSubsActiveName_Type.__name__ = "SnmpAdminString"
_RbnSubsActiveName_Object = MibTableColumn
rbnSubsActiveName = _RbnSubsActiveName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 1, 1, 1),
    _RbnSubsActiveName_Type()
)
rbnSubsActiveName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubsActiveName.setStatus("current")


class _RbnSubsActiveSessionId_Type(SnmpAdminString):
    """Custom type rbnSubsActiveSessionId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbnSubsActiveSessionId_Type.__name__ = "SnmpAdminString"
_RbnSubsActiveSessionId_Object = MibTableColumn
rbnSubsActiveSessionId = _RbnSubsActiveSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 1, 1, 2),
    _RbnSubsActiveSessionId_Type()
)
rbnSubsActiveSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubsActiveSessionId.setStatus("current")


class _RbnSubsActiveCircuitDescr_Type(SnmpAdminString):
    """Custom type rbnSubsActiveCircuitDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RbnSubsActiveCircuitDescr_Type.__name__ = "SnmpAdminString"
_RbnSubsActiveCircuitDescr_Object = MibTableColumn
rbnSubsActiveCircuitDescr = _RbnSubsActiveCircuitDescr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 1, 1, 3),
    _RbnSubsActiveCircuitDescr_Type()
)
rbnSubsActiveCircuitDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsActiveCircuitDescr.setStatus("current")
_RbnSubsActiveCircuitHandle_Type = RbnCircuitHandle
_RbnSubsActiveCircuitHandle_Object = MibTableColumn
rbnSubsActiveCircuitHandle = _RbnSubsActiveCircuitHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 1, 1, 4),
    _RbnSubsActiveCircuitHandle_Type()
)
rbnSubsActiveCircuitHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsActiveCircuitHandle.setStatus("current")
_RbnSubsActiveStartTime_Type = DateAndTime
_RbnSubsActiveStartTime_Object = MibTableColumn
rbnSubsActiveStartTime = _RbnSubsActiveStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 1, 1, 5),
    _RbnSubsActiveStartTime_Type()
)
rbnSubsActiveStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsActiveStartTime.setStatus("current")
_RbnSubsActiveClear_Type = TruthValue
_RbnSubsActiveClear_Object = MibTableColumn
rbnSubsActiveClear = _RbnSubsActiveClear_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 1, 1, 6),
    _RbnSubsActiveClear_Type()
)
rbnSubsActiveClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubsActiveClear.setStatus("current")
_RbnSubsActiveResend_Type = TruthValue
_RbnSubsActiveResend_Object = MibTableColumn
rbnSubsActiveResend = _RbnSubsActiveResend_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 1, 1, 7),
    _RbnSubsActiveResend_Type()
)
rbnSubsActiveResend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubsActiveResend.setStatus("current")
_RbnSubsActiveNasPortType_Type = Unsigned32
_RbnSubsActiveNasPortType_Object = MibTableColumn
rbnSubsActiveNasPortType = _RbnSubsActiveNasPortType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 1, 1, 8),
    _RbnSubsActiveNasPortType_Type()
)
rbnSubsActiveNasPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsActiveNasPortType.setStatus("current")
_RbnSubsActiveMediumType_Type = RbnPortMediumType
_RbnSubsActiveMediumType_Object = MibTableColumn
rbnSubsActiveMediumType = _RbnSubsActiveMediumType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 1, 1, 9),
    _RbnSubsActiveMediumType_Type()
)
rbnSubsActiveMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsActiveMediumType.setStatus("current")
_RbnSubsActiveResendSvcAcct_Type = TruthValue
_RbnSubsActiveResendSvcAcct_Object = MibTableColumn
rbnSubsActiveResendSvcAcct = _RbnSubsActiveResendSvcAcct_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 1, 1, 10),
    _RbnSubsActiveResendSvcAcct_Type()
)
rbnSubsActiveResendSvcAcct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubsActiveResendSvcAcct.setStatus("current")
_RbnSubsActiveIpTable_Object = MibTable
rbnSubsActiveIpTable = _RbnSubsActiveIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rbnSubsActiveIpTable.setStatus("current")
_RbnSubsActiveIpEntry_Object = MibTableRow
rbnSubsActiveIpEntry = _RbnSubsActiveIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 2, 1)
)
rbnSubsActiveIpEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveName"),
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveSessionId"),
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveAddrType"),
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveAddr"),
)
if mibBuilder.loadTexts:
    rbnSubsActiveIpEntry.setStatus("current")
_RbnSubsActiveAddrType_Type = InetAddressType
_RbnSubsActiveAddrType_Object = MibTableColumn
rbnSubsActiveAddrType = _RbnSubsActiveAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 2, 1, 1),
    _RbnSubsActiveAddrType_Type()
)
rbnSubsActiveAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubsActiveAddrType.setStatus("current")


class _RbnSubsActiveAddr_Type(InetAddress):
    """Custom type rbnSubsActiveAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_RbnSubsActiveAddr_Type.__name__ = "InetAddress"
_RbnSubsActiveAddr_Object = MibTableColumn
rbnSubsActiveAddr = _RbnSubsActiveAddr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 2, 1, 2),
    _RbnSubsActiveAddr_Type()
)
rbnSubsActiveAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsActiveAddr.setStatus("current")
_RbnSubsClear_ObjectIdentity = ObjectIdentity
rbnSubsClear = _RbnSubsClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 3)
)


class _RbnSubsClearSubscriberName_Type(SnmpAdminString):
    """Custom type rbnSubsClearSubscriberName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbnSubsClearSubscriberName_Type.__name__ = "SnmpAdminString"
_RbnSubsClearSubscriberName_Object = MibScalar
rbnSubsClearSubscriberName = _RbnSubsClearSubscriberName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 3, 1),
    _RbnSubsClearSubscriberName_Type()
)
rbnSubsClearSubscriberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubsClearSubscriberName.setStatus("current")


class _RbnSubsClearSessionId_Type(SnmpAdminString):
    """Custom type rbnSubsClearSessionId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbnSubsClearSessionId_Type.__name__ = "SnmpAdminString"
_RbnSubsClearSessionId_Object = MibScalar
rbnSubsClearSessionId = _RbnSubsClearSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 3, 2),
    _RbnSubsClearSessionId_Type()
)
rbnSubsClearSessionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubsClearSessionId.setStatus("current")


class _RbnSubsBounceName_Type(SnmpAdminString):
    """Custom type rbnSubsBounceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbnSubsBounceName_Type.__name__ = "SnmpAdminString"
_RbnSubsBounceName_Object = MibScalar
rbnSubsBounceName = _RbnSubsBounceName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 3, 3),
    _RbnSubsBounceName_Type()
)
rbnSubsBounceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubsBounceName.setStatus("current")


class _RbnSubsBounceSessionId_Type(SnmpAdminString):
    """Custom type rbnSubsBounceSessionId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbnSubsBounceSessionId_Type.__name__ = "SnmpAdminString"
_RbnSubsBounceSessionId_Object = MibScalar
rbnSubsBounceSessionId = _RbnSubsBounceSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 3, 4),
    _RbnSubsBounceSessionId_Type()
)
rbnSubsBounceSessionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubsBounceSessionId.setStatus("current")
_RbnSubsReauthRadiusIndex_Type = Unsigned32
_RbnSubsReauthRadiusIndex_Object = MibScalar
rbnSubsReauthRadiusIndex = _RbnSubsReauthRadiusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 3, 5),
    _RbnSubsReauthRadiusIndex_Type()
)
rbnSubsReauthRadiusIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubsReauthRadiusIndex.setStatus("current")


class _RbnSubsReauthRadiusID_Type(OctetString):
    """Custom type rbnSubsReauthRadiusID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_RbnSubsReauthRadiusID_Type.__name__ = "OctetString"
_RbnSubsReauthRadiusID_Object = MibScalar
rbnSubsReauthRadiusID = _RbnSubsReauthRadiusID_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 3, 6),
    _RbnSubsReauthRadiusID_Type()
)
rbnSubsReauthRadiusID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubsReauthRadiusID.setStatus("current")


class _RbnSubsReauthName_Type(SnmpAdminString):
    """Custom type rbnSubsReauthName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbnSubsReauthName_Type.__name__ = "SnmpAdminString"
_RbnSubsReauthName_Object = MibScalar
rbnSubsReauthName = _RbnSubsReauthName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 3, 7),
    _RbnSubsReauthName_Type()
)
rbnSubsReauthName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubsReauthName.setStatus("current")


class _RbnSubsReauthSessionId_Type(SnmpAdminString):
    """Custom type rbnSubsReauthSessionId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbnSubsReauthSessionId_Type.__name__ = "SnmpAdminString"
_RbnSubsReauthSessionId_Object = MibScalar
rbnSubsReauthSessionId = _RbnSubsReauthSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 3, 8),
    _RbnSubsReauthSessionId_Type()
)
rbnSubsReauthSessionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubsReauthSessionId.setStatus("current")
_RbnSubsClearReason_Type = Unsigned32
_RbnSubsClearReason_Object = MibScalar
rbnSubsClearReason = _RbnSubsClearReason_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 3, 9),
    _RbnSubsClearReason_Type()
)
rbnSubsClearReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubsClearReason.setStatus("current")
_RbnSubsServiceVolumeTable_Object = MibTable
rbnSubsServiceVolumeTable = _RbnSubsServiceVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4)
)
if mibBuilder.loadTexts:
    rbnSubsServiceVolumeTable.setStatus("current")
_RbnSubsServiceVolumeEntry_Object = MibTableRow
rbnSubsServiceVolumeEntry = _RbnSubsServiceVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4, 1)
)
rbnSubsServiceVolumeEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveName"),
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveSessionId"),
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceIndex"),
)
if mibBuilder.loadTexts:
    rbnSubsServiceVolumeEntry.setStatus("current")
_RbnSubsServiceVolumeLimitIn_Type = Unsigned32
_RbnSubsServiceVolumeLimitIn_Object = MibTableColumn
rbnSubsServiceVolumeLimitIn = _RbnSubsServiceVolumeLimitIn_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4, 1, 1),
    _RbnSubsServiceVolumeLimitIn_Type()
)
rbnSubsServiceVolumeLimitIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubsServiceVolumeLimitIn.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsServiceVolumeLimitIn.setUnits("KiloBytes")
_RbnSubsServiceVolumeLimitOut_Type = Unsigned32
_RbnSubsServiceVolumeLimitOut_Object = MibTableColumn
rbnSubsServiceVolumeLimitOut = _RbnSubsServiceVolumeLimitOut_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4, 1, 2),
    _RbnSubsServiceVolumeLimitOut_Type()
)
rbnSubsServiceVolumeLimitOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubsServiceVolumeLimitOut.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsServiceVolumeLimitOut.setUnits("KiloBytes")
_RbnSubsServiceActiveTime_Type = TimeStamp
_RbnSubsServiceActiveTime_Object = MibTableColumn
rbnSubsServiceActiveTime = _RbnSubsServiceActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4, 1, 3),
    _RbnSubsServiceActiveTime_Type()
)
rbnSubsServiceActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsServiceActiveTime.setStatus("current")
_RbnSubsServiceVolumeOctetsIn_Type = Counter64
_RbnSubsServiceVolumeOctetsIn_Object = MibTableColumn
rbnSubsServiceVolumeOctetsIn = _RbnSubsServiceVolumeOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4, 1, 4),
    _RbnSubsServiceVolumeOctetsIn_Type()
)
rbnSubsServiceVolumeOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsServiceVolumeOctetsIn.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsServiceVolumeOctetsIn.setUnits("Octets")
_RbnSubsServiceVolumeOctetsOut_Type = Counter64
_RbnSubsServiceVolumeOctetsOut_Object = MibTableColumn
rbnSubsServiceVolumeOctetsOut = _RbnSubsServiceVolumeOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4, 1, 5),
    _RbnSubsServiceVolumeOctetsOut_Type()
)
rbnSubsServiceVolumeOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsServiceVolumeOctetsOut.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsServiceVolumeOctetsOut.setUnits("Octets")
_RbnSubsServiceVolumePktsIn_Type = Counter64
_RbnSubsServiceVolumePktsIn_Object = MibTableColumn
rbnSubsServiceVolumePktsIn = _RbnSubsServiceVolumePktsIn_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4, 1, 6),
    _RbnSubsServiceVolumePktsIn_Type()
)
rbnSubsServiceVolumePktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsServiceVolumePktsIn.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsServiceVolumePktsIn.setUnits("packets")
_RbnSubsServiceVolumePktsOut_Type = Counter64
_RbnSubsServiceVolumePktsOut_Object = MibTableColumn
rbnSubsServiceVolumePktsOut = _RbnSubsServiceVolumePktsOut_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4, 1, 7),
    _RbnSubsServiceVolumePktsOut_Type()
)
rbnSubsServiceVolumePktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsServiceVolumePktsOut.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsServiceVolumePktsOut.setUnits("packets")
_RbnSubsServiceIPv4VolumeOctetsIn_Type = Counter64
_RbnSubsServiceIPv4VolumeOctetsIn_Object = MibTableColumn
rbnSubsServiceIPv4VolumeOctetsIn = _RbnSubsServiceIPv4VolumeOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4, 1, 8),
    _RbnSubsServiceIPv4VolumeOctetsIn_Type()
)
rbnSubsServiceIPv4VolumeOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsServiceIPv4VolumeOctetsIn.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsServiceIPv4VolumeOctetsIn.setUnits("Octets")
_RbnSubsServiceIPv4VolumeOctetsOut_Type = Counter64
_RbnSubsServiceIPv4VolumeOctetsOut_Object = MibTableColumn
rbnSubsServiceIPv4VolumeOctetsOut = _RbnSubsServiceIPv4VolumeOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4, 1, 9),
    _RbnSubsServiceIPv4VolumeOctetsOut_Type()
)
rbnSubsServiceIPv4VolumeOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsServiceIPv4VolumeOctetsOut.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsServiceIPv4VolumeOctetsOut.setUnits("Octets")
_RbnSubsServiceIPv6VolumeOctetsIn_Type = Counter64
_RbnSubsServiceIPv6VolumeOctetsIn_Object = MibTableColumn
rbnSubsServiceIPv6VolumeOctetsIn = _RbnSubsServiceIPv6VolumeOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4, 1, 10),
    _RbnSubsServiceIPv6VolumeOctetsIn_Type()
)
rbnSubsServiceIPv6VolumeOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsServiceIPv6VolumeOctetsIn.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsServiceIPv6VolumeOctetsIn.setUnits("Octets")
_RbnSubsServiceIPv6VolumeOctetsOut_Type = Counter64
_RbnSubsServiceIPv6VolumeOctetsOut_Object = MibTableColumn
rbnSubsServiceIPv6VolumeOctetsOut = _RbnSubsServiceIPv6VolumeOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4, 1, 11),
    _RbnSubsServiceIPv6VolumeOctetsOut_Type()
)
rbnSubsServiceIPv6VolumeOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsServiceIPv6VolumeOctetsOut.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsServiceIPv6VolumeOctetsOut.setUnits("Octets")
_RbnSubsServiceIPv4VolumePktsIn_Type = Counter64
_RbnSubsServiceIPv4VolumePktsIn_Object = MibTableColumn
rbnSubsServiceIPv4VolumePktsIn = _RbnSubsServiceIPv4VolumePktsIn_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4, 1, 12),
    _RbnSubsServiceIPv4VolumePktsIn_Type()
)
rbnSubsServiceIPv4VolumePktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsServiceIPv4VolumePktsIn.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsServiceIPv4VolumePktsIn.setUnits("packets")
_RbnSubsServiceIPv4VolumePktsOut_Type = Counter64
_RbnSubsServiceIPv4VolumePktsOut_Object = MibTableColumn
rbnSubsServiceIPv4VolumePktsOut = _RbnSubsServiceIPv4VolumePktsOut_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4, 1, 13),
    _RbnSubsServiceIPv4VolumePktsOut_Type()
)
rbnSubsServiceIPv4VolumePktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsServiceIPv4VolumePktsOut.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsServiceIPv4VolumePktsOut.setUnits("packets")
_RbnSubsServiceIPv6VolumePktsIn_Type = Counter64
_RbnSubsServiceIPv6VolumePktsIn_Object = MibTableColumn
rbnSubsServiceIPv6VolumePktsIn = _RbnSubsServiceIPv6VolumePktsIn_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4, 1, 14),
    _RbnSubsServiceIPv6VolumePktsIn_Type()
)
rbnSubsServiceIPv6VolumePktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsServiceIPv6VolumePktsIn.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsServiceIPv6VolumePktsIn.setUnits("packets")
_RbnSubsServiceIPv6VolumePktsOut_Type = Counter64
_RbnSubsServiceIPv6VolumePktsOut_Object = MibTableColumn
rbnSubsServiceIPv6VolumePktsOut = _RbnSubsServiceIPv6VolumePktsOut_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 4, 1, 15),
    _RbnSubsServiceIPv6VolumePktsOut_Type()
)
rbnSubsServiceIPv6VolumePktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsServiceIPv6VolumePktsOut.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsServiceIPv6VolumePktsOut.setUnits("packets")
_RbnSubsServicesTable_Object = MibTable
rbnSubsServicesTable = _RbnSubsServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 5)
)
if mibBuilder.loadTexts:
    rbnSubsServicesTable.setStatus("current")
_RbnSubsServicesEntry_Object = MibTableRow
rbnSubsServicesEntry = _RbnSubsServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 5, 1)
)
rbnSubsServicesEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceIndex"),
)
if mibBuilder.loadTexts:
    rbnSubsServicesEntry.setStatus("current")


class _RbnSubsServiceIndex_Type(Integer32):
    """Custom type rbnSubsServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RbnSubsServiceIndex_Type.__name__ = "Integer32"
_RbnSubsServiceIndex_Object = MibTableColumn
rbnSubsServiceIndex = _RbnSubsServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 5, 1, 1),
    _RbnSubsServiceIndex_Type()
)
rbnSubsServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubsServiceIndex.setStatus("current")


class _RbnSubsServiceName_Type(SnmpAdminString):
    """Custom type rbnSubsServiceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RbnSubsServiceName_Type.__name__ = "SnmpAdminString"
_RbnSubsServiceName_Object = MibTableColumn
rbnSubsServiceName = _RbnSubsServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 5, 1, 2),
    _RbnSubsServiceName_Type()
)
rbnSubsServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsServiceName.setStatus("current")


class _RbnSubsServiceTag_Type(SnmpAdminString):
    """Custom type rbnSubsServiceTag based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbnSubsServiceTag_Type.__name__ = "SnmpAdminString"
_RbnSubsServiceTag_Object = MibTableColumn
rbnSubsServiceTag = _RbnSubsServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 5, 1, 3),
    _RbnSubsServiceTag_Type()
)
rbnSubsServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsServiceTag.setStatus("current")
_RbnSubsActiveSessionTable_Object = MibTable
rbnSubsActiveSessionTable = _RbnSubsActiveSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 6)
)
if mibBuilder.loadTexts:
    rbnSubsActiveSessionTable.setStatus("current")
_RbnSubsActiveSessionEntry_Object = MibTableRow
rbnSubsActiveSessionEntry = _RbnSubsActiveSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 6, 1)
)
rbnSubsActiveSessionEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveSessionId"),
)
if mibBuilder.loadTexts:
    rbnSubsActiveSessionEntry.setStatus("current")


class _RbnSubsActiveSessionSubscriberName_Type(SnmpAdminString):
    """Custom type rbnSubsActiveSessionSubscriberName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_RbnSubsActiveSessionSubscriberName_Type.__name__ = "SnmpAdminString"
_RbnSubsActiveSessionSubscriberName_Object = MibTableColumn
rbnSubsActiveSessionSubscriberName = _RbnSubsActiveSessionSubscriberName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 6, 1, 1),
    _RbnSubsActiveSessionSubscriberName_Type()
)
rbnSubsActiveSessionSubscriberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsActiveSessionSubscriberName.setStatus("current")


class _RbnSubsActiveSessionPointer_Type(RowPointer):
    """Custom type rbnSubsActiveSessionPointer based on RowPointer"""
    defaultValue = (0, 0)


_RbnSubsActiveSessionPointer_Object = MibTableColumn
rbnSubsActiveSessionPointer = _RbnSubsActiveSessionPointer_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 6, 1, 2),
    _RbnSubsActiveSessionPointer_Type()
)
rbnSubsActiveSessionPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsActiveSessionPointer.setStatus("current")
_RbnSubsActiveIpAddrTable_Object = MibTable
rbnSubsActiveIpAddrTable = _RbnSubsActiveIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 7)
)
if mibBuilder.loadTexts:
    rbnSubsActiveIpAddrTable.setStatus("current")
_RbnSubsActiveIpAddrEntry_Object = MibTableRow
rbnSubsActiveIpAddrEntry = _RbnSubsActiveIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 7, 1)
)
rbnSubsActiveIpAddrEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveSessionId"),
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveIpAddrType"),
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveIpAddr"),
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveIpPfxLen"),
)
if mibBuilder.loadTexts:
    rbnSubsActiveIpAddrEntry.setStatus("current")
_RbnSubsActiveIpAddrType_Type = InetAddressType
_RbnSubsActiveIpAddrType_Object = MibTableColumn
rbnSubsActiveIpAddrType = _RbnSubsActiveIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 7, 1, 1),
    _RbnSubsActiveIpAddrType_Type()
)
rbnSubsActiveIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsActiveIpAddrType.setStatus("current")
_RbnSubsActiveIpAddr_Type = InetAddress
_RbnSubsActiveIpAddr_Object = MibTableColumn
rbnSubsActiveIpAddr = _RbnSubsActiveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 7, 1, 2),
    _RbnSubsActiveIpAddr_Type()
)
rbnSubsActiveIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsActiveIpAddr.setStatus("current")
_RbnSubsActiveIpPfxLen_Type = InetAddressPrefixLength
_RbnSubsActiveIpPfxLen_Object = MibTableColumn
rbnSubsActiveIpPfxLen = _RbnSubsActiveIpPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 7, 1, 3),
    _RbnSubsActiveIpPfxLen_Type()
)
rbnSubsActiveIpPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsActiveIpPfxLen.setStatus("current")
_RbnSubsActiveIpAddrDescr_Type = SnmpAdminString
_RbnSubsActiveIpAddrDescr_Object = MibTableColumn
rbnSubsActiveIpAddrDescr = _RbnSubsActiveIpAddrDescr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 1, 7, 1, 4),
    _RbnSubsActiveIpAddrDescr_Type()
)
rbnSubsActiveIpAddrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsActiveIpAddrDescr.setStatus("current")
_RbnSubsStats_ObjectIdentity = ObjectIdentity
rbnSubsStats = _RbnSubsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2)
)
_RbnSubsCntxtCountTable_Object = MibTable
rbnSubsCntxtCountTable = _RbnSubsCntxtCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rbnSubsCntxtCountTable.setStatus("current")
_RbnSubsCntxtCountEntry_Object = MibTableRow
rbnSubsCntxtCountEntry = _RbnSubsCntxtCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 1, 1)
)
rbnSubsCntxtCountEntry.setIndexNames(
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmContextName"),
)
if mibBuilder.loadTexts:
    rbnSubsCntxtCountEntry.setStatus("current")
_RbnSubsCntxtCount_Type = Gauge32
_RbnSubsCntxtCount_Object = MibTableColumn
rbnSubsCntxtCount = _RbnSubsCntxtCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 1, 1, 1),
    _RbnSubsCntxtCount_Type()
)
rbnSubsCntxtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsCntxtCount.setStatus("current")
_RbnSubsCntxtIp4OnlyCount_Type = Gauge32
_RbnSubsCntxtIp4OnlyCount_Object = MibTableColumn
rbnSubsCntxtIp4OnlyCount = _RbnSubsCntxtIp4OnlyCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 1, 1, 2),
    _RbnSubsCntxtIp4OnlyCount_Type()
)
rbnSubsCntxtIp4OnlyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsCntxtIp4OnlyCount.setStatus("current")
_RbnSubsCntxtIp6OnlyCount_Type = Gauge32
_RbnSubsCntxtIp6OnlyCount_Object = MibTableColumn
rbnSubsCntxtIp6OnlyCount = _RbnSubsCntxtIp6OnlyCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 1, 1, 3),
    _RbnSubsCntxtIp6OnlyCount_Type()
)
rbnSubsCntxtIp6OnlyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsCntxtIp6OnlyCount.setStatus("current")
_RbnSubsCntxtDualCount_Type = Gauge32
_RbnSubsCntxtDualCount_Object = MibTableColumn
rbnSubsCntxtDualCount = _RbnSubsCntxtDualCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 1, 1, 4),
    _RbnSubsCntxtDualCount_Type()
)
rbnSubsCntxtDualCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsCntxtDualCount.setStatus("current")
_RbnSubsCntxtLacCount_Type = Gauge32
_RbnSubsCntxtLacCount_Object = MibTableColumn
rbnSubsCntxtLacCount = _RbnSubsCntxtLacCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 1, 1, 5),
    _RbnSubsCntxtLacCount_Type()
)
rbnSubsCntxtLacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsCntxtLacCount.setStatus("current")
_RbnSubsEncapsCountTable_Object = MibTable
rbnSubsEncapsCountTable = _RbnSubsEncapsCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rbnSubsEncapsCountTable.setStatus("current")
_RbnSubsEncapsCountEntry_Object = MibTableRow
rbnSubsEncapsCountEntry = _RbnSubsEncapsCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 2, 1)
)
rbnSubsEncapsCountEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsEncapsulationType"),
)
if mibBuilder.loadTexts:
    rbnSubsEncapsCountEntry.setStatus("current")


class _RbnSubsEncapsulationType_Type(Integer32):
    """Custom type rbnSubsEncapsulationType based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("bridged1483", 3),
          ("bridged1490", 8),
          ("clips", 12),
          ("dot1q1483", 6),
          ("dot1q1490", 11),
          ("dot1qEnet", 7),
          ("multi1483", 5),
          ("multi1490", 10),
          ("other", 255),
          ("ppp", 1),
          ("pppoe", 2),
          ("routed1483", 4),
          ("routed1490", 9))
    )


_RbnSubsEncapsulationType_Type.__name__ = "Integer32"
_RbnSubsEncapsulationType_Object = MibTableColumn
rbnSubsEncapsulationType = _RbnSubsEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 2, 1, 1),
    _RbnSubsEncapsulationType_Type()
)
rbnSubsEncapsulationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubsEncapsulationType.setStatus("current")
_RbnSubsEncapsCount_Type = Gauge32
_RbnSubsEncapsCount_Object = MibTableColumn
rbnSubsEncapsCount = _RbnSubsEncapsCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 2, 1, 2),
    _RbnSubsEncapsCount_Type()
)
rbnSubsEncapsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsEncapsCount.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsEncapsCount.setUnits("subscribers")
_RbnSubsStatsTable_Object = MibTable
rbnSubsStatsTable = _RbnSubsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3)
)
if mibBuilder.loadTexts:
    rbnSubsStatsTable.setStatus("current")
_RbnSubsStatsEntry_Object = MibTableRow
rbnSubsStatsEntry = _RbnSubsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1)
)
rbnSubsStatsEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveName"),
    (0, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveSessionId"),
)
if mibBuilder.loadTexts:
    rbnSubsStatsEntry.setStatus("current")
_RbnSubsOctetsSent_Type = Counter64
_RbnSubsOctetsSent_Object = MibTableColumn
rbnSubsOctetsSent = _RbnSubsOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 1),
    _RbnSubsOctetsSent_Type()
)
rbnSubsOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsOctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsOctetsSent.setUnits("octets")
_RbnSubsOctetsReceived_Type = Counter64
_RbnSubsOctetsReceived_Object = MibTableColumn
rbnSubsOctetsReceived = _RbnSubsOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 2),
    _RbnSubsOctetsReceived_Type()
)
rbnSubsOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsOctetsReceived.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsOctetsReceived.setUnits("octets")
_RbnSubsPktsSent_Type = Counter64
_RbnSubsPktsSent_Object = MibTableColumn
rbnSubsPktsSent = _RbnSubsPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 3),
    _RbnSubsPktsSent_Type()
)
rbnSubsPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsPktsSent.setUnits("packets")
_RbnSubsPktsReceived_Type = Counter64
_RbnSubsPktsReceived_Object = MibTableColumn
rbnSubsPktsReceived = _RbnSubsPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 4),
    _RbnSubsPktsReceived_Type()
)
rbnSubsPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsPktsReceived.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsPktsReceived.setUnits("packets")
_RbnSubsXmitOctetsDropped_Type = Counter32
_RbnSubsXmitOctetsDropped_Object = MibTableColumn
rbnSubsXmitOctetsDropped = _RbnSubsXmitOctetsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 5),
    _RbnSubsXmitOctetsDropped_Type()
)
rbnSubsXmitOctetsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsXmitOctetsDropped.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsXmitOctetsDropped.setUnits("octets")
_RbnSubsXmitPktsDropped_Type = Counter32
_RbnSubsXmitPktsDropped_Object = MibTableColumn
rbnSubsXmitPktsDropped = _RbnSubsXmitPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 6),
    _RbnSubsXmitPktsDropped_Type()
)
rbnSubsXmitPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsXmitPktsDropped.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsXmitPktsDropped.setUnits("packets")
_RbnSubsMcastOctetsSent_Type = Counter64
_RbnSubsMcastOctetsSent_Object = MibTableColumn
rbnSubsMcastOctetsSent = _RbnSubsMcastOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 7),
    _RbnSubsMcastOctetsSent_Type()
)
rbnSubsMcastOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsMcastOctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsMcastOctetsSent.setUnits("octets")
_RbnSubsMcastOctetsReceived_Type = Counter64
_RbnSubsMcastOctetsReceived_Object = MibTableColumn
rbnSubsMcastOctetsReceived = _RbnSubsMcastOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 8),
    _RbnSubsMcastOctetsReceived_Type()
)
rbnSubsMcastOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsMcastOctetsReceived.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsMcastOctetsReceived.setUnits("octets")
_RbnSubsMcastPktsSent_Type = Counter64
_RbnSubsMcastPktsSent_Object = MibTableColumn
rbnSubsMcastPktsSent = _RbnSubsMcastPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 9),
    _RbnSubsMcastPktsSent_Type()
)
rbnSubsMcastPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsMcastPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsMcastPktsSent.setUnits("packets")
_RbnSubsMcastPktsReceived_Type = Counter64
_RbnSubsMcastPktsReceived_Object = MibTableColumn
rbnSubsMcastPktsReceived = _RbnSubsMcastPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 10),
    _RbnSubsMcastPktsReceived_Type()
)
rbnSubsMcastPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsMcastPktsReceived.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsMcastPktsReceived.setUnits("packets")
_RbnSubsIPv4OctetsSent_Type = Counter64
_RbnSubsIPv4OctetsSent_Object = MibTableColumn
rbnSubsIPv4OctetsSent = _RbnSubsIPv4OctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 11),
    _RbnSubsIPv4OctetsSent_Type()
)
rbnSubsIPv4OctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsIPv4OctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsIPv4OctetsSent.setUnits("octets")
_RbnSubsIPv4OctetsReceived_Type = Counter64
_RbnSubsIPv4OctetsReceived_Object = MibTableColumn
rbnSubsIPv4OctetsReceived = _RbnSubsIPv4OctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 12),
    _RbnSubsIPv4OctetsReceived_Type()
)
rbnSubsIPv4OctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsIPv4OctetsReceived.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsIPv4OctetsReceived.setUnits("octets")
_RbnSubsIPv6OctetsSent_Type = Counter64
_RbnSubsIPv6OctetsSent_Object = MibTableColumn
rbnSubsIPv6OctetsSent = _RbnSubsIPv6OctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 13),
    _RbnSubsIPv6OctetsSent_Type()
)
rbnSubsIPv6OctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsIPv6OctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsIPv6OctetsSent.setUnits("octets")
_RbnSubsIPv6OctetsReceived_Type = Counter64
_RbnSubsIPv6OctetsReceived_Object = MibTableColumn
rbnSubsIPv6OctetsReceived = _RbnSubsIPv6OctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 14),
    _RbnSubsIPv6OctetsReceived_Type()
)
rbnSubsIPv6OctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsIPv6OctetsReceived.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsIPv6OctetsReceived.setUnits("octets")
_RbnSubsIPv4PktsSent_Type = Counter64
_RbnSubsIPv4PktsSent_Object = MibTableColumn
rbnSubsIPv4PktsSent = _RbnSubsIPv4PktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 15),
    _RbnSubsIPv4PktsSent_Type()
)
rbnSubsIPv4PktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsIPv4PktsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsIPv4PktsSent.setUnits("packets")
_RbnSubsIPv4PktsReceived_Type = Counter64
_RbnSubsIPv4PktsReceived_Object = MibTableColumn
rbnSubsIPv4PktsReceived = _RbnSubsIPv4PktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 16),
    _RbnSubsIPv4PktsReceived_Type()
)
rbnSubsIPv4PktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsIPv4PktsReceived.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsIPv4PktsReceived.setUnits("packets")
_RbnSubsIPv6PktsSent_Type = Counter64
_RbnSubsIPv6PktsSent_Object = MibTableColumn
rbnSubsIPv6PktsSent = _RbnSubsIPv6PktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 17),
    _RbnSubsIPv6PktsSent_Type()
)
rbnSubsIPv6PktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsIPv6PktsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsIPv6PktsSent.setUnits("packets")
_RbnSubsIPv6PktsReceived_Type = Counter64
_RbnSubsIPv6PktsReceived_Object = MibTableColumn
rbnSubsIPv6PktsReceived = _RbnSubsIPv6PktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 18),
    _RbnSubsIPv6PktsReceived_Type()
)
rbnSubsIPv6PktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsIPv6PktsReceived.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsIPv6PktsReceived.setUnits("packets")
_RbnSubsIPv4McastOctetsSent_Type = Counter64
_RbnSubsIPv4McastOctetsSent_Object = MibTableColumn
rbnSubsIPv4McastOctetsSent = _RbnSubsIPv4McastOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 19),
    _RbnSubsIPv4McastOctetsSent_Type()
)
rbnSubsIPv4McastOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsIPv4McastOctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsIPv4McastOctetsSent.setUnits("octets")
_RbnSubsIPv4McastOctetsReceived_Type = Counter64
_RbnSubsIPv4McastOctetsReceived_Object = MibTableColumn
rbnSubsIPv4McastOctetsReceived = _RbnSubsIPv4McastOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 20),
    _RbnSubsIPv4McastOctetsReceived_Type()
)
rbnSubsIPv4McastOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsIPv4McastOctetsReceived.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsIPv4McastOctetsReceived.setUnits("octets")
_RbnSubsIPv6McastOctetsSent_Type = Counter64
_RbnSubsIPv6McastOctetsSent_Object = MibTableColumn
rbnSubsIPv6McastOctetsSent = _RbnSubsIPv6McastOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 21),
    _RbnSubsIPv6McastOctetsSent_Type()
)
rbnSubsIPv6McastOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsIPv6McastOctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsIPv6McastOctetsSent.setUnits("octets")
_RbnSubsIPv6McastOctetsReceived_Type = Counter64
_RbnSubsIPv6McastOctetsReceived_Object = MibTableColumn
rbnSubsIPv6McastOctetsReceived = _RbnSubsIPv6McastOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 22),
    _RbnSubsIPv6McastOctetsReceived_Type()
)
rbnSubsIPv6McastOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsIPv6McastOctetsReceived.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsIPv6McastOctetsReceived.setUnits("octets")
_RbnSubsIPv4McastPktsSent_Type = Counter64
_RbnSubsIPv4McastPktsSent_Object = MibTableColumn
rbnSubsIPv4McastPktsSent = _RbnSubsIPv4McastPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 23),
    _RbnSubsIPv4McastPktsSent_Type()
)
rbnSubsIPv4McastPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsIPv4McastPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsIPv4McastPktsSent.setUnits("packets")
_RbnSubsIPv4McastPktsReceived_Type = Counter64
_RbnSubsIPv4McastPktsReceived_Object = MibTableColumn
rbnSubsIPv4McastPktsReceived = _RbnSubsIPv4McastPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 24),
    _RbnSubsIPv4McastPktsReceived_Type()
)
rbnSubsIPv4McastPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsIPv4McastPktsReceived.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsIPv4McastPktsReceived.setUnits("packets")
_RbnSubsIPv6McastPktsSent_Type = Counter64
_RbnSubsIPv6McastPktsSent_Object = MibTableColumn
rbnSubsIPv6McastPktsSent = _RbnSubsIPv6McastPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 25),
    _RbnSubsIPv6McastPktsSent_Type()
)
rbnSubsIPv6McastPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsIPv6McastPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsIPv6McastPktsSent.setUnits("packets")
_RbnSubsIPv6McastPktsReceived_Type = Counter64
_RbnSubsIPv6McastPktsReceived_Object = MibTableColumn
rbnSubsIPv6McastPktsReceived = _RbnSubsIPv6McastPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 3, 1, 26),
    _RbnSubsIPv6McastPktsReceived_Type()
)
rbnSubsIPv6McastPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsIPv6McastPktsReceived.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsIPv6McastPktsReceived.setUnits("packets")
_RbnSubsProfileCountTable_Object = MibTable
rbnSubsProfileCountTable = _RbnSubsProfileCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 4)
)
if mibBuilder.loadTexts:
    rbnSubsProfileCountTable.setStatus("current")
_RbnSubsProfileCountEntry_Object = MibTableRow
rbnSubsProfileCountEntry = _RbnSubsProfileCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 4, 1)
)
rbnSubsProfileCountEntry.setIndexNames(
    (1, "RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsProfileName"),
)
if mibBuilder.loadTexts:
    rbnSubsProfileCountEntry.setStatus("current")


class _RbnSubsProfileName_Type(SnmpAdminString):
    """Custom type rbnSubsProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RbnSubsProfileName_Type.__name__ = "SnmpAdminString"
_RbnSubsProfileName_Object = MibTableColumn
rbnSubsProfileName = _RbnSubsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 4, 1, 1),
    _RbnSubsProfileName_Type()
)
rbnSubsProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubsProfileName.setStatus("current")
_RbnSubsProfileCount_Type = Gauge32
_RbnSubsProfileCount_Object = MibTableColumn
rbnSubsProfileCount = _RbnSubsProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 4, 1, 2),
    _RbnSubsProfileCount_Type()
)
rbnSubsProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsProfileCount.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubsProfileCount.setUnits("subscribers")
_RbnSubsLicense_ObjectIdentity = ObjectIdentity
rbnSubsLicense = _RbnSubsLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 5)
)
_RbnSubsMaxSupportedSessions_Type = Gauge32
_RbnSubsMaxSupportedSessions_Object = MibScalar
rbnSubsMaxSupportedSessions = _RbnSubsMaxSupportedSessions_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 5, 1),
    _RbnSubsMaxSupportedSessions_Type()
)
rbnSubsMaxSupportedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsMaxSupportedSessions.setStatus("current")
_RbnSubsLicensedSessions_Type = Gauge32
_RbnSubsLicensedSessions_Object = MibScalar
rbnSubsLicensedSessions = _RbnSubsLicensedSessions_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 5, 2),
    _RbnSubsLicensedSessions_Type()
)
rbnSubsLicensedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsLicensedSessions.setStatus("current")
_RbnSubsActiveSessions_Type = Gauge32
_RbnSubsActiveSessions_Object = MibScalar
rbnSubsActiveSessions = _RbnSubsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 5, 3),
    _RbnSubsActiveSessions_Type()
)
rbnSubsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsActiveSessions.setStatus("current")
_RbnSubsCapacityPercentageUsed_Type = RbnPercentage
_RbnSubsCapacityPercentageUsed_Object = MibScalar
rbnSubsCapacityPercentageUsed = _RbnSubsCapacityPercentageUsed_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 2, 5, 4),
    _RbnSubsCapacityPercentageUsed_Type()
)
rbnSubsCapacityPercentageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubsCapacityPercentageUsed.setStatus("current")
_RbnSubsNotify_ObjectIdentity = ObjectIdentity
rbnSubsNotify = _RbnSubsNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 3)
)


class _RbnSubsNotifyEnable_Type(TruthValue):
    """Custom type rbnSubsNotifyEnable based on TruthValue"""


_RbnSubsNotifyEnable_Object = MibScalar
rbnSubsNotifyEnable = _RbnSubsNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 3, 1),
    _RbnSubsNotifyEnable_Type()
)
rbnSubsNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubsNotifyEnable.setStatus("current")
_RbnSubsConfigErrorMsgs_Type = SnmpAdminString
_RbnSubsConfigErrorMsgs_Object = MibScalar
rbnSubsConfigErrorMsgs = _RbnSubsConfigErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 1, 3, 2),
    _RbnSubsConfigErrorMsgs_Type()
)
rbnSubsConfigErrorMsgs.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnSubsConfigErrorMsgs.setStatus("current")
_RbnSubsActiveConformance_ObjectIdentity = ObjectIdentity
rbnSubsActiveConformance = _RbnSubsActiveConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2)
)
_RbnSubsCompliances_ObjectIdentity = ObjectIdentity
rbnSubsCompliances = _RbnSubsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 1)
)
_RbnSubsGroups_ObjectIdentity = ObjectIdentity
rbnSubsGroups = _RbnSubsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 2)
)
_RbnSubsActiveNotifications_ObjectIdentity = ObjectIdentity
rbnSubsActiveNotifications = _RbnSubsActiveNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 3)
)
_RbnSubsNotifyPrefix_ObjectIdentity = ObjectIdentity
rbnSubsNotifyPrefix = _RbnSubsNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 3, 0)
)

# Managed Objects groups

rbnSubsActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 2, 1)
)
rbnSubsActiveGroup.setObjects(
      *(("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveCircuitDescr"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveCircuitHandle"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveStartTime"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveClear"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveAddr"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsClearSubscriberName"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsClearSessionId"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsBounceName"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsBounceSessionId"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsReauthRadiusIndex"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsReauthRadiusID"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsClearReason"))
)
if mibBuilder.loadTexts:
    rbnSubsActiveGroup.setStatus("obsolete")

rbnSubsStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 2, 2)
)
rbnSubsStatsGroup.setObjects(
      *(("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsCntxtCount"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsEncapsCount"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsOctetsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsOctetsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsPktsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsPktsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsXmitOctetsDropped"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsXmitPktsDropped"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsMcastOctetsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsMcastOctetsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsMcastPktsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsMcastPktsReceived"))
)
if mibBuilder.loadTexts:
    rbnSubsStatsGroup.setStatus("obsolete")

rbnSubsActiveGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 2, 3)
)
rbnSubsActiveGroup2.setObjects(
      *(("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveCircuitDescr"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveCircuitHandle"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveStartTime"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveClear"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveAddr"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsClearSubscriberName"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsClearSessionId"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsBounceName"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsBounceSessionId"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsReauthRadiusIndex"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsReauthRadiusID"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsReauthName"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsReauthSessionId"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsClearReason"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveResend"))
)
if mibBuilder.loadTexts:
    rbnSubsActiveGroup2.setStatus("deprecated")

rbnSubsStatsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 2, 4)
)
rbnSubsStatsGroup2.setObjects(
      *(("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsCntxtCount"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsEncapsCount"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsOctetsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsOctetsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsPktsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsPktsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsXmitOctetsDropped"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsXmitPktsDropped"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsMcastOctetsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsMcastOctetsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsMcastPktsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsMcastPktsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsProfileCount"))
)
if mibBuilder.loadTexts:
    rbnSubsStatsGroup2.setStatus("current")

rbnSubsActiveGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 2, 5)
)
rbnSubsActiveGroup3.setObjects(
      *(("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveCircuitDescr"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveCircuitHandle"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveStartTime"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveClear"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveAddr"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveNasPortType"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveMediumType"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsClearSubscriberName"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsClearSessionId"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsBounceName"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsBounceSessionId"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsReauthRadiusIndex"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsReauthRadiusID"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsReauthName"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsReauthSessionId"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsClearReason"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveResend"))
)
if mibBuilder.loadTexts:
    rbnSubsActiveGroup3.setStatus("current")

rbnSubsServicesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 2, 6)
)
rbnSubsServicesGroup.setObjects(
      *(("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceName"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceTag"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceVolumeLimitIn"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceVolumeLimitOut"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceActiveTime"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceVolumeOctetsIn"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceVolumeOctetsOut"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceVolumePktsIn"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceVolumePktsOut"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceIPv4VolumeOctetsIn"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceIPv4VolumeOctetsOut"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceIPv6VolumeOctetsIn"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceIPv6VolumeOctetsOut"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceIPv4VolumePktsIn"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceIPv4VolumePktsOut"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceIPv6VolumePktsIn"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsServiceIPv6VolumePktsOut"))
)
if mibBuilder.loadTexts:
    rbnSubsServicesGroup.setStatus("current")

rbnSubsNotifyObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 2, 7)
)
rbnSubsNotifyObjectGroup.setObjects(
      *(("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsNotifyEnable"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsConfigErrorMsgs"))
)
if mibBuilder.loadTexts:
    rbnSubsNotifyObjectGroup.setStatus("current")

rbnSubsLicenseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 2, 9)
)
rbnSubsLicenseGroup.setObjects(
      *(("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsMaxSupportedSessions"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsLicensedSessions"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveSessions"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsCapacityPercentageUsed"))
)
if mibBuilder.loadTexts:
    rbnSubsLicenseGroup.setStatus("current")

rbnSubsActiveGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 2, 10)
)
rbnSubsActiveGroup4.setObjects(
      *(("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveCircuitDescr"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveCircuitHandle"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveStartTime"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveClear"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveAddr"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveNasPortType"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveMediumType"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveResendSvcAcct"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsClearSubscriberName"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveSessionSubscriberName"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveSessionPointer"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveIpAddrDescr"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsClearSessionId"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsBounceName"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsBounceSessionId"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsReauthRadiusIndex"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsReauthRadiusID"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsReauthName"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsReauthSessionId"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsClearReason"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveResend"))
)
if mibBuilder.loadTexts:
    rbnSubsActiveGroup4.setStatus("current")

rbnSubsStatsGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 2, 11)
)
rbnSubsStatsGroup3.setObjects(
      *(("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsCntxtCount"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsCntxtIp4OnlyCount"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsCntxtIp6OnlyCount"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsCntxtDualCount"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsCntxtLacCount"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsEncapsCount"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsOctetsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsOctetsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsPktsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsPktsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsXmitOctetsDropped"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsXmitPktsDropped"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsMcastOctetsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsMcastOctetsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsMcastPktsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsMcastPktsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsProfileCount"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsIPv4OctetsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsIPv4OctetsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsIPv6OctetsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsIPv6OctetsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsIPv4PktsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsIPv4PktsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsIPv6PktsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsIPv6PktsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsIPv4McastOctetsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsIPv4McastOctetsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsIPv6McastOctetsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsIPv6McastOctetsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsIPv4McastPktsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsIPv4McastPktsReceived"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsIPv6McastPktsSent"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsIPv6McastPktsReceived"))
)
if mibBuilder.loadTexts:
    rbnSubsStatsGroup3.setStatus("current")


# Notification objects

rbnSubsConfigErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 3, 0, 1)
)
rbnSubsConfigErrorEvent.setObjects(
      *(("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsActiveCircuitHandle"),
        ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsConfigErrorMsgs"))
)
if mibBuilder.loadTexts:
    rbnSubsConfigErrorEvent.setStatus(
        "current"
    )


# Notifications groups

rbnSubsNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 2, 8)
)
rbnSubsNotifyGroup.setObjects(
    ("RBN-SUBSCRIBER-ACTIVE-MIB", "rbnSubsConfigErrorEvent")
)
if mibBuilder.loadTexts:
    rbnSubsNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnSubsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnSubsCompliance.setStatus(
        "obsolete"
    )

rbnSubsCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rbnSubsCompliance2.setStatus(
        "obsolete"
    )

rbnSubsCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 1, 3)
)
if mibBuilder.loadTexts:
    rbnSubsCompliance3.setStatus(
        "obsolete"
    )

rbnSubsCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 1, 4)
)
if mibBuilder.loadTexts:
    rbnSubsCompliance4.setStatus(
        "obsolete"
    )

rbnSubsCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 1, 5)
)
if mibBuilder.loadTexts:
    rbnSubsCompliance5.setStatus(
        "obsolete"
    )

rbnSubsCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 27, 2, 1, 6)
)
if mibBuilder.loadTexts:
    rbnSubsCompliance6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-SUBSCRIBER-ACTIVE-MIB",
    **{"rbnSubscriberActiveMib": rbnSubscriberActiveMib,
       "rbnSubsActiveObjects": rbnSubsActiveObjects,
       "rbnSubsActive": rbnSubsActive,
       "rbnSubsActiveTable": rbnSubsActiveTable,
       "rbnSubsActiveEntry": rbnSubsActiveEntry,
       "rbnSubsActiveName": rbnSubsActiveName,
       "rbnSubsActiveSessionId": rbnSubsActiveSessionId,
       "rbnSubsActiveCircuitDescr": rbnSubsActiveCircuitDescr,
       "rbnSubsActiveCircuitHandle": rbnSubsActiveCircuitHandle,
       "rbnSubsActiveStartTime": rbnSubsActiveStartTime,
       "rbnSubsActiveClear": rbnSubsActiveClear,
       "rbnSubsActiveResend": rbnSubsActiveResend,
       "rbnSubsActiveNasPortType": rbnSubsActiveNasPortType,
       "rbnSubsActiveMediumType": rbnSubsActiveMediumType,
       "rbnSubsActiveResendSvcAcct": rbnSubsActiveResendSvcAcct,
       "rbnSubsActiveIpTable": rbnSubsActiveIpTable,
       "rbnSubsActiveIpEntry": rbnSubsActiveIpEntry,
       "rbnSubsActiveAddrType": rbnSubsActiveAddrType,
       "rbnSubsActiveAddr": rbnSubsActiveAddr,
       "rbnSubsClear": rbnSubsClear,
       "rbnSubsClearSubscriberName": rbnSubsClearSubscriberName,
       "rbnSubsClearSessionId": rbnSubsClearSessionId,
       "rbnSubsBounceName": rbnSubsBounceName,
       "rbnSubsBounceSessionId": rbnSubsBounceSessionId,
       "rbnSubsReauthRadiusIndex": rbnSubsReauthRadiusIndex,
       "rbnSubsReauthRadiusID": rbnSubsReauthRadiusID,
       "rbnSubsReauthName": rbnSubsReauthName,
       "rbnSubsReauthSessionId": rbnSubsReauthSessionId,
       "rbnSubsClearReason": rbnSubsClearReason,
       "rbnSubsServiceVolumeTable": rbnSubsServiceVolumeTable,
       "rbnSubsServiceVolumeEntry": rbnSubsServiceVolumeEntry,
       "rbnSubsServiceVolumeLimitIn": rbnSubsServiceVolumeLimitIn,
       "rbnSubsServiceVolumeLimitOut": rbnSubsServiceVolumeLimitOut,
       "rbnSubsServiceActiveTime": rbnSubsServiceActiveTime,
       "rbnSubsServiceVolumeOctetsIn": rbnSubsServiceVolumeOctetsIn,
       "rbnSubsServiceVolumeOctetsOut": rbnSubsServiceVolumeOctetsOut,
       "rbnSubsServiceVolumePktsIn": rbnSubsServiceVolumePktsIn,
       "rbnSubsServiceVolumePktsOut": rbnSubsServiceVolumePktsOut,
       "rbnSubsServiceIPv4VolumeOctetsIn": rbnSubsServiceIPv4VolumeOctetsIn,
       "rbnSubsServiceIPv4VolumeOctetsOut": rbnSubsServiceIPv4VolumeOctetsOut,
       "rbnSubsServiceIPv6VolumeOctetsIn": rbnSubsServiceIPv6VolumeOctetsIn,
       "rbnSubsServiceIPv6VolumeOctetsOut": rbnSubsServiceIPv6VolumeOctetsOut,
       "rbnSubsServiceIPv4VolumePktsIn": rbnSubsServiceIPv4VolumePktsIn,
       "rbnSubsServiceIPv4VolumePktsOut": rbnSubsServiceIPv4VolumePktsOut,
       "rbnSubsServiceIPv6VolumePktsIn": rbnSubsServiceIPv6VolumePktsIn,
       "rbnSubsServiceIPv6VolumePktsOut": rbnSubsServiceIPv6VolumePktsOut,
       "rbnSubsServicesTable": rbnSubsServicesTable,
       "rbnSubsServicesEntry": rbnSubsServicesEntry,
       "rbnSubsServiceIndex": rbnSubsServiceIndex,
       "rbnSubsServiceName": rbnSubsServiceName,
       "rbnSubsServiceTag": rbnSubsServiceTag,
       "rbnSubsActiveSessionTable": rbnSubsActiveSessionTable,
       "rbnSubsActiveSessionEntry": rbnSubsActiveSessionEntry,
       "rbnSubsActiveSessionSubscriberName": rbnSubsActiveSessionSubscriberName,
       "rbnSubsActiveSessionPointer": rbnSubsActiveSessionPointer,
       "rbnSubsActiveIpAddrTable": rbnSubsActiveIpAddrTable,
       "rbnSubsActiveIpAddrEntry": rbnSubsActiveIpAddrEntry,
       "rbnSubsActiveIpAddrType": rbnSubsActiveIpAddrType,
       "rbnSubsActiveIpAddr": rbnSubsActiveIpAddr,
       "rbnSubsActiveIpPfxLen": rbnSubsActiveIpPfxLen,
       "rbnSubsActiveIpAddrDescr": rbnSubsActiveIpAddrDescr,
       "rbnSubsStats": rbnSubsStats,
       "rbnSubsCntxtCountTable": rbnSubsCntxtCountTable,
       "rbnSubsCntxtCountEntry": rbnSubsCntxtCountEntry,
       "rbnSubsCntxtCount": rbnSubsCntxtCount,
       "rbnSubsCntxtIp4OnlyCount": rbnSubsCntxtIp4OnlyCount,
       "rbnSubsCntxtIp6OnlyCount": rbnSubsCntxtIp6OnlyCount,
       "rbnSubsCntxtDualCount": rbnSubsCntxtDualCount,
       "rbnSubsCntxtLacCount": rbnSubsCntxtLacCount,
       "rbnSubsEncapsCountTable": rbnSubsEncapsCountTable,
       "rbnSubsEncapsCountEntry": rbnSubsEncapsCountEntry,
       "rbnSubsEncapsulationType": rbnSubsEncapsulationType,
       "rbnSubsEncapsCount": rbnSubsEncapsCount,
       "rbnSubsStatsTable": rbnSubsStatsTable,
       "rbnSubsStatsEntry": rbnSubsStatsEntry,
       "rbnSubsOctetsSent": rbnSubsOctetsSent,
       "rbnSubsOctetsReceived": rbnSubsOctetsReceived,
       "rbnSubsPktsSent": rbnSubsPktsSent,
       "rbnSubsPktsReceived": rbnSubsPktsReceived,
       "rbnSubsXmitOctetsDropped": rbnSubsXmitOctetsDropped,
       "rbnSubsXmitPktsDropped": rbnSubsXmitPktsDropped,
       "rbnSubsMcastOctetsSent": rbnSubsMcastOctetsSent,
       "rbnSubsMcastOctetsReceived": rbnSubsMcastOctetsReceived,
       "rbnSubsMcastPktsSent": rbnSubsMcastPktsSent,
       "rbnSubsMcastPktsReceived": rbnSubsMcastPktsReceived,
       "rbnSubsIPv4OctetsSent": rbnSubsIPv4OctetsSent,
       "rbnSubsIPv4OctetsReceived": rbnSubsIPv4OctetsReceived,
       "rbnSubsIPv6OctetsSent": rbnSubsIPv6OctetsSent,
       "rbnSubsIPv6OctetsReceived": rbnSubsIPv6OctetsReceived,
       "rbnSubsIPv4PktsSent": rbnSubsIPv4PktsSent,
       "rbnSubsIPv4PktsReceived": rbnSubsIPv4PktsReceived,
       "rbnSubsIPv6PktsSent": rbnSubsIPv6PktsSent,
       "rbnSubsIPv6PktsReceived": rbnSubsIPv6PktsReceived,
       "rbnSubsIPv4McastOctetsSent": rbnSubsIPv4McastOctetsSent,
       "rbnSubsIPv4McastOctetsReceived": rbnSubsIPv4McastOctetsReceived,
       "rbnSubsIPv6McastOctetsSent": rbnSubsIPv6McastOctetsSent,
       "rbnSubsIPv6McastOctetsReceived": rbnSubsIPv6McastOctetsReceived,
       "rbnSubsIPv4McastPktsSent": rbnSubsIPv4McastPktsSent,
       "rbnSubsIPv4McastPktsReceived": rbnSubsIPv4McastPktsReceived,
       "rbnSubsIPv6McastPktsSent": rbnSubsIPv6McastPktsSent,
       "rbnSubsIPv6McastPktsReceived": rbnSubsIPv6McastPktsReceived,
       "rbnSubsProfileCountTable": rbnSubsProfileCountTable,
       "rbnSubsProfileCountEntry": rbnSubsProfileCountEntry,
       "rbnSubsProfileName": rbnSubsProfileName,
       "rbnSubsProfileCount": rbnSubsProfileCount,
       "rbnSubsLicense": rbnSubsLicense,
       "rbnSubsMaxSupportedSessions": rbnSubsMaxSupportedSessions,
       "rbnSubsLicensedSessions": rbnSubsLicensedSessions,
       "rbnSubsActiveSessions": rbnSubsActiveSessions,
       "rbnSubsCapacityPercentageUsed": rbnSubsCapacityPercentageUsed,
       "rbnSubsNotify": rbnSubsNotify,
       "rbnSubsNotifyEnable": rbnSubsNotifyEnable,
       "rbnSubsConfigErrorMsgs": rbnSubsConfigErrorMsgs,
       "rbnSubsActiveConformance": rbnSubsActiveConformance,
       "rbnSubsCompliances": rbnSubsCompliances,
       "rbnSubsCompliance": rbnSubsCompliance,
       "rbnSubsCompliance2": rbnSubsCompliance2,
       "rbnSubsCompliance3": rbnSubsCompliance3,
       "rbnSubsCompliance4": rbnSubsCompliance4,
       "rbnSubsCompliance5": rbnSubsCompliance5,
       "rbnSubsCompliance6": rbnSubsCompliance6,
       "rbnSubsGroups": rbnSubsGroups,
       "rbnSubsActiveGroup": rbnSubsActiveGroup,
       "rbnSubsStatsGroup": rbnSubsStatsGroup,
       "rbnSubsActiveGroup2": rbnSubsActiveGroup2,
       "rbnSubsStatsGroup2": rbnSubsStatsGroup2,
       "rbnSubsActiveGroup3": rbnSubsActiveGroup3,
       "rbnSubsServicesGroup": rbnSubsServicesGroup,
       "rbnSubsNotifyObjectGroup": rbnSubsNotifyObjectGroup,
       "rbnSubsNotifyGroup": rbnSubsNotifyGroup,
       "rbnSubsLicenseGroup": rbnSubsLicenseGroup,
       "rbnSubsActiveGroup4": rbnSubsActiveGroup4,
       "rbnSubsStatsGroup3": rbnSubsStatsGroup3,
       "rbnSubsActiveNotifications": rbnSubsActiveNotifications,
       "rbnSubsNotifyPrefix": rbnSubsNotifyPrefix,
       "rbnSubsConfigErrorEvent": rbnSubsConfigErrorEvent}
)
