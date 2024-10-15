# SNMP MIB module (ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:26 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

etsysRadiusAcctClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27)
)
etsysRadiusAcctClientMIB.setRevisions(
        ("2009-08-07 15:48",
         "2004-11-12 15:23",
         "2004-09-09 14:37",
         "2004-08-30 15:55",
         "2004-08-25 15:03",
         "2002-09-13 19:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysRadiusAcctClientMIBObjects_ObjectIdentity = ObjectIdentity
etsysRadiusAcctClientMIBObjects = _EtsysRadiusAcctClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1)
)


class _EtsysRadiusAcctClientEnable_Type(Integer32):
    """Custom type etsysRadiusAcctClientEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_EtsysRadiusAcctClientEnable_Type.__name__ = "Integer32"
_EtsysRadiusAcctClientEnable_Object = MibScalar
etsysRadiusAcctClientEnable = _EtsysRadiusAcctClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 1),
    _EtsysRadiusAcctClientEnable_Type()
)
etsysRadiusAcctClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientEnable.setStatus("current")


class _EtsysRadiusAcctClientUpdateInterval_Type(Integer32):
    """Custom type etsysRadiusAcctClientUpdateInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EtsysRadiusAcctClientUpdateInterval_Type.__name__ = "Integer32"
_EtsysRadiusAcctClientUpdateInterval_Object = MibScalar
etsysRadiusAcctClientUpdateInterval = _EtsysRadiusAcctClientUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 2),
    _EtsysRadiusAcctClientUpdateInterval_Type()
)
etsysRadiusAcctClientUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientUpdateInterval.setUnits("seconds")


class _EtsysRadiusAcctClientIntervalMinimum_Type(Integer32):
    """Custom type etsysRadiusAcctClientIntervalMinimum based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 2147483647),
    )


_EtsysRadiusAcctClientIntervalMinimum_Type.__name__ = "Integer32"
_EtsysRadiusAcctClientIntervalMinimum_Object = MibScalar
etsysRadiusAcctClientIntervalMinimum = _EtsysRadiusAcctClientIntervalMinimum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 3),
    _EtsysRadiusAcctClientIntervalMinimum_Type()
)
etsysRadiusAcctClientIntervalMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientIntervalMinimum.setStatus("current")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientIntervalMinimum.setUnits("seconds")
_EtsysRadiusAcctClientServerTable_Object = MibTable
etsysRadiusAcctClientServerTable = _EtsysRadiusAcctClientServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 4)
)
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerTable.setStatus("current")
_EtsysRadiusAcctClientServerEntry_Object = MibTableRow
etsysRadiusAcctClientServerEntry = _EtsysRadiusAcctClientServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 4, 1)
)
etsysRadiusAcctClientServerEntry.setIndexNames(
    (0, "ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerIndex"),
)
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerEntry.setStatus("current")


class _EtsysRadiusAcctClientServerIndex_Type(Integer32):
    """Custom type etsysRadiusAcctClientServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysRadiusAcctClientServerIndex_Type.__name__ = "Integer32"
_EtsysRadiusAcctClientServerIndex_Object = MibTableColumn
etsysRadiusAcctClientServerIndex = _EtsysRadiusAcctClientServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 4, 1, 1),
    _EtsysRadiusAcctClientServerIndex_Type()
)
etsysRadiusAcctClientServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerIndex.setStatus("current")


class _EtsysRadiusAcctClientServerAddressType_Type(InetAddressType):
    """Custom type etsysRadiusAcctClientServerAddressType based on InetAddressType"""


_EtsysRadiusAcctClientServerAddressType_Object = MibTableColumn
etsysRadiusAcctClientServerAddressType = _EtsysRadiusAcctClientServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 4, 1, 2),
    _EtsysRadiusAcctClientServerAddressType_Type()
)
etsysRadiusAcctClientServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerAddressType.setStatus("current")


