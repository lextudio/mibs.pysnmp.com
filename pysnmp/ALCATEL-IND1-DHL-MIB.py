# SNMP MIB module (ALCATEL-IND1-DHL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-DHL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:53 2024
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

(softentIND1DHL,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1DHL")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1DHLMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1DHLMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1DHLMIBNotifications = _AlcatelIND1DHLMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1DHLMIBNotifications.setStatus("current")
_AlcatelIND1DHLMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1DHLMIBObjects = _AlcatelIND1DHLMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1DHLMIBObjects.setStatus("current")
_AlaDHLSessionConfig_ObjectIdentity = ObjectIdentity
alaDHLSessionConfig = _AlaDHLSessionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 1)
)
_AlaDHLSessionTable_Object = MibTable
alaDHLSessionTable = _AlaDHLSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaDHLSessionTable.setStatus("current")
_AlaDHLSessionEntry_Object = MibTableRow
alaDHLSessionEntry = _AlaDHLSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 1, 1, 1)
)
alaDHLSessionEntry.setIndexNames(
    (0, "ALCATEL-IND1-DHL-MIB", "alaDHLSessionIndex"),
)
if mibBuilder.loadTexts:
    alaDHLSessionEntry.setStatus("current")


class _AlaDHLSessionIndex_Type(Integer32):
    """Custom type alaDHLSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AlaDHLSessionIndex_Type.__name__ = "Integer32"
_AlaDHLSessionIndex_Object = MibTableColumn
alaDHLSessionIndex = _AlaDHLSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 1, 1, 1, 1),
    _AlaDHLSessionIndex_Type()
)
alaDHLSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHLSessionIndex.setStatus("current")
_AlaDHLSessionDescr_Type = SnmpAdminString
_AlaDHLSessionDescr_Object = MibTableColumn
alaDHLSessionDescr = _AlaDHLSessionDescr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 1, 1, 1, 2),
    _AlaDHLSessionDescr_Type()
)
alaDHLSessionDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHLSessionDescr.setStatus("current")


class _AlaDHLSessionAdminStatus_Type(Integer32):
    """Custom type alaDHLSessionAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AlaDHLSessionAdminStatus_Type.__name__ = "Integer32"
_AlaDHLSessionAdminStatus_Object = MibTableColumn
alaDHLSessionAdminStatus = _AlaDHLSessionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 1, 1, 1, 3),
    _AlaDHLSessionAdminStatus_Type()
)
alaDHLSessionAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHLSessionAdminStatus.setStatus("current")


class _AlaDHLSessionOperStatus_Type(Integer32):
    """Custom type alaDHLSessionOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AlaDHLSessionOperStatus_Type.__name__ = "Integer32"
_AlaDHLSessionOperStatus_Object = MibTableColumn
alaDHLSessionOperStatus = _AlaDHLSessionOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 1, 1, 1, 4),
    _AlaDHLSessionOperStatus_Type()
)
alaDHLSessionOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHLSessionOperStatus.setStatus("current")


class _AlaDHLSessionPreemptionTime_Type(Integer32):
    """Custom type alaDHLSessionPreemptionTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AlaDHLSessionPreemptionTime_Type.__name__ = "Integer32"
_AlaDHLSessionPreemptionTime_Object = MibTableColumn
alaDHLSessionPreemptionTime = _AlaDHLSessionPreemptionTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 1, 1, 1, 5),
    _AlaDHLSessionPreemptionTime_Type()
)
alaDHLSessionPreemptionTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHLSessionPreemptionTime.setStatus("current")
if mibBuilder.loadTexts:
    alaDHLSessionPreemptionTime.setUnits("seconds")


class _AlaDHLSessionAdminMacFlushing_Type(Integer32):
    """Custom type alaDHLSessionAdminMacFlushing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mvrp", 3),
          ("none", 1),
          ("raw", 2))
    )


_AlaDHLSessionAdminMacFlushing_Type.__name__ = "Integer32"
_AlaDHLSessionAdminMacFlushing_Object = MibTableColumn
alaDHLSessionAdminMacFlushing = _AlaDHLSessionAdminMacFlushing_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 1, 1, 1, 6),
    _AlaDHLSessionAdminMacFlushing_Type()
)
alaDHLSessionAdminMacFlushing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHLSessionAdminMacFlushing.setStatus("current")


class _AlaDHLSessionActiveMacFlushing_Type(Integer32):
    """Custom type alaDHLSessionActiveMacFlushing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mvrp", 3),
          ("none", 1),
          ("raw", 2))
    )


