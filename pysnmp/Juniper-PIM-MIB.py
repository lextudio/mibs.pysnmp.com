# SNMP MIB module (Juniper-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-PIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:55 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(pimInterfaceIfIndex,
 pimRPSetAddress,
 pimRPSetComponent,
 pimRPSetGroupAddress,
 pimRPSetGroupMask) = mibBuilder.importSymbols(
    "PIM-MIB",
    "pimInterfaceIfIndex",
    "pimRPSetAddress",
    "pimRPSetComponent",
    "pimRPSetGroupAddress",
    "pimRPSetGroupMask")

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

juniPimMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43)
)
juniPimMIB.setRevisions(
        ("2002-09-16 21:44",
         "2001-03-19 15:37")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniPimType(Integer32, TextualConvention):
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
        *(("dense", 1),
          ("invalid", 0),
          ("sparse", 2),
          ("sparseAndDense", 3))
    )



# MIB Managed Objects in the order of their OIDs

_JuniPimMIBObjects_ObjectIdentity = ObjectIdentity
juniPimMIBObjects = _JuniPimMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1)
)
_JuniPimTraps_ObjectIdentity = ObjectIdentity
juniPimTraps = _JuniPimTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 0)
)
_JuniPimGlobal_ObjectIdentity = ObjectIdentity
juniPimGlobal = _JuniPimGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1)
)
_JuniPimNumHelloRcvd_Type = Integer32
_JuniPimNumHelloRcvd_Object = MibScalar
juniPimNumHelloRcvd = _JuniPimNumHelloRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 1),
    _JuniPimNumHelloRcvd_Type()
)
juniPimNumHelloRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimNumHelloRcvd.setStatus("current")
_JuniPimNumJoinPruneRcvd_Type = Integer32
_JuniPimNumJoinPruneRcvd_Object = MibScalar
juniPimNumJoinPruneRcvd = _JuniPimNumJoinPruneRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 2),
    _JuniPimNumJoinPruneRcvd_Type()
)
juniPimNumJoinPruneRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimNumJoinPruneRcvd.setStatus("current")
_JuniPimNumAssertRcvd_Type = Integer32
_JuniPimNumAssertRcvd_Object = MibScalar
juniPimNumAssertRcvd = _JuniPimNumAssertRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 3),
    _JuniPimNumAssertRcvd_Type()
)
juniPimNumAssertRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimNumAssertRcvd.setStatus("current")
_JuniPimNumGraftRcvd_Type = Integer32
_JuniPimNumGraftRcvd_Object = MibScalar
juniPimNumGraftRcvd = _JuniPimNumGraftRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 4),
    _JuniPimNumGraftRcvd_Type()
)
juniPimNumGraftRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimNumGraftRcvd.setStatus("current")
_JuniPimNumGraftAckRcvd_Type = Integer32
_JuniPimNumGraftAckRcvd_Object = MibScalar
juniPimNumGraftAckRcvd = _JuniPimNumGraftAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 5),
    _JuniPimNumGraftAckRcvd_Type()
)
juniPimNumGraftAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimNumGraftAckRcvd.setStatus("current")
_JuniPimNumHelloSent_Type = Integer32
_JuniPimNumHelloSent_Object = MibScalar
juniPimNumHelloSent = _JuniPimNumHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 6),
    _JuniPimNumHelloSent_Type()
)
juniPimNumHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimNumHelloSent.setStatus("current")
_JuniPimNumJoinPruneSent_Type = Integer32
_JuniPimNumJoinPruneSent_Object = MibScalar
juniPimNumJoinPruneSent = _JuniPimNumJoinPruneSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 7),
    _JuniPimNumJoinPruneSent_Type()
)
juniPimNumJoinPruneSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimNumJoinPruneSent.setStatus("current")
_JuniPimNumAssertSent_Type = Integer32
_JuniPimNumAssertSent_Object = MibScalar
juniPimNumAssertSent = _JuniPimNumAssertSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 8),
    _JuniPimNumAssertSent_Type()
)
juniPimNumAssertSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimNumAssertSent.setStatus("current")
_JuniPimNumGraftSent_Type = Integer32
_JuniPimNumGraftSent_Object = MibScalar
juniPimNumGraftSent = _JuniPimNumGraftSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 9),
    _JuniPimNumGraftSent_Type()
)
juniPimNumGraftSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimNumGraftSent.setStatus("current")
_JuniPimNumGraftAckSent_Type = Integer32
_JuniPimNumGraftAckSent_Object = MibScalar
juniPimNumGraftAckSent = _JuniPimNumGraftAckSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 10),
    _JuniPimNumGraftAckSent_Type()
)
juniPimNumGraftAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimNumGraftAckSent.setStatus("current")
_JuniPimInterfaceTable_Object = MibTable
juniPimInterfaceTable = _JuniPimInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11)
)
if mibBuilder.loadTexts:
    juniPimInterfaceTable.setStatus("current")
_JuniPimInterfaceEntry_Object = MibTableRow
juniPimInterfaceEntry = _JuniPimInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1)
)
juniPimInterfaceEntry.setIndexNames(
    (0, "PIM-MIB", "pimInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    juniPimInterfaceEntry.setStatus("current")
_JuniPimIntfNumHelloRcvd_Type = Integer32
_JuniPimIntfNumHelloRcvd_Object = MibTableColumn
juniPimIntfNumHelloRcvd = _JuniPimIntfNumHelloRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 1),
    _JuniPimIntfNumHelloRcvd_Type()
)
juniPimIntfNumHelloRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPimIntfNumHelloRcvd.setStatus("current")
_JuniPimIntfNumJoinPruneRcvd_Type = Integer32
_JuniPimIntfNumJoinPruneRcvd_Object = MibTableColumn
juniPimIntfNumJoinPruneRcvd = _JuniPimIntfNumJoinPruneRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 2),
    _JuniPimIntfNumJoinPruneRcvd_Type()
)
juniPimIntfNumJoinPruneRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPimIntfNumJoinPruneRcvd.setStatus("current")
_JuniPimIntfNumAssertRcvd_Type = Integer32
_JuniPimIntfNumAssertRcvd_Object = MibTableColumn
juniPimIntfNumAssertRcvd = _JuniPimIntfNumAssertRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 3),
    _JuniPimIntfNumAssertRcvd_Type()
)
juniPimIntfNumAssertRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPimIntfNumAssertRcvd.setStatus("current")
_JuniPimIntfNumGraftRcvd_Type = Integer32
_JuniPimIntfNumGraftRcvd_Object = MibTableColumn
juniPimIntfNumGraftRcvd = _JuniPimIntfNumGraftRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 4),
    _JuniPimIntfNumGraftRcvd_Type()
)
juniPimIntfNumGraftRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPimIntfNumGraftRcvd.setStatus("current")
_JuniPimIntfNumGraftAckRcvd_Type = Integer32
_JuniPimIntfNumGraftAckRcvd_Object = MibTableColumn
juniPimIntfNumGraftAckRcvd = _JuniPimIntfNumGraftAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 5),
    _JuniPimIntfNumGraftAckRcvd_Type()
)
juniPimIntfNumGraftAckRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPimIntfNumGraftAckRcvd.setStatus("current")
_JuniPimIntfNumHelloSent_Type = Integer32
_JuniPimIntfNumHelloSent_Object = MibTableColumn
juniPimIntfNumHelloSent = _JuniPimIntfNumHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 6),
    _JuniPimIntfNumHelloSent_Type()
)
juniPimIntfNumHelloSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPimIntfNumHelloSent.setStatus("current")
_JuniPimIntfNumJoinPruneSent_Type = Integer32
_JuniPimIntfNumJoinPruneSent_Object = MibTableColumn
juniPimIntfNumJoinPruneSent = _JuniPimIntfNumJoinPruneSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 7),
    _JuniPimIntfNumJoinPruneSent_Type()
)
juniPimIntfNumJoinPruneSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPimIntfNumJoinPruneSent.setStatus("current")
_JuniPimIntfNumAssertSent_Type = Integer32
_JuniPimIntfNumAssertSent_Object = MibTableColumn
juniPimIntfNumAssertSent = _JuniPimIntfNumAssertSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 8),
    _JuniPimIntfNumAssertSent_Type()
)
juniPimIntfNumAssertSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPimIntfNumAssertSent.setStatus("current")
_JuniPimIntfNumGraftSent_Type = Integer32
_JuniPimIntfNumGraftSent_Object = MibTableColumn
juniPimIntfNumGraftSent = _JuniPimIntfNumGraftSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 9),
    _JuniPimIntfNumGraftSent_Type()
)
juniPimIntfNumGraftSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPimIntfNumGraftSent.setStatus("current")
_JuniPimIntfNumGraftAckSent_Type = Integer32
_JuniPimIntfNumGraftAckSent_Object = MibTableColumn
juniPimIntfNumGraftAckSent = _JuniPimIntfNumGraftAckSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 10),
    _JuniPimIntfNumGraftAckSent_Type()
)
juniPimIntfNumGraftAckSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPimIntfNumGraftAckSent.setStatus("current")


