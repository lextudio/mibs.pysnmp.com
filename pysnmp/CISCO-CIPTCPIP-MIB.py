# SNMP MIB module (CISCO-CIPTCPIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CIPTCPIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:28 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoCipTcpIpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 32)
)
ciscoCipTcpIpMIB.setRevisions(
        ("1998-01-06 00:00",
         "1995-08-21 00:00",
         "1995-04-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CipTcpIpObjects_ObjectIdentity = ObjectIdentity
cipTcpIpObjects = _CipTcpIpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1)
)
_CipIpObjects_ObjectIdentity = ObjectIdentity
cipIpObjects = _CipIpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1)
)
_CipIpTable_Object = MibTable
cipIpTable = _CipIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cipIpTable.setStatus("current")
_CipIpEntry_Object = MibTableRow
cipIpEntry = _CipIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1)
)
cipIpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CIPTCPIP-MIB", "cipIpAddress"),
)
if mibBuilder.loadTexts:
    cipIpEntry.setStatus("current")
_CipIpAddress_Type = IpAddress
_CipIpAddress_Object = MibTableColumn
cipIpAddress = _CipIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 1),
    _CipIpAddress_Type()
)
cipIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipIpAddress.setStatus("current")


class _CipIpForwarding_Type(Integer32):
    """Custom type cipIpForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notForwarding", 2))
    )


_CipIpForwarding_Type.__name__ = "Integer32"
_CipIpForwarding_Object = MibTableColumn
cipIpForwarding = _CipIpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 2),
    _CipIpForwarding_Type()
)
cipIpForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipIpForwarding.setStatus("current")


class _CipIpDefaultTTL_Type(Integer32):
    """Custom type cipIpDefaultTTL based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CipIpDefaultTTL_Type.__name__ = "Integer32"
