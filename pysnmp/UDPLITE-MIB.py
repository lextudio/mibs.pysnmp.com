# SNMP MIB module (UDPLITE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UDPLITE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:25 2024
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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

udpliteMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 170)
)
udpliteMIB.setRevisions(
        ("2007-12-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Udplite_ObjectIdentity = ObjectIdentity
udplite = _Udplite_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 170, 1)
)
_UdpliteInDatagrams_Type = Counter64
_UdpliteInDatagrams_Object = MibScalar
udpliteInDatagrams = _UdpliteInDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 1),
    _UdpliteInDatagrams_Type()
)
udpliteInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpliteInDatagrams.setStatus("current")
_UdpliteInPartialCov_Type = Counter64
_UdpliteInPartialCov_Object = MibScalar
udpliteInPartialCov = _UdpliteInPartialCov_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 2),
    _UdpliteInPartialCov_Type()
)
udpliteInPartialCov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpliteInPartialCov.setStatus("current")
_UdpliteNoPorts_Type = Counter32
_UdpliteNoPorts_Object = MibScalar
udpliteNoPorts = _UdpliteNoPorts_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 3),
    _UdpliteNoPorts_Type()
)
udpliteNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpliteNoPorts.setStatus("current")
_UdpliteInErrors_Type = Counter32
_UdpliteInErrors_Object = MibScalar
udpliteInErrors = _UdpliteInErrors_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 4),
    _UdpliteInErrors_Type()
)
udpliteInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpliteInErrors.setStatus("current")
_UdpliteInBadChecksum_Type = Counter32
_UdpliteInBadChecksum_Object = MibScalar
udpliteInBadChecksum = _UdpliteInBadChecksum_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 5),
    _UdpliteInBadChecksum_Type()
)
udpliteInBadChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpliteInBadChecksum.setStatus("current")
_UdpliteOutDatagrams_Type = Counter64
_UdpliteOutDatagrams_Object = MibScalar
udpliteOutDatagrams = _UdpliteOutDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 6),
    _UdpliteOutDatagrams_Type()
)
udpliteOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpliteOutDatagrams.setStatus("current")
_UdpliteOutPartialCov_Type = Counter64
_UdpliteOutPartialCov_Object = MibScalar
udpliteOutPartialCov = _UdpliteOutPartialCov_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 7),
    _UdpliteOutPartialCov_Type()
)
udpliteOutPartialCov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpliteOutPartialCov.setStatus("current")
_UdpliteEndpointTable_Object = MibTable
udpliteEndpointTable = _UdpliteEndpointTable_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 8)
)
if mibBuilder.loadTexts:
    udpliteEndpointTable.setStatus("current")
_UdpliteEndpointEntry_Object = MibTableRow
udpliteEndpointEntry = _UdpliteEndpointEntry_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 8, 1)
)
udpliteEndpointEntry.setIndexNames(
    (0, "UDPLITE-MIB", "udpliteEndpointLocalAddressType"),
    (0, "UDPLITE-MIB", "udpliteEndpointLocalAddress"),
    (0, "UDPLITE-MIB", "udpliteEndpointLocalPort"),
    (0, "UDPLITE-MIB", "udpliteEndpointRemoteAddressType"),
    (0, "UDPLITE-MIB", "udpliteEndpointRemoteAddress"),
    (0, "UDPLITE-MIB", "udpliteEndpointRemotePort"),
    (0, "UDPLITE-MIB", "udpliteEndpointInstance"),
)
if mibBuilder.loadTexts:
    udpliteEndpointEntry.setStatus("current")
