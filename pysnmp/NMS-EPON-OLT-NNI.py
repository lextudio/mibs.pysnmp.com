# SNMP MIB module (NMS-EPON-OLT-NNI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-EPON-OLT-NNI
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:45 2024
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

(nmsEPONGroup,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsEPONGroup")

(TimeTicks,) = mibBuilder.importSymbols(
    "RFC1213-MIB",
    "TimeTicks")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsEponOltNni_ObjectIdentity = ObjectIdentity
nmsEponOltNni = _NmsEponOltNni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 8)
)
_NmseponoltnniTable_Object = MibTable
nmseponoltnniTable = _NmseponoltnniTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 8, 1)
)
if mibBuilder.loadTexts:
    nmseponoltnniTable.setStatus("mandatory")
_NmsEponOltNniEntry_Object = MibTableRow
nmsEponOltNniEntry = _NmsEponOltNniEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 8, 1, 1)
)
nmsEponOltNniEntry.setIndexNames(
    (0, "NMS-EPON-OLT-NNI", "nniIfIndex"),
)
if mibBuilder.loadTexts:
    nmsEponOltNniEntry.setStatus("mandatory")
_NniIfIndex_Type = Integer32
_NniIfIndex_Object = MibTableColumn
nniIfIndex = _NniIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 8, 1, 1, 1),
    _NniIfIndex_Type()
)
nniIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nniIfIndex.setStatus("mandatory")


class _IsRouter_Type(Integer32):
    """Custom type isRouter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("no", 0),
          ("static", 1))
    )


_IsRouter_Type.__name__ = "Integer32"
_IsRouter_Object = MibTableColumn
isRouter = _IsRouter_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 8, 1, 1, 2),
    _IsRouter_Type()
)
isRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isRouter.setStatus("mandatory")
_McstQuerierExpireTime_Type = TimeTicks
_McstQuerierExpireTime_Object = MibTableColumn
mcstQuerierExpireTime = _McstQuerierExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 8, 1, 1, 3),
    _McstQuerierExpireTime_Type()
)
mcstQuerierExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcstQuerierExpireTime.setStatus("mandatory")


class _IfDuplix_Type(Integer32):
    """Custom type ifDuplix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("full", 1),
          ("half", 2))
    )


_IfDuplix_Type.__name__ = "Integer32"
_IfDuplix_Object = MibTableColumn
ifDuplix = _IfDuplix_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 8, 1, 1, 4),
    _IfDuplix_Type()
)
ifDuplix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifDuplix.setStatus("mandatory")


class _NniIfSpeed_Type(Integer32):
    """Custom type nniIfSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("speed_10000m", 4),
          ("speed_1000m", 3),
          ("speed_100m", 2),
          ("speed_10m", 1))
    )


_NniIfSpeed_Type.__name__ = "Integer32"
_NniIfSpeed_Object = MibTableColumn
nniIfSpeed = _NniIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 8, 1, 1, 5),
    _NniIfSpeed_Type()
)
nniIfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nniIfSpeed.setStatus("mandatory")


class _NniIfFlowControl_Type(Integer32):
    """Custom type nniIfFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NniIfFlowControl_Type.__name__ = "Integer32"
_NniIfFlowControl_Object = MibTableColumn
nniIfFlowControl = _NniIfFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 8, 1, 1, 6),
    _NniIfFlowControl_Type()
)
nniIfFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nniIfFlowControl.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-EPON-OLT-NNI",
    **{"nmsEponOltNni": nmsEponOltNni,
       "nmseponoltnniTable": nmseponoltnniTable,
       "nmsEponOltNniEntry": nmsEponOltNniEntry,
       "nniIfIndex": nniIfIndex,
       "isRouter": isRouter,
       "mcstQuerierExpireTime": mcstQuerierExpireTime,
       "ifDuplix": ifDuplix,
       "nniIfSpeed": nniIfSpeed,
       "nniIfFlowControl": nniIfFlowControl}
)