_CipIpDefaultTTL_Object = MibTableColumn
cipIpDefaultTTL = _CipIpDefaultTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 3),
    _CipIpDefaultTTL_Type()
)
cipIpDefaultTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipIpDefaultTTL.setStatus("current")
_CipIpInReceives_Type = Counter32
_CipIpInReceives_Object = MibTableColumn
cipIpInReceives = _CipIpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 4),
    _CipIpInReceives_Type()
)
cipIpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpInReceives.setStatus("current")
_CipIpInHdrErrors_Type = Counter32
_CipIpInHdrErrors_Object = MibTableColumn
cipIpInHdrErrors = _CipIpInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 5),
    _CipIpInHdrErrors_Type()
)
cipIpInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpInHdrErrors.setStatus("current")
_CipIpInAddrErrors_Type = Counter32
_CipIpInAddrErrors_Object = MibTableColumn
cipIpInAddrErrors = _CipIpInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 6),
    _CipIpInAddrErrors_Type()
)
cipIpInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpInAddrErrors.setStatus("current")
_CipIpForwDatagrams_Type = Counter32
_CipIpForwDatagrams_Object = MibTableColumn
cipIpForwDatagrams = _CipIpForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 7),
    _CipIpForwDatagrams_Type()
)
cipIpForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpForwDatagrams.setStatus("current")
_CipIpInUnknownProtos_Type = Counter32
_CipIpInUnknownProtos_Object = MibTableColumn
cipIpInUnknownProtos = _CipIpInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 8),
    _CipIpInUnknownProtos_Type()
)
cipIpInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpInUnknownProtos.setStatus("current")
_CipIpInDiscards_Type = Counter32
_CipIpInDiscards_Object = MibTableColumn
cipIpInDiscards = _CipIpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 9),
    _CipIpInDiscards_Type()
)
cipIpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpInDiscards.setStatus("current")
_CipIpInDelivers_Type = Counter32
_CipIpInDelivers_Object = MibTableColumn
cipIpInDelivers = _CipIpInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 10),
    _CipIpInDelivers_Type()
)
cipIpInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpInDelivers.setStatus("current")
_CipIpOutRequests_Type = Counter32
_CipIpOutRequests_Object = MibTableColumn
cipIpOutRequests = _CipIpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 11),
    _CipIpOutRequests_Type()
)
cipIpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpOutRequests.setStatus("current")
_CipIpOutDiscards_Type = Counter32
_CipIpOutDiscards_Object = MibTableColumn
cipIpOutDiscards = _CipIpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 12),
    _CipIpOutDiscards_Type()
)
cipIpOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpOutDiscards.setStatus("current")
_CipIpOutNoRoutes_Type = Counter32
_CipIpOutNoRoutes_Object = MibTableColumn
cipIpOutNoRoutes = _CipIpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 13),
    _CipIpOutNoRoutes_Type()
)
cipIpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpOutNoRoutes.setStatus("current")
_CipIpReasmTimeout_Type = Integer32
_CipIpReasmTimeout_Object = MibTableColumn
cipIpReasmTimeout = _CipIpReasmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 14),
    _CipIpReasmTimeout_Type()
)
cipIpReasmTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpReasmTimeout.setStatus("current")
_CipIpReasmReqds_Type = Counter32
_CipIpReasmReqds_Object = MibTableColumn
cipIpReasmReqds = _CipIpReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 15),
    _CipIpReasmReqds_Type()
)
cipIpReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpReasmReqds.setStatus("current")
_CipIpReasmOKs_Type = Counter32
_CipIpReasmOKs_Object = MibTableColumn
cipIpReasmOKs = _CipIpReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 16),
    _CipIpReasmOKs_Type()
)
cipIpReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpReasmOKs.setStatus("current")
_CipIpReasmFails_Type = Counter32
_CipIpReasmFails_Object = MibTableColumn
cipIpReasmFails = _CipIpReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 17),
    _CipIpReasmFails_Type()
)
cipIpReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpReasmFails.setStatus("current")
_CipIpFragOKs_Type = Counter32
_CipIpFragOKs_Object = MibTableColumn
cipIpFragOKs = _CipIpFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 18),
    _CipIpFragOKs_Type()
)
cipIpFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpFragOKs.setStatus("current")
_CipIpFragFails_Type = Counter32
_CipIpFragFails_Object = MibTableColumn
cipIpFragFails = _CipIpFragFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 19),
    _CipIpFragFails_Type()
)
cipIpFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpFragFails.setStatus("current")
_CipIpFragCreates_Type = Counter32
_CipIpFragCreates_Object = MibTableColumn
cipIpFragCreates = _CipIpFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 20),
    _CipIpFragCreates_Type()
)
cipIpFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpFragCreates.setStatus("current")
_CipIpRoutingDiscards_Type = Counter32
_CipIpRoutingDiscards_Object = MibTableColumn
cipIpRoutingDiscards = _CipIpRoutingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 21),
    _CipIpRoutingDiscards_Type()
)
cipIpRoutingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIpRoutingDiscards.setStatus("current")
_CipTcpObjects_ObjectIdentity = ObjectIdentity
cipTcpObjects = _CipTcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2)
)
_CipTcpStackTable_Object = MibTable
cipTcpStackTable = _CipTcpStackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cipTcpStackTable.setStatus("current")
_CipTcpStackEntry_Object = MibTableRow
cipTcpStackEntry = _CipTcpStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1)
)
cipTcpStackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CIPTCPIP-MIB", "cipIpAddress"),
)
if mibBuilder.loadTexts:
    cipTcpStackEntry.setStatus("current")


class _CipTcpRtoAlgorithm_Type(Integer32):
    """Custom type cipTcpRtoAlgorithm based on Integer32"""
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
        *(("constant", 2),
          ("other", 1),
          ("rsre", 3),
          ("vanj", 4))
    )


_CipTcpRtoAlgorithm_Type.__name__ = "Integer32"
_CipTcpRtoAlgorithm_Object = MibTableColumn
cipTcpRtoAlgorithm = _CipTcpRtoAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 1),
    _CipTcpRtoAlgorithm_Type()
)
cipTcpRtoAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpRtoAlgorithm.setStatus("current")
_CipTcpRtoMin_Type = Integer32
_CipTcpRtoMin_Object = MibTableColumn
cipTcpRtoMin = _CipTcpRtoMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 2),
    _CipTcpRtoMin_Type()
)
cipTcpRtoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpRtoMin.setStatus("current")
if mibBuilder.loadTexts:
    cipTcpRtoMin.setUnits("milliseconds")
_CipTcpRtoMax_Type = Integer32
_CipTcpRtoMax_Object = MibTableColumn
cipTcpRtoMax = _CipTcpRtoMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 3),
    _CipTcpRtoMax_Type()
)
cipTcpRtoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpRtoMax.setStatus("current")
if mibBuilder.loadTexts:
    cipTcpRtoMax.setUnits("milliseconds")
