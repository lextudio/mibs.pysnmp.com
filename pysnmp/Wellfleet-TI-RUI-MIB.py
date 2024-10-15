# SNMP MIB module (Wellfleet-TI-RUI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-TI-RUI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:20 2024
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

(wfServices,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfServices")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfTiRui_ObjectIdentity = ObjectIdentity
wfTiRui = _WfTiRui_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2)
)


class _WfTiRuiState_Type(Integer32):
    """Custom type wfTiRuiState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 2),
          ("idle", 1))
    )


_WfTiRuiState_Type.__name__ = "Integer32"
_WfTiRuiState_Object = MibScalar
wfTiRuiState = _WfTiRuiState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 1),
    _WfTiRuiState_Type()
)
wfTiRuiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTiRuiState.setStatus("mandatory")
_WfTiRuiAction_Type = DisplayString
_WfTiRuiAction_Object = MibScalar
wfTiRuiAction = _WfTiRuiAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 2),
    _WfTiRuiAction_Type()
)
wfTiRuiAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTiRuiAction.setStatus("mandatory")
_WfTiRuiResult_Type = DisplayString
_WfTiRuiResult_Object = MibScalar
wfTiRuiResult = _WfTiRuiResult_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 3),
    _WfTiRuiResult_Type()
)
wfTiRuiResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTiRuiResult.setStatus("mandatory")
_WfTiRuiInReqs_Type = Counter32
_WfTiRuiInReqs_Object = MibScalar
wfTiRuiInReqs = _WfTiRuiInReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 4),
    _WfTiRuiInReqs_Type()
)
wfTiRuiInReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTiRuiInReqs.setStatus("mandatory")
_WfTiRuiOutResults_Type = Counter32
_WfTiRuiOutResults_Object = MibScalar
wfTiRuiOutResults = _WfTiRuiOutResults_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 5),
    _WfTiRuiOutResults_Type()
)
wfTiRuiOutResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTiRuiOutResults.setStatus("mandatory")
_WfTiRuiOutResultsErr_Type = Counter32
_WfTiRuiOutResultsErr_Object = MibScalar
wfTiRuiOutResultsErr = _WfTiRuiOutResultsErr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 6),
    _WfTiRuiOutResultsErr_Type()
)
wfTiRuiOutResultsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTiRuiOutResultsErr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-TI-RUI-MIB",
    **{"wfTiRui": wfTiRui,
       "wfTiRuiState": wfTiRuiState,
       "wfTiRuiAction": wfTiRuiAction,
       "wfTiRuiResult": wfTiRuiResult,
       "wfTiRuiInReqs": wfTiRuiInReqs,
       "wfTiRuiOutResults": wfTiRuiOutResults,
       "wfTiRuiOutResultsErr": wfTiRuiOutResultsErr}
)