class _JuniPimIntfVersion_Type(Integer32):
    """Custom type juniPimIntfVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JuniPimIntfVersion_Type.__name__ = "Integer32"
_JuniPimIntfVersion_Object = MibTableColumn
juniPimIntfVersion = _JuniPimIntfVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 11),
    _JuniPimIntfVersion_Type()
)
juniPimIntfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimIntfVersion.setStatus("current")
_JuniPimIntfNumNbrs_Type = Integer32
_JuniPimIntfNumNbrs_Object = MibTableColumn
juniPimIntfNumNbrs = _JuniPimIntfNumNbrs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 12),
    _JuniPimIntfNumNbrs_Type()
)
juniPimIntfNumNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimIntfNumNbrs.setStatus("current")
_JuniPimMRouteTable_Object = MibTable
juniPimMRouteTable = _JuniPimMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12)
)
if mibBuilder.loadTexts:
    juniPimMRouteTable.setStatus("current")
_JuniPimMRouteEntry_Object = MibTableRow
juniPimMRouteEntry = _JuniPimMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1)
)
juniPimMRouteEntry.setIndexNames(
    (0, "Juniper-PIM-MIB", "juniPimMRouteGroup"),
    (0, "Juniper-PIM-MIB", "juniPimMRouteSource"),
    (0, "Juniper-PIM-MIB", "juniPimMRouteSourceMask"),
    (0, "Juniper-PIM-MIB", "juniPimMRouteRPAddress"),
)
if mibBuilder.loadTexts:
    juniPimMRouteEntry.setStatus("current")
_JuniPimMRouteGroup_Type = IpAddress
_JuniPimMRouteGroup_Object = MibTableColumn
juniPimMRouteGroup = _JuniPimMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 1),
    _JuniPimMRouteGroup_Type()
)
juniPimMRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimMRouteGroup.setStatus("current")
_JuniPimMRouteSource_Type = IpAddress
_JuniPimMRouteSource_Object = MibTableColumn
juniPimMRouteSource = _JuniPimMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 2),
    _JuniPimMRouteSource_Type()
)
juniPimMRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimMRouteSource.setStatus("current")
_JuniPimMRouteSourceMask_Type = IpAddress
_JuniPimMRouteSourceMask_Object = MibTableColumn
juniPimMRouteSourceMask = _JuniPimMRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 3),
    _JuniPimMRouteSourceMask_Type()
)
juniPimMRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimMRouteSourceMask.setStatus("current")
_JuniPimMRouteRPAddress_Type = IpAddress
_JuniPimMRouteRPAddress_Object = MibTableColumn
juniPimMRouteRPAddress = _JuniPimMRouteRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 4),
    _JuniPimMRouteRPAddress_Type()
)
juniPimMRouteRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimMRouteRPAddress.setStatus("current")
_JuniPimMRouteUpstreamAssertTimer_Type = TimeTicks
_JuniPimMRouteUpstreamAssertTimer_Object = MibTableColumn
juniPimMRouteUpstreamAssertTimer = _JuniPimMRouteUpstreamAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 5),
    _JuniPimMRouteUpstreamAssertTimer_Type()
)
juniPimMRouteUpstreamAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteUpstreamAssertTimer.setStatus("current")
_JuniPimMRouteAssertMetric_Type = Integer32
_JuniPimMRouteAssertMetric_Object = MibTableColumn
juniPimMRouteAssertMetric = _JuniPimMRouteAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 6),
    _JuniPimMRouteAssertMetric_Type()
)
juniPimMRouteAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteAssertMetric.setStatus("current")
_JuniPimMRouteAssertPref_Type = Integer32
_JuniPimMRouteAssertPref_Object = MibTableColumn
juniPimMRouteAssertPref = _JuniPimMRouteAssertPref_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 7),
    _JuniPimMRouteAssertPref_Type()
)
juniPimMRouteAssertPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteAssertPref.setStatus("current")
_JuniPimMRouteAssertRPTBit_Type = TruthValue
_JuniPimMRouteAssertRPTBit_Object = MibTableColumn
juniPimMRouteAssertRPTBit = _JuniPimMRouteAssertRPTBit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 8),
    _JuniPimMRouteAssertRPTBit_Type()
)
juniPimMRouteAssertRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteAssertRPTBit.setStatus("current")


class _JuniPimMRouteBits_Type(Bits):
    """Custom type juniPimMRouteBits based on Bits"""
    namedValues = NamedValues(
        *(("rpt", 0),
          ("spt", 1))
    )

_JuniPimMRouteBits_Type.__name__ = "Bits"
_JuniPimMRouteBits_Object = MibTableColumn
juniPimMRouteBits = _JuniPimMRouteBits_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 9),
    _JuniPimMRouteBits_Type()
)
juniPimMRouteBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteBits.setStatus("current")
_JuniPimMRouteRPAddrInUse_Type = IpAddress
_JuniPimMRouteRPAddrInUse_Object = MibTableColumn
juniPimMRouteRPAddrInUse = _JuniPimMRouteRPAddrInUse_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 10),
    _JuniPimMRouteRPAddrInUse_Type()
)
juniPimMRouteRPAddrInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteRPAddrInUse.setStatus("current")
_JuniPimMRouteUpstreamNbr_Type = IpAddress
_JuniPimMRouteUpstreamNbr_Object = MibTableColumn
juniPimMRouteUpstreamNbr = _JuniPimMRouteUpstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 11),
    _JuniPimMRouteUpstreamNbr_Type()
)
juniPimMRouteUpstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteUpstreamNbr.setStatus("current")
_JuniPimMRouteIifAddr_Type = IpAddress
_JuniPimMRouteIifAddr_Object = MibTableColumn
juniPimMRouteIifAddr = _JuniPimMRouteIifAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 12),
    _JuniPimMRouteIifAddr_Type()
)
juniPimMRouteIifAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteIifAddr.setStatus("current")
_JuniPimMRouteIsWaitingToSwitchToSPT_Type = TruthValue
_JuniPimMRouteIsWaitingToSwitchToSPT_Object = MibTableColumn
juniPimMRouteIsWaitingToSwitchToSPT = _JuniPimMRouteIsWaitingToSwitchToSPT_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 13),
    _JuniPimMRouteIsWaitingToSwitchToSPT_Type()
)
juniPimMRouteIsWaitingToSwitchToSPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteIsWaitingToSwitchToSPT.setStatus("current")
_JuniPimMRouteEntryExpiryTimer_Type = TimeTicks
_JuniPimMRouteEntryExpiryTimer_Object = MibTableColumn
juniPimMRouteEntryExpiryTimer = _JuniPimMRouteEntryExpiryTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 14),
    _JuniPimMRouteEntryExpiryTimer_Type()
)
juniPimMRouteEntryExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteEntryExpiryTimer.setStatus("current")
_JuniPimMRouteSenderDRAddr_Type = IpAddress
_JuniPimMRouteSenderDRAddr_Object = MibTableColumn
juniPimMRouteSenderDRAddr = _JuniPimMRouteSenderDRAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 15),
    _JuniPimMRouteSenderDRAddr_Type()
)
juniPimMRouteSenderDRAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteSenderDRAddr.setStatus("current")
_JuniPimMRouteRouteAddr_Type = IpAddress
_JuniPimMRouteRouteAddr_Object = MibTableColumn
juniPimMRouteRouteAddr = _JuniPimMRouteRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 16),
    _JuniPimMRouteRouteAddr_Type()
)
juniPimMRouteRouteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteRouteAddr.setStatus("current")
_JuniPimMRouteRouteMask_Type = IpAddress
_JuniPimMRouteRouteMask_Object = MibTableColumn
juniPimMRouteRouteMask = _JuniPimMRouteRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 17),
    _JuniPimMRouteRouteMask_Type()
)
juniPimMRouteRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteRouteMask.setStatus("current")
_JuniPimMRouteGRPAddr_Type = IpAddress
_JuniPimMRouteGRPAddr_Object = MibTableColumn
juniPimMRouteGRPAddr = _JuniPimMRouteGRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 18),
    _JuniPimMRouteGRPAddr_Type()
)
juniPimMRouteGRPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteGRPAddr.setStatus("current")
_JuniPimMRouteGRPMask_Type = IpAddress
_JuniPimMRouteGRPMask_Object = MibTableColumn
juniPimMRouteGRPMask = _JuniPimMRouteGRPMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 19),
    _JuniPimMRouteGRPMask_Type()
)
juniPimMRouteGRPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteGRPMask.setStatus("current")
_JuniPimMRouteOtherProtoOifJoinTypeAll_Type = TruthValue
_JuniPimMRouteOtherProtoOifJoinTypeAll_Object = MibTableColumn
juniPimMRouteOtherProtoOifJoinTypeAll = _JuniPimMRouteOtherProtoOifJoinTypeAll_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 20),
    _JuniPimMRouteOtherProtoOifJoinTypeAll_Type()
)
juniPimMRouteOtherProtoOifJoinTypeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteOtherProtoOifJoinTypeAll.setStatus("current")
_JuniPimMRouteOtherProtoOifJoinTypeG_Type = TruthValue
_JuniPimMRouteOtherProtoOifJoinTypeG_Object = MibTableColumn
juniPimMRouteOtherProtoOifJoinTypeG = _JuniPimMRouteOtherProtoOifJoinTypeG_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 21),
    _JuniPimMRouteOtherProtoOifJoinTypeG_Type()
)
juniPimMRouteOtherProtoOifJoinTypeG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteOtherProtoOifJoinTypeG.setStatus("current")
_JuniPimMRouteOtherProtoOifJoinTypeSG_Type = TruthValue
_JuniPimMRouteOtherProtoOifJoinTypeSG_Object = MibTableColumn
juniPimMRouteOtherProtoOifJoinTypeSG = _JuniPimMRouteOtherProtoOifJoinTypeSG_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 22),
    _JuniPimMRouteOtherProtoOifJoinTypeSG_Type()
)
juniPimMRouteOtherProtoOifJoinTypeSG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteOtherProtoOifJoinTypeSG.setStatus("current")
_JuniPimMRoutePimType_Type = JuniPimType
_JuniPimMRoutePimType_Object = MibTableColumn
juniPimMRoutePimType = _JuniPimMRoutePimType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 23),
    _JuniPimMRoutePimType_Type()
)
juniPimMRoutePimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRoutePimType.setStatus("current")
_JuniPimMRouteNextHopTable_Object = MibTable
juniPimMRouteNextHopTable = _JuniPimMRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13)
)
if mibBuilder.loadTexts:
    juniPimMRouteNextHopTable.setStatus("current")
_JuniPimMRouteNextHopEntry_Object = MibTableRow
juniPimMRouteNextHopEntry = _JuniPimMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1)
)
juniPimMRouteNextHopEntry.setIndexNames(
    (0, "Juniper-PIM-MIB", "juniPimMRouteNextHopGroupAddr"),
    (0, "Juniper-PIM-MIB", "juniPimMRouteNextHopSrcAddr"),
    (0, "Juniper-PIM-MIB", "juniPimMRouteNextHopSrcMask"),
    (0, "Juniper-PIM-MIB", "juniPimMRouteNextHopRPAddr"),
    (0, "Juniper-PIM-MIB", "juniPimMRouteNextHopIfId"),
    (0, "Juniper-PIM-MIB", "juniPimMRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    juniPimMRouteNextHopEntry.setStatus("current")
_JuniPimMRouteNextHopGroupAddr_Type = IpAddress
_JuniPimMRouteNextHopGroupAddr_Object = MibTableColumn
juniPimMRouteNextHopGroupAddr = _JuniPimMRouteNextHopGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 2),
    _JuniPimMRouteNextHopGroupAddr_Type()
)
juniPimMRouteNextHopGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopGroupAddr.setStatus("current")
_JuniPimMRouteNextHopSrcAddr_Type = IpAddress
_JuniPimMRouteNextHopSrcAddr_Object = MibTableColumn
juniPimMRouteNextHopSrcAddr = _JuniPimMRouteNextHopSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 3),
    _JuniPimMRouteNextHopSrcAddr_Type()
)
juniPimMRouteNextHopSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopSrcAddr.setStatus("current")
_JuniPimMRouteNextHopSrcMask_Type = IpAddress
_JuniPimMRouteNextHopSrcMask_Object = MibTableColumn
juniPimMRouteNextHopSrcMask = _JuniPimMRouteNextHopSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 4),
    _JuniPimMRouteNextHopSrcMask_Type()
)
juniPimMRouteNextHopSrcMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopSrcMask.setStatus("current")
_JuniPimMRouteNextHopRPAddr_Type = IpAddress
_JuniPimMRouteNextHopRPAddr_Object = MibTableColumn
juniPimMRouteNextHopRPAddr = _JuniPimMRouteNextHopRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 5),
    _JuniPimMRouteNextHopRPAddr_Type()
)
juniPimMRouteNextHopRPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopRPAddr.setStatus("current")
_JuniPimMRouteNextHopIfId_Type = InterfaceIndex
_JuniPimMRouteNextHopIfId_Object = MibTableColumn
juniPimMRouteNextHopIfId = _JuniPimMRouteNextHopIfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 6),
    _JuniPimMRouteNextHopIfId_Type()
)
juniPimMRouteNextHopIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopIfId.setStatus("current")
_JuniPimMRouteNextHopAddress_Type = IpAddress
_JuniPimMRouteNextHopAddress_Object = MibTableColumn
juniPimMRouteNextHopAddress = _JuniPimMRouteNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 7),
    _JuniPimMRouteNextHopAddress_Type()
)
juniPimMRouteNextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopAddress.setStatus("current")


class _JuniPimMRouteNextHopPruneReason_Type(Integer32):
    """Custom type juniPimMRouteNextHopPruneReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assert", 3),
          ("other", 1),
          ("prune", 2))
    )