_CipTcpMaxConn_Type = Integer32
_CipTcpMaxConn_Object = MibTableColumn
cipTcpMaxConn = _CipTcpMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 4),
    _CipTcpMaxConn_Type()
)
cipTcpMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpMaxConn.setStatus("current")
_CipTcpActiveOpens_Type = Counter32
_CipTcpActiveOpens_Object = MibTableColumn
cipTcpActiveOpens = _CipTcpActiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 5),
    _CipTcpActiveOpens_Type()
)
cipTcpActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpActiveOpens.setStatus("current")
_CipTcpPassiveOpens_Type = Counter32
_CipTcpPassiveOpens_Object = MibTableColumn
cipTcpPassiveOpens = _CipTcpPassiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 6),
    _CipTcpPassiveOpens_Type()
)
cipTcpPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpPassiveOpens.setStatus("current")
_CipTcpAttemptFails_Type = Counter32
_CipTcpAttemptFails_Object = MibTableColumn
cipTcpAttemptFails = _CipTcpAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 7),
    _CipTcpAttemptFails_Type()
)
cipTcpAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpAttemptFails.setStatus("current")
_CipTcpEstabResets_Type = Counter32
_CipTcpEstabResets_Object = MibTableColumn
cipTcpEstabResets = _CipTcpEstabResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 8),
    _CipTcpEstabResets_Type()
)
cipTcpEstabResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpEstabResets.setStatus("current")
_CipTcpCurrEstab_Type = Gauge32
_CipTcpCurrEstab_Object = MibTableColumn
cipTcpCurrEstab = _CipTcpCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 9),
    _CipTcpCurrEstab_Type()
)
cipTcpCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpCurrEstab.setStatus("current")
_CipTcpInSegs_Type = Counter32
_CipTcpInSegs_Object = MibTableColumn
cipTcpInSegs = _CipTcpInSegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 10),
    _CipTcpInSegs_Type()
)
cipTcpInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpInSegs.setStatus("current")
_CipTcpOutSegs_Type = Counter32
_CipTcpOutSegs_Object = MibTableColumn
cipTcpOutSegs = _CipTcpOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 11),
    _CipTcpOutSegs_Type()
)
cipTcpOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpOutSegs.setStatus("current")
_CipTcpRetransSegs_Type = Counter32
_CipTcpRetransSegs_Object = MibTableColumn
cipTcpRetransSegs = _CipTcpRetransSegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 12),
    _CipTcpRetransSegs_Type()
)
cipTcpRetransSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpRetransSegs.setStatus("current")
_CipTcpInErrs_Type = Counter32
_CipTcpInErrs_Object = MibTableColumn
cipTcpInErrs = _CipTcpInErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 13),
    _CipTcpInErrs_Type()
)
cipTcpInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpInErrs.setStatus("current")
_CipTcpOutRsts_Type = Counter32
_CipTcpOutRsts_Object = MibTableColumn
cipTcpOutRsts = _CipTcpOutRsts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 14),
    _CipTcpOutRsts_Type()
)
cipTcpOutRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpOutRsts.setStatus("current")
_CipTcpConnTable_Object = MibTable
cipTcpConnTable = _CipTcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cipTcpConnTable.setStatus("current")
_CipTcpConnEntry_Object = MibTableRow
cipTcpConnEntry = _CipTcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1)
)
cipTcpConnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CIPTCPIP-MIB", "cipIpAddress"),
    (0, "CISCO-CIPTCPIP-MIB", "cipTcpConnLocalPort"),
    (0, "CISCO-CIPTCPIP-MIB", "cipTcpConnRemAddress"),
    (0, "CISCO-CIPTCPIP-MIB", "cipTcpConnRemPort"),
)
if mibBuilder.loadTexts:
    cipTcpConnEntry.setStatus("current")


class _CipTcpConnLocalPort_Type(Integer32):
    """Custom type cipTcpConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CipTcpConnLocalPort_Type.__name__ = "Integer32"
_CipTcpConnLocalPort_Object = MibTableColumn
cipTcpConnLocalPort = _CipTcpConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1, 1),
    _CipTcpConnLocalPort_Type()
)
cipTcpConnLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipTcpConnLocalPort.setStatus("current")
_CipTcpConnRemAddress_Type = IpAddress
_CipTcpConnRemAddress_Object = MibTableColumn
cipTcpConnRemAddress = _CipTcpConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1, 2),
    _CipTcpConnRemAddress_Type()
)
cipTcpConnRemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipTcpConnRemAddress.setStatus("current")


class _CipTcpConnRemPort_Type(Integer32):
    """Custom type cipTcpConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CipTcpConnRemPort_Type.__name__ = "Integer32"