_AlaDHLSessionActiveMacFlushing_Type.__name__ = "Integer32"
_AlaDHLSessionActiveMacFlushing_Object = MibTableColumn
alaDHLSessionActiveMacFlushing = _AlaDHLSessionActiveMacFlushing_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 1, 1, 1, 7),
    _AlaDHLSessionActiveMacFlushing_Type()
)
alaDHLSessionActiveMacFlushing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHLSessionActiveMacFlushing.setStatus("current")
_AlaDHLSessionRowStatus_Type = RowStatus
_AlaDHLSessionRowStatus_Object = MibTableColumn
alaDHLSessionRowStatus = _AlaDHLSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 1, 1, 1, 8),
    _AlaDHLSessionRowStatus_Type()
)
alaDHLSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHLSessionRowStatus.setStatus("current")
_AlaDHLLinksConfig_ObjectIdentity = ObjectIdentity
alaDHLLinksConfig = _AlaDHLLinksConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 2)
)
_AlaDHLLinksTable_Object = MibTable
alaDHLLinksTable = _AlaDHLLinksTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaDHLLinksTable.setStatus("current")
_AlaDHLLinksEntry_Object = MibTableRow
alaDHLLinksEntry = _AlaDHLLinksEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 2, 1, 1)
)
alaDHLLinksEntry.setIndexNames(
    (0, "ALCATEL-IND1-DHL-MIB", "alaDHLSessionIndex"),
    (0, "ALCATEL-IND1-DHL-MIB", "alaDHLLinkslinkA"),
    (0, "ALCATEL-IND1-DHL-MIB", "alaDHLLinkslinkB"),
)
if mibBuilder.loadTexts:
    alaDHLLinksEntry.setStatus("current")
_AlaDHLLinkslinkA_Type = InterfaceIndex
_AlaDHLLinkslinkA_Object = MibTableColumn
alaDHLLinkslinkA = _AlaDHLLinkslinkA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 2, 1, 1, 1),
    _AlaDHLLinkslinkA_Type()
)
alaDHLLinkslinkA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHLLinkslinkA.setStatus("current")
_AlaDHLLinkslinkB_Type = InterfaceIndex
_AlaDHLLinkslinkB_Object = MibTableColumn
alaDHLLinkslinkB = _AlaDHLLinkslinkB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 2, 1, 1, 2),
    _AlaDHLLinkslinkB_Type()
)
alaDHLLinkslinkB.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHLLinkslinkB.setStatus("current")


class _AlaDHLLinkslinkAOperStatus_Type(Integer32):
    """Custom type alaDHLLinkslinkAOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AlaDHLLinkslinkAOperStatus_Type.__name__ = "Integer32"
_AlaDHLLinkslinkAOperStatus_Object = MibTableColumn
alaDHLLinkslinkAOperStatus = _AlaDHLLinkslinkAOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 2, 1, 1, 3),
    _AlaDHLLinkslinkAOperStatus_Type()
)
alaDHLLinkslinkAOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHLLinkslinkAOperStatus.setStatus("current")


class _AlaDHLLinkslinkBOperStatus_Type(Integer32):
    """Custom type alaDHLLinkslinkBOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AlaDHLLinkslinkBOperStatus_Type.__name__ = "Integer32"
_AlaDHLLinkslinkBOperStatus_Object = MibTableColumn
alaDHLLinkslinkBOperStatus = _AlaDHLLinkslinkBOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 2, 1, 1, 4),
    _AlaDHLLinkslinkBOperStatus_Type()
)
alaDHLLinkslinkBOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHLLinkslinkBOperStatus.setStatus("current")
_AlaDHLLinksRowStatus_Type = RowStatus
_AlaDHLLinksRowStatus_Object = MibTableColumn
alaDHLLinksRowStatus = _AlaDHLLinksRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 2, 1, 1, 5),
    _AlaDHLLinksRowStatus_Type()
)
alaDHLLinksRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHLLinksRowStatus.setStatus("current")
_AlaDHLVpa_ObjectIdentity = ObjectIdentity
alaDHLVpa = _AlaDHLVpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 3)
)
_AlaDHLVpaTable_Object = MibTable
alaDHLVpaTable = _AlaDHLVpaTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaDHLVpaTable.setStatus("current")
_AlaDHLVpaEntry_Object = MibTableRow
alaDHLVpaEntry = _AlaDHLVpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 3, 1, 1)
)
alaDHLVpaEntry.setIndexNames(
    (0, "ALCATEL-IND1-DHL-MIB", "alaDHLSessionIndex"),
    (0, "ALCATEL-IND1-DHL-MIB", "alaDHLVpalink"),
    (0, "ALCATEL-IND1-DHL-MIB", "alaDHLVpaVlan"),
)
if mibBuilder.loadTexts:
    alaDHLVpaEntry.setStatus("current")
