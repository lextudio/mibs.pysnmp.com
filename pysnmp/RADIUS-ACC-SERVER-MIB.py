# SNMP MIB module (RADIUS-ACC-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADIUS-ACC-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:23 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

radiusAccServMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 1)
)
radiusAccServMIB.setRevisions(
        ("2006-08-21 00:00",
         "1999-06-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RadiusMIB_ObjectIdentity = ObjectIdentity
radiusMIB = _RadiusMIB_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67)
)
if mibBuilder.loadTexts:
    radiusMIB.setStatus("current")
_RadiusAccounting_ObjectIdentity = ObjectIdentity
radiusAccounting = _RadiusAccounting_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2)
)
_RadiusAccServMIBObjects_ObjectIdentity = ObjectIdentity
radiusAccServMIBObjects = _RadiusAccServMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1)
)
_RadiusAccServ_ObjectIdentity = ObjectIdentity
radiusAccServ = _RadiusAccServ_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1)
)
_RadiusAccServIdent_Type = SnmpAdminString
_RadiusAccServIdent_Object = MibScalar
radiusAccServIdent = _RadiusAccServIdent_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 1),
    _RadiusAccServIdent_Type()
)
radiusAccServIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServIdent.setStatus("current")
_RadiusAccServUpTime_Type = TimeTicks
_RadiusAccServUpTime_Object = MibScalar
radiusAccServUpTime = _RadiusAccServUpTime_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 2),
    _RadiusAccServUpTime_Type()
)
radiusAccServUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServUpTime.setStatus("current")
_RadiusAccServResetTime_Type = TimeTicks
_RadiusAccServResetTime_Object = MibScalar
radiusAccServResetTime = _RadiusAccServResetTime_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 3),
    _RadiusAccServResetTime_Type()
)
radiusAccServResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServResetTime.setStatus("current")


class _RadiusAccServConfigReset_Type(Integer32):
    """Custom type radiusAccServConfigReset based on Integer32"""
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
        *(("initializing", 3),
          ("other", 1),
          ("reset", 2),
          ("running", 4))
    )


_RadiusAccServConfigReset_Type.__name__ = "Integer32"
_RadiusAccServConfigReset_Object = MibScalar
radiusAccServConfigReset = _RadiusAccServConfigReset_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 4),
    _RadiusAccServConfigReset_Type()
)
radiusAccServConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAccServConfigReset.setStatus("current")
_RadiusAccServTotalRequests_Type = Counter32
_RadiusAccServTotalRequests_Object = MibScalar
radiusAccServTotalRequests = _RadiusAccServTotalRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 5),
    _RadiusAccServTotalRequests_Type()
)
radiusAccServTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServTotalRequests.setUnits("packets")
_RadiusAccServTotalInvalidRequests_Type = Counter32
_RadiusAccServTotalInvalidRequests_Object = MibScalar
radiusAccServTotalInvalidRequests = _RadiusAccServTotalInvalidRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 6),
    _RadiusAccServTotalInvalidRequests_Type()
)
radiusAccServTotalInvalidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalInvalidRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServTotalInvalidRequests.setUnits("packets")
_RadiusAccServTotalDupRequests_Type = Counter32
_RadiusAccServTotalDupRequests_Object = MibScalar
radiusAccServTotalDupRequests = _RadiusAccServTotalDupRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 7),
    _RadiusAccServTotalDupRequests_Type()
)
radiusAccServTotalDupRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalDupRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServTotalDupRequests.setUnits("packets")
_RadiusAccServTotalResponses_Type = Counter32
_RadiusAccServTotalResponses_Object = MibScalar
radiusAccServTotalResponses = _RadiusAccServTotalResponses_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 8),
    _RadiusAccServTotalResponses_Type()
)
radiusAccServTotalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalResponses.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServTotalResponses.setUnits("packets")
_RadiusAccServTotalMalformedRequests_Type = Counter32
_RadiusAccServTotalMalformedRequests_Object = MibScalar
radiusAccServTotalMalformedRequests = _RadiusAccServTotalMalformedRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 9),
    _RadiusAccServTotalMalformedRequests_Type()
)
radiusAccServTotalMalformedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalMalformedRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServTotalMalformedRequests.setUnits("packets")
_RadiusAccServTotalBadAuthenticators_Type = Counter32
_RadiusAccServTotalBadAuthenticators_Object = MibScalar
radiusAccServTotalBadAuthenticators = _RadiusAccServTotalBadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 10),
    _RadiusAccServTotalBadAuthenticators_Type()
)
radiusAccServTotalBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalBadAuthenticators.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServTotalBadAuthenticators.setUnits("packets")
_RadiusAccServTotalPacketsDropped_Type = Counter32
_RadiusAccServTotalPacketsDropped_Object = MibScalar
radiusAccServTotalPacketsDropped = _RadiusAccServTotalPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 11),
    _RadiusAccServTotalPacketsDropped_Type()
)
radiusAccServTotalPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalPacketsDropped.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServTotalPacketsDropped.setUnits("packets")
_RadiusAccServTotalNoRecords_Type = Counter32
_RadiusAccServTotalNoRecords_Object = MibScalar
radiusAccServTotalNoRecords = _RadiusAccServTotalNoRecords_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 12),
    _RadiusAccServTotalNoRecords_Type()
)
radiusAccServTotalNoRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalNoRecords.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServTotalNoRecords.setUnits("packets")
_RadiusAccServTotalUnknownTypes_Type = Counter32
_RadiusAccServTotalUnknownTypes_Object = MibScalar
radiusAccServTotalUnknownTypes = _RadiusAccServTotalUnknownTypes_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 13),
    _RadiusAccServTotalUnknownTypes_Type()
)
radiusAccServTotalUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalUnknownTypes.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServTotalUnknownTypes.setUnits("packets")
_RadiusAccClientTable_Object = MibTable
radiusAccClientTable = _RadiusAccClientTable_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    radiusAccClientTable.setStatus("deprecated")
_RadiusAccClientEntry_Object = MibTableRow
radiusAccClientEntry = _RadiusAccClientEntry_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1)
)
radiusAccClientEntry.setIndexNames(
    (0, "RADIUS-ACC-SERVER-MIB", "radiusAccClientIndex"),
)
if mibBuilder.loadTexts:
    radiusAccClientEntry.setStatus("deprecated")


