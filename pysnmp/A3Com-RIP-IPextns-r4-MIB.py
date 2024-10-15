# SNMP MIB module (A3COM-RIP-IPEXTNS-R4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-RIP-IPEXTNS-R4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:45 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_BrouterMIB_ObjectIdentity = ObjectIdentity
brouterMIB = _BrouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2)
)
_A3ComRipIp_ObjectIdentity = ObjectIdentity
a3ComRipIp = _A3ComRipIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 8)
)


class _A3RipIpUpdateTime_Type(Integer32):
    """Custom type a3RipIpUpdateTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5400),
    )


_A3RipIpUpdateTime_Type.__name__ = "Integer32"
_A3RipIpUpdateTime_Object = MibScalar
a3RipIpUpdateTime = _A3RipIpUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 1),
    _A3RipIpUpdateTime_Type()
)
a3RipIpUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpUpdateTime.setStatus("mandatory")
_A3RipIpCtlTable_Object = MibTable
a3RipIpCtlTable = _A3RipIpCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2)
)
if mibBuilder.loadTexts:
    a3RipIpCtlTable.setStatus("mandatory")
_A3RipIpCtlEntry_Object = MibTableRow
a3RipIpCtlEntry = _A3RipIpCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1)
)
a3RipIpCtlEntry.setIndexNames(
    (0, "A3COM-RIP-IPEXTNS-R4-MIB", "a3RipIpPortIndex"),
)
if mibBuilder.loadTexts:
    a3RipIpCtlEntry.setStatus("mandatory")
_A3RipIpPortIndex_Type = Integer32
_A3RipIpPortIndex_Object = MibTableColumn
a3RipIpPortIndex = _A3RipIpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 1),
    _A3RipIpPortIndex_Type()
)
a3RipIpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RipIpPortIndex.setStatus("mandatory")


class _A3RipIpTalkCtl_Type(Integer32):
    """Custom type a3RipIpTalkCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTalk", 2),
          ("talk", 1))
    )


_A3RipIpTalkCtl_Type.__name__ = "Integer32"
_A3RipIpTalkCtl_Object = MibTableColumn
a3RipIpTalkCtl = _A3RipIpTalkCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 2),
    _A3RipIpTalkCtl_Type()
)
a3RipIpTalkCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpTalkCtl.setStatus("mandatory")


class _A3RipIpListenCtl_Type(Integer32):
    """Custom type a3RipIpListenCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("listen", 1),
          ("noListen", 2))
    )


_A3RipIpListenCtl_Type.__name__ = "Integer32"
_A3RipIpListenCtl_Object = MibTableColumn
a3RipIpListenCtl = _A3RipIpListenCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 3),
    _A3RipIpListenCtl_Type()
)
a3RipIpListenCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpListenCtl.setStatus("mandatory")


class _A3RipIpTrustedNbrCtl_Type(Integer32):
    """Custom type a3RipIpTrustedNbrCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_A3RipIpTrustedNbrCtl_Type.__name__ = "Integer32"
_A3RipIpTrustedNbrCtl_Object = MibTableColumn
a3RipIpTrustedNbrCtl = _A3RipIpTrustedNbrCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 4),
    _A3RipIpTrustedNbrCtl_Type()
)
a3RipIpTrustedNbrCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpTrustedNbrCtl.setStatus("mandatory")


class _A3RipIpPoisonCtl_Type(Integer32):
    """Custom type a3RipIpPoisonCtl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPoison", 2),
          ("poison", 1))
    )


_A3RipIpPoisonCtl_Type.__name__ = "Integer32"
_A3RipIpPoisonCtl_Object = MibTableColumn
a3RipIpPoisonCtl = _A3RipIpPoisonCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 5),
    _A3RipIpPoisonCtl_Type()
)
a3RipIpPoisonCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpPoisonCtl.setStatus("mandatory")


class _A3RipIpTriggerCtl_Type(Integer32):
    """Custom type a3RipIpTriggerCtl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTrigger", 2),
          ("trigger", 1))
    )


_A3RipIpTriggerCtl_Type.__name__ = "Integer32"
_A3RipIpTriggerCtl_Object = MibTableColumn
a3RipIpTriggerCtl = _A3RipIpTriggerCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 6),
    _A3RipIpTriggerCtl_Type()
)
a3RipIpTriggerCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpTriggerCtl.setStatus("mandatory")


