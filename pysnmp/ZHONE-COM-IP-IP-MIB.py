# SNMP MIB module (ZHONE-COM-IP-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-IP-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:16 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(rdEntry,) = mibBuilder.importSymbols(
    "ZHONE-COM-IP-RD-MIB",
    "rdEntry")

(zhoneIp,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp",
    "zhoneModules")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

comIpIp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 54)
)
comIpIp.setRevisions(
        ("2000-11-02 17:30",
         "2000-09-11 16:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4)
)
if mibBuilder.loadTexts:
    ip.setStatus("current")
_ZhoneIpTable_Object = MibTable
zhoneIpTable = _ZhoneIpTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    zhoneIpTable.setStatus("current")
_ZhoneIpEntry_Object = MibTableRow
zhoneIpEntry = _ZhoneIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    zhoneIpEntry.setStatus("current")


class _ZhIpForwarding_Type(Integer32):
    """Custom type zhIpForwarding based on Integer32"""
    defaultValue = 1

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


_ZhIpForwarding_Type.__name__ = "Integer32"
_ZhIpForwarding_Object = MibTableColumn
zhIpForwarding = _ZhIpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 1),
    _ZhIpForwarding_Type()
)
zhIpForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhIpForwarding.setStatus("current")


class _ZhIpDefaultTTL_Type(Integer32):
    """Custom type zhIpDefaultTTL based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZhIpDefaultTTL_Type.__name__ = "Integer32"
_ZhIpDefaultTTL_Object = MibTableColumn
zhIpDefaultTTL = _ZhIpDefaultTTL_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 2),
    _ZhIpDefaultTTL_Type()
)
zhIpDefaultTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhIpDefaultTTL.setStatus("current")
_ZhIpInReceives_Type = Counter32
_ZhIpInReceives_Object = MibTableColumn
zhIpInReceives = _ZhIpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 3),
    _ZhIpInReceives_Type()
)
zhIpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpInReceives.setStatus("current")
_ZhIpInHdrErrors_Type = Counter32
_ZhIpInHdrErrors_Object = MibTableColumn
zhIpInHdrErrors = _ZhIpInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 4),
    _ZhIpInHdrErrors_Type()
)
zhIpInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpInHdrErrors.setStatus("current")
_ZhIpInAddrErrors_Type = Counter32
_ZhIpInAddrErrors_Object = MibTableColumn
zhIpInAddrErrors = _ZhIpInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 5),
    _ZhIpInAddrErrors_Type()
)
zhIpInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpInAddrErrors.setStatus("current")
_ZhIpForwDatagrams_Type = Counter32
_ZhIpForwDatagrams_Object = MibTableColumn
zhIpForwDatagrams = _ZhIpForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 6),
    _ZhIpForwDatagrams_Type()
)
zhIpForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpForwDatagrams.setStatus("current")
_ZhIpInUnknownProtos_Type = Counter32
_ZhIpInUnknownProtos_Object = MibTableColumn
zhIpInUnknownProtos = _ZhIpInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 7),
    _ZhIpInUnknownProtos_Type()
)
zhIpInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpInUnknownProtos.setStatus("current")
_ZhIpInDiscards_Type = Counter32
_ZhIpInDiscards_Object = MibTableColumn
zhIpInDiscards = _ZhIpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 8),
    _ZhIpInDiscards_Type()
)
zhIpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpInDiscards.setStatus("current")
_ZhIpInDelivers_Type = Counter32
_ZhIpInDelivers_Object = MibTableColumn
zhIpInDelivers = _ZhIpInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 9),
    _ZhIpInDelivers_Type()
)
zhIpInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpInDelivers.setStatus("current")
_ZhIpOutRequests_Type = Counter32
_ZhIpOutRequests_Object = MibTableColumn
zhIpOutRequests = _ZhIpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 10),
    _ZhIpOutRequests_Type()
)
zhIpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpOutRequests.setStatus("current")
_ZhIpOutDiscards_Type = Counter32
_ZhIpOutDiscards_Object = MibTableColumn
zhIpOutDiscards = _ZhIpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 11),
    _ZhIpOutDiscards_Type()
)
zhIpOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpOutDiscards.setStatus("current")
_ZhIpOutNoRoutes_Type = Counter32
_ZhIpOutNoRoutes_Object = MibTableColumn
zhIpOutNoRoutes = _ZhIpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 12),
    _ZhIpOutNoRoutes_Type()
)
zhIpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpOutNoRoutes.setStatus("current")
_ZhIpReasmTimeout_Type = Unsigned32
_ZhIpReasmTimeout_Object = MibTableColumn
zhIpReasmTimeout = _ZhIpReasmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 13),
    _ZhIpReasmTimeout_Type()
)
zhIpReasmTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpReasmTimeout.setStatus("current")
if mibBuilder.loadTexts:
    zhIpReasmTimeout.setUnits("seconds")
_ZhIpReasmReqds_Type = Counter32
_ZhIpReasmReqds_Object = MibTableColumn
zhIpReasmReqds = _ZhIpReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 14),
    _ZhIpReasmReqds_Type()
)
zhIpReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpReasmReqds.setStatus("current")
_ZhIpReasmOKs_Type = Counter32
_ZhIpReasmOKs_Object = MibTableColumn
zhIpReasmOKs = _ZhIpReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 15),
    _ZhIpReasmOKs_Type()
)
zhIpReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpReasmOKs.setStatus("current")
_ZhIpReasmFails_Type = Counter32
_ZhIpReasmFails_Object = MibTableColumn
zhIpReasmFails = _ZhIpReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 16),
    _ZhIpReasmFails_Type()
)
zhIpReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpReasmFails.setStatus("current")
_ZhIpFragOKs_Type = Counter32
_ZhIpFragOKs_Object = MibTableColumn
zhIpFragOKs = _ZhIpFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 17),
    _ZhIpFragOKs_Type()
)
zhIpFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpFragOKs.setStatus("current")
_ZhIpFragFails_Type = Counter32
_ZhIpFragFails_Object = MibTableColumn
zhIpFragFails = _ZhIpFragFails_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 18),
    _ZhIpFragFails_Type()
)
zhIpFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpFragFails.setStatus("current")
_ZhIpFragCreates_Type = Counter32
_ZhIpFragCreates_Object = MibTableColumn
zhIpFragCreates = _ZhIpFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 19),
    _ZhIpFragCreates_Type()
)
zhIpFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpFragCreates.setStatus("current")
_ZhIpRoutingDiscards_Type = Counter32
_ZhIpRoutingDiscards_Object = MibTableColumn
zhIpRoutingDiscards = _ZhIpRoutingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 2, 1, 20),
    _ZhIpRoutingDiscards_Type()
)
zhIpRoutingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpRoutingDiscards.setStatus("current")
_ZhoneIpNetToMediaTable_Object = MibTable
zhoneIpNetToMediaTable = _ZhoneIpNetToMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 4)
)
if mibBuilder.loadTexts:
    zhoneIpNetToMediaTable.setStatus("current")
_ZhoneIpNetToMediaEntry_Object = MibTableRow
zhoneIpNetToMediaEntry = _ZhoneIpNetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 4, 1)
)
zhoneIpNetToMediaEntry.setIndexNames(
    (0, "ZHONE-COM-IP-IP-MIB", "zhIpNetToMediaIfIndex"),
    (0, "ZHONE-COM-IP-IP-MIB", "zhIpNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    zhoneIpNetToMediaEntry.setStatus("current")
_ZhIpNetToMediaIfIndex_Type = InterfaceIndex
_ZhIpNetToMediaIfIndex_Object = MibTableColumn
zhIpNetToMediaIfIndex = _ZhIpNetToMediaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 4, 1, 1),
    _ZhIpNetToMediaIfIndex_Type()
)
zhIpNetToMediaIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhIpNetToMediaIfIndex.setStatus("current")
_ZhIpNetToMediaNetAddress_Type = IpAddress
_ZhIpNetToMediaNetAddress_Object = MibTableColumn
zhIpNetToMediaNetAddress = _ZhIpNetToMediaNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 4, 1, 2),
    _ZhIpNetToMediaNetAddress_Type()
)
zhIpNetToMediaNetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhIpNetToMediaNetAddress.setStatus("current")
_ZhIpNetToMediaPhysAddress_Type = PhysAddress
_ZhIpNetToMediaPhysAddress_Object = MibTableColumn
zhIpNetToMediaPhysAddress = _ZhIpNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 4, 1, 3),
    _ZhIpNetToMediaPhysAddress_Type()
)
zhIpNetToMediaPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhIpNetToMediaPhysAddress.setStatus("current")


class _ZhIpNetToMediaType_Type(Integer32):
    """Custom type zhIpNetToMediaType based on Integer32"""
    defaultValue = 4

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
        *(("dynamic", 3),
          ("invalid", 2),
          ("other", 1),
          ("static", 4))
    )


_ZhIpNetToMediaType_Type.__name__ = "Integer32"
_ZhIpNetToMediaType_Object = MibTableColumn
zhIpNetToMediaType = _ZhIpNetToMediaType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 4, 1, 4),
    _ZhIpNetToMediaType_Type()
)
zhIpNetToMediaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhIpNetToMediaType.setStatus("current")
_ZhIpNetToMediaRowStatus_Type = ZhoneRowStatus
_ZhIpNetToMediaRowStatus_Object = MibTableColumn
zhIpNetToMediaRowStatus = _ZhIpNetToMediaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 4, 4, 1, 5),
    _ZhIpNetToMediaRowStatus_Type()
)
zhIpNetToMediaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhIpNetToMediaRowStatus.setStatus("current")
rdEntry.registerAugmentions(
    ("ZHONE-COM-IP-IP-MIB",
     "zhoneIpEntry")
)
zhoneIpEntry.setIndexNames(*rdEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-IP-IP-MIB",
    **{"ip": ip,
       "zhoneIpTable": zhoneIpTable,
       "zhoneIpEntry": zhoneIpEntry,
       "zhIpForwarding": zhIpForwarding,
       "zhIpDefaultTTL": zhIpDefaultTTL,
       "zhIpInReceives": zhIpInReceives,
       "zhIpInHdrErrors": zhIpInHdrErrors,
       "zhIpInAddrErrors": zhIpInAddrErrors,
       "zhIpForwDatagrams": zhIpForwDatagrams,
       "zhIpInUnknownProtos": zhIpInUnknownProtos,
       "zhIpInDiscards": zhIpInDiscards,
       "zhIpInDelivers": zhIpInDelivers,
       "zhIpOutRequests": zhIpOutRequests,
       "zhIpOutDiscards": zhIpOutDiscards,
       "zhIpOutNoRoutes": zhIpOutNoRoutes,
       "zhIpReasmTimeout": zhIpReasmTimeout,
       "zhIpReasmReqds": zhIpReasmReqds,
       "zhIpReasmOKs": zhIpReasmOKs,
       "zhIpReasmFails": zhIpReasmFails,
       "zhIpFragOKs": zhIpFragOKs,
       "zhIpFragFails": zhIpFragFails,
       "zhIpFragCreates": zhIpFragCreates,
       "zhIpRoutingDiscards": zhIpRoutingDiscards,
       "zhoneIpNetToMediaTable": zhoneIpNetToMediaTable,
       "zhoneIpNetToMediaEntry": zhoneIpNetToMediaEntry,
       "zhIpNetToMediaIfIndex": zhIpNetToMediaIfIndex,
       "zhIpNetToMediaNetAddress": zhIpNetToMediaNetAddress,
       "zhIpNetToMediaPhysAddress": zhIpNetToMediaPhysAddress,
       "zhIpNetToMediaType": zhIpNetToMediaType,
       "zhIpNetToMediaRowStatus": zhIpNetToMediaRowStatus,
       "comIpIp": comIpIp}
)