_JuniPimMRouteNextHopPruneReason_Type.__name__ = "Integer32"
_JuniPimMRouteNextHopPruneReason_Object = MibTableColumn
juniPimMRouteNextHopPruneReason = _JuniPimMRouteNextHopPruneReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 8),
    _JuniPimMRouteNextHopPruneReason_Type()
)
juniPimMRouteNextHopPruneReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopPruneReason.setStatus("current")
_JuniPimMRouteNextHopJoinTypeSSRP_Type = TruthValue
_JuniPimMRouteNextHopJoinTypeSSRP_Object = MibTableColumn
juniPimMRouteNextHopJoinTypeSSRP = _JuniPimMRouteNextHopJoinTypeSSRP_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 9),
    _JuniPimMRouteNextHopJoinTypeSSRP_Type()
)
juniPimMRouteNextHopJoinTypeSSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopJoinTypeSSRP.setStatus("current")
_JuniPimMRouteNextHopJoinTypeG_Type = TruthValue
_JuniPimMRouteNextHopJoinTypeG_Object = MibTableColumn
juniPimMRouteNextHopJoinTypeG = _JuniPimMRouteNextHopJoinTypeG_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 10),
    _JuniPimMRouteNextHopJoinTypeG_Type()
)
juniPimMRouteNextHopJoinTypeG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopJoinTypeG.setStatus("current")
_JuniPimMRouteNextHopJoinTypeSG_Type = TruthValue
_JuniPimMRouteNextHopJoinTypeSG_Object = MibTableColumn
juniPimMRouteNextHopJoinTypeSG = _JuniPimMRouteNextHopJoinTypeSG_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 11),
    _JuniPimMRouteNextHopJoinTypeSG_Type()
)
juniPimMRouteNextHopJoinTypeSG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopJoinTypeSG.setStatus("current")
_JuniPimMRouteNextHopHasLGM_Type = TruthValue
_JuniPimMRouteNextHopHasLGM_Object = MibTableColumn
juniPimMRouteNextHopHasLGM = _JuniPimMRouteNextHopHasLGM_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 12),
    _JuniPimMRouteNextHopHasLGM_Type()
)
juniPimMRouteNextHopHasLGM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopHasLGM.setStatus("current")
_JuniPimMRouteNextHopHasOifAW_Type = TruthValue
_JuniPimMRouteNextHopHasOifAW_Object = MibTableColumn
juniPimMRouteNextHopHasOifAW = _JuniPimMRouteNextHopHasOifAW_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 13),
    _JuniPimMRouteNextHopHasOifAW_Type()
)
juniPimMRouteNextHopHasOifAW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopHasOifAW.setStatus("current")
_JuniPimMRouteNextHopHasOifSendAssert_Type = TruthValue
_JuniPimMRouteNextHopHasOifSendAssert_Object = MibTableColumn
juniPimMRouteNextHopHasOifSendAssert = _JuniPimMRouteNextHopHasOifSendAssert_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 14),
    _JuniPimMRouteNextHopHasOifSendAssert_Type()
)
juniPimMRouteNextHopHasOifSendAssert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopHasOifSendAssert.setStatus("current")
_JuniPimMRouteNextHopHasOifRegister_Type = TruthValue
_JuniPimMRouteNextHopHasOifRegister_Object = MibTableColumn
juniPimMRouteNextHopHasOifRegister = _JuniPimMRouteNextHopHasOifRegister_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 15),
    _JuniPimMRouteNextHopHasOifRegister_Type()
)
juniPimMRouteNextHopHasOifRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopHasOifRegister.setStatus("current")
_JuniPimMRouteNextHopHasOifBorderBit_Type = TruthValue
_JuniPimMRouteNextHopHasOifBorderBit_Object = MibTableColumn
juniPimMRouteNextHopHasOifBorderBit = _JuniPimMRouteNextHopHasOifBorderBit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 16),
    _JuniPimMRouteNextHopHasOifBorderBit_Type()
)
juniPimMRouteNextHopHasOifBorderBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopHasOifBorderBit.setStatus("current")
_JuniPimMRouteNextHopHasOifNullEncapsBit_Type = TruthValue
_JuniPimMRouteNextHopHasOifNullEncapsBit_Object = MibTableColumn
juniPimMRouteNextHopHasOifNullEncapsBit = _JuniPimMRouteNextHopHasOifNullEncapsBit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 17),
    _JuniPimMRouteNextHopHasOifNullEncapsBit_Type()
)
juniPimMRouteNextHopHasOifNullEncapsBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopHasOifNullEncapsBit.setStatus("current")
_JuniPimMRouteNextHopJoinEndTimer_Type = TimeTicks
_JuniPimMRouteNextHopJoinEndTimer_Object = MibTableColumn
juniPimMRouteNextHopJoinEndTimer = _JuniPimMRouteNextHopJoinEndTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 18),
    _JuniPimMRouteNextHopJoinEndTimer_Type()
)
juniPimMRouteNextHopJoinEndTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopJoinEndTimer.setStatus("current")
_JuniPimMRouteNextHopAssertEndTimer_Type = TimeTicks
_JuniPimMRouteNextHopAssertEndTimer_Object = MibTableColumn
juniPimMRouteNextHopAssertEndTimer = _JuniPimMRouteNextHopAssertEndTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 19),
    _JuniPimMRouteNextHopAssertEndTimer_Type()
)
juniPimMRouteNextHopAssertEndTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopAssertEndTimer.setStatus("current")
_JuniPimMRouteNextHopNextAssertTimer_Type = TimeTicks
_JuniPimMRouteNextHopNextAssertTimer_Object = MibTableColumn
juniPimMRouteNextHopNextAssertTimer = _JuniPimMRouteNextHopNextAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 20),
    _JuniPimMRouteNextHopNextAssertTimer_Type()
)
juniPimMRouteNextHopNextAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopNextAssertTimer.setStatus("current")
_JuniPimMRouteNextHopAssertSrcAddress_Type = IpAddress
_JuniPimMRouteNextHopAssertSrcAddress_Object = MibTableColumn
juniPimMRouteNextHopAssertSrcAddress = _JuniPimMRouteNextHopAssertSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 21),
    _JuniPimMRouteNextHopAssertSrcAddress_Type()
)
juniPimMRouteNextHopAssertSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopAssertSrcAddress.setStatus("current")
_JuniPimMRouteNextHopRegisterSuppressionTimer_Type = TimeTicks
_JuniPimMRouteNextHopRegisterSuppressionTimer_Object = MibTableColumn
juniPimMRouteNextHopRegisterSuppressionTimer = _JuniPimMRouteNextHopRegisterSuppressionTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 22),
    _JuniPimMRouteNextHopRegisterSuppressionTimer_Type()
)
juniPimMRouteNextHopRegisterSuppressionTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopRegisterSuppressionTimer.setStatus("current")
_JuniPimMRouteNextHopPimType_Type = JuniPimType
_JuniPimMRouteNextHopPimType_Object = MibTableColumn
juniPimMRouteNextHopPimType = _JuniPimMRouteNextHopPimType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 23),
    _JuniPimMRouteNextHopPimType_Type()
)
juniPimMRouteNextHopPimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopPimType.setStatus("current")
_JuniPimMRouteNextHopPruneTimeLeft_Type = TimeTicks
_JuniPimMRouteNextHopPruneTimeLeft_Object = MibTableColumn
juniPimMRouteNextHopPruneTimeLeft = _JuniPimMRouteNextHopPruneTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 24),
    _JuniPimMRouteNextHopPruneTimeLeft_Type()
)
juniPimMRouteNextHopPruneTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopPruneTimeLeft.setStatus("current")
_JuniPimMRouteNextHopsendingIpAddress_Type = IpAddress
_JuniPimMRouteNextHopsendingIpAddress_Object = MibTableColumn
juniPimMRouteNextHopsendingIpAddress = _JuniPimMRouteNextHopsendingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 25),
    _JuniPimMRouteNextHopsendingIpAddress_Type()
)
juniPimMRouteNextHopsendingIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimMRouteNextHopsendingIpAddress.setStatus("current")
_JuniPimRPSetTable_Object = MibTable
juniPimRPSetTable = _JuniPimRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 14)
)
if mibBuilder.loadTexts:
    juniPimRPSetTable.setStatus("current")