class _A3RipIpDefMetric_Type(Integer32):
    """Custom type a3RipIpDefMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_A3RipIpDefMetric_Type.__name__ = "Integer32"
_A3RipIpDefMetric_Object = MibTableColumn
a3RipIpDefMetric = _A3RipIpDefMetric_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 7),
    _A3RipIpDefMetric_Type()
)
a3RipIpDefMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpDefMetric.setStatus("mandatory")


class _A3RipIpExtPolCtl_Type(Integer32):
    """Custom type a3RipIpExtPolCtl based on Integer32"""
    defaultValue = 2

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
        *(("all", 1),
          ("exclude", 4),
          ("include", 3),
          ("none", 2))
    )


_A3RipIpExtPolCtl_Type.__name__ = "Integer32"
_A3RipIpExtPolCtl_Object = MibTableColumn
a3RipIpExtPolCtl = _A3RipIpExtPolCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 8),
    _A3RipIpExtPolCtl_Type()
)
a3RipIpExtPolCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpExtPolCtl.setStatus("mandatory")


class _A3RipIpIntPolCtl_Type(Integer32):
    """Custom type a3RipIpIntPolCtl based on Integer32"""
    defaultValue = 2

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
        *(("all", 1),
          ("exclude", 4),
          ("include", 3),
          ("none", 2))
    )


_A3RipIpIntPolCtl_Type.__name__ = "Integer32"
_A3RipIpIntPolCtl_Object = MibTableColumn
a3RipIpIntPolCtl = _A3RipIpIntPolCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 9),
    _A3RipIpIntPolCtl_Type()
)
a3RipIpIntPolCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpIntPolCtl.setStatus("mandatory")


class _A3RipIpNetPolCtl_Type(Integer32):
    """Custom type a3RipIpNetPolCtl based on Integer32"""
    defaultValue = 1

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
        *(("all", 1),
          ("exclude", 4),
          ("include", 3),
          ("none", 2))
    )


_A3RipIpNetPolCtl_Type.__name__ = "Integer32"
_A3RipIpNetPolCtl_Object = MibTableColumn
a3RipIpNetPolCtl = _A3RipIpNetPolCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 10),
    _A3RipIpNetPolCtl_Type()
)
a3RipIpNetPolCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpNetPolCtl.setStatus("mandatory")


class _A3RipIpRcvPolCtl_Type(Integer32):
    """Custom type a3RipIpRcvPolCtl based on Integer32"""
    defaultValue = 1

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
        *(("all", 1),
          ("exclude", 4),
          ("include", 3),
          ("none", 2))
    )


_A3RipIpRcvPolCtl_Type.__name__ = "Integer32"
_A3RipIpRcvPolCtl_Object = MibTableColumn
a3RipIpRcvPolCtl = _A3RipIpRcvPolCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 11),
    _A3RipIpRcvPolCtl_Type()
)
a3RipIpRcvPolCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpRcvPolCtl.setStatus("mandatory")


class _A3RipIpStaPolCtl_Type(Integer32):
    """Custom type a3RipIpStaPolCtl based on Integer32"""
    defaultValue = 2

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
        *(("all", 1),
          ("exclude", 4),
          ("include", 3),
          ("none", 2))
    )


_A3RipIpStaPolCtl_Type.__name__ = "Integer32"
_A3RipIpStaPolCtl_Object = MibTableColumn
a3RipIpStaPolCtl = _A3RipIpStaPolCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 12),
    _A3RipIpStaPolCtl_Type()
)
a3RipIpStaPolCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpStaPolCtl.setStatus("mandatory")


class _A3RipIpUnnAdvCtl_Type(Integer32):
    """Custom type a3RipIpUnnAdvCtl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("netAdvUnn", 2),
          ("subnetAdvUnn", 1))
    )


_A3RipIpUnnAdvCtl_Type.__name__ = "Integer32"
_A3RipIpUnnAdvCtl_Object = MibTableColumn
a3RipIpUnnAdvCtl = _A3RipIpUnnAdvCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 13),
    _A3RipIpUnnAdvCtl_Type()
)
a3RipIpUnnAdvCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpUnnAdvCtl.setStatus("mandatory")


class _A3RipIpBcastCtl_Type(Integer32):
    """Custom type a3RipIpBcastCtl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all1sBcast", 2),
          ("subnetBcast", 1))
    )


_A3RipIpBcastCtl_Type.__name__ = "Integer32"
_A3RipIpBcastCtl_Object = MibTableColumn
a3RipIpBcastCtl = _A3RipIpBcastCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 14),
    _A3RipIpBcastCtl_Type()
)
a3RipIpBcastCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpBcastCtl.setStatus("mandatory")


class _A3RipIpExtPolAllMet_Type(Integer32):
    """Custom type a3RipIpExtPolAllMet based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_A3RipIpExtPolAllMet_Type.__name__ = "Integer32"
_A3RipIpExtPolAllMet_Object = MibTableColumn
a3RipIpExtPolAllMet = _A3RipIpExtPolAllMet_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 15),
    _A3RipIpExtPolAllMet_Type()
)
a3RipIpExtPolAllMet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpExtPolAllMet.setStatus("mandatory")


