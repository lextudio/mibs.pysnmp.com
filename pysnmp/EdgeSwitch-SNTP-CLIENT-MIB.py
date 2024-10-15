# SNMP MIB module (EdgeSwitch-SNTP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EdgeSwitch-SNTP-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:07 2024
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

(fastPath,) = mibBuilder.importSymbols(
    "EdgeSwitch-REF-MIB",
    "fastPath")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

agentSntpClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17)
)
agentSntpClientMIB.setRevisions(
        ("2011-12-14 00:00",
         "2011-01-26 00:00",
         "2007-05-23 00:00",
         "2003-12-18 16:29")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SntpClientAdminMode(Bits, TextualConvention):
    status = "current"


class SntpClientUpdateStatus(Integer32, TextualConvention):
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
        *(("badDateEncoded", 4),
          ("other", 1),
          ("requestTimedOut", 3),
          ("serverKissOfDeath", 7),
          ("serverUnsychronized", 6),
          ("success", 2),
          ("versionNotSupported", 5))
    )



# MIB Managed Objects in the order of their OIDs

_AgentSntpClientObjects_ObjectIdentity = ObjectIdentity
agentSntpClientObjects = _AgentSntpClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1)
)
_AgentSntpClient_ObjectIdentity = ObjectIdentity
agentSntpClient = _AgentSntpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 1)
)


class _AgentSntpClientVersion_Type(Integer32):
    """Custom type agentSntpClientVersion based on Integer32"""
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
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3),
          ("version4", 4))
    )


_AgentSntpClientVersion_Type.__name__ = "Integer32"
_AgentSntpClientVersion_Object = MibScalar
agentSntpClientVersion = _AgentSntpClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 1, 1),
    _AgentSntpClientVersion_Type()
)
agentSntpClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientVersion.setStatus("current")
_AgentSntpClientSupportedMode_Type = SntpClientAdminMode
_AgentSntpClientSupportedMode_Object = MibScalar
agentSntpClientSupportedMode = _AgentSntpClientSupportedMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 1, 2),
    _AgentSntpClientSupportedMode_Type()
)
agentSntpClientSupportedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientSupportedMode.setStatus("current")


class _AgentSntpClientMode_Type(Integer32):
    """Custom type agentSntpClientMode based on Integer32"""
    defaultValue = 0

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
        *(("broadcast", 2),
          ("disabled", 0),
          ("multicast", 3),
          ("unicast", 1))
    )


_AgentSntpClientMode_Type.__name__ = "Integer32"
_AgentSntpClientMode_Object = MibScalar
agentSntpClientMode = _AgentSntpClientMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 1, 3),
    _AgentSntpClientMode_Type()
)
agentSntpClientMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSntpClientMode.setStatus("current")


class _AgentSntpClientPort_Type(InetPortNumber):
    """Custom type agentSntpClientPort based on InetPortNumber"""
    defaultValue = 0

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(123, 123),
        ValueRangeConstraint(1025, 65535),
    )


_AgentSntpClientPort_Type.__name__ = "InetPortNumber"
_AgentSntpClientPort_Object = MibScalar
agentSntpClientPort = _AgentSntpClientPort_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 1, 4),
    _AgentSntpClientPort_Type()
)
agentSntpClientPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSntpClientPort.setStatus("current")


class _AgentSntpClientLastUpdateTime_Type(DateAndTime):
    """Custom type agentSntpClientLastUpdateTime based on DateAndTime"""
    defaultHexValue = "00000000"


_AgentSntpClientLastUpdateTime_Object = MibScalar
agentSntpClientLastUpdateTime = _AgentSntpClientLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 1, 5),
    _AgentSntpClientLastUpdateTime_Type()
)
agentSntpClientLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientLastUpdateTime.setStatus("current")


class _AgentSntpClientLastAttemptTime_Type(DateAndTime):
    """Custom type agentSntpClientLastAttemptTime based on DateAndTime"""
    defaultHexValue = "00000000"


_AgentSntpClientLastAttemptTime_Object = MibScalar
agentSntpClientLastAttemptTime = _AgentSntpClientLastAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 1, 6),
    _AgentSntpClientLastAttemptTime_Type()
)
agentSntpClientLastAttemptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientLastAttemptTime.setStatus("current")