_JuniPimRPSetEntry_Object = MibTableRow
juniPimRPSetEntry = _JuniPimRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 14, 1)
)
juniPimRPSetEntry.setIndexNames(
    (0, "PIM-MIB", "pimRPSetComponent"),
    (0, "PIM-MIB", "pimRPSetGroupAddress"),
    (0, "PIM-MIB", "pimRPSetGroupMask"),
    (0, "PIM-MIB", "pimRPSetAddress"),
)
if mibBuilder.loadTexts:
    juniPimRPSetEntry.setStatus("current")


class _JuniPimRPSetPriority_Type(Integer32):
    """Custom type juniPimRPSetPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniPimRPSetPriority_Type.__name__ = "Integer32"
_JuniPimRPSetPriority_Object = MibTableColumn
juniPimRPSetPriority = _JuniPimRPSetPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 14, 1, 1),
    _JuniPimRPSetPriority_Type()
)
juniPimRPSetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimRPSetPriority.setStatus("current")


class _JuniPimRPSetTypeInfo_Type(Integer32):
    """Custom type juniPimRPSetTypeInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("pimRPTypeAutoRP", 3),
          ("pimRPTypeAutoRPNegative", 7),
          ("pimRPTypeBSR", 4),
          ("pimRPTypeBSRNegative", 8),
          ("pimRPTypeInvalid", 0),
          ("pimRPTypeStatic", 1),
          ("pimRPTypeStaticNegative", 5),
          ("pimRPTypeStaticOverride", 2),
          ("pimRPTypeStaticOverrideNegative", 6))
    )


_JuniPimRPSetTypeInfo_Type.__name__ = "Integer32"
_JuniPimRPSetTypeInfo_Object = MibTableColumn
juniPimRPSetTypeInfo = _JuniPimRPSetTypeInfo_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 14, 1, 2),
    _JuniPimRPSetTypeInfo_Type()
)
juniPimRPSetTypeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimRPSetTypeInfo.setStatus("current")


class _JuniPimRPSetAccessListName_Type(OctetString):
    """Custom type juniPimRPSetAccessListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniPimRPSetAccessListName_Type.__name__ = "OctetString"
_JuniPimRPSetAccessListName_Object = MibTableColumn
juniPimRPSetAccessListName = _JuniPimRPSetAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 14, 1, 3),
    _JuniPimRPSetAccessListName_Type()
)
juniPimRPSetAccessListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimRPSetAccessListName.setStatus("current")
_JuniPimStaticRPConfTable_Object = MibTable
juniPimStaticRPConfTable = _JuniPimStaticRPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 15)
)
if mibBuilder.loadTexts:
    juniPimStaticRPConfTable.setStatus("current")
_JuniPimStaticRPConfEntry_Object = MibTableRow
juniPimStaticRPConfEntry = _JuniPimStaticRPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 15, 1)
)
juniPimStaticRPConfEntry.setIndexNames(
    (0, "Juniper-PIM-MIB", "juniPimStaticRPConfComponentIndex"),
    (0, "Juniper-PIM-MIB", "juniPimStaticRPConfRPAddr"),
    (0, "Juniper-PIM-MIB", "juniPimStaticRPConfAccessListName"),
)
if mibBuilder.loadTexts:
    juniPimStaticRPConfEntry.setStatus("current")


class _JuniPimStaticRPConfComponentIndex_Type(Integer32):
    """Custom type juniPimStaticRPConfComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPimStaticRPConfComponentIndex_Type.__name__ = "Integer32"
_JuniPimStaticRPConfComponentIndex_Object = MibTableColumn
juniPimStaticRPConfComponentIndex = _JuniPimStaticRPConfComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 15, 1, 1),
    _JuniPimStaticRPConfComponentIndex_Type()
)
juniPimStaticRPConfComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimStaticRPConfComponentIndex.setStatus("current")
_JuniPimStaticRPConfRPAddr_Type = IpAddress
_JuniPimStaticRPConfRPAddr_Object = MibTableColumn
juniPimStaticRPConfRPAddr = _JuniPimStaticRPConfRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 15, 1, 2),
    _JuniPimStaticRPConfRPAddr_Type()
)
juniPimStaticRPConfRPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimStaticRPConfRPAddr.setStatus("current")


class _JuniPimStaticRPConfAccessListName_Type(OctetString):
    """Custom type juniPimStaticRPConfAccessListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniPimStaticRPConfAccessListName_Type.__name__ = "OctetString"
_JuniPimStaticRPConfAccessListName_Object = MibTableColumn
juniPimStaticRPConfAccessListName = _JuniPimStaticRPConfAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 15, 1, 3),
    _JuniPimStaticRPConfAccessListName_Type()
)
juniPimStaticRPConfAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimStaticRPConfAccessListName.setStatus("current")
_JuniPimStaticRPConfRowStatus_Type = RowStatus
_JuniPimStaticRPConfRowStatus_Object = MibTableColumn
juniPimStaticRPConfRowStatus = _JuniPimStaticRPConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 15, 1, 4),
    _JuniPimStaticRPConfRowStatus_Type()
)
juniPimStaticRPConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPimStaticRPConfRowStatus.setStatus("current")


class _JuniPimStaticRPConfOverride_Type(TruthValue):
    """Custom type juniPimStaticRPConfOverride based on TruthValue"""


_JuniPimStaticRPConfOverride_Object = MibTableColumn
juniPimStaticRPConfOverride = _JuniPimStaticRPConfOverride_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 15, 1, 5),
    _JuniPimStaticRPConfOverride_Type()
)
juniPimStaticRPConfOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPimStaticRPConfOverride.setStatus("current")
_JuniPimAutoRPConfTable_Object = MibTable
juniPimAutoRPConfTable = _JuniPimAutoRPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16)
)
if mibBuilder.loadTexts:
    juniPimAutoRPConfTable.setStatus("current")
_JuniPimAutoRPConfEntry_Object = MibTableRow
juniPimAutoRPConfEntry = _JuniPimAutoRPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16, 1)
)
juniPimAutoRPConfEntry.setIndexNames(
    (0, "Juniper-PIM-MIB", "juniPimAutoRPConfComponentIndex"),
    (0, "Juniper-PIM-MIB", "juniPimAutoRPConfCandRPAddr"),
    (0, "Juniper-PIM-MIB", "juniPimAutoRPConfGroupAccessListName"),
)
if mibBuilder.loadTexts:
    juniPimAutoRPConfEntry.setStatus("current")


class _JuniPimAutoRPConfComponentIndex_Type(Integer32):
    """Custom type juniPimAutoRPConfComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPimAutoRPConfComponentIndex_Type.__name__ = "Integer32"
_JuniPimAutoRPConfComponentIndex_Object = MibTableColumn
juniPimAutoRPConfComponentIndex = _JuniPimAutoRPConfComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16, 1, 1),
    _JuniPimAutoRPConfComponentIndex_Type()
)
juniPimAutoRPConfComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimAutoRPConfComponentIndex.setStatus("current")
_JuniPimAutoRPConfCandRPAddr_Type = IpAddress
_JuniPimAutoRPConfCandRPAddr_Object = MibTableColumn
juniPimAutoRPConfCandRPAddr = _JuniPimAutoRPConfCandRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16, 1, 2),
    _JuniPimAutoRPConfCandRPAddr_Type()
)
juniPimAutoRPConfCandRPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimAutoRPConfCandRPAddr.setStatus("current")


class _JuniPimAutoRPConfGroupAccessListName_Type(OctetString):
    """Custom type juniPimAutoRPConfGroupAccessListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniPimAutoRPConfGroupAccessListName_Type.__name__ = "OctetString"
_JuniPimAutoRPConfGroupAccessListName_Object = MibTableColumn
juniPimAutoRPConfGroupAccessListName = _JuniPimAutoRPConfGroupAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16, 1, 3),
    _JuniPimAutoRPConfGroupAccessListName_Type()
)
juniPimAutoRPConfGroupAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimAutoRPConfGroupAccessListName.setStatus("current")
_JuniPimAutoRPConfRowStatus_Type = RowStatus
_JuniPimAutoRPConfRowStatus_Object = MibTableColumn
juniPimAutoRPConfRowStatus = _JuniPimAutoRPConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16, 1, 4),
    _JuniPimAutoRPConfRowStatus_Type()
)
juniPimAutoRPConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPimAutoRPConfRowStatus.setStatus("current")


class _JuniPimAutoRPConfTTL_Type(Integer32):
    """Custom type juniPimAutoRPConfTTL based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniPimAutoRPConfTTL_Type.__name__ = "Integer32"
_JuniPimAutoRPConfTTL_Object = MibTableColumn
juniPimAutoRPConfTTL = _JuniPimAutoRPConfTTL_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16, 1, 5),
    _JuniPimAutoRPConfTTL_Type()
)
juniPimAutoRPConfTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPimAutoRPConfTTL.setStatus("current")