class _A3RipIpIntPolAllMet_Type(Integer32):
    """Custom type a3RipIpIntPolAllMet based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_A3RipIpIntPolAllMet_Type.__name__ = "Integer32"
_A3RipIpIntPolAllMet_Object = MibTableColumn
a3RipIpIntPolAllMet = _A3RipIpIntPolAllMet_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 16),
    _A3RipIpIntPolAllMet_Type()
)
a3RipIpIntPolAllMet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpIntPolAllMet.setStatus("mandatory")


class _A3RipIpNetPolAllMet_Type(Integer32):
    """Custom type a3RipIpNetPolAllMet based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_A3RipIpNetPolAllMet_Type.__name__ = "Integer32"
_A3RipIpNetPolAllMet_Object = MibTableColumn
a3RipIpNetPolAllMet = _A3RipIpNetPolAllMet_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 17),
    _A3RipIpNetPolAllMet_Type()
)
a3RipIpNetPolAllMet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpNetPolAllMet.setStatus("mandatory")


class _A3RipIpRcvPolAllMet_Type(Integer32):
    """Custom type a3RipIpRcvPolAllMet based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_A3RipIpRcvPolAllMet_Type.__name__ = "Integer32"
_A3RipIpRcvPolAllMet_Object = MibTableColumn
a3RipIpRcvPolAllMet = _A3RipIpRcvPolAllMet_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 18),
    _A3RipIpRcvPolAllMet_Type()
)
a3RipIpRcvPolAllMet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpRcvPolAllMet.setStatus("mandatory")


class _A3RipIpStaPolAllMet_Type(Integer32):
    """Custom type a3RipIpStaPolAllMet based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_A3RipIpStaPolAllMet_Type.__name__ = "Integer32"
_A3RipIpStaPolAllMet_Object = MibTableColumn
a3RipIpStaPolAllMet = _A3RipIpStaPolAllMet_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 19),
    _A3RipIpStaPolAllMet_Type()
)
a3RipIpStaPolAllMet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpStaPolAllMet.setStatus("mandatory")


class _A3RipIpDynNbrCtl_Type(Integer32):
    """Custom type a3RipIpDynNbrCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamicNbr", 1),
          ("noDynamicNbr", 2))
    )


_A3RipIpDynNbrCtl_Type.__name__ = "Integer32"
_A3RipIpDynNbrCtl_Object = MibTableColumn
a3RipIpDynNbrCtl = _A3RipIpDynNbrCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 20),
    _A3RipIpDynNbrCtl_Type()
)
a3RipIpDynNbrCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpDynNbrCtl.setStatus("mandatory")


class _A3RipIpAggregateCtl_Type(Integer32):
    """Custom type a3RipIpAggregateCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 1),
          ("noAggregate", 2))
    )


_A3RipIpAggregateCtl_Type.__name__ = "Integer32"
_A3RipIpAggregateCtl_Object = MibTableColumn
a3RipIpAggregateCtl = _A3RipIpAggregateCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 21),
    _A3RipIpAggregateCtl_Type()
)
a3RipIpAggregateCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpAggregateCtl.setStatus("mandatory")


class _A3RipIpDeAggregateCtl_Type(Integer32):
    """Custom type a3RipIpDeAggregateCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deAggregate", 1),
          ("noDeAggregate", 2))
    )


_A3RipIpDeAggregateCtl_Type.__name__ = "Integer32"
_A3RipIpDeAggregateCtl_Object = MibTableColumn
a3RipIpDeAggregateCtl = _A3RipIpDeAggregateCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 22),
    _A3RipIpDeAggregateCtl_Type()
)
a3RipIpDeAggregateCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpDeAggregateCtl.setStatus("mandatory")


class _A3RipIpNBMAmodeCtl_Type(Integer32):
    """Custom type a3RipIpNBMAmodeCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullMesh", 1),
          ("nonMesh", 2))
    )


_A3RipIpNBMAmodeCtl_Type.__name__ = "Integer32"
_A3RipIpNBMAmodeCtl_Object = MibTableColumn
a3RipIpNBMAmodeCtl = _A3RipIpNBMAmodeCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 2, 1, 23),
    _A3RipIpNBMAmodeCtl_Type()
)
a3RipIpNBMAmodeCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpNBMAmodeCtl.setStatus("mandatory")
_A3RipIpExtPolTable_Object = MibTable
a3RipIpExtPolTable = _A3RipIpExtPolTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 3)
)
if mibBuilder.loadTexts:
    a3RipIpExtPolTable.setStatus("mandatory")