class _RadiusAccClientIndex_Type(Integer32):
    """Custom type radiusAccClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RadiusAccClientIndex_Type.__name__ = "Integer32"
_RadiusAccClientIndex_Object = MibTableColumn
radiusAccClientIndex = _RadiusAccClientIndex_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 1),
    _RadiusAccClientIndex_Type()
)
radiusAccClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAccClientIndex.setStatus("deprecated")
_RadiusAccClientAddress_Type = IpAddress
_RadiusAccClientAddress_Object = MibTableColumn
radiusAccClientAddress = _RadiusAccClientAddress_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 2),
    _RadiusAccClientAddress_Type()
)
radiusAccClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientAddress.setStatus("deprecated")
_RadiusAccClientID_Type = SnmpAdminString
_RadiusAccClientID_Object = MibTableColumn
radiusAccClientID = _RadiusAccClientID_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 3),
    _RadiusAccClientID_Type()
)
radiusAccClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientID.setStatus("deprecated")
_RadiusAccServPacketsDropped_Type = Counter32
_RadiusAccServPacketsDropped_Object = MibTableColumn
radiusAccServPacketsDropped = _RadiusAccServPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 4),
    _RadiusAccServPacketsDropped_Type()
)
radiusAccServPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServPacketsDropped.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccServPacketsDropped.setUnits("packets")
_RadiusAccServRequests_Type = Counter32
_RadiusAccServRequests_Object = MibTableColumn
radiusAccServRequests = _RadiusAccServRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 5),
    _RadiusAccServRequests_Type()
)
radiusAccServRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServRequests.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccServRequests.setUnits("packets")
_RadiusAccServDupRequests_Type = Counter32
_RadiusAccServDupRequests_Object = MibTableColumn
radiusAccServDupRequests = _RadiusAccServDupRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 6),
    _RadiusAccServDupRequests_Type()
)
radiusAccServDupRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServDupRequests.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccServDupRequests.setUnits("packets")
_RadiusAccServResponses_Type = Counter32
_RadiusAccServResponses_Object = MibTableColumn
radiusAccServResponses = _RadiusAccServResponses_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 7),
    _RadiusAccServResponses_Type()
)
radiusAccServResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServResponses.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccServResponses.setUnits("packets")
_RadiusAccServBadAuthenticators_Type = Counter32
_RadiusAccServBadAuthenticators_Object = MibTableColumn
radiusAccServBadAuthenticators = _RadiusAccServBadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 8),
    _RadiusAccServBadAuthenticators_Type()
)
radiusAccServBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServBadAuthenticators.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccServBadAuthenticators.setUnits("packets")
_RadiusAccServMalformedRequests_Type = Counter32
_RadiusAccServMalformedRequests_Object = MibTableColumn
radiusAccServMalformedRequests = _RadiusAccServMalformedRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 9),
    _RadiusAccServMalformedRequests_Type()
)
radiusAccServMalformedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServMalformedRequests.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccServMalformedRequests.setUnits("packets")
_RadiusAccServNoRecords_Type = Counter32
_RadiusAccServNoRecords_Object = MibTableColumn
radiusAccServNoRecords = _RadiusAccServNoRecords_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 10),
    _RadiusAccServNoRecords_Type()
)
radiusAccServNoRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServNoRecords.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccServNoRecords.setUnits("packets")
_RadiusAccServUnknownTypes_Type = Counter32
_RadiusAccServUnknownTypes_Object = MibTableColumn
radiusAccServUnknownTypes = _RadiusAccServUnknownTypes_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 11),
    _RadiusAccServUnknownTypes_Type()
)
radiusAccServUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServUnknownTypes.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAccServUnknownTypes.setUnits("packets")
_RadiusAccClientExtTable_Object = MibTable
radiusAccClientExtTable = _RadiusAccClientExtTable_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15)
)
if mibBuilder.loadTexts:
    radiusAccClientExtTable.setStatus("current")
_RadiusAccClientExtEntry_Object = MibTableRow
radiusAccClientExtEntry = _RadiusAccClientExtEntry_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1)
)
radiusAccClientExtEntry.setIndexNames(
    (0, "RADIUS-ACC-SERVER-MIB", "radiusAccClientExtIndex"),
)
if mibBuilder.loadTexts:
    radiusAccClientExtEntry.setStatus("current")


class _RadiusAccClientExtIndex_Type(Integer32):
    """Custom type radiusAccClientExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RadiusAccClientExtIndex_Type.__name__ = "Integer32"