class _AgentSntpClientLastAttemptStatus_Type(SntpClientUpdateStatus):
    """Custom type agentSntpClientLastAttemptStatus based on SntpClientUpdateStatus"""


_AgentSntpClientLastAttemptStatus_Object = MibScalar
agentSntpClientLastAttemptStatus = _AgentSntpClientLastAttemptStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 1, 7),
    _AgentSntpClientLastAttemptStatus_Type()
)
agentSntpClientLastAttemptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientLastAttemptStatus.setStatus("current")
_AgentSntpClientServerAddressType_Type = InetAddressType
_AgentSntpClientServerAddressType_Object = MibScalar
agentSntpClientServerAddressType = _AgentSntpClientServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 1, 8),
    _AgentSntpClientServerAddressType_Type()
)
agentSntpClientServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientServerAddressType.setStatus("current")


class _AgentSntpClientServerAddress_Type(InetAddress):
    """Custom type agentSntpClientServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AgentSntpClientServerAddress_Type.__name__ = "InetAddress"
_AgentSntpClientServerAddress_Object = MibScalar
agentSntpClientServerAddress = _AgentSntpClientServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 1, 9),
    _AgentSntpClientServerAddress_Type()
)
agentSntpClientServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientServerAddress.setStatus("current")


class _AgentSntpClientServerMode_Type(Unsigned32):
    """Custom type agentSntpClientServerMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentSntpClientServerMode_Type.__name__ = "Unsigned32"
_AgentSntpClientServerMode_Object = MibScalar
agentSntpClientServerMode = _AgentSntpClientServerMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 1, 10),
    _AgentSntpClientServerMode_Type()
)
agentSntpClientServerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientServerMode.setStatus("current")


class _AgentSntpClientServerStratum_Type(Unsigned32):
    """Custom type agentSntpClientServerStratum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentSntpClientServerStratum_Type.__name__ = "Unsigned32"
_AgentSntpClientServerStratum_Object = MibScalar
agentSntpClientServerStratum = _AgentSntpClientServerStratum_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 1, 11),
    _AgentSntpClientServerStratum_Type()
)
agentSntpClientServerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientServerStratum.setStatus("current")


class _AgentSntpClientServerRefClkId_Type(OctetString):
    """Custom type agentSntpClientServerRefClkId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AgentSntpClientServerRefClkId_Type.__name__ = "OctetString"
_AgentSntpClientServerRefClkId_Object = MibScalar
agentSntpClientServerRefClkId = _AgentSntpClientServerRefClkId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 1, 12),
    _AgentSntpClientServerRefClkId_Type()
)
agentSntpClientServerRefClkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientServerRefClkId.setStatus("current")


class _AgentSntpClientPollInterval_Type(Unsigned32):
    """Custom type agentSntpClientPollInterval based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 10),
    )


_AgentSntpClientPollInterval_Type.__name__ = "Unsigned32"
_AgentSntpClientPollInterval_Object = MibScalar
agentSntpClientPollInterval = _AgentSntpClientPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 1, 13),
    _AgentSntpClientPollInterval_Type()
)
agentSntpClientPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSntpClientPollInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    agentSntpClientPollInterval.setUnits("seconds")
_AgentSntpClientSourceInterface_Type = InterfaceIndexOrZero
_AgentSntpClientSourceInterface_Object = MibScalar
agentSntpClientSourceInterface = _AgentSntpClientSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 1, 14),
    _AgentSntpClientSourceInterface_Type()
)
agentSntpClientSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSntpClientSourceInterface.setStatus("current")
_AgentSntpClientUnicast_ObjectIdentity = ObjectIdentity
agentSntpClientUnicast = _AgentSntpClientUnicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2)
)


class _AgentSntpClientUnicastPollInterval_Type(Unsigned32):
    """Custom type agentSntpClientUnicastPollInterval based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 10),
    )


_AgentSntpClientUnicastPollInterval_Type.__name__ = "Unsigned32"
_AgentSntpClientUnicastPollInterval_Object = MibScalar
agentSntpClientUnicastPollInterval = _AgentSntpClientUnicastPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 1),
    _AgentSntpClientUnicastPollInterval_Type()
)
agentSntpClientUnicastPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSntpClientUnicastPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    agentSntpClientUnicastPollInterval.setUnits("seconds")