_CipTcpConnRemPort_Object = MibTableColumn
cipTcpConnRemPort = _CipTcpConnRemPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1, 3),
    _CipTcpConnRemPort_Type()
)
cipTcpConnRemPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipTcpConnRemPort.setStatus("current")


class _CipTcpConnState_Type(Integer32):
    """Custom type cipTcpConnState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("closeWait", 8),
          ("closed", 1),
          ("closing", 10),
          ("deleteTCB", 12),
          ("established", 5),
          ("finWait1", 6),
          ("finWait2", 7),
          ("lastAck", 9),
          ("listen", 2),
          ("synReceived", 4),
          ("synSent", 3),
          ("timeWait", 11))
    )


_CipTcpConnState_Type.__name__ = "Integer32"
_CipTcpConnState_Object = MibTableColumn
cipTcpConnState = _CipTcpConnState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1, 4),
    _CipTcpConnState_Type()
)
cipTcpConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipTcpConnState.setStatus("current")
_CipTcpConnInHCBytes_Type = Counter64
_CipTcpConnInHCBytes_Object = MibTableColumn
cipTcpConnInHCBytes = _CipTcpConnInHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1, 5),
    _CipTcpConnInHCBytes_Type()
)
cipTcpConnInHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpConnInHCBytes.setStatus("current")
if mibBuilder.loadTexts:
    cipTcpConnInHCBytes.setUnits("octets")
_CipTcpConnInBytes_Type = Counter32
_CipTcpConnInBytes_Object = MibTableColumn
cipTcpConnInBytes = _CipTcpConnInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1, 6),
    _CipTcpConnInBytes_Type()
)
cipTcpConnInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpConnInBytes.setStatus("current")
if mibBuilder.loadTexts:
    cipTcpConnInBytes.setUnits("octets")
_CipTcpConnOutHCBytes_Type = Counter64
_CipTcpConnOutHCBytes_Object = MibTableColumn
cipTcpConnOutHCBytes = _CipTcpConnOutHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1, 7),
    _CipTcpConnOutHCBytes_Type()
)
cipTcpConnOutHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpConnOutHCBytes.setStatus("current")
if mibBuilder.loadTexts:
    cipTcpConnOutHCBytes.setUnits("octets")
_CipTcpConnOutBytes_Type = Counter32
_CipTcpConnOutBytes_Object = MibTableColumn
cipTcpConnOutBytes = _CipTcpConnOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1, 8),
    _CipTcpConnOutBytes_Type()
)
cipTcpConnOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTcpConnOutBytes.setStatus("current")
if mibBuilder.loadTexts:
    cipTcpConnOutBytes.setUnits("octets")
_CipIcmpObjects_ObjectIdentity = ObjectIdentity
cipIcmpObjects = _CipIcmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3)
)
_CipIcmpTable_Object = MibTable
cipIcmpTable = _CipIcmpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cipIcmpTable.setStatus("current")
_CipIcmpEntry_Object = MibTableRow
cipIcmpEntry = _CipIcmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1)
)
cipIcmpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CIPTCPIP-MIB", "cipIpAddress"),
)
if mibBuilder.loadTexts:
    cipIcmpEntry.setStatus("current")
_CipIcmpInMsgs_Type = Counter32
_CipIcmpInMsgs_Object = MibTableColumn
cipIcmpInMsgs = _CipIcmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 1),
    _CipIcmpInMsgs_Type()
)
cipIcmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpInMsgs.setStatus("current")
_CipIcmpInErrors_Type = Counter32
_CipIcmpInErrors_Object = MibTableColumn
cipIcmpInErrors = _CipIcmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 2),
    _CipIcmpInErrors_Type()
)
cipIcmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpInErrors.setStatus("current")
_CipIcmpInDestUnreachs_Type = Counter32
_CipIcmpInDestUnreachs_Object = MibTableColumn
cipIcmpInDestUnreachs = _CipIcmpInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 3),
    _CipIcmpInDestUnreachs_Type()
)
cipIcmpInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpInDestUnreachs.setStatus("current")
_CipIcmpInTimeExcds_Type = Counter32
_CipIcmpInTimeExcds_Object = MibTableColumn
cipIcmpInTimeExcds = _CipIcmpInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 4),
    _CipIcmpInTimeExcds_Type()
)
cipIcmpInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpInTimeExcds.setStatus("current")
_CipIcmpInParmProbs_Type = Counter32
_CipIcmpInParmProbs_Object = MibTableColumn
cipIcmpInParmProbs = _CipIcmpInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 5),
    _CipIcmpInParmProbs_Type()
)
cipIcmpInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpInParmProbs.setStatus("current")
_CipIcmpInSrcQuenchs_Type = Counter32
_CipIcmpInSrcQuenchs_Object = MibTableColumn
cipIcmpInSrcQuenchs = _CipIcmpInSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 6),
    _CipIcmpInSrcQuenchs_Type()
)
cipIcmpInSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpInSrcQuenchs.setStatus("current")
_CipIcmpInRedirects_Type = Counter32
_CipIcmpInRedirects_Object = MibTableColumn
cipIcmpInRedirects = _CipIcmpInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 7),
    _CipIcmpInRedirects_Type()
)
cipIcmpInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpInRedirects.setStatus("current")
_CipIcmpInEchos_Type = Counter32
_CipIcmpInEchos_Object = MibTableColumn
cipIcmpInEchos = _CipIcmpInEchos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 8),
    _CipIcmpInEchos_Type()
)
cipIcmpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpInEchos.setStatus("current")
_CipIcmpInAddrMaskReps_Type = Counter32
_CipIcmpInAddrMaskReps_Object = MibTableColumn
cipIcmpInAddrMaskReps = _CipIcmpInAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 9),
    _CipIcmpInAddrMaskReps_Type()
)
cipIcmpInAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpInAddrMaskReps.setStatus("current")
_CipIcmpOutMsgs_Type = Counter32
_CipIcmpOutMsgs_Object = MibTableColumn
cipIcmpOutMsgs = _CipIcmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 10),
    _CipIcmpOutMsgs_Type()
)
cipIcmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpOutMsgs.setStatus("current")
_CipIcmpOutErrors_Type = Counter32
_CipIcmpOutErrors_Object = MibTableColumn
cipIcmpOutErrors = _CipIcmpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 11),
    _CipIcmpOutErrors_Type()
)
cipIcmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpOutErrors.setStatus("current")
_CipIcmpOutDestUnreachs_Type = Counter32
_CipIcmpOutDestUnreachs_Object = MibTableColumn
cipIcmpOutDestUnreachs = _CipIcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 12),
    _CipIcmpOutDestUnreachs_Type()
)
cipIcmpOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpOutDestUnreachs.setStatus("current")
_CipIcmpOutEchos_Type = Counter32
_CipIcmpOutEchos_Object = MibTableColumn
cipIcmpOutEchos = _CipIcmpOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 13),
    _CipIcmpOutEchos_Type()
)
cipIcmpOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpOutEchos.setStatus("current")
_CipIcmpOutEchoReps_Type = Counter32
_CipIcmpOutEchoReps_Object = MibTableColumn
cipIcmpOutEchoReps = _CipIcmpOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 14),
    _CipIcmpOutEchoReps_Type()
)
cipIcmpOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpOutEchoReps.setStatus("current")
_CipIcmpOutTimestamps_Type = Counter32
_CipIcmpOutTimestamps_Object = MibTableColumn
cipIcmpOutTimestamps = _CipIcmpOutTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 15),
    _CipIcmpOutTimestamps_Type()
)
cipIcmpOutTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpOutTimestamps.setStatus("current")
_CipIcmpOutTimestampReps_Type = Counter32
_CipIcmpOutTimestampReps_Object = MibTableColumn
cipIcmpOutTimestampReps = _CipIcmpOutTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 16),
    _CipIcmpOutTimestampReps_Type()
)
cipIcmpOutTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpOutTimestampReps.setStatus("current")
_CipIcmpOutAddrMasks_Type = Counter32
_CipIcmpOutAddrMasks_Object = MibTableColumn
cipIcmpOutAddrMasks = _CipIcmpOutAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 17),
    _CipIcmpOutAddrMasks_Type()
)
cipIcmpOutAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpOutAddrMasks.setStatus("current")
_CipIcmpOutAddrMaskReps_Type = Counter32
_CipIcmpOutAddrMaskReps_Object = MibTableColumn
cipIcmpOutAddrMaskReps = _CipIcmpOutAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 18),
    _CipIcmpOutAddrMaskReps_Type()
)
cipIcmpOutAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipIcmpOutAddrMaskReps.setStatus("current")
_CipUdpObjects_ObjectIdentity = ObjectIdentity
cipUdpObjects = _CipUdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4)
)
_CipUdpTable_Object = MibTable
cipUdpTable = _CipUdpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cipUdpTable.setStatus("current")
_CipUdpEntry_Object = MibTableRow
cipUdpEntry = _CipUdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 1, 1)
)
cipUdpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CIPTCPIP-MIB", "cipIpAddress"),
)
if mibBuilder.loadTexts:
    cipUdpEntry.setStatus("current")
_CipUdpInDatagrams_Type = Counter32
_CipUdpInDatagrams_Object = MibTableColumn
cipUdpInDatagrams = _CipUdpInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 1, 1, 1),
    _CipUdpInDatagrams_Type()
)
cipUdpInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUdpInDatagrams.setStatus("current")
_CipUdpNoPorts_Type = Counter32
_CipUdpNoPorts_Object = MibTableColumn
cipUdpNoPorts = _CipUdpNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 1, 1, 2),
    _CipUdpNoPorts_Type()
)
cipUdpNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUdpNoPorts.setStatus("current")
_CipUdpInErrors_Type = Counter32
_CipUdpInErrors_Object = MibTableColumn
cipUdpInErrors = _CipUdpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 1, 1, 3),
    _CipUdpInErrors_Type()
)
cipUdpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUdpInErrors.setStatus("current")
_CipUdpOutDatagrams_Type = Counter32
_CipUdpOutDatagrams_Object = MibTableColumn
cipUdpOutDatagrams = _CipUdpOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 1, 1, 4),
    _CipUdpOutDatagrams_Type()
)
cipUdpOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUdpOutDatagrams.setStatus("current")
_CipUdpListenersTable_Object = MibTable
cipUdpListenersTable = _CipUdpListenersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cipUdpListenersTable.setStatus("current")
_CipUdpListenersEntry_Object = MibTableRow
cipUdpListenersEntry = _CipUdpListenersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 2, 1)
)
cipUdpListenersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CIPTCPIP-MIB", "cipIpAddress"),
    (0, "CISCO-CIPTCPIP-MIB", "cipUdpLocalPort"),
)
if mibBuilder.loadTexts:
    cipUdpListenersEntry.setStatus("current")


class _CipUdpLocalPort_Type(Integer32):
    """Custom type cipUdpLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CipUdpLocalPort_Type.__name__ = "Integer32"