class _EtsysRadiusAcctClientServerAddress_Type(InetAddress):
    """Custom type etsysRadiusAcctClientServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysRadiusAcctClientServerAddress_Type.__name__ = "InetAddress"
_EtsysRadiusAcctClientServerAddress_Object = MibTableColumn
etsysRadiusAcctClientServerAddress = _EtsysRadiusAcctClientServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 4, 1, 3),
    _EtsysRadiusAcctClientServerAddress_Type()
)
etsysRadiusAcctClientServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerAddress.setStatus("current")


class _EtsysRadiusAcctClientServerPortNumber_Type(Integer32):
    """Custom type etsysRadiusAcctClientServerPortNumber based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysRadiusAcctClientServerPortNumber_Type.__name__ = "Integer32"
_EtsysRadiusAcctClientServerPortNumber_Object = MibTableColumn
etsysRadiusAcctClientServerPortNumber = _EtsysRadiusAcctClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 4, 1, 4),
    _EtsysRadiusAcctClientServerPortNumber_Type()
)
etsysRadiusAcctClientServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerPortNumber.setStatus("current")


class _EtsysRadiusAcctClientServerSecret_Type(OctetString):
    """Custom type etsysRadiusAcctClientServerSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysRadiusAcctClientServerSecret_Type.__name__ = "OctetString"
_EtsysRadiusAcctClientServerSecret_Object = MibTableColumn
etsysRadiusAcctClientServerSecret = _EtsysRadiusAcctClientServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 4, 1, 5),
    _EtsysRadiusAcctClientServerSecret_Type()
)
etsysRadiusAcctClientServerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerSecret.setStatus("current")
_EtsysRadiusAcctClientServerSecretEntered_Type = TruthValue
_EtsysRadiusAcctClientServerSecretEntered_Object = MibTableColumn
etsysRadiusAcctClientServerSecretEntered = _EtsysRadiusAcctClientServerSecretEntered_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 4, 1, 6),
    _EtsysRadiusAcctClientServerSecretEntered_Type()
)
etsysRadiusAcctClientServerSecretEntered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerSecretEntered.setStatus("current")


class _EtsysRadiusAcctClientServerRetryTimeout_Type(Integer32):
    """Custom type etsysRadiusAcctClientServerRetryTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_EtsysRadiusAcctClientServerRetryTimeout_Type.__name__ = "Integer32"
_EtsysRadiusAcctClientServerRetryTimeout_Object = MibTableColumn
etsysRadiusAcctClientServerRetryTimeout = _EtsysRadiusAcctClientServerRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 4, 1, 7),
    _EtsysRadiusAcctClientServerRetryTimeout_Type()
)
etsysRadiusAcctClientServerRetryTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerRetryTimeout.setUnits("seconds")


class _EtsysRadiusAcctClientServerRetries_Type(Integer32):
    """Custom type etsysRadiusAcctClientServerRetries based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_EtsysRadiusAcctClientServerRetries_Type.__name__ = "Integer32"
_EtsysRadiusAcctClientServerRetries_Object = MibTableColumn
etsysRadiusAcctClientServerRetries = _EtsysRadiusAcctClientServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 4, 1, 8),
    _EtsysRadiusAcctClientServerRetries_Type()
)
etsysRadiusAcctClientServerRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerRetries.setStatus("current")


class _EtsysRadiusAcctClientServerClearTime_Type(Integer32):
    """Custom type etsysRadiusAcctClientServerClearTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysRadiusAcctClientServerClearTime_Type.__name__ = "Integer32"