_AlaDHLVpalink_Type = InterfaceIndex
_AlaDHLVpalink_Object = MibTableColumn
alaDHLVpalink = _AlaDHLVpalink_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 3, 1, 1, 1),
    _AlaDHLVpalink_Type()
)
alaDHLVpalink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHLVpalink.setStatus("current")


class _AlaDHLVpaVlan_Type(Integer32):
    """Custom type alaDHLVpaVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDHLVpaVlan_Type.__name__ = "Integer32"
_AlaDHLVpaVlan_Object = MibTableColumn
alaDHLVpaVlan = _AlaDHLVpaVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 3, 1, 1, 2),
    _AlaDHLVpaVlan_Type()
)
alaDHLVpaVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHLVpaVlan.setStatus("current")


class _AlaDHLVpaVlanType_Type(Integer32):
    """Custom type alaDHLVpaVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protectedVlan", 1),
          ("unprotectedVlan", 2))
    )


_AlaDHLVpaVlanType_Type.__name__ = "Integer32"
_AlaDHLVpaVlanType_Object = MibTableColumn
alaDHLVpaVlanType = _AlaDHLVpaVlanType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 3, 1, 1, 3),
    _AlaDHLVpaVlanType_Type()
)
alaDHLVpaVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHLVpaVlanType.setStatus("current")
_AlaDHLVpaActiveLink_Type = InterfaceIndex
_AlaDHLVpaActiveLink_Object = MibTableColumn
alaDHLVpaActiveLink = _AlaDHLVpaActiveLink_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 3, 1, 1, 4),
    _AlaDHLVpaActiveLink_Type()
)
alaDHLVpaActiveLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHLVpaActiveLink.setStatus("current")
_AlaDHLVlanMap_ObjectIdentity = ObjectIdentity
alaDHLVlanMap = _AlaDHLVlanMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 4)
)
_AlaDHLVlanMapTable_Object = MibTable
alaDHLVlanMapTable = _AlaDHLVlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alaDHLVlanMapTable.setStatus("current")
_AlaDHLVlanMapEntry_Object = MibTableRow
alaDHLVlanMapEntry = _AlaDHLVlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 4, 1, 1)
)
alaDHLVlanMapEntry.setIndexNames(
    (0, "ALCATEL-IND1-DHL-MIB", "alaDHLSessionIndex"),
    (0, "ALCATEL-IND1-DHL-MIB", "alaDHLVlanMapVlanStart"),
    (0, "ALCATEL-IND1-DHL-MIB", "alaDHLVlanMapVlanEnd"),
)
if mibBuilder.loadTexts:
    alaDHLVlanMapEntry.setStatus("current")


class _AlaDHLVlanMapVlanStart_Type(Integer32):
    """Custom type alaDHLVlanMapVlanStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDHLVlanMapVlanStart_Type.__name__ = "Integer32"
_AlaDHLVlanMapVlanStart_Object = MibTableColumn
alaDHLVlanMapVlanStart = _AlaDHLVlanMapVlanStart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 4, 1, 1, 1),
    _AlaDHLVlanMapVlanStart_Type()
)
alaDHLVlanMapVlanStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHLVlanMapVlanStart.setStatus("current")


class _AlaDHLVlanMapVlanEnd_Type(Integer32):
    """Custom type alaDHLVlanMapVlanEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDHLVlanMapVlanEnd_Type.__name__ = "Integer32"
_AlaDHLVlanMapVlanEnd_Object = MibTableColumn
alaDHLVlanMapVlanEnd = _AlaDHLVlanMapVlanEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 4, 1, 1, 2),
    _AlaDHLVlanMapVlanEnd_Type()
)
alaDHLVlanMapVlanEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHLVlanMapVlanEnd.setStatus("current")
_AlaDHLVlanMapRowStatus_Type = RowStatus
_AlaDHLVlanMapRowStatus_Object = MibTableColumn
alaDHLVlanMapRowStatus = _AlaDHLVlanMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 4, 1, 1, 3),
    _AlaDHLVlanMapRowStatus_Type()
)
alaDHLVlanMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHLVlanMapRowStatus.setStatus("current")
_AlaDHLTrapsObj_ObjectIdentity = ObjectIdentity
alaDHLTrapsObj = _AlaDHLTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 5)
)
_AlaDHLSessionID_Type = Integer32
_AlaDHLSessionID_Object = MibScalar
alaDHLSessionID = _AlaDHLSessionID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 5, 1),
    _AlaDHLSessionID_Type()
)
alaDHLSessionID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDHLSessionID.setStatus("current")
_AlaDHLPortFrom_Type = InterfaceIndex
_AlaDHLPortFrom_Object = MibScalar
alaDHLPortFrom = _AlaDHLPortFrom_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 5, 2),
    _AlaDHLPortFrom_Type()
)
alaDHLPortFrom.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDHLPortFrom.setStatus("current")
_AlaDHLPortTo_Type = InterfaceIndex
_AlaDHLPortTo_Object = MibScalar
alaDHLPortTo = _AlaDHLPortTo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 5, 3),
    _AlaDHLPortTo_Type()
)
alaDHLPortTo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDHLPortTo.setStatus("current")


