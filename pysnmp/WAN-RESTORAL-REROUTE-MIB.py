# SNMP MIB module (WAN-RESTORAL-REROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WAN-RESTORAL-REROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:28 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbmWanRestoralRerouteMIB_ObjectIdentity = ObjectIdentity
ibmWanRestoralRerouteMIB = _IbmWanRestoralRerouteMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11)
)
_IbmWanRestoral_ObjectIdentity = ObjectIdentity
ibmWanRestoral = _IbmWanRestoral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1)
)
_IbmWanRestoralTable_Object = MibTable
ibmWanRestoralTable = _IbmWanRestoralTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1)
)
if mibBuilder.loadTexts:
    ibmWanRestoralTable.setStatus("mandatory")
_IbmWanRestoralEntry_Object = MibTableRow
ibmWanRestoralEntry = _IbmWanRestoralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1)
)
ibmWanRestoralEntry.setIndexNames(
    (0, "WAN-RESTORAL-REROUTE-MIB", "ibmwrsPriNetifIndex"),
)
if mibBuilder.loadTexts:
    ibmWanRestoralEntry.setStatus("mandatory")
_IbmwrsPriNetifIndex_Type = Integer32
_IbmwrsPriNetifIndex_Object = MibTableColumn
ibmwrsPriNetifIndex = _IbmwrsPriNetifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1, 1),
    _IbmwrsPriNetifIndex_Type()
)
ibmwrsPriNetifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrsPriNetifIndex.setStatus("mandatory")
_IbmwrsSecNetifIndex_Type = Integer32
_IbmwrsSecNetifIndex_Object = MibTableColumn
ibmwrsSecNetifIndex = _IbmwrsSecNetifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1, 2),
    _IbmwrsSecNetifIndex_Type()
)
ibmwrsSecNetifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrsSecNetifIndex.setStatus("mandatory")


class _IbmwrsEnabled_Type(Integer32):
    """Custom type ibmwrsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmwrsEnabled_Type.__name__ = "Integer32"
_IbmwrsEnabled_Object = MibTableColumn
ibmwrsEnabled = _IbmwrsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1, 3),
    _IbmwrsEnabled_Type()
)
ibmwrsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrsEnabled.setStatus("mandatory")


class _IbmwrsActive_Type(Integer32):
    """Custom type ibmwrsActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmwrsActive_Type.__name__ = "Integer32"
_IbmwrsActive_Object = MibTableColumn
ibmwrsActive = _IbmwrsActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1, 4),
    _IbmwrsActive_Type()
)
ibmwrsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrsActive.setStatus("mandatory")
_IbmwrsDuration_Type = TimeTicks
_IbmwrsDuration_Object = MibTableColumn
ibmwrsDuration = _IbmwrsDuration_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1, 5),
    _IbmwrsDuration_Type()
)
ibmwrsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrsDuration.setStatus("mandatory")
_IbmwrsAttempts_Type = Counter32
_IbmwrsAttempts_Object = MibTableColumn
ibmwrsAttempts = _IbmwrsAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1, 6),
    _IbmwrsAttempts_Type()
)
ibmwrsAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrsAttempts.setStatus("mandatory")
_IbmwrsActuals_Type = Counter32
_IbmwrsActuals_Object = MibTableColumn
ibmwrsActuals = _IbmwrsActuals_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1, 7),
    _IbmwrsActuals_Type()
)
ibmwrsActuals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrsActuals.setStatus("mandatory")
_IbmwrsFwdPkts_Type = Counter32
_IbmwrsFwdPkts_Object = MibTableColumn
ibmwrsFwdPkts = _IbmwrsFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1, 8),
    _IbmwrsFwdPkts_Type()
)
ibmwrsFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrsFwdPkts.setStatus("mandatory")
_IbmWanReroute_ObjectIdentity = ObjectIdentity
ibmWanReroute = _IbmWanReroute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2)
)
_IbmWanRerouteTable_Object = MibTable
ibmWanRerouteTable = _IbmWanRerouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1)
)
if mibBuilder.loadTexts:
    ibmWanRerouteTable.setStatus("mandatory")
_IbmWanRerouteEntry_Object = MibTableRow
ibmWanRerouteEntry = _IbmWanRerouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1)
)
ibmWanRerouteEntry.setIndexNames(
    (0, "WAN-RESTORAL-REROUTE-MIB", "ibmwrrPriNetifIndex"),
)
if mibBuilder.loadTexts:
    ibmWanRerouteEntry.setStatus("mandatory")
_IbmwrrPriNetifIndex_Type = Integer32
_IbmwrrPriNetifIndex_Object = MibTableColumn
ibmwrrPriNetifIndex = _IbmwrrPriNetifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 1),
    _IbmwrrPriNetifIndex_Type()
)
ibmwrrPriNetifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrrPriNetifIndex.setStatus("mandatory")
_IbmwrrAltNetifIndex_Type = Integer32
_IbmwrrAltNetifIndex_Object = MibTableColumn
ibmwrrAltNetifIndex = _IbmwrrAltNetifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 2),
    _IbmwrrAltNetifIndex_Type()
)
ibmwrrAltNetifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrrAltNetifIndex.setStatus("mandatory")