class _AgentSntpClientUnicastPollTimeout_Type(Unsigned32):
    """Custom type agentSntpClientUnicastPollTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AgentSntpClientUnicastPollTimeout_Type.__name__ = "Unsigned32"
_AgentSntpClientUnicastPollTimeout_Object = MibScalar
agentSntpClientUnicastPollTimeout = _AgentSntpClientUnicastPollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 2),
    _AgentSntpClientUnicastPollTimeout_Type()
)
agentSntpClientUnicastPollTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSntpClientUnicastPollTimeout.setStatus("current")
if mibBuilder.loadTexts:
    agentSntpClientUnicastPollTimeout.setUnits("seconds")


class _AgentSntpClientUnicastPollRetry_Type(Unsigned32):
    """Custom type agentSntpClientUnicastPollRetry based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AgentSntpClientUnicastPollRetry_Type.__name__ = "Unsigned32"
_AgentSntpClientUnicastPollRetry_Object = MibScalar
agentSntpClientUnicastPollRetry = _AgentSntpClientUnicastPollRetry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 3),
    _AgentSntpClientUnicastPollRetry_Type()
)
agentSntpClientUnicastPollRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSntpClientUnicastPollRetry.setStatus("current")
_AgentSntpClientUcastServerMaxEntries_Type = Unsigned32
_AgentSntpClientUcastServerMaxEntries_Object = MibScalar
agentSntpClientUcastServerMaxEntries = _AgentSntpClientUcastServerMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 4),
    _AgentSntpClientUcastServerMaxEntries_Type()
)
agentSntpClientUcastServerMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientUcastServerMaxEntries.setStatus("current")


class _AgentSntpClientUcastServerCurrEntries_Type(Gauge32):
    """Custom type agentSntpClientUcastServerCurrEntries based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AgentSntpClientUcastServerCurrEntries_Type.__name__ = "Gauge32"
_AgentSntpClientUcastServerCurrEntries_Object = MibScalar
agentSntpClientUcastServerCurrEntries = _AgentSntpClientUcastServerCurrEntries_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 5),
    _AgentSntpClientUcastServerCurrEntries_Type()
)
agentSntpClientUcastServerCurrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientUcastServerCurrEntries.setStatus("current")
_AgentSntpClientUcastServerTable_Object = MibTable
agentSntpClientUcastServerTable = _AgentSntpClientUcastServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 6)
)
if mibBuilder.loadTexts:
    agentSntpClientUcastServerTable.setStatus("current")
_AgentSntpClientUcastServerEntry_Object = MibTableRow
agentSntpClientUcastServerEntry = _AgentSntpClientUcastServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 6, 1)
)
agentSntpClientUcastServerEntry.setIndexNames(
    (0, "EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientUcastServerIndex"),
)
if mibBuilder.loadTexts:
    agentSntpClientUcastServerEntry.setStatus("current")
_AgentSntpClientUcastServerIndex_Type = Unsigned32
_AgentSntpClientUcastServerIndex_Object = MibTableColumn
agentSntpClientUcastServerIndex = _AgentSntpClientUcastServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 6, 1, 1),
    _AgentSntpClientUcastServerIndex_Type()
)
agentSntpClientUcastServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSntpClientUcastServerIndex.setStatus("current")
_AgentSntpClientUcastServerAddressType_Type = InetAddressType
_AgentSntpClientUcastServerAddressType_Object = MibTableColumn
agentSntpClientUcastServerAddressType = _AgentSntpClientUcastServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 6, 1, 2),
    _AgentSntpClientUcastServerAddressType_Type()
)
agentSntpClientUcastServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSntpClientUcastServerAddressType.setStatus("current")


class _AgentSntpClientUcastServerAddress_Type(InetAddress):
    """Custom type agentSntpClientUcastServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AgentSntpClientUcastServerAddress_Type.__name__ = "InetAddress"
_AgentSntpClientUcastServerAddress_Object = MibTableColumn
agentSntpClientUcastServerAddress = _AgentSntpClientUcastServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 6, 1, 3),
    _AgentSntpClientUcastServerAddress_Type()
)
agentSntpClientUcastServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSntpClientUcastServerAddress.setStatus("current")