_RadiusAccClientExtIndex_Object = MibTableColumn
radiusAccClientExtIndex = _RadiusAccClientExtIndex_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 1),
    _RadiusAccClientExtIndex_Type()
)
radiusAccClientExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAccClientExtIndex.setStatus("current")
_RadiusAccClientInetAddressType_Type = InetAddressType
_RadiusAccClientInetAddressType_Object = MibTableColumn
radiusAccClientInetAddressType = _RadiusAccClientInetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 2),
    _RadiusAccClientInetAddressType_Type()
)
radiusAccClientInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientInetAddressType.setStatus("current")
_RadiusAccClientInetAddress_Type = InetAddress
_RadiusAccClientInetAddress_Object = MibTableColumn
radiusAccClientInetAddress = _RadiusAccClientInetAddress_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 3),
    _RadiusAccClientInetAddress_Type()
)
radiusAccClientInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientInetAddress.setStatus("current")
_RadiusAccClientExtID_Type = SnmpAdminString
_RadiusAccClientExtID_Object = MibTableColumn
radiusAccClientExtID = _RadiusAccClientExtID_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 4),
    _RadiusAccClientExtID_Type()
)
radiusAccClientExtID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientExtID.setStatus("current")
_RadiusAccServExtPacketsDropped_Type = Counter32
_RadiusAccServExtPacketsDropped_Object = MibTableColumn
radiusAccServExtPacketsDropped = _RadiusAccServExtPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 5),
    _RadiusAccServExtPacketsDropped_Type()
)
radiusAccServExtPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServExtPacketsDropped.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServExtPacketsDropped.setUnits("packets")
_RadiusAccServExtRequests_Type = Counter32
_RadiusAccServExtRequests_Object = MibTableColumn
radiusAccServExtRequests = _RadiusAccServExtRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 6),
    _RadiusAccServExtRequests_Type()
)
radiusAccServExtRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServExtRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServExtRequests.setUnits("packets")
_RadiusAccServExtDupRequests_Type = Counter32
_RadiusAccServExtDupRequests_Object = MibTableColumn
radiusAccServExtDupRequests = _RadiusAccServExtDupRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 7),
    _RadiusAccServExtDupRequests_Type()
)
radiusAccServExtDupRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServExtDupRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServExtDupRequests.setUnits("packets")
_RadiusAccServExtResponses_Type = Counter32
_RadiusAccServExtResponses_Object = MibTableColumn
radiusAccServExtResponses = _RadiusAccServExtResponses_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 8),
    _RadiusAccServExtResponses_Type()
)
radiusAccServExtResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServExtResponses.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServExtResponses.setUnits("packets")
_RadiusAccServExtBadAuthenticators_Type = Counter32
_RadiusAccServExtBadAuthenticators_Object = MibTableColumn
radiusAccServExtBadAuthenticators = _RadiusAccServExtBadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 9),
    _RadiusAccServExtBadAuthenticators_Type()
)
radiusAccServExtBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServExtBadAuthenticators.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServExtBadAuthenticators.setUnits("packets")
_RadiusAccServExtMalformedRequests_Type = Counter32
_RadiusAccServExtMalformedRequests_Object = MibTableColumn
radiusAccServExtMalformedRequests = _RadiusAccServExtMalformedRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 10),
    _RadiusAccServExtMalformedRequests_Type()
)
radiusAccServExtMalformedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServExtMalformedRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServExtMalformedRequests.setUnits("packets")
_RadiusAccServExtNoRecords_Type = Counter32
_RadiusAccServExtNoRecords_Object = MibTableColumn
radiusAccServExtNoRecords = _RadiusAccServExtNoRecords_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 11),
    _RadiusAccServExtNoRecords_Type()
)
radiusAccServExtNoRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServExtNoRecords.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServExtNoRecords.setUnits("packets")
_RadiusAccServExtUnknownTypes_Type = Counter32
_RadiusAccServExtUnknownTypes_Object = MibTableColumn
radiusAccServExtUnknownTypes = _RadiusAccServExtUnknownTypes_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 12),
    _RadiusAccServExtUnknownTypes_Type()
)
radiusAccServExtUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServExtUnknownTypes.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServExtUnknownTypes.setUnits("packets")
_RadiusAccServerCounterDiscontinuity_Type = TimeTicks
_RadiusAccServerCounterDiscontinuity_Object = MibTableColumn
radiusAccServerCounterDiscontinuity = _RadiusAccServerCounterDiscontinuity_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 13),
    _RadiusAccServerCounterDiscontinuity_Type()
)
radiusAccServerCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServerCounterDiscontinuity.setStatus("current")
if mibBuilder.loadTexts:
    radiusAccServerCounterDiscontinuity.setUnits("centiseconds")