_A3RipIpExtPolEntry_Object = MibTableRow
a3RipIpExtPolEntry = _A3RipIpExtPolEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 3, 1)
)
a3RipIpExtPolEntry.setIndexNames(
    (0, "A3COM-RIP-IPEXTNS-R4-MIB", "a3RipIpExtPolPort"),
    (0, "A3COM-RIP-IPEXTNS-R4-MIB", "a3RipIpExtPolAddr"),
)
if mibBuilder.loadTexts:
    a3RipIpExtPolEntry.setStatus("mandatory")
_A3RipIpExtPolPort_Type = Integer32
_A3RipIpExtPolPort_Object = MibTableColumn
a3RipIpExtPolPort = _A3RipIpExtPolPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 3, 1, 1),
    _A3RipIpExtPolPort_Type()
)
a3RipIpExtPolPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RipIpExtPolPort.setStatus("mandatory")
_A3RipIpExtPolAddr_Type = IpAddress
_A3RipIpExtPolAddr_Object = MibTableColumn
a3RipIpExtPolAddr = _A3RipIpExtPolAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 3, 1, 2),
    _A3RipIpExtPolAddr_Type()
)
a3RipIpExtPolAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RipIpExtPolAddr.setStatus("mandatory")


class _A3RipIpExtPolMetric_Type(Integer32):
    """Custom type a3RipIpExtPolMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_A3RipIpExtPolMetric_Type.__name__ = "Integer32"
_A3RipIpExtPolMetric_Object = MibTableColumn
a3RipIpExtPolMetric = _A3RipIpExtPolMetric_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 3, 1, 3),
    _A3RipIpExtPolMetric_Type()
)
a3RipIpExtPolMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpExtPolMetric.setStatus("mandatory")
_A3RipIpExtPolStatus_Type = RowStatus
_A3RipIpExtPolStatus_Object = MibTableColumn
a3RipIpExtPolStatus = _A3RipIpExtPolStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 3, 1, 4),
    _A3RipIpExtPolStatus_Type()
)
a3RipIpExtPolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpExtPolStatus.setStatus("mandatory")
_A3RipIpIntPolTable_Object = MibTable
a3RipIpIntPolTable = _A3RipIpIntPolTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 4)
)
if mibBuilder.loadTexts:
    a3RipIpIntPolTable.setStatus("mandatory")
_A3RipIpIntPolEntry_Object = MibTableRow
a3RipIpIntPolEntry = _A3RipIpIntPolEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 4, 1)
)
a3RipIpIntPolEntry.setIndexNames(
    (0, "A3COM-RIP-IPEXTNS-R4-MIB", "a3RipIpIntPolPort"),
    (0, "A3COM-RIP-IPEXTNS-R4-MIB", "a3RipIpIntPolAddr"),
)
if mibBuilder.loadTexts:
    a3RipIpIntPolEntry.setStatus("mandatory")
_A3RipIpIntPolPort_Type = Integer32
_A3RipIpIntPolPort_Object = MibTableColumn
a3RipIpIntPolPort = _A3RipIpIntPolPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 4, 1, 1),
    _A3RipIpIntPolPort_Type()
)
a3RipIpIntPolPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RipIpIntPolPort.setStatus("mandatory")
_A3RipIpIntPolAddr_Type = IpAddress
_A3RipIpIntPolAddr_Object = MibTableColumn
a3RipIpIntPolAddr = _A3RipIpIntPolAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 4, 1, 2),
    _A3RipIpIntPolAddr_Type()
)
a3RipIpIntPolAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RipIpIntPolAddr.setStatus("mandatory")


class _A3RipIpIntPolMetric_Type(Integer32):
    """Custom type a3RipIpIntPolMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_A3RipIpIntPolMetric_Type.__name__ = "Integer32"
_A3RipIpIntPolMetric_Object = MibTableColumn
a3RipIpIntPolMetric = _A3RipIpIntPolMetric_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 4, 1, 3),
    _A3RipIpIntPolMetric_Type()
)
a3RipIpIntPolMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpIntPolMetric.setStatus("mandatory")
_A3RipIpIntPolStatus_Type = RowStatus
_A3RipIpIntPolStatus_Object = MibTableColumn
a3RipIpIntPolStatus = _A3RipIpIntPolStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 4, 1, 4),
    _A3RipIpIntPolStatus_Type()
)
a3RipIpIntPolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpIntPolStatus.setStatus("mandatory")
_A3RipIpNetPolTable_Object = MibTable
a3RipIpNetPolTable = _A3RipIpNetPolTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 5)
)
if mibBuilder.loadTexts:
    a3RipIpNetPolTable.setStatus("mandatory")
