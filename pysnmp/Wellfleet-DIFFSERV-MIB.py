# SNMP MIB module (Wellfleet-DIFFSERV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-DIFFSERV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:01 2024
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

(wfDiffServAppGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfDiffServAppGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfDiffServ_ObjectIdentity = ObjectIdentity
wfDiffServ = _WfDiffServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 26, 1)
)


class _WfDiffServCreate_Type(Integer32):
    """Custom type wfDiffServCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDiffServCreate_Type.__name__ = "Integer32"
_WfDiffServCreate_Object = MibScalar
wfDiffServCreate = _WfDiffServCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 26, 1, 1),
    _WfDiffServCreate_Type()
)
wfDiffServCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDiffServCreate.setStatus("mandatory")


class _WfDiffServEnable_Type(Integer32):
    """Custom type wfDiffServEnable based on Integer32"""
    defaultValue = 1

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


_WfDiffServEnable_Type.__name__ = "Integer32"
_WfDiffServEnable_Object = MibScalar
wfDiffServEnable = _WfDiffServEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 26, 1, 2),
    _WfDiffServEnable_Type()
)
wfDiffServEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDiffServEnable.setStatus("mandatory")
_WfDiffServDsByteMask_Type = Integer32
_WfDiffServDsByteMask_Object = MibScalar
wfDiffServDsByteMask = _WfDiffServDsByteMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 26, 1, 3),
    _WfDiffServDsByteMask_Type()
)
wfDiffServDsByteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDiffServDsByteMask.setStatus("mandatory")
_WfDiffServIntfTable_Object = MibTable
wfDiffServIntfTable = _WfDiffServIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 26, 2)
)
if mibBuilder.loadTexts:
    wfDiffServIntfTable.setStatus("mandatory")
_WfDiffServIntfEntry_Object = MibTableRow
wfDiffServIntfEntry = _WfDiffServIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 26, 2, 1)
)
wfDiffServIntfEntry.setIndexNames(
    (0, "Wellfleet-DIFFSERV-MIB", "wfDiffServIntfIpAddr"),
    (0, "Wellfleet-DIFFSERV-MIB", "wfDiffServIntfIfIndex"),
)
if mibBuilder.loadTexts:
    wfDiffServIntfEntry.setStatus("mandatory")


class _WfDiffServIntfCreate_Type(Integer32):
    """Custom type wfDiffServIntfCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDiffServIntfCreate_Type.__name__ = "Integer32"
_WfDiffServIntfCreate_Object = MibTableColumn
wfDiffServIntfCreate = _WfDiffServIntfCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 26, 2, 1, 1),
    _WfDiffServIntfCreate_Type()
)
wfDiffServIntfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDiffServIntfCreate.setStatus("mandatory")


class _WfDiffServIntfEnable_Type(Integer32):
    """Custom type wfDiffServIntfEnable based on Integer32"""
    defaultValue = 1

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


_WfDiffServIntfEnable_Type.__name__ = "Integer32"
_WfDiffServIntfEnable_Object = MibTableColumn
wfDiffServIntfEnable = _WfDiffServIntfEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 26, 2, 1, 2),
    _WfDiffServIntfEnable_Type()
)
wfDiffServIntfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDiffServIntfEnable.setStatus("mandatory")


class _WfDiffServIntfState_Type(Integer32):
    """Custom type wfDiffServIntfState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("notpres", 3),
          ("up", 1))
    )


_WfDiffServIntfState_Type.__name__ = "Integer32"
_WfDiffServIntfState_Object = MibTableColumn
wfDiffServIntfState = _WfDiffServIntfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 26, 2, 1, 3),
    _WfDiffServIntfState_Type()
)
wfDiffServIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDiffServIntfState.setStatus("mandatory")
_WfDiffServIntfIpAddr_Type = IpAddress
_WfDiffServIntfIpAddr_Object = MibTableColumn
wfDiffServIntfIpAddr = _WfDiffServIntfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 26, 2, 1, 4),
    _WfDiffServIntfIpAddr_Type()
)
wfDiffServIntfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDiffServIntfIpAddr.setStatus("mandatory")
_WfDiffServIntfIfIndex_Type = Integer32
_WfDiffServIntfIfIndex_Object = MibTableColumn
wfDiffServIntfIfIndex = _WfDiffServIntfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 26, 2, 1, 5),
    _WfDiffServIntfIfIndex_Type()
)
wfDiffServIntfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDiffServIntfIfIndex.setStatus("mandatory")


class _WfDiffServIntfLogMask_Type(Integer32):
    """Custom type wfDiffServIntfLogMask based on Integer32"""
    defaultValue = 1


_WfDiffServIntfLogMask_Object = MibTableColumn
wfDiffServIntfLogMask = _WfDiffServIntfLogMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 26, 2, 1, 6),
    _WfDiffServIntfLogMask_Type()
)
wfDiffServIntfLogMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDiffServIntfLogMask.setStatus("mandatory")


class _WfDiffServIntfCfgType_Type(Integer32):
    """Custom type wfDiffServIntfCfgType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cops", 2),
          ("static", 1))
    )


_WfDiffServIntfCfgType_Type.__name__ = "Integer32"
_WfDiffServIntfCfgType_Object = MibTableColumn
wfDiffServIntfCfgType = _WfDiffServIntfCfgType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 26, 2, 1, 7),
    _WfDiffServIntfCfgType_Type()
)
wfDiffServIntfCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDiffServIntfCfgType.setStatus("mandatory")


class _WfDiffServIntfUrlIdleOutTimer_Type(Integer32):
    """Custom type wfDiffServIntfUrlIdleOutTimer based on Integer32"""
    defaultValue = 120


_WfDiffServIntfUrlIdleOutTimer_Object = MibTableColumn
wfDiffServIntfUrlIdleOutTimer = _WfDiffServIntfUrlIdleOutTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 26, 2, 1, 8),
    _WfDiffServIntfUrlIdleOutTimer_Type()
)
wfDiffServIntfUrlIdleOutTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDiffServIntfUrlIdleOutTimer.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-DIFFSERV-MIB",
    **{"wfDiffServ": wfDiffServ,
       "wfDiffServCreate": wfDiffServCreate,
       "wfDiffServEnable": wfDiffServEnable,
       "wfDiffServDsByteMask": wfDiffServDsByteMask,
       "wfDiffServIntfTable": wfDiffServIntfTable,
       "wfDiffServIntfEntry": wfDiffServIntfEntry,
       "wfDiffServIntfCreate": wfDiffServIntfCreate,
       "wfDiffServIntfEnable": wfDiffServIntfEnable,
       "wfDiffServIntfState": wfDiffServIntfState,
       "wfDiffServIntfIpAddr": wfDiffServIntfIpAddr,
       "wfDiffServIntfIfIndex": wfDiffServIntfIfIndex,
       "wfDiffServIntfLogMask": wfDiffServIntfLogMask,
       "wfDiffServIntfCfgType": wfDiffServIntfCfgType,
       "wfDiffServIntfUrlIdleOutTimer": wfDiffServIntfUrlIdleOutTimer}
)
