# SNMP MIB module (GERP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GERP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:35 2024
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

(gbnL2,) = mibBuilder.importSymbols(
    "GREENTECH-MASTER-MIB",
    "gbnL2")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

gerpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7)
)
gerpMib.setRevisions(
        ("1908-04-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GerpMIBObjects_ObjectIdentity = ObjectIdentity
gerpMIBObjects = _GerpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1)
)
_Gerp_ObjectIdentity = ObjectIdentity
gerp = _Gerp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1)
)


class _GerpOnoff_Type(Integer32):
    """Custom type gerpOnoff based on Integer32"""
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


_GerpOnoff_Type.__name__ = "Integer32"
_GerpOnoff_Object = MibScalar
gerpOnoff = _GerpOnoff_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 1),
    _GerpOnoff_Type()
)
gerpOnoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gerpOnoff.setStatus("current")


class _GerpHealthTime_Type(Integer32):
    """Custom type gerpHealthTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_GerpHealthTime_Type.__name__ = "Integer32"
_GerpHealthTime_Object = MibScalar
gerpHealthTime = _GerpHealthTime_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 2),
    _GerpHealthTime_Type()
)
gerpHealthTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gerpHealthTime.setStatus("current")


class _GerpHealthTimeout_Type(Integer32):
    """Custom type gerpHealthTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_GerpHealthTimeout_Type.__name__ = "Integer32"
_GerpHealthTimeout_Object = MibScalar
gerpHealthTimeout = _GerpHealthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 3),
    _GerpHealthTimeout_Type()
)
gerpHealthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gerpHealthTimeout.setStatus("current")


class _GerpMajorFaultTime_Type(Integer32):
    """Custom type gerpMajorFaultTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 29),
    )


_GerpMajorFaultTime_Type.__name__ = "Integer32"
_GerpMajorFaultTime_Object = MibScalar
gerpMajorFaultTime = _GerpMajorFaultTime_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 4),
    _GerpMajorFaultTime_Type()
)
gerpMajorFaultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gerpMajorFaultTime.setStatus("current")


class _GerpPrefwdTimeout_Type(Integer32):
    """Custom type gerpPrefwdTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_GerpPrefwdTimeout_Type.__name__ = "Integer32"
_GerpPrefwdTimeout_Object = MibScalar
gerpPrefwdTimeout = _GerpPrefwdTimeout_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 5),
    _GerpPrefwdTimeout_Type()
)
gerpPrefwdTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gerpPrefwdTimeout.setStatus("current")
_GerpDomainTable_Object = MibTable
gerpDomainTable = _GerpDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 6)
)
if mibBuilder.loadTexts:
    gerpDomainTable.setStatus("current")
_GerpDomainEntry_Object = MibTableRow
gerpDomainEntry = _GerpDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 6, 1)
)
gerpDomainEntry.setIndexNames(
    (0, "GERP-MIB", "gerpDomainId"),
)
if mibBuilder.loadTexts:
    gerpDomainEntry.setStatus("current")


class _GerpDomainId_Type(Integer32):
    """Custom type gerpDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GerpDomainId_Type.__name__ = "Integer32"
_GerpDomainId_Object = MibTableColumn
gerpDomainId = _GerpDomainId_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 6, 1, 1),
    _GerpDomainId_Type()
)
gerpDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gerpDomainId.setStatus("current")


class _GerpMVlanId_Type(Integer32):
    """Custom type gerpMVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_GerpMVlanId_Type.__name__ = "Integer32"
_GerpMVlanId_Object = MibTableColumn
gerpMVlanId = _GerpMVlanId_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 6, 1, 2),
    _GerpMVlanId_Type()
)
gerpMVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gerpMVlanId.setStatus("current")
_GerpRingTable_Object = MibTable
gerpRingTable = _GerpRingTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 7)
)
if mibBuilder.loadTexts:
    gerpRingTable.setStatus("current")