class _AgentSntpClientUcastServerPort_Type(InetPortNumber):
    """Custom type agentSntpClientUcastServerPort based on InetPortNumber"""
    defaultValue = 123

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentSntpClientUcastServerPort_Type.__name__ = "InetPortNumber"
_AgentSntpClientUcastServerPort_Object = MibTableColumn
agentSntpClientUcastServerPort = _AgentSntpClientUcastServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 6, 1, 4),
    _AgentSntpClientUcastServerPort_Type()
)
agentSntpClientUcastServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSntpClientUcastServerPort.setStatus("current")


class _AgentSntpClientUcastServerVersion_Type(Integer32):
    """Custom type agentSntpClientUcastServerVersion based on Integer32"""
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
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3),
          ("version4", 4))
    )


_AgentSntpClientUcastServerVersion_Type.__name__ = "Integer32"
_AgentSntpClientUcastServerVersion_Object = MibTableColumn
agentSntpClientUcastServerVersion = _AgentSntpClientUcastServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 6, 1, 5),
    _AgentSntpClientUcastServerVersion_Type()
)
agentSntpClientUcastServerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSntpClientUcastServerVersion.setStatus("current")


class _AgentSntpClientUcastServerPrecedence_Type(Unsigned32):
    """Custom type agentSntpClientUcastServerPrecedence based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AgentSntpClientUcastServerPrecedence_Type.__name__ = "Unsigned32"
_AgentSntpClientUcastServerPrecedence_Object = MibTableColumn
agentSntpClientUcastServerPrecedence = _AgentSntpClientUcastServerPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 6, 1, 6),
    _AgentSntpClientUcastServerPrecedence_Type()
)
agentSntpClientUcastServerPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSntpClientUcastServerPrecedence.setStatus("current")


class _AgentSntpClientUcastServerLastUpdateTime_Type(DateAndTime):
    """Custom type agentSntpClientUcastServerLastUpdateTime based on DateAndTime"""
    defaultHexValue = "00000000"


_AgentSntpClientUcastServerLastUpdateTime_Object = MibTableColumn
agentSntpClientUcastServerLastUpdateTime = _AgentSntpClientUcastServerLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 6, 1, 7),
    _AgentSntpClientUcastServerLastUpdateTime_Type()
)
agentSntpClientUcastServerLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientUcastServerLastUpdateTime.setStatus("current")


class _AgentSntpClientUcastServerLastAttemptTime_Type(DateAndTime):
    """Custom type agentSntpClientUcastServerLastAttemptTime based on DateAndTime"""
    defaultHexValue = "00000000"


_AgentSntpClientUcastServerLastAttemptTime_Object = MibTableColumn
agentSntpClientUcastServerLastAttemptTime = _AgentSntpClientUcastServerLastAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 6, 1, 8),
    _AgentSntpClientUcastServerLastAttemptTime_Type()
)
agentSntpClientUcastServerLastAttemptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientUcastServerLastAttemptTime.setStatus("current")


class _AgentSntpClientUcastServerLastAttemptStatus_Type(SntpClientUpdateStatus):
    """Custom type agentSntpClientUcastServerLastAttemptStatus based on SntpClientUpdateStatus"""


_AgentSntpClientUcastServerLastAttemptStatus_Object = MibTableColumn
agentSntpClientUcastServerLastAttemptStatus = _AgentSntpClientUcastServerLastAttemptStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 6, 1, 9),
    _AgentSntpClientUcastServerLastAttemptStatus_Type()
)
agentSntpClientUcastServerLastAttemptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientUcastServerLastAttemptStatus.setStatus("current")
_AgentSntpClientUcastServerNumRequests_Type = Counter32
_AgentSntpClientUcastServerNumRequests_Object = MibTableColumn
agentSntpClientUcastServerNumRequests = _AgentSntpClientUcastServerNumRequests_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 6, 1, 10),
    _AgentSntpClientUcastServerNumRequests_Type()
)
agentSntpClientUcastServerNumRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientUcastServerNumRequests.setStatus("current")
_AgentSntpClientUcastServerNumFailedRequests_Type = Counter32
_AgentSntpClientUcastServerNumFailedRequests_Object = MibTableColumn
agentSntpClientUcastServerNumFailedRequests = _AgentSntpClientUcastServerNumFailedRequests_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 6, 1, 11),
    _AgentSntpClientUcastServerNumFailedRequests_Type()
)
agentSntpClientUcastServerNumFailedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientUcastServerNumFailedRequests.setStatus("current")
_AgentSntpClientUcastServerRowStatus_Type = RowStatus
_AgentSntpClientUcastServerRowStatus_Object = MibTableColumn
agentSntpClientUcastServerRowStatus = _AgentSntpClientUcastServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 2, 6, 1, 12),
    _AgentSntpClientUcastServerRowStatus_Type()
)
agentSntpClientUcastServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSntpClientUcastServerRowStatus.setStatus("current")
_AgentSntpClientBroadcast_ObjectIdentity = ObjectIdentity
agentSntpClientBroadcast = _AgentSntpClientBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 3)
)
_AgentSntpClientBroadcastCount_Type = Counter32
_AgentSntpClientBroadcastCount_Object = MibScalar
agentSntpClientBroadcastCount = _AgentSntpClientBroadcastCount_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 3, 1),
    _AgentSntpClientBroadcastCount_Type()
)
agentSntpClientBroadcastCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSntpClientBroadcastCount.setStatus("current")


class _AgentSntpClientBroadcastInterval_Type(Unsigned32):
    """Custom type agentSntpClientBroadcastInterval based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 10),
    )