_EtsysRadiusAcctClientServerClearTime_Object = MibTableColumn
etsysRadiusAcctClientServerClearTime = _EtsysRadiusAcctClientServerClearTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 4, 1, 9),
    _EtsysRadiusAcctClientServerClearTime_Type()
)
etsysRadiusAcctClientServerClearTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerClearTime.setStatus("deprecated")
_EtsysRadiusAcctClientServerStatus_Type = RowStatus
_EtsysRadiusAcctClientServerStatus_Object = MibTableColumn
etsysRadiusAcctClientServerStatus = _EtsysRadiusAcctClientServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 4, 1, 10),
    _EtsysRadiusAcctClientServerStatus_Type()
)
etsysRadiusAcctClientServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerStatus.setStatus("current")


class _EtsysRadiusAcctClientServerUpdateInterval_Type(Integer32):
    """Custom type etsysRadiusAcctClientServerUpdateInterval based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_EtsysRadiusAcctClientServerUpdateInterval_Type.__name__ = "Integer32"
_EtsysRadiusAcctClientServerUpdateInterval_Object = MibTableColumn
etsysRadiusAcctClientServerUpdateInterval = _EtsysRadiusAcctClientServerUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 4, 1, 11),
    _EtsysRadiusAcctClientServerUpdateInterval_Type()
)
etsysRadiusAcctClientServerUpdateInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerUpdateInterval.setUnits("seconds")


class _EtsysRadiusAcctClientServerIntervalMinimum_Type(Integer32):
    """Custom type etsysRadiusAcctClientServerIntervalMinimum based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(60, 2147483647),
    )


_EtsysRadiusAcctClientServerIntervalMinimum_Type.__name__ = "Integer32"
_EtsysRadiusAcctClientServerIntervalMinimum_Object = MibTableColumn
etsysRadiusAcctClientServerIntervalMinimum = _EtsysRadiusAcctClientServerIntervalMinimum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 1, 4, 1, 12),
    _EtsysRadiusAcctClientServerIntervalMinimum_Type()
)
etsysRadiusAcctClientServerIntervalMinimum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerIntervalMinimum.setStatus("current")
if mibBuilder.loadTexts:
    etsysRadiusAcctClientServerIntervalMinimum.setUnits("seconds")
_EtsysRadiusAcctClientMIBConformance_ObjectIdentity = ObjectIdentity
etsysRadiusAcctClientMIBConformance = _EtsysRadiusAcctClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 2)
)
_EtsysRadiusAcctClientMIBCompliances_ObjectIdentity = ObjectIdentity
etsysRadiusAcctClientMIBCompliances = _EtsysRadiusAcctClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 2, 1)
)
_EtsysRadiusAcctClientMIBGroups_ObjectIdentity = ObjectIdentity
etsysRadiusAcctClientMIBGroups = _EtsysRadiusAcctClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 2, 2)
)

# Managed Objects groups

etsysRadiusAcctClientMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 2, 2, 1)
)
etsysRadiusAcctClientMIBGroup.setObjects(
      *(("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientEnable"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientUpdateInterval"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientIntervalMinimum"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerAddressType"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerAddress"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerPortNumber"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerSecret"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerSecretEntered"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerRetryTimeout"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerRetries"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerClearTime"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerStatus"))
)
if mibBuilder.loadTexts:
    etsysRadiusAcctClientMIBGroup.setStatus("deprecated")

etsysRadiusAcctClientMIBGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 2, 2, 2)
)
etsysRadiusAcctClientMIBGroupV2.setObjects(
      *(("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientEnable"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientUpdateInterval"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientIntervalMinimum"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerAddressType"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerAddress"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerPortNumber"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerSecret"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerSecretEntered"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerRetryTimeout"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerRetries"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerStatus"))
)
if mibBuilder.loadTexts:
    etsysRadiusAcctClientMIBGroupV2.setStatus("deprecated")

etsysRadiusAcctClientMIBGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 2, 2, 3)
)
etsysRadiusAcctClientMIBGroupV3.setObjects(
      *(("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientEnable"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientUpdateInterval"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientIntervalMinimum"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerAddressType"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerAddress"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerPortNumber"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerSecret"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerSecretEntered"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerRetryTimeout"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerRetries"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerStatus"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerIntervalMinimum"),
        ("ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB", "etsysRadiusAcctClientServerUpdateInterval"))
)
if mibBuilder.loadTexts:
    etsysRadiusAcctClientMIBGroupV3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysRadiusAcctClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 2, 1, 2)
)
if mibBuilder.loadTexts:
    etsysRadiusAcctClientMIBCompliance.setStatus(
        "deprecated"
    )

etsysRadiusAcctClientMIBComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 2, 1, 3)
)
if mibBuilder.loadTexts:
    etsysRadiusAcctClientMIBComplianceV2.setStatus(
        "deprecated"
    )

etsysRadiusAcctClientMIBComplianceV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 27, 2, 1, 4)
)
if mibBuilder.loadTexts:
    etsysRadiusAcctClientMIBComplianceV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-RADIUS-ACCT-CLIENT-EXT-MIB",
    **{"etsysRadiusAcctClientMIB": etsysRadiusAcctClientMIB,
       "etsysRadiusAcctClientMIBObjects": etsysRadiusAcctClientMIBObjects,
       "etsysRadiusAcctClientEnable": etsysRadiusAcctClientEnable,
       "etsysRadiusAcctClientUpdateInterval": etsysRadiusAcctClientUpdateInterval,
       "etsysRadiusAcctClientIntervalMinimum": etsysRadiusAcctClientIntervalMinimum,
       "etsysRadiusAcctClientServerTable": etsysRadiusAcctClientServerTable,
       "etsysRadiusAcctClientServerEntry": etsysRadiusAcctClientServerEntry,
       "etsysRadiusAcctClientServerIndex": etsysRadiusAcctClientServerIndex,
       "etsysRadiusAcctClientServerAddressType": etsysRadiusAcctClientServerAddressType,
       "etsysRadiusAcctClientServerAddress": etsysRadiusAcctClientServerAddress,
       "etsysRadiusAcctClientServerPortNumber": etsysRadiusAcctClientServerPortNumber,
       "etsysRadiusAcctClientServerSecret": etsysRadiusAcctClientServerSecret,
       "etsysRadiusAcctClientServerSecretEntered": etsysRadiusAcctClientServerSecretEntered,
       "etsysRadiusAcctClientServerRetryTimeout": etsysRadiusAcctClientServerRetryTimeout,
       "etsysRadiusAcctClientServerRetries": etsysRadiusAcctClientServerRetries,
       "etsysRadiusAcctClientServerClearTime": etsysRadiusAcctClientServerClearTime,
       "etsysRadiusAcctClientServerStatus": etsysRadiusAcctClientServerStatus,
       "etsysRadiusAcctClientServerUpdateInterval": etsysRadiusAcctClientServerUpdateInterval,
       "etsysRadiusAcctClientServerIntervalMinimum": etsysRadiusAcctClientServerIntervalMinimum,
       "etsysRadiusAcctClientMIBConformance": etsysRadiusAcctClientMIBConformance,
       "etsysRadiusAcctClientMIBCompliances": etsysRadiusAcctClientMIBCompliances,
       "etsysRadiusAcctClientMIBCompliance": etsysRadiusAcctClientMIBCompliance,
       "etsysRadiusAcctClientMIBComplianceV2": etsysRadiusAcctClientMIBComplianceV2,
       "etsysRadiusAcctClientMIBComplianceV3": etsysRadiusAcctClientMIBComplianceV3,
       "etsysRadiusAcctClientMIBGroups": etsysRadiusAcctClientMIBGroups,
       "etsysRadiusAcctClientMIBGroup": etsysRadiusAcctClientMIBGroup,
       "etsysRadiusAcctClientMIBGroupV2": etsysRadiusAcctClientMIBGroupV2,
       "etsysRadiusAcctClientMIBGroupV3": etsysRadiusAcctClientMIBGroupV3}
)