class _IbmwrrEnabled_Type(Integer32):
    """Custom type ibmwrrEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmwrrEnabled_Type.__name__ = "Integer32"
_IbmwrrEnabled_Object = MibTableColumn
ibmwrrEnabled = _IbmwrrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 3),
    _IbmwrrEnabled_Type()
)
ibmwrrEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrrEnabled.setStatus("mandatory")


class _IbmwrrActive_Type(Integer32):
    """Custom type ibmwrrActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmwrrActive_Type.__name__ = "Integer32"
_IbmwrrActive_Object = MibTableColumn
ibmwrrActive = _IbmwrrActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 4),
    _IbmwrrActive_Type()
)
ibmwrrActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrrActive.setStatus("mandatory")
_IbmwrrDuration_Type = TimeTicks
_IbmwrrDuration_Object = MibTableColumn
ibmwrrDuration = _IbmwrrDuration_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 5),
    _IbmwrrDuration_Type()
)
ibmwrrDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrrDuration.setStatus("mandatory")
_IbmwrrAttempts_Type = Counter32
_IbmwrrAttempts_Object = MibTableColumn
ibmwrrAttempts = _IbmwrrAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 6),
    _IbmwrrAttempts_Type()
)
ibmwrrAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrrAttempts.setStatus("mandatory")
_IbmwrrActuals_Type = Counter32
_IbmwrrActuals_Object = MibTableColumn
ibmwrrActuals = _IbmwrrActuals_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 7),
    _IbmwrrActuals_Type()
)
ibmwrrActuals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrrActuals.setStatus("mandatory")


class _IbmwrrOverflowEnabled_Type(Integer32):
    """Custom type ibmwrrOverflowEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmwrrOverflowEnabled_Type.__name__ = "Integer32"
_IbmwrrOverflowEnabled_Object = MibTableColumn
ibmwrrOverflowEnabled = _IbmwrrOverflowEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 8),
    _IbmwrrOverflowEnabled_Type()
)
ibmwrrOverflowEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrrOverflowEnabled.setStatus("mandatory")


class _IbmwrrOverflowActive_Type(Integer32):
    """Custom type ibmwrrOverflowActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmwrrOverflowActive_Type.__name__ = "Integer32"
_IbmwrrOverflowActive_Object = MibTableColumn
ibmwrrOverflowActive = _IbmwrrOverflowActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 9),
    _IbmwrrOverflowActive_Type()
)
ibmwrrOverflowActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrrOverflowActive.setStatus("mandatory")
_IbmwrrOverflowDuration_Type = TimeTicks
_IbmwrrOverflowDuration_Object = MibTableColumn
ibmwrrOverflowDuration = _IbmwrrOverflowDuration_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 10),
    _IbmwrrOverflowDuration_Type()
)
ibmwrrOverflowDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrrOverflowDuration.setStatus("mandatory")
_IbmwrrOverflowAttempts_Type = Counter32
_IbmwrrOverflowAttempts_Object = MibTableColumn
ibmwrrOverflowAttempts = _IbmwrrOverflowAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 11),
    _IbmwrrOverflowAttempts_Type()
)
ibmwrrOverflowAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrrOverflowAttempts.setStatus("mandatory")
_IbmwrrOverflowActuals_Type = Counter32
_IbmwrrOverflowActuals_Object = MibTableColumn
ibmwrrOverflowActuals = _IbmwrrOverflowActuals_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 12),
    _IbmwrrOverflowActuals_Type()
)
ibmwrrOverflowActuals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwrrOverflowActuals.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WAN-RESTORAL-REROUTE-MIB",
    **{"ibmWanRestoralRerouteMIB": ibmWanRestoralRerouteMIB,
       "ibmWanRestoral": ibmWanRestoral,
       "ibmWanRestoralTable": ibmWanRestoralTable,
       "ibmWanRestoralEntry": ibmWanRestoralEntry,
       "ibmwrsPriNetifIndex": ibmwrsPriNetifIndex,
       "ibmwrsSecNetifIndex": ibmwrsSecNetifIndex,
       "ibmwrsEnabled": ibmwrsEnabled,
       "ibmwrsActive": ibmwrsActive,
       "ibmwrsDuration": ibmwrsDuration,
       "ibmwrsAttempts": ibmwrsAttempts,
       "ibmwrsActuals": ibmwrsActuals,
       "ibmwrsFwdPkts": ibmwrsFwdPkts,
       "ibmWanReroute": ibmWanReroute,
       "ibmWanRerouteTable": ibmWanRerouteTable,
       "ibmWanRerouteEntry": ibmWanRerouteEntry,
       "ibmwrrPriNetifIndex": ibmwrrPriNetifIndex,
       "ibmwrrAltNetifIndex": ibmwrrAltNetifIndex,
       "ibmwrrEnabled": ibmwrrEnabled,
       "ibmwrrActive": ibmwrrActive,
       "ibmwrrDuration": ibmwrrDuration,
       "ibmwrrAttempts": ibmwrrAttempts,
       "ibmwrrActuals": ibmwrrActuals,
       "ibmwrrOverflowEnabled": ibmwrrOverflowEnabled,
       "ibmwrrOverflowActive": ibmwrrOverflowActive,
       "ibmwrrOverflowDuration": ibmwrrOverflowDuration,
       "ibmwrrOverflowAttempts": ibmwrrOverflowAttempts,
       "ibmwrrOverflowActuals": ibmwrrOverflowActuals}
)