class _JuniPimAutoRPConfAncmntIntvl_Type(TimeTicks):
    """Custom type juniPimAutoRPConfAncmntIntvl based on TimeTicks"""
    defaultValue = 60


_JuniPimAutoRPConfAncmntIntvl_Object = MibTableColumn
juniPimAutoRPConfAncmntIntvl = _JuniPimAutoRPConfAncmntIntvl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16, 1, 6),
    _JuniPimAutoRPConfAncmntIntvl_Type()
)
juniPimAutoRPConfAncmntIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPimAutoRPConfAncmntIntvl.setStatus("current")
_JuniPimAutoRPConfifId_Type = InterfaceIndex
_JuniPimAutoRPConfifId_Object = MibTableColumn
juniPimAutoRPConfifId = _JuniPimAutoRPConfifId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16, 1, 7),
    _JuniPimAutoRPConfifId_Type()
)
juniPimAutoRPConfifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimAutoRPConfifId.setStatus("current")
_JuniPimAutoRPCandTable_Object = MibTable
juniPimAutoRPCandTable = _JuniPimAutoRPCandTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17)
)
if mibBuilder.loadTexts:
    juniPimAutoRPCandTable.setStatus("current")
_JuniPimAutoRPCandEntry_Object = MibTableRow
juniPimAutoRPCandEntry = _JuniPimAutoRPCandEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1)
)
juniPimAutoRPCandEntry.setIndexNames(
    (0, "Juniper-PIM-MIB", "juniPimAutoRPCandComponentIndex"),
    (0, "Juniper-PIM-MIB", "juniPimAutoRPCandRPAddr"),
    (0, "Juniper-PIM-MIB", "juniPimAutoRPCandGroupAddr"),
    (0, "Juniper-PIM-MIB", "juniPimAutoRPCandGroupMask"),
)
if mibBuilder.loadTexts:
    juniPimAutoRPCandEntry.setStatus("current")


class _JuniPimAutoRPCandComponentIndex_Type(Integer32):
    """Custom type juniPimAutoRPCandComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPimAutoRPCandComponentIndex_Type.__name__ = "Integer32"
_JuniPimAutoRPCandComponentIndex_Object = MibTableColumn
juniPimAutoRPCandComponentIndex = _JuniPimAutoRPCandComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 1),
    _JuniPimAutoRPCandComponentIndex_Type()
)
juniPimAutoRPCandComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimAutoRPCandComponentIndex.setStatus("current")
_JuniPimAutoRPCandRPAddr_Type = IpAddress
_JuniPimAutoRPCandRPAddr_Object = MibTableColumn
juniPimAutoRPCandRPAddr = _JuniPimAutoRPCandRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 2),
    _JuniPimAutoRPCandRPAddr_Type()
)
juniPimAutoRPCandRPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimAutoRPCandRPAddr.setStatus("current")
_JuniPimAutoRPCandGroupAddr_Type = IpAddress
_JuniPimAutoRPCandGroupAddr_Object = MibTableColumn
juniPimAutoRPCandGroupAddr = _JuniPimAutoRPCandGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 3),
    _JuniPimAutoRPCandGroupAddr_Type()
)
juniPimAutoRPCandGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimAutoRPCandGroupAddr.setStatus("current")
_JuniPimAutoRPCandGroupMask_Type = IpAddress
_JuniPimAutoRPCandGroupMask_Object = MibTableColumn
juniPimAutoRPCandGroupMask = _JuniPimAutoRPCandGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 4),
    _JuniPimAutoRPCandGroupMask_Type()
)
juniPimAutoRPCandGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimAutoRPCandGroupMask.setStatus("current")
_JuniPimAutoRPCandRowStatus_Type = RowStatus
_JuniPimAutoRPCandRowStatus_Object = MibTableColumn
juniPimAutoRPCandRowStatus = _JuniPimAutoRPCandRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 5),
    _JuniPimAutoRPCandRowStatus_Type()
)
juniPimAutoRPCandRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimAutoRPCandRowStatus.setStatus("current")


class _JuniPimAutoRPCandAccessListName_Type(OctetString):
    """Custom type juniPimAutoRPCandAccessListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniPimAutoRPCandAccessListName_Type.__name__ = "OctetString"
_JuniPimAutoRPCandAccessListName_Object = MibTableColumn
juniPimAutoRPCandAccessListName = _JuniPimAutoRPCandAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 6),
    _JuniPimAutoRPCandAccessListName_Type()
)
juniPimAutoRPCandAccessListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimAutoRPCandAccessListName.setStatus("current")


class _JuniPimAutoRPCandAutoRPTTL_Type(Integer32):
    """Custom type juniPimAutoRPCandAutoRPTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniPimAutoRPCandAutoRPTTL_Type.__name__ = "Integer32"
_JuniPimAutoRPCandAutoRPTTL_Object = MibTableColumn
juniPimAutoRPCandAutoRPTTL = _JuniPimAutoRPCandAutoRPTTL_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 7),
    _JuniPimAutoRPCandAutoRPTTL_Type()
)
juniPimAutoRPCandAutoRPTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimAutoRPCandAutoRPTTL.setStatus("current")
_JuniPimAutoRPCandAutoRPAncmntIntvl_Type = TimeTicks
_JuniPimAutoRPCandAutoRPAncmntIntvl_Object = MibTableColumn
juniPimAutoRPCandAutoRPAncmntIntvl = _JuniPimAutoRPCandAutoRPAncmntIntvl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 8),
    _JuniPimAutoRPCandAutoRPAncmntIntvl_Type()
)
juniPimAutoRPCandAutoRPAncmntIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimAutoRPCandAutoRPAncmntIntvl.setStatus("current")
_JuniPimAutoRPCandIfId_Type = InterfaceIndex
_JuniPimAutoRPCandIfId_Object = MibTableColumn
juniPimAutoRPCandIfId = _JuniPimAutoRPCandIfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 9),
    _JuniPimAutoRPCandIfId_Type()
)
juniPimAutoRPCandIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimAutoRPCandIfId.setStatus("current")
_JuniPimComponentTable_Object = MibTable
juniPimComponentTable = _JuniPimComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18)
)
if mibBuilder.loadTexts:
    juniPimComponentTable.setStatus("current")
_JuniPimComponentEntry_Object = MibTableRow
juniPimComponentEntry = _JuniPimComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1)
)
juniPimComponentEntry.setIndexNames(
    (0, "Juniper-PIM-MIB", "juniPimComponentIndex"),
)
if mibBuilder.loadTexts:
    juniPimComponentEntry.setStatus("current")


class _JuniPimComponentIndex_Type(Integer32):
    """Custom type juniPimComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPimComponentIndex_Type.__name__ = "Integer32"
_JuniPimComponentIndex_Object = MibTableColumn
juniPimComponentIndex = _JuniPimComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1, 1),
    _JuniPimComponentIndex_Type()
)
juniPimComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimComponentIndex.setStatus("current")
_JuniPimComponentAutoRPMappingAgentRowStatus_Type = RowStatus
_JuniPimComponentAutoRPMappingAgentRowStatus_Object = MibTableColumn
juniPimComponentAutoRPMappingAgentRowStatus = _JuniPimComponentAutoRPMappingAgentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1, 2),
    _JuniPimComponentAutoRPMappingAgentRowStatus_Type()
)
juniPimComponentAutoRPMappingAgentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPimComponentAutoRPMappingAgentRowStatus.setStatus("current")
_JuniPimComponentConfiguredAutoRPMappingAgentIfId_Type = InterfaceIndex
_JuniPimComponentConfiguredAutoRPMappingAgentIfId_Object = MibTableColumn
juniPimComponentConfiguredAutoRPMappingAgentIfId = _JuniPimComponentConfiguredAutoRPMappingAgentIfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1, 3),
    _JuniPimComponentConfiguredAutoRPMappingAgentIfId_Type()
)
juniPimComponentConfiguredAutoRPMappingAgentIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPimComponentConfiguredAutoRPMappingAgentIfId.setStatus("current")


class _JuniPimComponentAutoRPMappingAgentInterval_Type(TimeTicks):
    """Custom type juniPimComponentAutoRPMappingAgentInterval based on TimeTicks"""
    defaultValue = 60


_JuniPimComponentAutoRPMappingAgentInterval_Object = MibTableColumn
juniPimComponentAutoRPMappingAgentInterval = _JuniPimComponentAutoRPMappingAgentInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1, 4),
    _JuniPimComponentAutoRPMappingAgentInterval_Type()
)
juniPimComponentAutoRPMappingAgentInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPimComponentAutoRPMappingAgentInterval.setStatus("current")