class _AlaDHLVlanMoveReason_Type(Integer32):
    """Custom type alaDHLVlanMoveReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_AlaDHLVlanMoveReason_Type.__name__ = "Integer32"
_AlaDHLVlanMoveReason_Object = MibScalar
alaDHLVlanMoveReason = _AlaDHLVlanMoveReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 1, 5, 4),
    _AlaDHLVlanMoveReason_Type()
)
alaDHLVlanMoveReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDHLVlanMoveReason.setStatus("current")
_AlcatelIND1DHLMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1DHLMIBConformance = _AlcatelIND1DHLMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1DHLMIBConformance.setStatus("current")
_AlcatelIND1DHLMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1DHLMIBGroups = _AlcatelIND1DHLMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1DHLMIBGroups.setStatus("current")
_AlcatelIND1DHLMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1DHLMIBCompliances = _AlcatelIND1DHLMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1DHLMIBCompliances.setStatus("current")

# Managed Objects groups

alaDHLSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 2, 1, 1)
)
alaDHLSessionGroup.setObjects(
      *(("ALCATEL-IND1-DHL-MIB", "alaDHLSessionDescr"),
        ("ALCATEL-IND1-DHL-MIB", "alaDHLSessionAdminStatus"),
        ("ALCATEL-IND1-DHL-MIB", "alaDHLSessionOperStatus"),
        ("ALCATEL-IND1-DHL-MIB", "alaDHLSessionPreemptionTime"),
        ("ALCATEL-IND1-DHL-MIB", "alaDHLSessionAdminMacFlushing"),
        ("ALCATEL-IND1-DHL-MIB", "alaDHLSessionActiveMacFlushing"),
        ("ALCATEL-IND1-DHL-MIB", "alaDHLSessionRowStatus"))
)
if mibBuilder.loadTexts:
    alaDHLSessionGroup.setStatus("current")

alaDHLLinksGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 2, 1, 2)
)
alaDHLLinksGroup.setObjects(
      *(("ALCATEL-IND1-DHL-MIB", "alaDHLLinkslinkAOperStatus"),
        ("ALCATEL-IND1-DHL-MIB", "alaDHLLinkslinkBOperStatus"),
        ("ALCATEL-IND1-DHL-MIB", "alaDHLLinksRowStatus"))
)
if mibBuilder.loadTexts:
    alaDHLLinksGroup.setStatus("current")

alaDHLVpaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 2, 1, 3)
)
alaDHLVpaGroup.setObjects(
      *(("ALCATEL-IND1-DHL-MIB", "alaDHLVpaVlanType"),
        ("ALCATEL-IND1-DHL-MIB", "alaDHLVpaActiveLink"))
)
if mibBuilder.loadTexts:
    alaDHLVpaGroup.setStatus("current")

alaDHLVlanMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 2, 1, 4)
)
alaDHLVlanMapGroup.setObjects(
    ("ALCATEL-IND1-DHL-MIB", "alaDHLVlanMapRowStatus")
)
if mibBuilder.loadTexts:
    alaDHLVlanMapGroup.setStatus("current")

alaDHLNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 2, 1, 5)
)
alaDHLNotificationObjectGroup.setObjects(
      *(("ALCATEL-IND1-DHL-MIB", "alaDHLSessionID"),
        ("ALCATEL-IND1-DHL-MIB", "alaDHLPortFrom"),
        ("ALCATEL-IND1-DHL-MIB", "alaDHLPortTo"),
        ("ALCATEL-IND1-DHL-MIB", "alaDHLVlanMoveReason"))
)
if mibBuilder.loadTexts:
    alaDHLNotificationObjectGroup.setStatus("current")


# Notification objects

alaDHLVlanMoveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 0, 1)
)
alaDHLVlanMoveTrap.setObjects(
      *(("ALCATEL-IND1-DHL-MIB", "alaDHLSessionID"),
        ("ALCATEL-IND1-DHL-MIB", "alaDHLPortFrom"),
        ("ALCATEL-IND1-DHL-MIB", "alaDHLPortTo"),
        ("ALCATEL-IND1-DHL-MIB", "alaDHLVlanMoveReason"))
)
if mibBuilder.loadTexts:
    alaDHLVlanMoveTrap.setStatus(
        "current"
    )


# Notifications groups

alaDHLNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 2, 1, 6)
)
alaDHLNotificationGroup.setObjects(
    ("ALCATEL-IND1-DHL-MIB", "alaDHLVlanMoveTrap")
)
if mibBuilder.loadTexts:
    alaDHLNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1DHLMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1DHLMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-DHL-MIB",
    **{"alcatelIND1DHLMIB": alcatelIND1DHLMIB,
       "alcatelIND1DHLMIBNotifications": alcatelIND1DHLMIBNotifications,
       "alaDHLVlanMoveTrap": alaDHLVlanMoveTrap,
       "alcatelIND1DHLMIBObjects": alcatelIND1DHLMIBObjects,
       "alaDHLSessionConfig": alaDHLSessionConfig,
       "alaDHLSessionTable": alaDHLSessionTable,
       "alaDHLSessionEntry": alaDHLSessionEntry,
       "alaDHLSessionIndex": alaDHLSessionIndex,
       "alaDHLSessionDescr": alaDHLSessionDescr,
       "alaDHLSessionAdminStatus": alaDHLSessionAdminStatus,
       "alaDHLSessionOperStatus": alaDHLSessionOperStatus,
       "alaDHLSessionPreemptionTime": alaDHLSessionPreemptionTime,
       "alaDHLSessionAdminMacFlushing": alaDHLSessionAdminMacFlushing,
       "alaDHLSessionActiveMacFlushing": alaDHLSessionActiveMacFlushing,
       "alaDHLSessionRowStatus": alaDHLSessionRowStatus,
       "alaDHLLinksConfig": alaDHLLinksConfig,
       "alaDHLLinksTable": alaDHLLinksTable,
       "alaDHLLinksEntry": alaDHLLinksEntry,
       "alaDHLLinkslinkA": alaDHLLinkslinkA,
       "alaDHLLinkslinkB": alaDHLLinkslinkB,
       "alaDHLLinkslinkAOperStatus": alaDHLLinkslinkAOperStatus,
       "alaDHLLinkslinkBOperStatus": alaDHLLinkslinkBOperStatus,
       "alaDHLLinksRowStatus": alaDHLLinksRowStatus,
       "alaDHLVpa": alaDHLVpa,
       "alaDHLVpaTable": alaDHLVpaTable,
       "alaDHLVpaEntry": alaDHLVpaEntry,
       "alaDHLVpalink": alaDHLVpalink,
       "alaDHLVpaVlan": alaDHLVpaVlan,
       "alaDHLVpaVlanType": alaDHLVpaVlanType,
       "alaDHLVpaActiveLink": alaDHLVpaActiveLink,
       "alaDHLVlanMap": alaDHLVlanMap,
       "alaDHLVlanMapTable": alaDHLVlanMapTable,
       "alaDHLVlanMapEntry": alaDHLVlanMapEntry,
       "alaDHLVlanMapVlanStart": alaDHLVlanMapVlanStart,
       "alaDHLVlanMapVlanEnd": alaDHLVlanMapVlanEnd,
       "alaDHLVlanMapRowStatus": alaDHLVlanMapRowStatus,
       "alaDHLTrapsObj": alaDHLTrapsObj,
       "alaDHLSessionID": alaDHLSessionID,
       "alaDHLPortFrom": alaDHLPortFrom,
       "alaDHLPortTo": alaDHLPortTo,
       "alaDHLVlanMoveReason": alaDHLVlanMoveReason,
       "alcatelIND1DHLMIBConformance": alcatelIND1DHLMIBConformance,
       "alcatelIND1DHLMIBGroups": alcatelIND1DHLMIBGroups,
       "alaDHLSessionGroup": alaDHLSessionGroup,
       "alaDHLLinksGroup": alaDHLLinksGroup,
       "alaDHLVpaGroup": alaDHLVpaGroup,
       "alaDHLVlanMapGroup": alaDHLVlanMapGroup,
       "alaDHLNotificationObjectGroup": alaDHLNotificationObjectGroup,
       "alaDHLNotificationGroup": alaDHLNotificationGroup,
       "alcatelIND1DHLMIBCompliances": alcatelIND1DHLMIBCompliances,
       "alcatelIND1DHLMIBCompliance": alcatelIND1DHLMIBCompliance}
)
