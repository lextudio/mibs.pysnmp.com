# SNMP MIB module (BIANCA-BRICK-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:44 2024
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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bintecsec_ObjectIdentity = ObjectIdentity
bintecsec = _Bintecsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 254)
)
_Radius_ObjectIdentity = ObjectIdentity
radius = _Radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 254, 8)
)
_RadiusServerTable_Object = MibTable
radiusServerTable = _RadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1)
)
if mibBuilder.loadTexts:
    radiusServerTable.setStatus("mandatory")
_RadiusServerEntry_Object = MibTableRow
radiusServerEntry = _RadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1)
)
radiusServerEntry.setIndexNames(
    (0, "BIANCA-BRICK-RADIUS-MIB", "radiusSrvProtocol"),
)
if mibBuilder.loadTexts:
    radiusServerEntry.setStatus("mandatory")


class _RadiusSrvProtocol_Type(Integer32):
    """Custom type radiusSrvProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 2),
          ("authentication", 1),
          ("login", 3))
    )


_RadiusSrvProtocol_Type.__name__ = "Integer32"
_RadiusSrvProtocol_Object = MibTableColumn
radiusSrvProtocol = _RadiusSrvProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 1),
    _RadiusSrvProtocol_Type()
)
radiusSrvProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvProtocol.setStatus("mandatory")
_RadiusSrvAddress_Type = IpAddress
_RadiusSrvAddress_Object = MibTableColumn
radiusSrvAddress = _RadiusSrvAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 2),
    _RadiusSrvAddress_Type()
)
radiusSrvAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvAddress.setStatus("mandatory")
_RadiusSrvPort_Type = Integer32
_RadiusSrvPort_Object = MibTableColumn
radiusSrvPort = _RadiusSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 3),
    _RadiusSrvPort_Type()
)
radiusSrvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvPort.setStatus("mandatory")
_RadiusSrvSecret_Type = DisplayString
_RadiusSrvSecret_Object = MibTableColumn
radiusSrvSecret = _RadiusSrvSecret_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 4),
    _RadiusSrvSecret_Type()
)
radiusSrvSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvSecret.setStatus("mandatory")


class _RadiusSrvPriority_Type(Integer32):
    """Custom type radiusSrvPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RadiusSrvPriority_Type.__name__ = "Integer32"
_RadiusSrvPriority_Object = MibTableColumn
radiusSrvPriority = _RadiusSrvPriority_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 5),
    _RadiusSrvPriority_Type()
)
radiusSrvPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvPriority.setStatus("mandatory")


class _RadiusSrvTimeout_Type(Integer32):
    """Custom type radiusSrvTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 50000),
    )


_RadiusSrvTimeout_Type.__name__ = "Integer32"
_RadiusSrvTimeout_Object = MibTableColumn
radiusSrvTimeout = _RadiusSrvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 6),
    _RadiusSrvTimeout_Type()
)
radiusSrvTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvTimeout.setStatus("mandatory")


class _RadiusSrvRetries_Type(Integer32):
    """Custom type radiusSrvRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RadiusSrvRetries_Type.__name__ = "Integer32"
_RadiusSrvRetries_Object = MibTableColumn
radiusSrvRetries = _RadiusSrvRetries_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 7),
    _RadiusSrvRetries_Type()
)
radiusSrvRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvRetries.setStatus("mandatory")


class _RadiusSrvState_Type(Integer32):
    """Custom type radiusSrvState based on Integer32"""
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
        *(("active", 1),
          ("delete", 4),
          ("disabled", 3),
          ("inactive", 2))
    )


_RadiusSrvState_Type.__name__ = "Integer32"
_RadiusSrvState_Object = MibTableColumn
radiusSrvState = _RadiusSrvState_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 8),
    _RadiusSrvState_Type()
)
radiusSrvState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvState.setStatus("mandatory")


class _RadiusSrvPolicy_Type(Integer32):
    """Custom type radiusSrvPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authoritative", 1),
          ("non-authoritative", 2))
    )


_RadiusSrvPolicy_Type.__name__ = "Integer32"
_RadiusSrvPolicy_Object = MibTableColumn
radiusSrvPolicy = _RadiusSrvPolicy_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 9),
    _RadiusSrvPolicy_Type()
)
radiusSrvPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvPolicy.setStatus("mandatory")


class _RadiusSrvValidate_Type(Integer32):
    """Custom type radiusSrvValidate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RadiusSrvValidate_Type.__name__ = "Integer32"
_RadiusSrvValidate_Object = MibTableColumn
radiusSrvValidate = _RadiusSrvValidate_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 10),
    _RadiusSrvValidate_Type()
)
radiusSrvValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvValidate.setStatus("mandatory")


class _RadiusSrvDialout_Type(Integer32):
    """Custom type radiusSrvDialout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("reload", 3))
    )


_RadiusSrvDialout_Type.__name__ = "Integer32"
_RadiusSrvDialout_Object = MibTableColumn
radiusSrvDialout = _RadiusSrvDialout_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 11),
    _RadiusSrvDialout_Type()
)
radiusSrvDialout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvDialout.setStatus("mandatory")
_RadiusSrvDefaultPW_Type = DisplayString
_RadiusSrvDefaultPW_Object = MibTableColumn
radiusSrvDefaultPW = _RadiusSrvDefaultPW_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 12),
    _RadiusSrvDefaultPW_Type()
)
radiusSrvDefaultPW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvDefaultPW.setStatus("mandatory")


class _RadiusSrvReloadInterval_Type(Integer32):
    """Custom type radiusSrvReloadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_RadiusSrvReloadInterval_Type.__name__ = "Integer32"