class _JuniPimComponentAutoRPMappingTTL_Type(Integer32):
    """Custom type juniPimComponentAutoRPMappingTTL based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniPimComponentAutoRPMappingTTL_Type.__name__ = "Integer32"
_JuniPimComponentAutoRPMappingTTL_Object = MibTableColumn
juniPimComponentAutoRPMappingTTL = _JuniPimComponentAutoRPMappingTTL_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1, 5),
    _JuniPimComponentAutoRPMappingTTL_Type()
)
juniPimComponentAutoRPMappingTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPimComponentAutoRPMappingTTL.setStatus("current")
_JuniPimComponentAutoRPMappingAgentIntfAddr_Type = IpAddress
_JuniPimComponentAutoRPMappingAgentIntfAddr_Object = MibTableColumn
juniPimComponentAutoRPMappingAgentIntfAddr = _JuniPimComponentAutoRPMappingAgentIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1, 6),
    _JuniPimComponentAutoRPMappingAgentIntfAddr_Type()
)
juniPimComponentAutoRPMappingAgentIntfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimComponentAutoRPMappingAgentIntfAddr.setStatus("current")
_JuniPimComponentAutoRPMappingAgentWinnerAddr_Type = IpAddress
_JuniPimComponentAutoRPMappingAgentWinnerAddr_Object = MibTableColumn
juniPimComponentAutoRPMappingAgentWinnerAddr = _JuniPimComponentAutoRPMappingAgentWinnerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1, 7),
    _JuniPimComponentAutoRPMappingAgentWinnerAddr_Type()
)
juniPimComponentAutoRPMappingAgentWinnerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimComponentAutoRPMappingAgentWinnerAddr.setStatus("current")
_JuniPimComponentAutoRPMappingAgentWinnerLastHeard_Type = TimeTicks
_JuniPimComponentAutoRPMappingAgentWinnerLastHeard_Object = MibTableColumn
juniPimComponentAutoRPMappingAgentWinnerLastHeard = _JuniPimComponentAutoRPMappingAgentWinnerLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1, 8),
    _JuniPimComponentAutoRPMappingAgentWinnerLastHeard_Type()
)
juniPimComponentAutoRPMappingAgentWinnerLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimComponentAutoRPMappingAgentWinnerLastHeard.setStatus("current")
_JuniPimUnicastRouteTable_Object = MibTable
juniPimUnicastRouteTable = _JuniPimUnicastRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19)
)
if mibBuilder.loadTexts:
    juniPimUnicastRouteTable.setStatus("current")
_JuniPimUnicastRouteEntry_Object = MibTableRow
juniPimUnicastRouteEntry = _JuniPimUnicastRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1)
)
juniPimUnicastRouteEntry.setIndexNames(
    (0, "Juniper-PIM-MIB", "juniPimUnicastRouteEntryAddr"),
    (0, "Juniper-PIM-MIB", "juniPimUnicastRouteEntryMask"),
)
if mibBuilder.loadTexts:
    juniPimUnicastRouteEntry.setStatus("current")
_JuniPimUnicastRouteEntryAddr_Type = IpAddress
_JuniPimUnicastRouteEntryAddr_Object = MibTableColumn
juniPimUnicastRouteEntryAddr = _JuniPimUnicastRouteEntryAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1, 1),
    _JuniPimUnicastRouteEntryAddr_Type()
)
juniPimUnicastRouteEntryAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimUnicastRouteEntryAddr.setStatus("current")
_JuniPimUnicastRouteEntryMask_Type = IpAddress
_JuniPimUnicastRouteEntryMask_Object = MibTableColumn
juniPimUnicastRouteEntryMask = _JuniPimUnicastRouteEntryMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1, 2),
    _JuniPimUnicastRouteEntryMask_Type()
)
juniPimUnicastRouteEntryMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimUnicastRouteEntryMask.setStatus("current")
_JuniPimUnicastRouteEntryRpfNbr_Type = IpAddress
_JuniPimUnicastRouteEntryRpfNbr_Object = MibTableColumn
juniPimUnicastRouteEntryRpfNbr = _JuniPimUnicastRouteEntryRpfNbr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1, 3),
    _JuniPimUnicastRouteEntryRpfNbr_Type()
)
juniPimUnicastRouteEntryRpfNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimUnicastRouteEntryRpfNbr.setStatus("current")
_JuniPimUnicastRouteEntryIifId_Type = InterfaceIndex
_JuniPimUnicastRouteEntryIifId_Object = MibTableColumn
juniPimUnicastRouteEntryIifId = _JuniPimUnicastRouteEntryIifId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1, 4),
    _JuniPimUnicastRouteEntryIifId_Type()
)
juniPimUnicastRouteEntryIifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimUnicastRouteEntryIifId.setStatus("current")
_JuniPimUnicastRouteEntryIifAddr_Type = IpAddress
_JuniPimUnicastRouteEntryIifAddr_Object = MibTableColumn
juniPimUnicastRouteEntryIifAddr = _JuniPimUnicastRouteEntryIifAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1, 5),
    _JuniPimUnicastRouteEntryIifAddr_Type()
)
juniPimUnicastRouteEntryIifAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimUnicastRouteEntryIifAddr.setStatus("current")
_JuniPimUnicastRouteEntryPref_Type = Integer32
_JuniPimUnicastRouteEntryPref_Object = MibTableColumn
juniPimUnicastRouteEntryPref = _JuniPimUnicastRouteEntryPref_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1, 6),
    _JuniPimUnicastRouteEntryPref_Type()
)
juniPimUnicastRouteEntryPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimUnicastRouteEntryPref.setStatus("current")
_JuniPimUnicastRouteEntryMetric_Type = Integer32
_JuniPimUnicastRouteEntryMetric_Object = MibTableColumn
juniPimUnicastRouteEntryMetric = _JuniPimUnicastRouteEntryMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1, 7),
    _JuniPimUnicastRouteEntryMetric_Type()
)
juniPimUnicastRouteEntryMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimUnicastRouteEntryMetric.setStatus("current")
_JuniPimUnicastRouteEntryPimType_Type = JuniPimType
_JuniPimUnicastRouteEntryPimType_Object = MibTableColumn
juniPimUnicastRouteEntryPimType = _JuniPimUnicastRouteEntryPimType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1, 8),
    _JuniPimUnicastRouteEntryPimType_Type()
)
juniPimUnicastRouteEntryPimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPimUnicastRouteEntryPimType.setStatus("current")
_JuniPimSPTThresholdTable_Object = MibTable
juniPimSPTThresholdTable = _JuniPimSPTThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 20)
)
if mibBuilder.loadTexts:
    juniPimSPTThresholdTable.setStatus("current")
_JuniPimSPTThresholdEntry_Object = MibTableRow
juniPimSPTThresholdEntry = _JuniPimSPTThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 20, 1)
)
juniPimSPTThresholdEntry.setIndexNames(
    (0, "Juniper-PIM-MIB", "juniPimSPTThresholdAccessListName"),
)
if mibBuilder.loadTexts:
    juniPimSPTThresholdEntry.setStatus("current")


class _JuniPimSPTThresholdAccessListName_Type(OctetString):
    """Custom type juniPimSPTThresholdAccessListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniPimSPTThresholdAccessListName_Type.__name__ = "OctetString"
_JuniPimSPTThresholdAccessListName_Object = MibTableColumn
juniPimSPTThresholdAccessListName = _JuniPimSPTThresholdAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 20, 1, 1),
    _JuniPimSPTThresholdAccessListName_Type()
)
juniPimSPTThresholdAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPimSPTThresholdAccessListName.setStatus("current")
_JuniPimSPTThresholdRowStatus_Type = RowStatus
_JuniPimSPTThresholdRowStatus_Object = MibTableColumn
juniPimSPTThresholdRowStatus = _JuniPimSPTThresholdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 20, 1, 2),
    _JuniPimSPTThresholdRowStatus_Type()
)
juniPimSPTThresholdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPimSPTThresholdRowStatus.setStatus("current")


class _JuniPimSPTThresholdKbps_Type(Integer32):
    """Custom type juniPimSPTThresholdKbps based on Integer32"""
    defaultValue = 0


_JuniPimSPTThresholdKbps_Object = MibTableColumn
juniPimSPTThresholdKbps = _JuniPimSPTThresholdKbps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 20, 1, 3),
    _JuniPimSPTThresholdKbps_Type()
)
juniPimSPTThresholdKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPimSPTThresholdKbps.setStatus("current")
_JuniPimConformance_ObjectIdentity = ObjectIdentity
juniPimConformance = _JuniPimConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2)
)
_JuniPimCompliances_ObjectIdentity = ObjectIdentity
juniPimCompliances = _JuniPimCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 1)
)
_JuniPimGroups_ObjectIdentity = ObjectIdentity
juniPimGroups = _JuniPimGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2)
)

# Managed Objects groups

juniPimGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 1)
)
juniPimGeneralGroup.setObjects(
      *(("Juniper-PIM-MIB", "juniPimNumHelloRcvd"),
        ("Juniper-PIM-MIB", "juniPimNumJoinPruneRcvd"),
        ("Juniper-PIM-MIB", "juniPimNumAssertRcvd"),
        ("Juniper-PIM-MIB", "juniPimNumGraftRcvd"),
        ("Juniper-PIM-MIB", "juniPimNumGraftAckRcvd"),
        ("Juniper-PIM-MIB", "juniPimNumHelloSent"),
        ("Juniper-PIM-MIB", "juniPimNumJoinPruneSent"),
        ("Juniper-PIM-MIB", "juniPimNumAssertSent"),
        ("Juniper-PIM-MIB", "juniPimNumGraftSent"),
        ("Juniper-PIM-MIB", "juniPimNumGraftAckSent"))
)
if mibBuilder.loadTexts:
    juniPimGeneralGroup.setStatus("current")

juniPimInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 2)
)
juniPimInterfaceGroup.setObjects(
      *(("Juniper-PIM-MIB", "juniPimIntfNumHelloRcvd"),
        ("Juniper-PIM-MIB", "juniPimIntfNumJoinPruneRcvd"),
        ("Juniper-PIM-MIB", "juniPimIntfNumAssertRcvd"),
        ("Juniper-PIM-MIB", "juniPimIntfNumGraftRcvd"),
        ("Juniper-PIM-MIB", "juniPimIntfNumGraftAckRcvd"),
        ("Juniper-PIM-MIB", "juniPimIntfNumHelloSent"),
        ("Juniper-PIM-MIB", "juniPimIntfNumJoinPruneSent"),
        ("Juniper-PIM-MIB", "juniPimIntfNumAssertSent"),
        ("Juniper-PIM-MIB", "juniPimIntfNumGraftSent"),
        ("Juniper-PIM-MIB", "juniPimIntfNumGraftAckSent"),
        ("Juniper-PIM-MIB", "juniPimIntfVersion"),
        ("Juniper-PIM-MIB", "juniPimIntfNumNbrs"))
)
if mibBuilder.loadTexts:
    juniPimInterfaceGroup.setStatus("current")

juniPimMRouteConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 3)
)
juniPimMRouteConfGroup.setObjects(
      *(("Juniper-PIM-MIB", "juniPimMRouteUpstreamAssertTimer"),
        ("Juniper-PIM-MIB", "juniPimMRouteAssertMetric"),
        ("Juniper-PIM-MIB", "juniPimMRouteAssertPref"),
        ("Juniper-PIM-MIB", "juniPimMRouteAssertRPTBit"),
        ("Juniper-PIM-MIB", "juniPimMRouteBits"),
        ("Juniper-PIM-MIB", "juniPimMRouteRPAddrInUse"),
        ("Juniper-PIM-MIB", "juniPimMRouteUpstreamNbr"),
        ("Juniper-PIM-MIB", "juniPimMRouteIifAddr"),
        ("Juniper-PIM-MIB", "juniPimMRouteIsWaitingToSwitchToSPT"),
        ("Juniper-PIM-MIB", "juniPimMRouteEntryExpiryTimer"),
        ("Juniper-PIM-MIB", "juniPimMRouteSenderDRAddr"),
        ("Juniper-PIM-MIB", "juniPimMRouteRouteAddr"),
        ("Juniper-PIM-MIB", "juniPimMRouteRouteMask"),
        ("Juniper-PIM-MIB", "juniPimMRouteGRPAddr"),
        ("Juniper-PIM-MIB", "juniPimMRouteGRPMask"),
        ("Juniper-PIM-MIB", "juniPimMRouteOtherProtoOifJoinTypeAll"),
        ("Juniper-PIM-MIB", "juniPimMRouteOtherProtoOifJoinTypeG"),
        ("Juniper-PIM-MIB", "juniPimMRouteOtherProtoOifJoinTypeSG"),
        ("Juniper-PIM-MIB", "juniPimMRoutePimType"))
)
if mibBuilder.loadTexts:
    juniPimMRouteConfGroup.setStatus("current")

juniPimMRouteNextHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 4)
)
juniPimMRouteNextHopGroup.setObjects(
      *(("Juniper-PIM-MIB", "juniPimMRouteNextHopPruneReason"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopJoinTypeSSRP"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopJoinTypeG"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopJoinTypeSG"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopHasLGM"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopHasOifAW"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopHasOifSendAssert"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopHasOifRegister"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopHasOifBorderBit"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopHasOifNullEncapsBit"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopJoinEndTimer"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopAssertEndTimer"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopNextAssertTimer"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopAssertSrcAddress"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopRegisterSuppressionTimer"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopPimType"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopPruneTimeLeft"),
        ("Juniper-PIM-MIB", "juniPimMRouteNextHopsendingIpAddress"))
)
if mibBuilder.loadTexts:
    juniPimMRouteNextHopGroup.setStatus("current")

juniPimRPSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 5)
)
juniPimRPSetGroup.setObjects(
      *(("Juniper-PIM-MIB", "juniPimRPSetPriority"),
        ("Juniper-PIM-MIB", "juniPimRPSetTypeInfo"),
        ("Juniper-PIM-MIB", "juniPimRPSetAccessListName"))
)
if mibBuilder.loadTexts:
    juniPimRPSetGroup.setStatus("current")

juniPimStaticRPConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 6)
)
juniPimStaticRPConfGroup.setObjects(
      *(("Juniper-PIM-MIB", "juniPimStaticRPConfRowStatus"),
        ("Juniper-PIM-MIB", "juniPimStaticRPConfOverride"))
)
if mibBuilder.loadTexts:
    juniPimStaticRPConfGroup.setStatus("current")

juniPimAutoRPConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 7)
)
juniPimAutoRPConfGroup.setObjects(
      *(("Juniper-PIM-MIB", "juniPimAutoRPConfRowStatus"),
        ("Juniper-PIM-MIB", "juniPimAutoRPConfTTL"),
        ("Juniper-PIM-MIB", "juniPimAutoRPConfAncmntIntvl"),
        ("Juniper-PIM-MIB", "juniPimAutoRPConfifId"))
)
if mibBuilder.loadTexts:
    juniPimAutoRPConfGroup.setStatus("current")

juniPimAutoRPCandGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 8)
)
juniPimAutoRPCandGroup.setObjects(
      *(("Juniper-PIM-MIB", "juniPimAutoRPCandRowStatus"),
        ("Juniper-PIM-MIB", "juniPimAutoRPCandAccessListName"),
        ("Juniper-PIM-MIB", "juniPimAutoRPCandAutoRPTTL"),
        ("Juniper-PIM-MIB", "juniPimAutoRPCandAutoRPAncmntIntvl"),
        ("Juniper-PIM-MIB", "juniPimAutoRPCandIfId"))
)
if mibBuilder.loadTexts:
    juniPimAutoRPCandGroup.setStatus("current")

juniPimComponentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 9)
)
juniPimComponentGroup.setObjects(
      *(("Juniper-PIM-MIB", "juniPimComponentAutoRPMappingAgentRowStatus"),
        ("Juniper-PIM-MIB", "juniPimComponentConfiguredAutoRPMappingAgentIfId"),
        ("Juniper-PIM-MIB", "juniPimComponentAutoRPMappingAgentInterval"),
        ("Juniper-PIM-MIB", "juniPimComponentAutoRPMappingTTL"),
        ("Juniper-PIM-MIB", "juniPimComponentAutoRPMappingAgentIntfAddr"),
        ("Juniper-PIM-MIB", "juniPimComponentAutoRPMappingAgentWinnerAddr"),
        ("Juniper-PIM-MIB", "juniPimComponentAutoRPMappingAgentWinnerLastHeard"))
)
if mibBuilder.loadTexts:
    juniPimComponentGroup.setStatus("current")

juniPimUnicastRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 10)
)
juniPimUnicastRouteGroup.setObjects(
      *(("Juniper-PIM-MIB", "juniPimUnicastRouteEntryRpfNbr"),
        ("Juniper-PIM-MIB", "juniPimUnicastRouteEntryIifId"),
        ("Juniper-PIM-MIB", "juniPimUnicastRouteEntryIifAddr"),
        ("Juniper-PIM-MIB", "juniPimUnicastRouteEntryPref"),
        ("Juniper-PIM-MIB", "juniPimUnicastRouteEntryMetric"),
        ("Juniper-PIM-MIB", "juniPimUnicastRouteEntryPimType"))
)
if mibBuilder.loadTexts:
    juniPimUnicastRouteGroup.setStatus("current")

juniPimSPTThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 11)
)
juniPimSPTThresholdGroup.setObjects(
      *(("Juniper-PIM-MIB", "juniPimSPTThresholdRowStatus"),
        ("Juniper-PIM-MIB", "juniPimSPTThresholdKbps"))
)
if mibBuilder.loadTexts:
    juniPimSPTThresholdGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniPimCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniPimCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-PIM-MIB",
    **{"JuniPimType": JuniPimType,
       "juniPimMIB": juniPimMIB,
       "juniPimMIBObjects": juniPimMIBObjects,
       "juniPimTraps": juniPimTraps,
       "juniPimGlobal": juniPimGlobal,
       "juniPimNumHelloRcvd": juniPimNumHelloRcvd,
       "juniPimNumJoinPruneRcvd": juniPimNumJoinPruneRcvd,
       "juniPimNumAssertRcvd": juniPimNumAssertRcvd,
       "juniPimNumGraftRcvd": juniPimNumGraftRcvd,
       "juniPimNumGraftAckRcvd": juniPimNumGraftAckRcvd,
       "juniPimNumHelloSent": juniPimNumHelloSent,
       "juniPimNumJoinPruneSent": juniPimNumJoinPruneSent,
       "juniPimNumAssertSent": juniPimNumAssertSent,
       "juniPimNumGraftSent": juniPimNumGraftSent,
       "juniPimNumGraftAckSent": juniPimNumGraftAckSent,
       "juniPimInterfaceTable": juniPimInterfaceTable,
       "juniPimInterfaceEntry": juniPimInterfaceEntry,
       "juniPimIntfNumHelloRcvd": juniPimIntfNumHelloRcvd,
       "juniPimIntfNumJoinPruneRcvd": juniPimIntfNumJoinPruneRcvd,
       "juniPimIntfNumAssertRcvd": juniPimIntfNumAssertRcvd,
       "juniPimIntfNumGraftRcvd": juniPimIntfNumGraftRcvd,
       "juniPimIntfNumGraftAckRcvd": juniPimIntfNumGraftAckRcvd,
       "juniPimIntfNumHelloSent": juniPimIntfNumHelloSent,
       "juniPimIntfNumJoinPruneSent": juniPimIntfNumJoinPruneSent,
       "juniPimIntfNumAssertSent": juniPimIntfNumAssertSent,
       "juniPimIntfNumGraftSent": juniPimIntfNumGraftSent,
       "juniPimIntfNumGraftAckSent": juniPimIntfNumGraftAckSent,
       "juniPimIntfVersion": juniPimIntfVersion,
       "juniPimIntfNumNbrs": juniPimIntfNumNbrs,
       "juniPimMRouteTable": juniPimMRouteTable,
       "juniPimMRouteEntry": juniPimMRouteEntry,
       "juniPimMRouteGroup": juniPimMRouteGroup,
       "juniPimMRouteSource": juniPimMRouteSource,
       "juniPimMRouteSourceMask": juniPimMRouteSourceMask,
       "juniPimMRouteRPAddress": juniPimMRouteRPAddress,
       "juniPimMRouteUpstreamAssertTimer": juniPimMRouteUpstreamAssertTimer,
       "juniPimMRouteAssertMetric": juniPimMRouteAssertMetric,
       "juniPimMRouteAssertPref": juniPimMRouteAssertPref,
       "juniPimMRouteAssertRPTBit": juniPimMRouteAssertRPTBit,
       "juniPimMRouteBits": juniPimMRouteBits,
       "juniPimMRouteRPAddrInUse": juniPimMRouteRPAddrInUse,
       "juniPimMRouteUpstreamNbr": juniPimMRouteUpstreamNbr,
       "juniPimMRouteIifAddr": juniPimMRouteIifAddr,
       "juniPimMRouteIsWaitingToSwitchToSPT": juniPimMRouteIsWaitingToSwitchToSPT,
       "juniPimMRouteEntryExpiryTimer": juniPimMRouteEntryExpiryTimer,
       "juniPimMRouteSenderDRAddr": juniPimMRouteSenderDRAddr,
       "juniPimMRouteRouteAddr": juniPimMRouteRouteAddr,
       "juniPimMRouteRouteMask": juniPimMRouteRouteMask,
       "juniPimMRouteGRPAddr": juniPimMRouteGRPAddr,
       "juniPimMRouteGRPMask": juniPimMRouteGRPMask,
       "juniPimMRouteOtherProtoOifJoinTypeAll": juniPimMRouteOtherProtoOifJoinTypeAll,
       "juniPimMRouteOtherProtoOifJoinTypeG": juniPimMRouteOtherProtoOifJoinTypeG,
       "juniPimMRouteOtherProtoOifJoinTypeSG": juniPimMRouteOtherProtoOifJoinTypeSG,
       "juniPimMRoutePimType": juniPimMRoutePimType,
       "juniPimMRouteNextHopTable": juniPimMRouteNextHopTable,
       "juniPimMRouteNextHopEntry": juniPimMRouteNextHopEntry,
       "juniPimMRouteNextHopGroupAddr": juniPimMRouteNextHopGroupAddr,
       "juniPimMRouteNextHopSrcAddr": juniPimMRouteNextHopSrcAddr,
       "juniPimMRouteNextHopSrcMask": juniPimMRouteNextHopSrcMask,
       "juniPimMRouteNextHopRPAddr": juniPimMRouteNextHopRPAddr,
       "juniPimMRouteNextHopIfId": juniPimMRouteNextHopIfId,
       "juniPimMRouteNextHopAddress": juniPimMRouteNextHopAddress,
       "juniPimMRouteNextHopPruneReason": juniPimMRouteNextHopPruneReason,
       "juniPimMRouteNextHopJoinTypeSSRP": juniPimMRouteNextHopJoinTypeSSRP,
       "juniPimMRouteNextHopJoinTypeG": juniPimMRouteNextHopJoinTypeG,
       "juniPimMRouteNextHopJoinTypeSG": juniPimMRouteNextHopJoinTypeSG,
       "juniPimMRouteNextHopHasLGM": juniPimMRouteNextHopHasLGM,
       "juniPimMRouteNextHopHasOifAW": juniPimMRouteNextHopHasOifAW,
       "juniPimMRouteNextHopHasOifSendAssert": juniPimMRouteNextHopHasOifSendAssert,
       "juniPimMRouteNextHopHasOifRegister": juniPimMRouteNextHopHasOifRegister,
       "juniPimMRouteNextHopHasOifBorderBit": juniPimMRouteNextHopHasOifBorderBit,
       "juniPimMRouteNextHopHasOifNullEncapsBit": juniPimMRouteNextHopHasOifNullEncapsBit,
       "juniPimMRouteNextHopJoinEndTimer": juniPimMRouteNextHopJoinEndTimer,
       "juniPimMRouteNextHopAssertEndTimer": juniPimMRouteNextHopAssertEndTimer,
       "juniPimMRouteNextHopNextAssertTimer": juniPimMRouteNextHopNextAssertTimer,
       "juniPimMRouteNextHopAssertSrcAddress": juniPimMRouteNextHopAssertSrcAddress,
       "juniPimMRouteNextHopRegisterSuppressionTimer": juniPimMRouteNextHopRegisterSuppressionTimer,
       "juniPimMRouteNextHopPimType": juniPimMRouteNextHopPimType,
       "juniPimMRouteNextHopPruneTimeLeft": juniPimMRouteNextHopPruneTimeLeft,
       "juniPimMRouteNextHopsendingIpAddress": juniPimMRouteNextHopsendingIpAddress,
       "juniPimRPSetTable": juniPimRPSetTable,
       "juniPimRPSetEntry": juniPimRPSetEntry,
       "juniPimRPSetPriority": juniPimRPSetPriority,
       "juniPimRPSetTypeInfo": juniPimRPSetTypeInfo,
       "juniPimRPSetAccessListName": juniPimRPSetAccessListName,
       "juniPimStaticRPConfTable": juniPimStaticRPConfTable,
       "juniPimStaticRPConfEntry": juniPimStaticRPConfEntry,
       "juniPimStaticRPConfComponentIndex": juniPimStaticRPConfComponentIndex,
       "juniPimStaticRPConfRPAddr": juniPimStaticRPConfRPAddr,
       "juniPimStaticRPConfAccessListName": juniPimStaticRPConfAccessListName,
       "juniPimStaticRPConfRowStatus": juniPimStaticRPConfRowStatus,
       "juniPimStaticRPConfOverride": juniPimStaticRPConfOverride,
       "juniPimAutoRPConfTable": juniPimAutoRPConfTable,
       "juniPimAutoRPConfEntry": juniPimAutoRPConfEntry,
       "juniPimAutoRPConfComponentIndex": juniPimAutoRPConfComponentIndex,
       "juniPimAutoRPConfCandRPAddr": juniPimAutoRPConfCandRPAddr,
       "juniPimAutoRPConfGroupAccessListName": juniPimAutoRPConfGroupAccessListName,
       "juniPimAutoRPConfRowStatus": juniPimAutoRPConfRowStatus,
       "juniPimAutoRPConfTTL": juniPimAutoRPConfTTL,
       "juniPimAutoRPConfAncmntIntvl": juniPimAutoRPConfAncmntIntvl,
       "juniPimAutoRPConfifId": juniPimAutoRPConfifId,
       "juniPimAutoRPCandTable": juniPimAutoRPCandTable,
       "juniPimAutoRPCandEntry": juniPimAutoRPCandEntry,
       "juniPimAutoRPCandComponentIndex": juniPimAutoRPCandComponentIndex,
       "juniPimAutoRPCandRPAddr": juniPimAutoRPCandRPAddr,
       "juniPimAutoRPCandGroupAddr": juniPimAutoRPCandGroupAddr,
       "juniPimAutoRPCandGroupMask": juniPimAutoRPCandGroupMask,
       "juniPimAutoRPCandRowStatus": juniPimAutoRPCandRowStatus,
       "juniPimAutoRPCandAccessListName": juniPimAutoRPCandAccessListName,
       "juniPimAutoRPCandAutoRPTTL": juniPimAutoRPCandAutoRPTTL,
       "juniPimAutoRPCandAutoRPAncmntIntvl": juniPimAutoRPCandAutoRPAncmntIntvl,
       "juniPimAutoRPCandIfId": juniPimAutoRPCandIfId,
       "juniPimComponentTable": juniPimComponentTable,
       "juniPimComponentEntry": juniPimComponentEntry,
       "juniPimComponentIndex": juniPimComponentIndex,
       "juniPimComponentAutoRPMappingAgentRowStatus": juniPimComponentAutoRPMappingAgentRowStatus,
       "juniPimComponentConfiguredAutoRPMappingAgentIfId": juniPimComponentConfiguredAutoRPMappingAgentIfId,
       "juniPimComponentAutoRPMappingAgentInterval": juniPimComponentAutoRPMappingAgentInterval,
       "juniPimComponentAutoRPMappingTTL": juniPimComponentAutoRPMappingTTL,
       "juniPimComponentAutoRPMappingAgentIntfAddr": juniPimComponentAutoRPMappingAgentIntfAddr,
       "juniPimComponentAutoRPMappingAgentWinnerAddr": juniPimComponentAutoRPMappingAgentWinnerAddr,
       "juniPimComponentAutoRPMappingAgentWinnerLastHeard": juniPimComponentAutoRPMappingAgentWinnerLastHeard,
       "juniPimUnicastRouteTable": juniPimUnicastRouteTable,
       "juniPimUnicastRouteEntry": juniPimUnicastRouteEntry,
       "juniPimUnicastRouteEntryAddr": juniPimUnicastRouteEntryAddr,
       "juniPimUnicastRouteEntryMask": juniPimUnicastRouteEntryMask,
       "juniPimUnicastRouteEntryRpfNbr": juniPimUnicastRouteEntryRpfNbr,
       "juniPimUnicastRouteEntryIifId": juniPimUnicastRouteEntryIifId,
       "juniPimUnicastRouteEntryIifAddr": juniPimUnicastRouteEntryIifAddr,
       "juniPimUnicastRouteEntryPref": juniPimUnicastRouteEntryPref,
       "juniPimUnicastRouteEntryMetric": juniPimUnicastRouteEntryMetric,
       "juniPimUnicastRouteEntryPimType": juniPimUnicastRouteEntryPimType,
       "juniPimSPTThresholdTable": juniPimSPTThresholdTable,
       "juniPimSPTThresholdEntry": juniPimSPTThresholdEntry,
       "juniPimSPTThresholdAccessListName": juniPimSPTThresholdAccessListName,
       "juniPimSPTThresholdRowStatus": juniPimSPTThresholdRowStatus,
       "juniPimSPTThresholdKbps": juniPimSPTThresholdKbps,
       "juniPimConformance": juniPimConformance,
       "juniPimCompliances": juniPimCompliances,
       "juniPimCompliance": juniPimCompliance,
       "juniPimGroups": juniPimGroups,
       "juniPimGeneralGroup": juniPimGeneralGroup,
       "juniPimInterfaceGroup": juniPimInterfaceGroup,
       "juniPimMRouteConfGroup": juniPimMRouteConfGroup,
       "juniPimMRouteNextHopGroup": juniPimMRouteNextHopGroup,
       "juniPimRPSetGroup": juniPimRPSetGroup,
       "juniPimStaticRPConfGroup": juniPimStaticRPConfGroup,
       "juniPimAutoRPConfGroup": juniPimAutoRPConfGroup,
       "juniPimAutoRPCandGroup": juniPimAutoRPCandGroup,
       "juniPimComponentGroup": juniPimComponentGroup,
       "juniPimUnicastRouteGroup": juniPimUnicastRouteGroup,
       "juniPimSPTThresholdGroup": juniPimSPTThresholdGroup}
)