_A3RipIpNetPolEntry_Object = MibTableRow
a3RipIpNetPolEntry = _A3RipIpNetPolEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 5, 1)
)
a3RipIpNetPolEntry.setIndexNames(
    (0, "A3COM-RIP-IPEXTNS-R4-MIB", "a3RipIpNetPolPort"),
    (0, "A3COM-RIP-IPEXTNS-R4-MIB", "a3RipIpNetPolAddr"),
)
if mibBuilder.loadTexts:
    a3RipIpNetPolEntry.setStatus("mandatory")
_A3RipIpNetPolPort_Type = Integer32
_A3RipIpNetPolPort_Object = MibTableColumn
a3RipIpNetPolPort = _A3RipIpNetPolPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 5, 1, 1),
    _A3RipIpNetPolPort_Type()
)
a3RipIpNetPolPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RipIpNetPolPort.setStatus("mandatory")
_A3RipIpNetPolAddr_Type = IpAddress
_A3RipIpNetPolAddr_Object = MibTableColumn
a3RipIpNetPolAddr = _A3RipIpNetPolAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 5, 1, 2),
    _A3RipIpNetPolAddr_Type()
)
a3RipIpNetPolAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RipIpNetPolAddr.setStatus("mandatory")


class _A3RipIpNetPolMetric_Type(Integer32):
    """Custom type a3RipIpNetPolMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_A3RipIpNetPolMetric_Type.__name__ = "Integer32"
_A3RipIpNetPolMetric_Object = MibTableColumn
a3RipIpNetPolMetric = _A3RipIpNetPolMetric_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 5, 1, 3),
    _A3RipIpNetPolMetric_Type()
)
a3RipIpNetPolMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpNetPolMetric.setStatus("mandatory")
_A3RipIpNetPolStatus_Type = RowStatus
_A3RipIpNetPolStatus_Object = MibTableColumn
a3RipIpNetPolStatus = _A3RipIpNetPolStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 5, 1, 4),
    _A3RipIpNetPolStatus_Type()
)
a3RipIpNetPolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpNetPolStatus.setStatus("mandatory")
_A3RipIpRcvPolTable_Object = MibTable
a3RipIpRcvPolTable = _A3RipIpRcvPolTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 6)
)
if mibBuilder.loadTexts:
    a3RipIpRcvPolTable.setStatus("mandatory")
_A3RipIpRcvPolEntry_Object = MibTableRow
a3RipIpRcvPolEntry = _A3RipIpRcvPolEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 6, 1)
)
a3RipIpRcvPolEntry.setIndexNames(
    (0, "A3COM-RIP-IPEXTNS-R4-MIB", "a3RipIpRcvPolPort"),
    (0, "A3COM-RIP-IPEXTNS-R4-MIB", "a3RipIpRcvPolAddr"),
)
if mibBuilder.loadTexts:
    a3RipIpRcvPolEntry.setStatus("mandatory")
_A3RipIpRcvPolPort_Type = Integer32
_A3RipIpRcvPolPort_Object = MibTableColumn
a3RipIpRcvPolPort = _A3RipIpRcvPolPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 6, 1, 1),
    _A3RipIpRcvPolPort_Type()
)
a3RipIpRcvPolPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RipIpRcvPolPort.setStatus("mandatory")
_A3RipIpRcvPolAddr_Type = IpAddress
_A3RipIpRcvPolAddr_Object = MibTableColumn
a3RipIpRcvPolAddr = _A3RipIpRcvPolAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 6, 1, 2),
    _A3RipIpRcvPolAddr_Type()
)
a3RipIpRcvPolAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RipIpRcvPolAddr.setStatus("mandatory")


class _A3RipIpRcvPolMetric_Type(Integer32):
    """Custom type a3RipIpRcvPolMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_A3RipIpRcvPolMetric_Type.__name__ = "Integer32"
_A3RipIpRcvPolMetric_Object = MibTableColumn
a3RipIpRcvPolMetric = _A3RipIpRcvPolMetric_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 6, 1, 3),
    _A3RipIpRcvPolMetric_Type()
)
a3RipIpRcvPolMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpRcvPolMetric.setStatus("mandatory")
_A3RipIpRcvPolStatus_Type = RowStatus
_A3RipIpRcvPolStatus_Object = MibTableColumn
a3RipIpRcvPolStatus = _A3RipIpRcvPolStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 6, 1, 4),
    _A3RipIpRcvPolStatus_Type()
)
a3RipIpRcvPolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpRcvPolStatus.setStatus("mandatory")
_A3RipIpStaPolTable_Object = MibTable
a3RipIpStaPolTable = _A3RipIpStaPolTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 7)
)
if mibBuilder.loadTexts:
    a3RipIpStaPolTable.setStatus("mandatory")