_GerpRingEntry_Object = MibTableRow
gerpRingEntry = _GerpRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 7, 1)
)
gerpRingEntry.setIndexNames(
    (0, "GERP-MIB", "gerpDomainId"),
    (0, "GERP-MIB", "gerpRingId"),
)
if mibBuilder.loadTexts:
    gerpRingEntry.setStatus("current")


class _GerpRingId_Type(Integer32):
    """Custom type gerpRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GerpRingId_Type.__name__ = "Integer32"
_GerpRingId_Object = MibTableColumn
gerpRingId = _GerpRingId_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 7, 1, 1),
    _GerpRingId_Type()
)
gerpRingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gerpRingId.setStatus("current")


class _GerpRingLevel_Type(Integer32):
    """Custom type gerpRingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GerpRingLevel_Type.__name__ = "Integer32"
_GerpRingLevel_Object = MibTableColumn
gerpRingLevel = _GerpRingLevel_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 7, 1, 2),
    _GerpRingLevel_Type()
)
gerpRingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gerpRingLevel.setStatus("current")


class _GerpBrdgRole_Type(Integer32):
    """Custom type gerpBrdgRole based on Integer32"""
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
        *(("assEdge", 4),
          ("edge", 3),
          ("master", 1),
          ("trans", 2))
    )


_GerpBrdgRole_Type.__name__ = "Integer32"
_GerpBrdgRole_Object = MibTableColumn
gerpBrdgRole = _GerpBrdgRole_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 7, 1, 3),
    _GerpBrdgRole_Type()
)
gerpBrdgRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gerpBrdgRole.setStatus("current")


class _GerpPriComPortId_Type(Integer32):
    """Custom type gerpPriComPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GerpPriComPortId_Type.__name__ = "Integer32"
_GerpPriComPortId_Object = MibTableColumn
gerpPriComPortId = _GerpPriComPortId_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 7, 1, 4),
    _GerpPriComPortId_Type()
)
gerpPriComPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gerpPriComPortId.setStatus("current")


class _GerpSecEdgePortId_Type(Integer32):
    """Custom type gerpSecEdgePortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GerpSecEdgePortId_Type.__name__ = "Integer32"
_GerpSecEdgePortId_Object = MibTableColumn
gerpSecEdgePortId = _GerpSecEdgePortId_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 7, 1, 5),
    _GerpSecEdgePortId_Type()
)
gerpSecEdgePortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gerpSecEdgePortId.setStatus("current")


class _GerpRowStatus_Type(RowStatus):
    """Custom type gerpRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_GerpRowStatus_Type.__name__ = "RowStatus"
_GerpRowStatus_Object = MibTableColumn
gerpRowStatus = _GerpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 7, 1, 6),
    _GerpRowStatus_Type()
)
gerpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gerpRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GERP-MIB",
    **{"gerpMib": gerpMib,
       "gerpMIBObjects": gerpMIBObjects,
       "gerp": gerp,
       "gerpOnoff": gerpOnoff,
       "gerpHealthTime": gerpHealthTime,
       "gerpHealthTimeout": gerpHealthTimeout,
       "gerpMajorFaultTime": gerpMajorFaultTime,
       "gerpPrefwdTimeout": gerpPrefwdTimeout,
       "gerpDomainTable": gerpDomainTable,
       "gerpDomainEntry": gerpDomainEntry,
       "gerpDomainId": gerpDomainId,
       "gerpMVlanId": gerpMVlanId,
       "gerpRingTable": gerpRingTable,
       "gerpRingEntry": gerpRingEntry,
       "gerpRingId": gerpRingId,
       "gerpRingLevel": gerpRingLevel,
       "gerpBrdgRole": gerpBrdgRole,
       "gerpPriComPortId": gerpPriComPortId,
       "gerpSecEdgePortId": gerpSecEdgePortId,
       "gerpRowStatus": gerpRowStatus}
)
