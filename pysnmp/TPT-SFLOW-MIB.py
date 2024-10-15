# SNMP MIB module (TPT-SFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-SFLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:09 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tpt_tpa_objs,) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-objs")


# MODULE-IDENTITY

tpt_sflow_objs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18)
)
tpt_sflow_objs.setRevisions(
        ("2016-05-25 18:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SflowStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("disable", 0),
          ("enable", 1),
          ("error", 2),
          ("not-applicable", 3))
    )



# MIB Managed Objects in the order of their OIDs

_SFlowCollectorTable_Object = MibTable
sFlowCollectorTable = _SFlowCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1)
)
if mibBuilder.loadTexts:
    sFlowCollectorTable.setStatus("current")
_SFlowCollectorEntry_Object = MibTableRow
sFlowCollectorEntry = _SFlowCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1)
)
sFlowCollectorEntry.setIndexNames(
    (0, "TPT-SFLOW-MIB", "collectorIndex"),
)
if mibBuilder.loadTexts:
    sFlowCollectorEntry.setStatus("current")
_CollectorIndex_Type = Unsigned32
_CollectorIndex_Object = MibTableColumn
collectorIndex = _CollectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1, 1),
    _CollectorIndex_Type()
)
collectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    collectorIndex.setStatus("current")


class _CollectorAddr_Type(OctetString):
    """Custom type collectorAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CollectorAddr_Type.__name__ = "OctetString"
_CollectorAddr_Object = MibTableColumn
collectorAddr = _CollectorAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1, 2),
    _CollectorAddr_Type()
)
collectorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    collectorAddr.setStatus("current")
_UdpPort_Type = Unsigned32
_UdpPort_Object = MibTableColumn
udpPort = _UdpPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1, 3),
    _UdpPort_Type()
)
udpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpPort.setStatus("current")


class _CollectorAddrV6_Type(OctetString):
    """Custom type collectorAddrV6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_CollectorAddrV6_Type.__name__ = "OctetString"
_CollectorAddrV6_Object = MibTableColumn
collectorAddrV6 = _CollectorAddrV6_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1, 4),
    _CollectorAddrV6_Type()
)
collectorAddrV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    collectorAddrV6.setStatus("current")
_SFlowStatus_Type = SflowStatus
_SFlowStatus_Object = MibScalar
sFlowStatus = _SFlowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 2),
    _SFlowStatus_Type()
)
sFlowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFlowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-SFLOW-MIB",
    **{"SflowStatus": SflowStatus,
       "tpt-sflow-objs": tpt_sflow_objs,
       "sFlowCollectorTable": sFlowCollectorTable,
       "sFlowCollectorEntry": sFlowCollectorEntry,
       "collectorIndex": collectorIndex,
       "collectorAddr": collectorAddr,
       "udpPort": udpPort,
       "collectorAddrV6": collectorAddrV6,
       "sFlowStatus": sFlowStatus}
)