_CipUdpLocalPort_Object = MibTableColumn
cipUdpLocalPort = _CipUdpLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 2, 1, 1),
    _CipUdpLocalPort_Type()
)
cipUdpLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUdpLocalPort.setStatus("current")
_CiscoCipTcpIpMibConformance_ObjectIdentity = ObjectIdentity
ciscoCipTcpIpMibConformance = _CiscoCipTcpIpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 2)
)
_CiscoCipTcpIpMibCompliances_ObjectIdentity = ObjectIdentity
ciscoCipTcpIpMibCompliances = _CiscoCipTcpIpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 2, 1)
)
_CiscoCipTcpIpMibGroups_ObjectIdentity = ObjectIdentity
ciscoCipTcpIpMibGroups = _CiscoCipTcpIpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 2, 2)
)

# Managed Objects groups

ciscoCipTcpIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 2, 2, 1)
)
ciscoCipTcpIpGroup.setObjects(
      *(("CISCO-CIPTCPIP-MIB", "cipIpForwarding"),
        ("CISCO-CIPTCPIP-MIB", "cipIpDefaultTTL"),
        ("CISCO-CIPTCPIP-MIB", "cipIpInReceives"),
        ("CISCO-CIPTCPIP-MIB", "cipIpInHdrErrors"),
        ("CISCO-CIPTCPIP-MIB", "cipIpInAddrErrors"),
        ("CISCO-CIPTCPIP-MIB", "cipIpForwDatagrams"),
        ("CISCO-CIPTCPIP-MIB", "cipIpInUnknownProtos"),
        ("CISCO-CIPTCPIP-MIB", "cipIpInDiscards"),
        ("CISCO-CIPTCPIP-MIB", "cipIpInDelivers"),
        ("CISCO-CIPTCPIP-MIB", "cipIpOutRequests"),
        ("CISCO-CIPTCPIP-MIB", "cipIpOutDiscards"),
        ("CISCO-CIPTCPIP-MIB", "cipIpOutNoRoutes"),
        ("CISCO-CIPTCPIP-MIB", "cipIpReasmTimeout"),
        ("CISCO-CIPTCPIP-MIB", "cipIpReasmReqds"),
        ("CISCO-CIPTCPIP-MIB", "cipIpReasmOKs"),
        ("CISCO-CIPTCPIP-MIB", "cipIpReasmFails"),
        ("CISCO-CIPTCPIP-MIB", "cipIpFragOKs"),
        ("CISCO-CIPTCPIP-MIB", "cipIpFragFails"),
        ("CISCO-CIPTCPIP-MIB", "cipIpFragCreates"),
        ("CISCO-CIPTCPIP-MIB", "cipIpRoutingDiscards"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpRtoAlgorithm"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpRtoMin"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpRtoMax"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpMaxConn"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpActiveOpens"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpPassiveOpens"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpAttemptFails"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpEstabResets"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpCurrEstab"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpInSegs"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpOutSegs"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpRetransSegs"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpInErrs"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpOutRsts"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpConnState"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpConnInBytes"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpConnInHCBytes"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpConnOutBytes"),
        ("CISCO-CIPTCPIP-MIB", "cipTcpConnOutHCBytes"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpInMsgs"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpInErrors"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpInDestUnreachs"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpInTimeExcds"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpInParmProbs"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpInSrcQuenchs"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpInRedirects"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpInEchos"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpInAddrMaskReps"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpOutMsgs"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpOutErrors"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpOutDestUnreachs"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpOutEchos"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpOutEchoReps"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpOutTimestamps"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpOutTimestampReps"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpOutAddrMasks"),
        ("CISCO-CIPTCPIP-MIB", "cipIcmpOutAddrMaskReps"),
        ("CISCO-CIPTCPIP-MIB", "cipUdpInDatagrams"),
        ("CISCO-CIPTCPIP-MIB", "cipUdpNoPorts"),
        ("CISCO-CIPTCPIP-MIB", "cipUdpInErrors"),
        ("CISCO-CIPTCPIP-MIB", "cipUdpOutDatagrams"),
        ("CISCO-CIPTCPIP-MIB", "cipUdpLocalPort"))
)
if mibBuilder.loadTexts:
    ciscoCipTcpIpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCipTcpIpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 32, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCipTcpIpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CIPTCPIP-MIB",
    **{"ciscoCipTcpIpMIB": ciscoCipTcpIpMIB,
       "cipTcpIpObjects": cipTcpIpObjects,
       "cipIpObjects": cipIpObjects,
       "cipIpTable": cipIpTable,
       "cipIpEntry": cipIpEntry,
       "cipIpAddress": cipIpAddress,
       "cipIpForwarding": cipIpForwarding,
       "cipIpDefaultTTL": cipIpDefaultTTL,
       "cipIpInReceives": cipIpInReceives,
       "cipIpInHdrErrors": cipIpInHdrErrors,
       "cipIpInAddrErrors": cipIpInAddrErrors,
       "cipIpForwDatagrams": cipIpForwDatagrams,
       "cipIpInUnknownProtos": cipIpInUnknownProtos,
       "cipIpInDiscards": cipIpInDiscards,
       "cipIpInDelivers": cipIpInDelivers,
       "cipIpOutRequests": cipIpOutRequests,
       "cipIpOutDiscards": cipIpOutDiscards,
       "cipIpOutNoRoutes": cipIpOutNoRoutes,
       "cipIpReasmTimeout": cipIpReasmTimeout,
       "cipIpReasmReqds": cipIpReasmReqds,
       "cipIpReasmOKs": cipIpReasmOKs,
       "cipIpReasmFails": cipIpReasmFails,
       "cipIpFragOKs": cipIpFragOKs,
       "cipIpFragFails": cipIpFragFails,
       "cipIpFragCreates": cipIpFragCreates,
       "cipIpRoutingDiscards": cipIpRoutingDiscards,
       "cipTcpObjects": cipTcpObjects,
       "cipTcpStackTable": cipTcpStackTable,
       "cipTcpStackEntry": cipTcpStackEntry,
       "cipTcpRtoAlgorithm": cipTcpRtoAlgorithm,
       "cipTcpRtoMin": cipTcpRtoMin,
       "cipTcpRtoMax": cipTcpRtoMax,
       "cipTcpMaxConn": cipTcpMaxConn,
       "cipTcpActiveOpens": cipTcpActiveOpens,
       "cipTcpPassiveOpens": cipTcpPassiveOpens,
       "cipTcpAttemptFails": cipTcpAttemptFails,
       "cipTcpEstabResets": cipTcpEstabResets,
       "cipTcpCurrEstab": cipTcpCurrEstab,
       "cipTcpInSegs": cipTcpInSegs,
       "cipTcpOutSegs": cipTcpOutSegs,
       "cipTcpRetransSegs": cipTcpRetransSegs,
       "cipTcpInErrs": cipTcpInErrs,
       "cipTcpOutRsts": cipTcpOutRsts,
       "cipTcpConnTable": cipTcpConnTable,
       "cipTcpConnEntry": cipTcpConnEntry,
       "cipTcpConnLocalPort": cipTcpConnLocalPort,
       "cipTcpConnRemAddress": cipTcpConnRemAddress,
       "cipTcpConnRemPort": cipTcpConnRemPort,
       "cipTcpConnState": cipTcpConnState,
       "cipTcpConnInHCBytes": cipTcpConnInHCBytes,
       "cipTcpConnInBytes": cipTcpConnInBytes,
       "cipTcpConnOutHCBytes": cipTcpConnOutHCBytes,
       "cipTcpConnOutBytes": cipTcpConnOutBytes,
       "cipIcmpObjects": cipIcmpObjects,
       "cipIcmpTable": cipIcmpTable,
       "cipIcmpEntry": cipIcmpEntry,
       "cipIcmpInMsgs": cipIcmpInMsgs,
       "cipIcmpInErrors": cipIcmpInErrors,
       "cipIcmpInDestUnreachs": cipIcmpInDestUnreachs,
       "cipIcmpInTimeExcds": cipIcmpInTimeExcds,
       "cipIcmpInParmProbs": cipIcmpInParmProbs,
       "cipIcmpInSrcQuenchs": cipIcmpInSrcQuenchs,
       "cipIcmpInRedirects": cipIcmpInRedirects,
       "cipIcmpInEchos": cipIcmpInEchos,
       "cipIcmpInAddrMaskReps": cipIcmpInAddrMaskReps,
       "cipIcmpOutMsgs": cipIcmpOutMsgs,
       "cipIcmpOutErrors": cipIcmpOutErrors,
       "cipIcmpOutDestUnreachs": cipIcmpOutDestUnreachs,
       "cipIcmpOutEchos": cipIcmpOutEchos,
       "cipIcmpOutEchoReps": cipIcmpOutEchoReps,
       "cipIcmpOutTimestamps": cipIcmpOutTimestamps,
       "cipIcmpOutTimestampReps": cipIcmpOutTimestampReps,
       "cipIcmpOutAddrMasks": cipIcmpOutAddrMasks,
       "cipIcmpOutAddrMaskReps": cipIcmpOutAddrMaskReps,
       "cipUdpObjects": cipUdpObjects,
       "cipUdpTable": cipUdpTable,
       "cipUdpEntry": cipUdpEntry,
       "cipUdpInDatagrams": cipUdpInDatagrams,
       "cipUdpNoPorts": cipUdpNoPorts,
       "cipUdpInErrors": cipUdpInErrors,
       "cipUdpOutDatagrams": cipUdpOutDatagrams,
       "cipUdpListenersTable": cipUdpListenersTable,
       "cipUdpListenersEntry": cipUdpListenersEntry,
       "cipUdpLocalPort": cipUdpLocalPort,
       "ciscoCipTcpIpMibConformance": ciscoCipTcpIpMibConformance,
       "ciscoCipTcpIpMibCompliances": ciscoCipTcpIpMibCompliances,
       "ciscoCipTcpIpMibCompliance": ciscoCipTcpIpMibCompliance,
       "ciscoCipTcpIpMibGroups": ciscoCipTcpIpMibGroups,
       "ciscoCipTcpIpGroup": ciscoCipTcpIpGroup}
)