_A3RipIpStaPolEntry_Object = MibTableRow
a3RipIpStaPolEntry = _A3RipIpStaPolEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 7, 1)
)
a3RipIpStaPolEntry.setIndexNames(
    (0, "A3COM-RIP-IPEXTNS-R4-MIB", "a3RipIpStaPolPort"),
    (0, "A3COM-RIP-IPEXTNS-R4-MIB", "a3RipIpStaPolAddr"),
)
if mibBuilder.loadTexts:
    a3RipIpStaPolEntry.setStatus("mandatory")
_A3RipIpStaPolPort_Type = Integer32
_A3RipIpStaPolPort_Object = MibTableColumn
a3RipIpStaPolPort = _A3RipIpStaPolPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 7, 1, 1),
    _A3RipIpStaPolPort_Type()
)
a3RipIpStaPolPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RipIpStaPolPort.setStatus("mandatory")
_A3RipIpStaPolAddr_Type = IpAddress
_A3RipIpStaPolAddr_Object = MibTableColumn
a3RipIpStaPolAddr = _A3RipIpStaPolAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 7, 1, 2),
    _A3RipIpStaPolAddr_Type()
)
a3RipIpStaPolAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RipIpStaPolAddr.setStatus("mandatory")


class _A3RipIpStaPolMetric_Type(Integer32):
    """Custom type a3RipIpStaPolMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_A3RipIpStaPolMetric_Type.__name__ = "Integer32"
_A3RipIpStaPolMetric_Object = MibTableColumn
a3RipIpStaPolMetric = _A3RipIpStaPolMetric_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 7, 1, 3),
    _A3RipIpStaPolMetric_Type()
)
a3RipIpStaPolMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpStaPolMetric.setStatus("mandatory")
_A3RipIpStaPolStatus_Type = RowStatus
_A3RipIpStaPolStatus_Object = MibTableColumn
a3RipIpStaPolStatus = _A3RipIpStaPolStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 7, 1, 4),
    _A3RipIpStaPolStatus_Type()
)
a3RipIpStaPolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpStaPolStatus.setStatus("mandatory")
_A3RipIpNeighborTable_Object = MibTable
a3RipIpNeighborTable = _A3RipIpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 8)
)
if mibBuilder.loadTexts:
    a3RipIpNeighborTable.setStatus("mandatory")
_A3RipIpNeighborEntry_Object = MibTableRow
a3RipIpNeighborEntry = _A3RipIpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 8, 1)
)
a3RipIpNeighborEntry.setIndexNames(
    (0, "A3COM-RIP-IPEXTNS-R4-MIB", "a3RipIpNeighborPort"),
    (0, "A3COM-RIP-IPEXTNS-R4-MIB", "a3RipIpNeighborAddr"),
)
if mibBuilder.loadTexts:
    a3RipIpNeighborEntry.setStatus("mandatory")
_A3RipIpNeighborPort_Type = Integer32
_A3RipIpNeighborPort_Object = MibTableColumn
a3RipIpNeighborPort = _A3RipIpNeighborPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 8, 1, 1),
    _A3RipIpNeighborPort_Type()
)
a3RipIpNeighborPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RipIpNeighborPort.setStatus("mandatory")
_A3RipIpNeighborAddr_Type = IpAddress
_A3RipIpNeighborAddr_Object = MibTableColumn
a3RipIpNeighborAddr = _A3RipIpNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 8, 1, 2),
    _A3RipIpNeighborAddr_Type()
)
a3RipIpNeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RipIpNeighborAddr.setStatus("mandatory")
_A3RipIpNeighborStatus_Type = RowStatus
_A3RipIpNeighborStatus_Object = MibTableColumn
a3RipIpNeighborStatus = _A3RipIpNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 8, 1, 3),
    _A3RipIpNeighborStatus_Type()
)
a3RipIpNeighborStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpNeighborStatus.setStatus("mandatory")
_A3RipIpTrustedNbrTable_Object = MibTable
a3RipIpTrustedNbrTable = _A3RipIpTrustedNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 9)
)
if mibBuilder.loadTexts:
    a3RipIpTrustedNbrTable.setStatus("mandatory")
_A3RipIpTrustedNbrEntry_Object = MibTableRow
a3RipIpTrustedNbrEntry = _A3RipIpTrustedNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 9, 1)
)
a3RipIpTrustedNbrEntry.setIndexNames(
    (0, "A3COM-RIP-IPEXTNS-R4-MIB", "a3RipIpTrustedNbrPort"),
    (0, "A3COM-RIP-IPEXTNS-R4-MIB", "a3RipIpTrustedNbrAddr"),
)
if mibBuilder.loadTexts:
    a3RipIpTrustedNbrEntry.setStatus("mandatory")
_A3RipIpTrustedNbrPort_Type = Integer32
_A3RipIpTrustedNbrPort_Object = MibTableColumn
a3RipIpTrustedNbrPort = _A3RipIpTrustedNbrPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 9, 1, 1),
    _A3RipIpTrustedNbrPort_Type()
)
a3RipIpTrustedNbrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RipIpTrustedNbrPort.setStatus("mandatory")
_A3RipIpTrustedNbrAddr_Type = IpAddress
_A3RipIpTrustedNbrAddr_Object = MibTableColumn
a3RipIpTrustedNbrAddr = _A3RipIpTrustedNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 9, 1, 2),
    _A3RipIpTrustedNbrAddr_Type()
)
a3RipIpTrustedNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RipIpTrustedNbrAddr.setStatus("mandatory")
_A3RipIpTrustedNbrStatus_Type = RowStatus
_A3RipIpTrustedNbrStatus_Object = MibTableColumn
a3RipIpTrustedNbrStatus = _A3RipIpTrustedNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 9, 1, 3),
    _A3RipIpTrustedNbrStatus_Type()
)
a3RipIpTrustedNbrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpTrustedNbrStatus.setStatus("mandatory")
_A3RipIpImpMetTable_Object = MibTable
a3RipIpImpMetTable = _A3RipIpImpMetTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 10)
)
if mibBuilder.loadTexts:
    a3RipIpImpMetTable.setStatus("mandatory")
_A3RipIpImpMetEntry_Object = MibTableRow
a3RipIpImpMetEntry = _A3RipIpImpMetEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 10, 1)
)
a3RipIpImpMetEntry.setIndexNames(
    (0, "A3COM-RIP-IPEXTNS-R4-MIB", "a3RipIpImpMetProtocol"),
)
if mibBuilder.loadTexts:
    a3RipIpImpMetEntry.setStatus("mandatory")


class _A3RipIpImpMetProtocol_Type(Integer32):
    """Custom type a3RipIpImpMetProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 4),
          ("egp", 3),
          ("iisis", 2),
          ("ospf", 1),
          ("static", 5))
    )