_UdpliteEndpointLocalAddressType_Type = InetAddressType
_UdpliteEndpointLocalAddressType_Object = MibTableColumn
udpliteEndpointLocalAddressType = _UdpliteEndpointLocalAddressType_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 8, 1, 1),
    _UdpliteEndpointLocalAddressType_Type()
)
udpliteEndpointLocalAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    udpliteEndpointLocalAddressType.setStatus("current")
_UdpliteEndpointLocalAddress_Type = InetAddress
_UdpliteEndpointLocalAddress_Object = MibTableColumn
udpliteEndpointLocalAddress = _UdpliteEndpointLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 8, 1, 2),
    _UdpliteEndpointLocalAddress_Type()
)
udpliteEndpointLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    udpliteEndpointLocalAddress.setStatus("current")
_UdpliteEndpointLocalPort_Type = InetPortNumber
_UdpliteEndpointLocalPort_Object = MibTableColumn
udpliteEndpointLocalPort = _UdpliteEndpointLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 8, 1, 3),
    _UdpliteEndpointLocalPort_Type()
)
udpliteEndpointLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    udpliteEndpointLocalPort.setStatus("current")
_UdpliteEndpointRemoteAddressType_Type = InetAddressType
_UdpliteEndpointRemoteAddressType_Object = MibTableColumn
udpliteEndpointRemoteAddressType = _UdpliteEndpointRemoteAddressType_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 8, 1, 4),
    _UdpliteEndpointRemoteAddressType_Type()
)
udpliteEndpointRemoteAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    udpliteEndpointRemoteAddressType.setStatus("current")
_UdpliteEndpointRemoteAddress_Type = InetAddress
_UdpliteEndpointRemoteAddress_Object = MibTableColumn
udpliteEndpointRemoteAddress = _UdpliteEndpointRemoteAddress_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 8, 1, 5),
    _UdpliteEndpointRemoteAddress_Type()
)
udpliteEndpointRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    udpliteEndpointRemoteAddress.setStatus("current")
_UdpliteEndpointRemotePort_Type = InetPortNumber
_UdpliteEndpointRemotePort_Object = MibTableColumn
udpliteEndpointRemotePort = _UdpliteEndpointRemotePort_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 8, 1, 6),
    _UdpliteEndpointRemotePort_Type()
)
udpliteEndpointRemotePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    udpliteEndpointRemotePort.setStatus("current")