_RadiusSrvReloadInterval_Object = MibTableColumn
radiusSrvReloadInterval = _RadiusSrvReloadInterval_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 13),
    _RadiusSrvReloadInterval_Type()
)
radiusSrvReloadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvReloadInterval.setStatus("mandatory")
_RadiusSrvAuthRequests_Type = Counter32
_RadiusSrvAuthRequests_Object = MibTableColumn
radiusSrvAuthRequests = _RadiusSrvAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 14),
    _RadiusSrvAuthRequests_Type()
)
radiusSrvAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSrvAuthRequests.setStatus("mandatory")
_RadiusSrvAuthAccepts_Type = Counter32
_RadiusSrvAuthAccepts_Object = MibTableColumn
radiusSrvAuthAccepts = _RadiusSrvAuthAccepts_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 15),
    _RadiusSrvAuthAccepts_Type()
)
radiusSrvAuthAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSrvAuthAccepts.setStatus("mandatory")
_RadiusSrvAuthRejects_Type = Counter32
_RadiusSrvAuthRejects_Object = MibTableColumn
radiusSrvAuthRejects = _RadiusSrvAuthRejects_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 16),
    _RadiusSrvAuthRejects_Type()
)
radiusSrvAuthRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSrvAuthRejects.setStatus("mandatory")
_RadiusSrvAuthReqRetrans_Type = Counter32
_RadiusSrvAuthReqRetrans_Object = MibTableColumn
radiusSrvAuthReqRetrans = _RadiusSrvAuthReqRetrans_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 17),
    _RadiusSrvAuthReqRetrans_Type()
)
radiusSrvAuthReqRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSrvAuthReqRetrans.setStatus("mandatory")
_RadiusSrvAuthReqFailed_Type = Counter32
_RadiusSrvAuthReqFailed_Object = MibTableColumn
radiusSrvAuthReqFailed = _RadiusSrvAuthReqFailed_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 18),
    _RadiusSrvAuthReqFailed_Type()
)
radiusSrvAuthReqFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSrvAuthReqFailed.setStatus("mandatory")
_RadiusSrvAuthReqPending_Type = Counter32
_RadiusSrvAuthReqPending_Object = MibTableColumn
radiusSrvAuthReqPending = _RadiusSrvAuthReqPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 19),
    _RadiusSrvAuthReqPending_Type()
)
radiusSrvAuthReqPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSrvAuthReqPending.setStatus("mandatory")
_RadiusSrvAcctStarts_Type = Counter32
_RadiusSrvAcctStarts_Object = MibTableColumn
radiusSrvAcctStarts = _RadiusSrvAcctStarts_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 20),
    _RadiusSrvAcctStarts_Type()
)
radiusSrvAcctStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSrvAcctStarts.setStatus("mandatory")
_RadiusSrvAcctStops_Type = Counter32
_RadiusSrvAcctStops_Object = MibTableColumn
radiusSrvAcctStops = _RadiusSrvAcctStops_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 21),
    _RadiusSrvAcctStops_Type()
)
radiusSrvAcctStops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSrvAcctStops.setStatus("mandatory")


class _RadiusSrvKeepalive_Type(Integer32):
    """Custom type radiusSrvKeepalive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RadiusSrvKeepalive_Type.__name__ = "Integer32"
_RadiusSrvKeepalive_Object = MibTableColumn
radiusSrvKeepalive = _RadiusSrvKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 22),
    _RadiusSrvKeepalive_Type()
)
radiusSrvKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSrvKeepalive.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-RADIUS-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bintecsec": bintecsec,
       "radius": radius,
       "radiusServerTable": radiusServerTable,
       "radiusServerEntry": radiusServerEntry,
       "radiusSrvProtocol": radiusSrvProtocol,
       "radiusSrvAddress": radiusSrvAddress,
       "radiusSrvPort": radiusSrvPort,
       "radiusSrvSecret": radiusSrvSecret,
       "radiusSrvPriority": radiusSrvPriority,
       "radiusSrvTimeout": radiusSrvTimeout,
       "radiusSrvRetries": radiusSrvRetries,
       "radiusSrvState": radiusSrvState,
       "radiusSrvPolicy": radiusSrvPolicy,
       "radiusSrvValidate": radiusSrvValidate,
       "radiusSrvDialout": radiusSrvDialout,
       "radiusSrvDefaultPW": radiusSrvDefaultPW,
       "radiusSrvReloadInterval": radiusSrvReloadInterval,
       "radiusSrvAuthRequests": radiusSrvAuthRequests,
       "radiusSrvAuthAccepts": radiusSrvAuthAccepts,
       "radiusSrvAuthRejects": radiusSrvAuthRejects,
       "radiusSrvAuthReqRetrans": radiusSrvAuthReqRetrans,
       "radiusSrvAuthReqFailed": radiusSrvAuthReqFailed,
       "radiusSrvAuthReqPending": radiusSrvAuthReqPending,
       "radiusSrvAcctStarts": radiusSrvAcctStarts,
       "radiusSrvAcctStops": radiusSrvAcctStops,
       "radiusSrvKeepalive": radiusSrvKeepalive}
)