_AgentSntpClientBroadcastInterval_Type.__name__ = "Unsigned32"
_AgentSntpClientBroadcastInterval_Object = MibScalar
agentSntpClientBroadcastInterval = _AgentSntpClientBroadcastInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 1, 3, 2),
    _AgentSntpClientBroadcastInterval_Type()
)
agentSntpClientBroadcastInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSntpClientBroadcastInterval.setStatus("current")
if mibBuilder.loadTexts:
    agentSntpClientBroadcastInterval.setUnits("seconds")
_AgentSntpClientConformance_ObjectIdentity = ObjectIdentity
agentSntpClientConformance = _AgentSntpClientConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 2)
)
_AgentSntpClientGroups_ObjectIdentity = ObjectIdentity
agentSntpClientGroups = _AgentSntpClientGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 2, 1)
)
_AgentSntpClientCompliances_ObjectIdentity = ObjectIdentity
agentSntpClientCompliances = _AgentSntpClientCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 2, 2)
)

# Managed Objects groups

agentSntpClientDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 2, 1, 1)
)
agentSntpClientDeviceGroup.setObjects(
      *(("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientVersion"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientSupportedMode"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientMode"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientLastUpdateTime"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientLastAttemptTime"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientLastAttemptStatus"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientServerAddressType"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientServerAddress"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientServerMode"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientServerStratum"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientServerRefClkId"))
)
if mibBuilder.loadTexts:
    agentSntpClientDeviceGroup.setStatus("current")

agentSntpClientUnicastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 2, 1, 2)
)
agentSntpClientUnicastGroup.setObjects(
      *(("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientUnicastPollInterval"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientUnicastPollTimeout"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientUnicastPollRetry"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientUcastServerMaxEntries"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientUcastServerCurrEntries"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientUcastServerAddress"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientUcastServerAddressType"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientUcastServerPrecedence"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientUcastServerLastUpdateTime"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientUcastServerLastAttemptTime"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientUcastServerLastAttemptStatus"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientUcastServerNumRequests"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientUcastServerNumFailedRequests"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientUcastServerRowStatus"))
)
if mibBuilder.loadTexts:
    agentSntpClientUnicastGroup.setStatus("current")

agentSntpClientBroadcastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 2, 1, 3)
)
agentSntpClientBroadcastGroup.setObjects(
      *(("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientBroadcastCount"),
        ("EdgeSwitch-SNTP-CLIENT-MIB", "agentSntpClientBroadcastInterval"))
)
if mibBuilder.loadTexts:
    agentSntpClientBroadcastGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

agentSntpClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 17, 2, 2, 1)
)
if mibBuilder.loadTexts:
    agentSntpClientCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EdgeSwitch-SNTP-CLIENT-MIB",
    **{"SntpClientAdminMode": SntpClientAdminMode,
       "SntpClientUpdateStatus": SntpClientUpdateStatus,
       "agentSntpClientMIB": agentSntpClientMIB,
       "agentSntpClientObjects": agentSntpClientObjects,
       "agentSntpClient": agentSntpClient,
       "agentSntpClientVersion": agentSntpClientVersion,
       "agentSntpClientSupportedMode": agentSntpClientSupportedMode,
       "agentSntpClientMode": agentSntpClientMode,
       "agentSntpClientPort": agentSntpClientPort,
       "agentSntpClientLastUpdateTime": agentSntpClientLastUpdateTime,
       "agentSntpClientLastAttemptTime": agentSntpClientLastAttemptTime,
       "agentSntpClientLastAttemptStatus": agentSntpClientLastAttemptStatus,
       "agentSntpClientServerAddressType": agentSntpClientServerAddressType,
       "agentSntpClientServerAddress": agentSntpClientServerAddress,
       "agentSntpClientServerMode": agentSntpClientServerMode,
       "agentSntpClientServerStratum": agentSntpClientServerStratum,
       "agentSntpClientServerRefClkId": agentSntpClientServerRefClkId,
       "agentSntpClientPollInterval": agentSntpClientPollInterval,
       "agentSntpClientSourceInterface": agentSntpClientSourceInterface,
       "agentSntpClientUnicast": agentSntpClientUnicast,
       "agentSntpClientUnicastPollInterval": agentSntpClientUnicastPollInterval,
       "agentSntpClientUnicastPollTimeout": agentSntpClientUnicastPollTimeout,
       "agentSntpClientUnicastPollRetry": agentSntpClientUnicastPollRetry,
       "agentSntpClientUcastServerMaxEntries": agentSntpClientUcastServerMaxEntries,
       "agentSntpClientUcastServerCurrEntries": agentSntpClientUcastServerCurrEntries,
       "agentSntpClientUcastServerTable": agentSntpClientUcastServerTable,
       "agentSntpClientUcastServerEntry": agentSntpClientUcastServerEntry,
       "agentSntpClientUcastServerIndex": agentSntpClientUcastServerIndex,
       "agentSntpClientUcastServerAddressType": agentSntpClientUcastServerAddressType,
       "agentSntpClientUcastServerAddress": agentSntpClientUcastServerAddress,
       "agentSntpClientUcastServerPort": agentSntpClientUcastServerPort,
       "agentSntpClientUcastServerVersion": agentSntpClientUcastServerVersion,
       "agentSntpClientUcastServerPrecedence": agentSntpClientUcastServerPrecedence,
       "agentSntpClientUcastServerLastUpdateTime": agentSntpClientUcastServerLastUpdateTime,
       "agentSntpClientUcastServerLastAttemptTime": agentSntpClientUcastServerLastAttemptTime,
       "agentSntpClientUcastServerLastAttemptStatus": agentSntpClientUcastServerLastAttemptStatus,
       "agentSntpClientUcastServerNumRequests": agentSntpClientUcastServerNumRequests,
       "agentSntpClientUcastServerNumFailedRequests": agentSntpClientUcastServerNumFailedRequests,
       "agentSntpClientUcastServerRowStatus": agentSntpClientUcastServerRowStatus,
       "agentSntpClientBroadcast": agentSntpClientBroadcast,
       "agentSntpClientBroadcastCount": agentSntpClientBroadcastCount,
       "agentSntpClientBroadcastInterval": agentSntpClientBroadcastInterval,
       "agentSntpClientConformance": agentSntpClientConformance,
       "agentSntpClientGroups": agentSntpClientGroups,
       "agentSntpClientDeviceGroup": agentSntpClientDeviceGroup,
       "agentSntpClientUnicastGroup": agentSntpClientUnicastGroup,
       "agentSntpClientBroadcastGroup": agentSntpClientBroadcastGroup,
       "agentSntpClientCompliances": agentSntpClientCompliances,
       "agentSntpClientCompliance": agentSntpClientCompliance}
)