class _UdpliteEndpointInstance_Type(Unsigned32):
    """Custom type udpliteEndpointInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_UdpliteEndpointInstance_Type.__name__ = "Unsigned32"
_UdpliteEndpointInstance_Object = MibTableColumn
udpliteEndpointInstance = _UdpliteEndpointInstance_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 8, 1, 7),
    _UdpliteEndpointInstance_Type()
)
udpliteEndpointInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    udpliteEndpointInstance.setStatus("current")
_UdpliteEndpointProcess_Type = Unsigned32
_UdpliteEndpointProcess_Object = MibTableColumn
udpliteEndpointProcess = _UdpliteEndpointProcess_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 8, 1, 8),
    _UdpliteEndpointProcess_Type()
)
udpliteEndpointProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpliteEndpointProcess.setStatus("current")
_UdpliteEndpointMinCoverage_Type = Unsigned32
_UdpliteEndpointMinCoverage_Object = MibTableColumn
udpliteEndpointMinCoverage = _UdpliteEndpointMinCoverage_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 8, 1, 9),
    _UdpliteEndpointMinCoverage_Type()
)
udpliteEndpointMinCoverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpliteEndpointMinCoverage.setStatus("current")
_UdpliteEndpointViolCoverage_Type = Counter32
_UdpliteEndpointViolCoverage_Object = MibTableColumn
udpliteEndpointViolCoverage = _UdpliteEndpointViolCoverage_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 8, 1, 10),
    _UdpliteEndpointViolCoverage_Type()
)
udpliteEndpointViolCoverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpliteEndpointViolCoverage.setStatus("current")
_UdpliteStatsDiscontinuityTime_Type = TimeStamp
_UdpliteStatsDiscontinuityTime_Object = MibScalar
udpliteStatsDiscontinuityTime = _UdpliteStatsDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 170, 1, 9),
    _UdpliteStatsDiscontinuityTime_Type()
)
udpliteStatsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpliteStatsDiscontinuityTime.setStatus("current")
_UdpliteMIBConformance_ObjectIdentity = ObjectIdentity
udpliteMIBConformance = _UdpliteMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 170, 2)
)
_UdpliteMIBGroups_ObjectIdentity = ObjectIdentity
udpliteMIBGroups = _UdpliteMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 170, 2, 2)
)

# Managed Objects groups

udpliteBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 170, 2, 2, 1)
)
udpliteBaseGroup.setObjects(
      *(("UDPLITE-MIB", "udpliteInDatagrams"),
        ("UDPLITE-MIB", "udpliteNoPorts"),
        ("UDPLITE-MIB", "udpliteInErrors"),
        ("UDPLITE-MIB", "udpliteOutDatagrams"),
        ("UDPLITE-MIB", "udpliteStatsDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    udpliteBaseGroup.setStatus("current")

udplitePartialCsumGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 170, 2, 2, 2)
)
udplitePartialCsumGroup.setObjects(
      *(("UDPLITE-MIB", "udpliteInPartialCov"),
        ("UDPLITE-MIB", "udpliteInBadChecksum"),
        ("UDPLITE-MIB", "udpliteOutPartialCov"))
)
if mibBuilder.loadTexts:
    udplitePartialCsumGroup.setStatus("current")

udpliteEndpointGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 170, 2, 2, 3)
)
udpliteEndpointGroup.setObjects(
      *(("UDPLITE-MIB", "udpliteEndpointProcess"),
        ("UDPLITE-MIB", "udpliteEndpointMinCoverage"))
)
if mibBuilder.loadTexts:
    udpliteEndpointGroup.setStatus("current")

udpliteAppGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 170, 2, 2, 4)
)
udpliteAppGroup.setObjects(
    ("UDPLITE-MIB", "udpliteEndpointViolCoverage")
)
if mibBuilder.loadTexts:
    udpliteAppGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

udpliteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 170, 2, 1)
)
if mibBuilder.loadTexts:
    udpliteMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UDPLITE-MIB",
    **{"udpliteMIB": udpliteMIB,
       "udplite": udplite,
       "udpliteInDatagrams": udpliteInDatagrams,
       "udpliteInPartialCov": udpliteInPartialCov,
       "udpliteNoPorts": udpliteNoPorts,
       "udpliteInErrors": udpliteInErrors,
       "udpliteInBadChecksum": udpliteInBadChecksum,
       "udpliteOutDatagrams": udpliteOutDatagrams,
       "udpliteOutPartialCov": udpliteOutPartialCov,
       "udpliteEndpointTable": udpliteEndpointTable,
       "udpliteEndpointEntry": udpliteEndpointEntry,
       "udpliteEndpointLocalAddressType": udpliteEndpointLocalAddressType,
       "udpliteEndpointLocalAddress": udpliteEndpointLocalAddress,
       "udpliteEndpointLocalPort": udpliteEndpointLocalPort,
       "udpliteEndpointRemoteAddressType": udpliteEndpointRemoteAddressType,
       "udpliteEndpointRemoteAddress": udpliteEndpointRemoteAddress,
       "udpliteEndpointRemotePort": udpliteEndpointRemotePort,
       "udpliteEndpointInstance": udpliteEndpointInstance,
       "udpliteEndpointProcess": udpliteEndpointProcess,
       "udpliteEndpointMinCoverage": udpliteEndpointMinCoverage,
       "udpliteEndpointViolCoverage": udpliteEndpointViolCoverage,
       "udpliteStatsDiscontinuityTime": udpliteStatsDiscontinuityTime,
       "udpliteMIBConformance": udpliteMIBConformance,
       "udpliteMIBCompliance": udpliteMIBCompliance,
       "udpliteMIBGroups": udpliteMIBGroups,
       "udpliteBaseGroup": udpliteBaseGroup,
       "udplitePartialCsumGroup": udplitePartialCsumGroup,
       "udpliteEndpointGroup": udpliteEndpointGroup,
       "udpliteAppGroup": udpliteAppGroup}
)