_RadiusAccServMIBConformance_ObjectIdentity = ObjectIdentity
radiusAccServMIBConformance = _RadiusAccServMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 2)
)
_RadiusAccServMIBCompliances_ObjectIdentity = ObjectIdentity
radiusAccServMIBCompliances = _RadiusAccServMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 1)
)
_RadiusAccServMIBGroups_ObjectIdentity = ObjectIdentity
radiusAccServMIBGroups = _RadiusAccServMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 2)
)

# Managed Objects groups

radiusAccServMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 2, 1)
)
radiusAccServMIBGroup.setObjects(
      *(("RADIUS-ACC-SERVER-MIB", "radiusAccServIdent"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServUpTime"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServResetTime"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServConfigReset"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalInvalidRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalDupRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalResponses"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalMalformedRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalBadAuthenticators"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalPacketsDropped"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalNoRecords"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalUnknownTypes"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccClientAddress"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccClientID"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServPacketsDropped"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServDupRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServResponses"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServBadAuthenticators"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServMalformedRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServNoRecords"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServUnknownTypes"))
)
if mibBuilder.loadTexts:
    radiusAccServMIBGroup.setStatus("deprecated")

radiusAccServExtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 2, 2)
)
radiusAccServExtMIBGroup.setObjects(
      *(("RADIUS-ACC-SERVER-MIB", "radiusAccServIdent"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServUpTime"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServResetTime"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServConfigReset"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalInvalidRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalDupRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalResponses"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalMalformedRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalBadAuthenticators"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalPacketsDropped"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalNoRecords"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalUnknownTypes"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccClientInetAddressType"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccClientInetAddress"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccClientExtID"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtPacketsDropped"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtDupRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtResponses"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtBadAuthenticators"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtMalformedRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtNoRecords"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServExtUnknownTypes"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServerCounterDiscontinuity"))
)
if mibBuilder.loadTexts:
    radiusAccServExtMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

radiusAccServMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    radiusAccServMIBCompliance.setStatus(
        "deprecated"
    )

radiusAccServExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    radiusAccServExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADIUS-ACC-SERVER-MIB",
    **{"radiusMIB": radiusMIB,
       "radiusAccounting": radiusAccounting,
       "radiusAccServMIB": radiusAccServMIB,
       "radiusAccServMIBObjects": radiusAccServMIBObjects,
       "radiusAccServ": radiusAccServ,
       "radiusAccServIdent": radiusAccServIdent,
       "radiusAccServUpTime": radiusAccServUpTime,
       "radiusAccServResetTime": radiusAccServResetTime,
       "radiusAccServConfigReset": radiusAccServConfigReset,
       "radiusAccServTotalRequests": radiusAccServTotalRequests,
       "radiusAccServTotalInvalidRequests": radiusAccServTotalInvalidRequests,
       "radiusAccServTotalDupRequests": radiusAccServTotalDupRequests,
       "radiusAccServTotalResponses": radiusAccServTotalResponses,
       "radiusAccServTotalMalformedRequests": radiusAccServTotalMalformedRequests,
       "radiusAccServTotalBadAuthenticators": radiusAccServTotalBadAuthenticators,
       "radiusAccServTotalPacketsDropped": radiusAccServTotalPacketsDropped,
       "radiusAccServTotalNoRecords": radiusAccServTotalNoRecords,
       "radiusAccServTotalUnknownTypes": radiusAccServTotalUnknownTypes,
       "radiusAccClientTable": radiusAccClientTable,
       "radiusAccClientEntry": radiusAccClientEntry,
       "radiusAccClientIndex": radiusAccClientIndex,
       "radiusAccClientAddress": radiusAccClientAddress,
       "radiusAccClientID": radiusAccClientID,
       "radiusAccServPacketsDropped": radiusAccServPacketsDropped,
       "radiusAccServRequests": radiusAccServRequests,
       "radiusAccServDupRequests": radiusAccServDupRequests,
       "radiusAccServResponses": radiusAccServResponses,
       "radiusAccServBadAuthenticators": radiusAccServBadAuthenticators,
       "radiusAccServMalformedRequests": radiusAccServMalformedRequests,
       "radiusAccServNoRecords": radiusAccServNoRecords,
       "radiusAccServUnknownTypes": radiusAccServUnknownTypes,
       "radiusAccClientExtTable": radiusAccClientExtTable,
       "radiusAccClientExtEntry": radiusAccClientExtEntry,
       "radiusAccClientExtIndex": radiusAccClientExtIndex,
       "radiusAccClientInetAddressType": radiusAccClientInetAddressType,
       "radiusAccClientInetAddress": radiusAccClientInetAddress,
       "radiusAccClientExtID": radiusAccClientExtID,
       "radiusAccServExtPacketsDropped": radiusAccServExtPacketsDropped,
       "radiusAccServExtRequests": radiusAccServExtRequests,
       "radiusAccServExtDupRequests": radiusAccServExtDupRequests,
       "radiusAccServExtResponses": radiusAccServExtResponses,
       "radiusAccServExtBadAuthenticators": radiusAccServExtBadAuthenticators,
       "radiusAccServExtMalformedRequests": radiusAccServExtMalformedRequests,
       "radiusAccServExtNoRecords": radiusAccServExtNoRecords,
       "radiusAccServExtUnknownTypes": radiusAccServExtUnknownTypes,
       "radiusAccServerCounterDiscontinuity": radiusAccServerCounterDiscontinuity,
       "radiusAccServMIBConformance": radiusAccServMIBConformance,
       "radiusAccServMIBCompliances": radiusAccServMIBCompliances,
       "radiusAccServMIBCompliance": radiusAccServMIBCompliance,
       "radiusAccServExtMIBCompliance": radiusAccServExtMIBCompliance,
       "radiusAccServMIBGroups": radiusAccServMIBGroups,
       "radiusAccServMIBGroup": radiusAccServMIBGroup,
       "radiusAccServExtMIBGroup": radiusAccServExtMIBGroup}
)