_A3RipIpImpMetProtocol_Type.__name__ = "Integer32"
_A3RipIpImpMetProtocol_Object = MibTableColumn
a3RipIpImpMetProtocol = _A3RipIpImpMetProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 10, 1, 1),
    _A3RipIpImpMetProtocol_Type()
)
a3RipIpImpMetProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RipIpImpMetProtocol.setStatus("mandatory")


class _A3RipIpImpMetOperation_Type(Integer32):
    """Custom type a3RipIpImpMetOperation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("divide", 2),
          ("multiply", 1))
    )


_A3RipIpImpMetOperation_Type.__name__ = "Integer32"
_A3RipIpImpMetOperation_Object = MibTableColumn
a3RipIpImpMetOperation = _A3RipIpImpMetOperation_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 10, 1, 2),
    _A3RipIpImpMetOperation_Type()
)
a3RipIpImpMetOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpImpMetOperation.setStatus("mandatory")


class _A3RipIpImpMetOperand_Type(Integer32):
    """Custom type a3RipIpImpMetOperand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1073741823),
    )


_A3RipIpImpMetOperand_Type.__name__ = "Integer32"
_A3RipIpImpMetOperand_Object = MibTableColumn
a3RipIpImpMetOperand = _A3RipIpImpMetOperand_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 8, 10, 1, 3),
    _A3RipIpImpMetOperand_Type()
)
a3RipIpImpMetOperand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3RipIpImpMetOperand.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-RIP-IPEXTNS-R4-MIB",
    **{"RowStatus": RowStatus,
       "a3Com": a3Com,
       "brouterMIB": brouterMIB,
       "a3ComRipIp": a3ComRipIp,
       "a3RipIpUpdateTime": a3RipIpUpdateTime,
       "a3RipIpCtlTable": a3RipIpCtlTable,
       "a3RipIpCtlEntry": a3RipIpCtlEntry,
       "a3RipIpPortIndex": a3RipIpPortIndex,
       "a3RipIpTalkCtl": a3RipIpTalkCtl,
       "a3RipIpListenCtl": a3RipIpListenCtl,
       "a3RipIpTrustedNbrCtl": a3RipIpTrustedNbrCtl,
       "a3RipIpPoisonCtl": a3RipIpPoisonCtl,
       "a3RipIpTriggerCtl": a3RipIpTriggerCtl,
       "a3RipIpDefMetric": a3RipIpDefMetric,
       "a3RipIpExtPolCtl": a3RipIpExtPolCtl,
       "a3RipIpIntPolCtl": a3RipIpIntPolCtl,
       "a3RipIpNetPolCtl": a3RipIpNetPolCtl,
       "a3RipIpRcvPolCtl": a3RipIpRcvPolCtl,
       "a3RipIpStaPolCtl": a3RipIpStaPolCtl,
       "a3RipIpUnnAdvCtl": a3RipIpUnnAdvCtl,
       "a3RipIpBcastCtl": a3RipIpBcastCtl,
       "a3RipIpExtPolAllMet": a3RipIpExtPolAllMet,
       "a3RipIpIntPolAllMet": a3RipIpIntPolAllMet,
       "a3RipIpNetPolAllMet": a3RipIpNetPolAllMet,
       "a3RipIpRcvPolAllMet": a3RipIpRcvPolAllMet,
       "a3RipIpStaPolAllMet": a3RipIpStaPolAllMet,
       "a3RipIpDynNbrCtl": a3RipIpDynNbrCtl,
       "a3RipIpAggregateCtl": a3RipIpAggregateCtl,
       "a3RipIpDeAggregateCtl": a3RipIpDeAggregateCtl,
       "a3RipIpNBMAmodeCtl": a3RipIpNBMAmodeCtl,
       "a3RipIpExtPolTable": a3RipIpExtPolTable,
       "a3RipIpExtPolEntry": a3RipIpExtPolEntry,
       "a3RipIpExtPolPort": a3RipIpExtPolPort,
       "a3RipIpExtPolAddr": a3RipIpExtPolAddr,
       "a3RipIpExtPolMetric": a3RipIpExtPolMetric,
       "a3RipIpExtPolStatus": a3RipIpExtPolStatus,
       "a3RipIpIntPolTable": a3RipIpIntPolTable,
       "a3RipIpIntPolEntry": a3RipIpIntPolEntry,
       "a3RipIpIntPolPort": a3RipIpIntPolPort,
       "a3RipIpIntPolAddr": a3RipIpIntPolAddr,
       "a3RipIpIntPolMetric": a3RipIpIntPolMetric,
       "a3RipIpIntPolStatus": a3RipIpIntPolStatus,
       "a3RipIpNetPolTable": a3RipIpNetPolTable,
       "a3RipIpNetPolEntry": a3RipIpNetPolEntry,
       "a3RipIpNetPolPort": a3RipIpNetPolPort,
       "a3RipIpNetPolAddr": a3RipIpNetPolAddr,
       "a3RipIpNetPolMetric": a3RipIpNetPolMetric,
       "a3RipIpNetPolStatus": a3RipIpNetPolStatus,
       "a3RipIpRcvPolTable": a3RipIpRcvPolTable,
       "a3RipIpRcvPolEntry": a3RipIpRcvPolEntry,
       "a3RipIpRcvPolPort": a3RipIpRcvPolPort,
       "a3RipIpRcvPolAddr": a3RipIpRcvPolAddr,
       "a3RipIpRcvPolMetric": a3RipIpRcvPolMetric,
       "a3RipIpRcvPolStatus": a3RipIpRcvPolStatus,
       "a3RipIpStaPolTable": a3RipIpStaPolTable,
       "a3RipIpStaPolEntry": a3RipIpStaPolEntry,
       "a3RipIpStaPolPort": a3RipIpStaPolPort,
       "a3RipIpStaPolAddr": a3RipIpStaPolAddr,
       "a3RipIpStaPolMetric": a3RipIpStaPolMetric,
       "a3RipIpStaPolStatus": a3RipIpStaPolStatus,
       "a3RipIpNeighborTable": a3RipIpNeighborTable,
       "a3RipIpNeighborEntry": a3RipIpNeighborEntry,
       "a3RipIpNeighborPort": a3RipIpNeighborPort,
       "a3RipIpNeighborAddr": a3RipIpNeighborAddr,
       "a3RipIpNeighborStatus": a3RipIpNeighborStatus,
       "a3RipIpTrustedNbrTable": a3RipIpTrustedNbrTable,
       "a3RipIpTrustedNbrEntry": a3RipIpTrustedNbrEntry,
       "a3RipIpTrustedNbrPort": a3RipIpTrustedNbrPort,
       "a3RipIpTrustedNbrAddr": a3RipIpTrustedNbrAddr,
       "a3RipIpTrustedNbrStatus": a3RipIpTrustedNbrStatus,
       "a3RipIpImpMetTable": a3RipIpImpMetTable,
       "a3RipIpImpMetEntry": a3RipIpImpMetEntry,
       "a3RipIpImpMetProtocol": a3RipIpImpMetProtocol,
       "a3RipIpImpMetOperation": a3RipIpImpMetOperation,
       "a3RipIpImpMetOperand": a3RipIpImpMetOperand}
)
