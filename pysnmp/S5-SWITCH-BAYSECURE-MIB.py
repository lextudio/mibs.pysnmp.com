# SNMP MIB module (S5-SWITCH-BAYSECURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/S5-SWITCH-BAYSECURE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:08 2024
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

(s5Com,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "s5Com")

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
 MacAddress,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

s5SbsAuth = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3)
)
s5SbsAuth.setRevisions(
        ("2012-09-13 00:00",
         "2011-01-10 00:00",
         "2009-05-28 00:00",
         "2009-02-24 00:00",
         "2006-09-18 00:00",
         "2005-03-09 00:00",
         "2004-09-03 00:00",
         "2004-07-22 00:00",
         "2004-07-20 00:00",
         "2003-02-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortSet(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs



class _S5SbsAuthSecurityLock_Type(Integer32):
    """Custom type s5SbsAuthSecurityLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("notlocked", 3),
          ("other", 1))
    )


_S5SbsAuthSecurityLock_Type.__name__ = "Integer32"
_S5SbsAuthSecurityLock_Object = MibScalar
s5SbsAuthSecurityLock = _S5SbsAuthSecurityLock_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 1),
    _S5SbsAuthSecurityLock_Type()
)
s5SbsAuthSecurityLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsAuthSecurityLock.setStatus("current")


class _S5SbsAuthCtlPartTime_Type(Integer32):
    """Custom type s5SbsAuthCtlPartTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5SbsAuthCtlPartTime_Type.__name__ = "Integer32"
_S5SbsAuthCtlPartTime_Object = MibScalar
s5SbsAuthCtlPartTime = _S5SbsAuthCtlPartTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 2),
    _S5SbsAuthCtlPartTime_Type()
)
s5SbsAuthCtlPartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsAuthCtlPartTime.setStatus("current")


class _S5SbsSecurityStatus_Type(Integer32):
    """Custom type s5SbsSecurityStatus based on Integer32"""
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


_S5SbsSecurityStatus_Type.__name__ = "Integer32"
_S5SbsSecurityStatus_Object = MibScalar
s5SbsSecurityStatus = _S5SbsSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 3),
    _S5SbsSecurityStatus_Type()
)
s5SbsSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsSecurityStatus.setStatus("current")


class _S5SbsSecurityMode_Type(Integer32):
    """Custom type s5SbsSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoLearn", 3),
          ("macList", 2),
          ("singleMACperPort", 1))
    )


_S5SbsSecurityMode_Type.__name__ = "Integer32"
_S5SbsSecurityMode_Object = MibScalar
s5SbsSecurityMode = _S5SbsSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 4),
    _S5SbsSecurityMode_Type()
)
s5SbsSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsSecurityMode.setStatus("current")


class _S5SbsSecurityAction_Type(Integer32):
    """Custom type s5SbsSecurityAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("daFiltering", 5),
          ("daFilteringAndsendTrap", 6),
          ("noAction", 1),
          ("partitionPort", 3),
          ("partitionPortAnddaFiltering", 7),
          ("partitionPortAndsendTrap", 4),
          ("partitionPortdaFilteringAndsendTrap", 8),
          ("trap", 2))
    )


_S5SbsSecurityAction_Type.__name__ = "Integer32"
_S5SbsSecurityAction_Object = MibScalar
s5SbsSecurityAction = _S5SbsSecurityAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 5),
    _S5SbsSecurityAction_Type()
)
s5SbsSecurityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsSecurityAction.setStatus("current")


class _S5SbsCurrNodesAllowed_Type(Integer32):
    """Custom type s5SbsCurrNodesAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_S5SbsCurrNodesAllowed_Type.__name__ = "Integer32"
_S5SbsCurrNodesAllowed_Object = MibScalar
s5SbsCurrNodesAllowed = _S5SbsCurrNodesAllowed_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 6),
    _S5SbsCurrNodesAllowed_Type()
)
s5SbsCurrNodesAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsCurrNodesAllowed.setStatus("current")


class _S5SbsMaxNodesAllowed_Type(Integer32):
    """Custom type s5SbsMaxNodesAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_S5SbsMaxNodesAllowed_Type.__name__ = "Integer32"
_S5SbsMaxNodesAllowed_Object = MibScalar
s5SbsMaxNodesAllowed = _S5SbsMaxNodesAllowed_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 7),
    _S5SbsMaxNodesAllowed_Type()
)
s5SbsMaxNodesAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsMaxNodesAllowed.setStatus("current")


class _S5SbsCurrNodesBlocked_Type(Integer32):
    """Custom type s5SbsCurrNodesBlocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_S5SbsCurrNodesBlocked_Type.__name__ = "Integer32"
_S5SbsCurrNodesBlocked_Object = MibScalar
s5SbsCurrNodesBlocked = _S5SbsCurrNodesBlocked_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 8),
    _S5SbsCurrNodesBlocked_Type()
)
s5SbsCurrNodesBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsCurrNodesBlocked.setStatus("current")


class _S5SbsMaxNodesBlocked_Type(Integer32):
    """Custom type s5SbsMaxNodesBlocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_S5SbsMaxNodesBlocked_Type.__name__ = "Integer32"
_S5SbsMaxNodesBlocked_Object = MibScalar
s5SbsMaxNodesBlocked = _S5SbsMaxNodesBlocked_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 9),
    _S5SbsMaxNodesBlocked_Type()
)
s5SbsMaxNodesBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsMaxNodesBlocked.setStatus("current")
_S5SbsAuthCfgTable_Object = MibTable
s5SbsAuthCfgTable = _S5SbsAuthCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10)
)
if mibBuilder.loadTexts:
    s5SbsAuthCfgTable.setStatus("current")
_S5SbsAuthCfgEntry_Object = MibTableRow
s5SbsAuthCfgEntry = _S5SbsAuthCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1)
)
s5SbsAuthCfgEntry.setIndexNames(
    (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsAuthCfgBrdIndx"),
    (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsAuthCfgPortIndx"),
    (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsAuthCfgMACIndx"),
)
if mibBuilder.loadTexts:
    s5SbsAuthCfgEntry.setStatus("current")


class _S5SbsAuthCfgBrdIndx_Type(Integer32):
    """Custom type s5SbsAuthCfgBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5SbsAuthCfgBrdIndx_Type.__name__ = "Integer32"
_S5SbsAuthCfgBrdIndx_Object = MibTableColumn
s5SbsAuthCfgBrdIndx = _S5SbsAuthCfgBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 1),
    _S5SbsAuthCfgBrdIndx_Type()
)
s5SbsAuthCfgBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsAuthCfgBrdIndx.setStatus("current")


class _S5SbsAuthCfgPortIndx_Type(Integer32):
    """Custom type s5SbsAuthCfgPortIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5SbsAuthCfgPortIndx_Type.__name__ = "Integer32"
_S5SbsAuthCfgPortIndx_Object = MibTableColumn
s5SbsAuthCfgPortIndx = _S5SbsAuthCfgPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 2),
    _S5SbsAuthCfgPortIndx_Type()
)
s5SbsAuthCfgPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsAuthCfgPortIndx.setStatus("current")
_S5SbsAuthCfgMACIndx_Type = MacAddress
_S5SbsAuthCfgMACIndx_Object = MibTableColumn
s5SbsAuthCfgMACIndx = _S5SbsAuthCfgMACIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 3),
    _S5SbsAuthCfgMACIndx_Type()
)
s5SbsAuthCfgMACIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsAuthCfgMACIndx.setStatus("current")


class _S5SbsAuthCfgAccessCtrlType_Type(Integer32):
    """Custom type s5SbsAuthCfgAccessCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("blocked", 2))
    )


_S5SbsAuthCfgAccessCtrlType_Type.__name__ = "Integer32"
_S5SbsAuthCfgAccessCtrlType_Object = MibTableColumn
s5SbsAuthCfgAccessCtrlType = _S5SbsAuthCfgAccessCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 4),
    _S5SbsAuthCfgAccessCtrlType_Type()
)
s5SbsAuthCfgAccessCtrlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsAuthCfgAccessCtrlType.setStatus("current")


class _S5SbsAuthCfgStatus_Type(Integer32):
    """Custom type s5SbsAuthCfgStatus based on Integer32"""
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
        *(("create", 2),
          ("createSticky", 5),
          ("delete", 3),
          ("modify", 4),
          ("valid", 1))
    )


_S5SbsAuthCfgStatus_Type.__name__ = "Integer32"
_S5SbsAuthCfgStatus_Object = MibTableColumn
s5SbsAuthCfgStatus = _S5SbsAuthCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 5),
    _S5SbsAuthCfgStatus_Type()
)
s5SbsAuthCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsAuthCfgStatus.setStatus("current")


class _S5SbsAuthCfgSecureList_Type(Integer32):
    """Custom type s5SbsAuthCfgSecureList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5SbsAuthCfgSecureList_Type.__name__ = "Integer32"
_S5SbsAuthCfgSecureList_Object = MibTableColumn
s5SbsAuthCfgSecureList = _S5SbsAuthCfgSecureList_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 6),
    _S5SbsAuthCfgSecureList_Type()
)
s5SbsAuthCfgSecureList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsAuthCfgSecureList.setStatus("current")


class _S5SbsAuthCfgSource_Type(Integer32):
    """Custom type s5SbsAuthCfgSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoLearn", 2),
          ("static", 1),
          ("sticky", 3))
    )


_S5SbsAuthCfgSource_Type.__name__ = "Integer32"
_S5SbsAuthCfgSource_Object = MibTableColumn
s5SbsAuthCfgSource = _S5SbsAuthCfgSource_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 7),
    _S5SbsAuthCfgSource_Type()
)
s5SbsAuthCfgSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsAuthCfgSource.setStatus("current")
_S5SbsAuthCfgLifetime_Type = TimeInterval
_S5SbsAuthCfgLifetime_Object = MibTableColumn
s5SbsAuthCfgLifetime = _S5SbsAuthCfgLifetime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 8),
    _S5SbsAuthCfgLifetime_Type()
)
s5SbsAuthCfgLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsAuthCfgLifetime.setStatus("current")


class _S5SbsAuthCfgTrunk_Type(Integer32):
    """Custom type s5SbsAuthCfgTrunk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_S5SbsAuthCfgTrunk_Type.__name__ = "Integer32"
_S5SbsAuthCfgTrunk_Object = MibTableColumn
s5SbsAuthCfgTrunk = _S5SbsAuthCfgTrunk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 9),
    _S5SbsAuthCfgTrunk_Type()
)
s5SbsAuthCfgTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsAuthCfgTrunk.setStatus("current")
_S5SbsAuthStatusTable_Object = MibTable
s5SbsAuthStatusTable = _S5SbsAuthStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 11)
)
if mibBuilder.loadTexts:
    s5SbsAuthStatusTable.setStatus("current")
_S5SbsAuthStatusEntry_Object = MibTableRow
s5SbsAuthStatusEntry = _S5SbsAuthStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 11, 1)
)
s5SbsAuthStatusEntry.setIndexNames(
    (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsAuthStatusBrdIndx"),
    (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsAuthStatusPortIndx"),
    (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsAuthStatusMACIndx"),
)
if mibBuilder.loadTexts:
    s5SbsAuthStatusEntry.setStatus("current")


class _S5SbsAuthStatusBrdIndx_Type(Integer32):
    """Custom type s5SbsAuthStatusBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5SbsAuthStatusBrdIndx_Type.__name__ = "Integer32"
_S5SbsAuthStatusBrdIndx_Object = MibTableColumn
s5SbsAuthStatusBrdIndx = _S5SbsAuthStatusBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 11, 1, 1),
    _S5SbsAuthStatusBrdIndx_Type()
)
s5SbsAuthStatusBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsAuthStatusBrdIndx.setStatus("current")


class _S5SbsAuthStatusPortIndx_Type(Integer32):
    """Custom type s5SbsAuthStatusPortIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5SbsAuthStatusPortIndx_Type.__name__ = "Integer32"
_S5SbsAuthStatusPortIndx_Object = MibTableColumn
s5SbsAuthStatusPortIndx = _S5SbsAuthStatusPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 11, 1, 2),
    _S5SbsAuthStatusPortIndx_Type()
)
s5SbsAuthStatusPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsAuthStatusPortIndx.setStatus("current")
_S5SbsAuthStatusMACIndx_Type = MacAddress
_S5SbsAuthStatusMACIndx_Object = MibTableColumn
s5SbsAuthStatusMACIndx = _S5SbsAuthStatusMACIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 11, 1, 3),
    _S5SbsAuthStatusMACIndx_Type()
)
s5SbsAuthStatusMACIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsAuthStatusMACIndx.setStatus("current")


class _S5SbsCurrentAccessCtrlType_Type(Integer32):
    """Custom type s5SbsCurrentAccessCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("block", 2))
    )


_S5SbsCurrentAccessCtrlType_Type.__name__ = "Integer32"
_S5SbsCurrentAccessCtrlType_Object = MibTableColumn
s5SbsCurrentAccessCtrlType = _S5SbsCurrentAccessCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 11, 1, 4),
    _S5SbsCurrentAccessCtrlType_Type()
)
s5SbsCurrentAccessCtrlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsCurrentAccessCtrlType.setStatus("current")


class _S5SbsCurrentActionMode_Type(Integer32):
    """Custom type s5SbsCurrentActionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("daFiltering", 4),
          ("daFilteringAndsendTrap", 5),
          ("noAction", 1),
          ("partitionPort", 2),
          ("partitionPortAnddaFiltering", 7),
          ("partitionPortAndsendTrap", 3),
          ("partitionPortdaFilteringAndsendTrap", 8),
          ("sendTrap", 6))
    )


_S5SbsCurrentActionMode_Type.__name__ = "Integer32"
_S5SbsCurrentActionMode_Object = MibTableColumn
s5SbsCurrentActionMode = _S5SbsCurrentActionMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 11, 1, 5),
    _S5SbsCurrentActionMode_Type()
)
s5SbsCurrentActionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsCurrentActionMode.setStatus("current")


class _S5SbsCurrentPortSecurStatus_Type(Integer32):
    """Custom type s5SbsCurrentPortSecurStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("portPartition", 3),
          ("portSecure", 2))
    )


_S5SbsCurrentPortSecurStatus_Type.__name__ = "Integer32"
_S5SbsCurrentPortSecurStatus_Object = MibTableColumn
s5SbsCurrentPortSecurStatus = _S5SbsCurrentPortSecurStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 11, 1, 6),
    _S5SbsCurrentPortSecurStatus_Type()
)
s5SbsCurrentPortSecurStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsCurrentPortSecurStatus.setStatus("current")
_S5SbsViolationStatusTable_Object = MibTable
s5SbsViolationStatusTable = _S5SbsViolationStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 12)
)
if mibBuilder.loadTexts:
    s5SbsViolationStatusTable.setStatus("current")
_S5SbsViolationStatusEntry_Object = MibTableRow
s5SbsViolationStatusEntry = _S5SbsViolationStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 12, 1)
)
s5SbsViolationStatusEntry.setIndexNames(
    (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusBrdIndx"),
    (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusPortIndx"),
)
if mibBuilder.loadTexts:
    s5SbsViolationStatusEntry.setStatus("current")


class _S5SbsViolationStatusBrdIndx_Type(Integer32):
    """Custom type s5SbsViolationStatusBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5SbsViolationStatusBrdIndx_Type.__name__ = "Integer32"
_S5SbsViolationStatusBrdIndx_Object = MibTableColumn
s5SbsViolationStatusBrdIndx = _S5SbsViolationStatusBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 12, 1, 1),
    _S5SbsViolationStatusBrdIndx_Type()
)
s5SbsViolationStatusBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsViolationStatusBrdIndx.setStatus("current")


class _S5SbsViolationStatusPortIndx_Type(Integer32):
    """Custom type s5SbsViolationStatusPortIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5SbsViolationStatusPortIndx_Type.__name__ = "Integer32"
_S5SbsViolationStatusPortIndx_Object = MibTableColumn
s5SbsViolationStatusPortIndx = _S5SbsViolationStatusPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 12, 1, 2),
    _S5SbsViolationStatusPortIndx_Type()
)
s5SbsViolationStatusPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsViolationStatusPortIndx.setStatus("current")
_S5SbsViolationStatusMACAddress_Type = MacAddress
_S5SbsViolationStatusMACAddress_Object = MibTableColumn
s5SbsViolationStatusMACAddress = _S5SbsViolationStatusMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 12, 1, 3),
    _S5SbsViolationStatusMACAddress_Type()
)
s5SbsViolationStatusMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsViolationStatusMACAddress.setStatus("current")


class _S5SbsMgmViolationType_Type(Integer32):
    """Custom type s5SbsMgmViolationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmp", 1),
          ("telnet", 3),
          ("web", 2))
    )


_S5SbsMgmViolationType_Type.__name__ = "Integer32"
_S5SbsMgmViolationType_Object = MibScalar
s5SbsMgmViolationType = _S5SbsMgmViolationType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 13),
    _S5SbsMgmViolationType_Type()
)
s5SbsMgmViolationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsMgmViolationType.setStatus("current")
_S5SbsMgmViolationIpAddress_Type = IpAddress
_S5SbsMgmViolationIpAddress_Object = MibScalar
s5SbsMgmViolationIpAddress = _S5SbsMgmViolationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 14),
    _S5SbsMgmViolationIpAddress_Type()
)
s5SbsMgmViolationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsMgmViolationIpAddress.setStatus("current")
_S5SbsPortSecurityStatus_Type = PortSet
_S5SbsPortSecurityStatus_Object = MibScalar
s5SbsPortSecurityStatus = _S5SbsPortSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 15),
    _S5SbsPortSecurityStatus_Type()
)
s5SbsPortSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsPortSecurityStatus.setStatus("current")
_S5SbsPortLearnStatus_Type = PortSet
_S5SbsPortLearnStatus_Object = MibScalar
s5SbsPortLearnStatus = _S5SbsPortLearnStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 16),
    _S5SbsPortLearnStatus_Type()
)
s5SbsPortLearnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsPortLearnStatus.setStatus("current")


class _S5SbsCurrSecurityLists_Type(Integer32):
    """Custom type s5SbsCurrSecurityLists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5SbsCurrSecurityLists_Type.__name__ = "Integer32"
_S5SbsCurrSecurityLists_Object = MibScalar
s5SbsCurrSecurityLists = _S5SbsCurrSecurityLists_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 17),
    _S5SbsCurrSecurityLists_Type()
)
s5SbsCurrSecurityLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsCurrSecurityLists.setStatus("current")


class _S5SbsMaxSecurityLists_Type(Integer32):
    """Custom type s5SbsMaxSecurityLists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5SbsMaxSecurityLists_Type.__name__ = "Integer32"
_S5SbsMaxSecurityLists_Object = MibScalar
s5SbsMaxSecurityLists = _S5SbsMaxSecurityLists_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 18),
    _S5SbsMaxSecurityLists_Type()
)
s5SbsMaxSecurityLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsMaxSecurityLists.setStatus("current")
_S5SbsSecurityListTable_Object = MibTable
s5SbsSecurityListTable = _S5SbsSecurityListTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 19)
)
if mibBuilder.loadTexts:
    s5SbsSecurityListTable.setStatus("current")
_S5SbsSecurityListEntry_Object = MibTableRow
s5SbsSecurityListEntry = _S5SbsSecurityListEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 19, 1)
)
s5SbsSecurityListEntry.setIndexNames(
    (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsSecurityListIndx"),
)
if mibBuilder.loadTexts:
    s5SbsSecurityListEntry.setStatus("current")


class _S5SbsSecurityListIndx_Type(Integer32):
    """Custom type s5SbsSecurityListIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5SbsSecurityListIndx_Type.__name__ = "Integer32"
_S5SbsSecurityListIndx_Object = MibTableColumn
s5SbsSecurityListIndx = _S5SbsSecurityListIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 19, 1, 1),
    _S5SbsSecurityListIndx_Type()
)
s5SbsSecurityListIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsSecurityListIndx.setStatus("current")
_S5SbsSecurityListMembers_Type = PortSet
_S5SbsSecurityListMembers_Object = MibTableColumn
s5SbsSecurityListMembers = _S5SbsSecurityListMembers_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 19, 1, 2),
    _S5SbsSecurityListMembers_Type()
)
s5SbsSecurityListMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsSecurityListMembers.setStatus("current")


class _S5SbsSecurityListStatus_Type(Integer32):
    """Custom type s5SbsSecurityListStatus based on Integer32"""
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
        *(("create", 2),
          ("delete", 3),
          ("modify", 4),
          ("valid", 1))
    )


_S5SbsSecurityListStatus_Type.__name__ = "Integer32"
_S5SbsSecurityListStatus_Object = MibTableColumn
s5SbsSecurityListStatus = _S5SbsSecurityListStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 19, 1, 3),
    _S5SbsSecurityListStatus_Type()
)
s5SbsSecurityListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsSecurityListStatus.setStatus("current")
_S5SbsMacViolation_ObjectIdentity = ObjectIdentity
s5SbsMacViolation = _S5SbsMacViolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 20)
)


class _S5SbsMacViolationClear_Type(Integer32):
    """Custom type s5SbsMacViolationClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("other", 1))
    )


_S5SbsMacViolationClear_Type.__name__ = "Integer32"
_S5SbsMacViolationClear_Object = MibScalar
s5SbsMacViolationClear = _S5SbsMacViolationClear_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 20, 1),
    _S5SbsMacViolationClear_Type()
)
s5SbsMacViolationClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsMacViolationClear.setStatus("current")
_S5SbsMacViolationTable_Object = MibTable
s5SbsMacViolationTable = _S5SbsMacViolationTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 20, 2)
)
if mibBuilder.loadTexts:
    s5SbsMacViolationTable.setStatus("current")
_S5SbsMacViolationEntry_Object = MibTableRow
s5SbsMacViolationEntry = _S5SbsMacViolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 20, 2, 1)
)
s5SbsMacViolationEntry.setIndexNames(
    (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsMacViolationAddress"),
)
if mibBuilder.loadTexts:
    s5SbsMacViolationEntry.setStatus("current")
_S5SbsMacViolationAddress_Type = MacAddress
_S5SbsMacViolationAddress_Object = MibTableColumn
s5SbsMacViolationAddress = _S5SbsMacViolationAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 20, 2, 1, 1),
    _S5SbsMacViolationAddress_Type()
)
s5SbsMacViolationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsMacViolationAddress.setStatus("current")


class _S5SbsMacViolationBrd_Type(Integer32):
    """Custom type s5SbsMacViolationBrd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5SbsMacViolationBrd_Type.__name__ = "Integer32"
_S5SbsMacViolationBrd_Object = MibTableColumn
s5SbsMacViolationBrd = _S5SbsMacViolationBrd_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 20, 2, 1, 2),
    _S5SbsMacViolationBrd_Type()
)
s5SbsMacViolationBrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsMacViolationBrd.setStatus("current")


class _S5SbsMacViolationPort_Type(Integer32):
    """Custom type s5SbsMacViolationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5SbsMacViolationPort_Type.__name__ = "Integer32"
_S5SbsMacViolationPort_Object = MibTableColumn
s5SbsMacViolationPort = _S5SbsMacViolationPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 20, 2, 1, 3),
    _S5SbsMacViolationPort_Type()
)
s5SbsMacViolationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5SbsMacViolationPort.setStatus("current")


class _S5SbsAutoLearningAgingTime_Type(Integer32):
    """Custom type s5SbsAutoLearningAgingTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5SbsAutoLearningAgingTime_Type.__name__ = "Integer32"
_S5SbsAutoLearningAgingTime_Object = MibScalar
s5SbsAutoLearningAgingTime = _S5SbsAutoLearningAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 21),
    _S5SbsAutoLearningAgingTime_Type()
)
s5SbsAutoLearningAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsAutoLearningAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    s5SbsAutoLearningAgingTime.setUnits("Minutes")
_S5SbsAutoLearningConfigTable_Object = MibTable
s5SbsAutoLearningConfigTable = _S5SbsAutoLearningConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 22)
)
if mibBuilder.loadTexts:
    s5SbsAutoLearningConfigTable.setStatus("current")
_S5SbsAutoLearningConfigEntry_Object = MibTableRow
s5SbsAutoLearningConfigEntry = _S5SbsAutoLearningConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 22, 1)
)
s5SbsAutoLearningConfigEntry.setIndexNames(
    (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsAutoLearningConfigBrd"),
    (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsAutoLearningConfigPort"),
)
if mibBuilder.loadTexts:
    s5SbsAutoLearningConfigEntry.setStatus("current")


class _S5SbsAutoLearningConfigBrd_Type(Integer32):
    """Custom type s5SbsAutoLearningConfigBrd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5SbsAutoLearningConfigBrd_Type.__name__ = "Integer32"
_S5SbsAutoLearningConfigBrd_Object = MibTableColumn
s5SbsAutoLearningConfigBrd = _S5SbsAutoLearningConfigBrd_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 22, 1, 1),
    _S5SbsAutoLearningConfigBrd_Type()
)
s5SbsAutoLearningConfigBrd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s5SbsAutoLearningConfigBrd.setStatus("current")


class _S5SbsAutoLearningConfigPort_Type(Integer32):
    """Custom type s5SbsAutoLearningConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5SbsAutoLearningConfigPort_Type.__name__ = "Integer32"
_S5SbsAutoLearningConfigPort_Object = MibTableColumn
s5SbsAutoLearningConfigPort = _S5SbsAutoLearningConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 22, 1, 2),
    _S5SbsAutoLearningConfigPort_Type()
)
s5SbsAutoLearningConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s5SbsAutoLearningConfigPort.setStatus("current")


class _S5SbsAutoLearningConfigEnabled_Type(TruthValue):
    """Custom type s5SbsAutoLearningConfigEnabled based on TruthValue"""


_S5SbsAutoLearningConfigEnabled_Object = MibTableColumn
s5SbsAutoLearningConfigEnabled = _S5SbsAutoLearningConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 22, 1, 3),
    _S5SbsAutoLearningConfigEnabled_Type()
)
s5SbsAutoLearningConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsAutoLearningConfigEnabled.setStatus("current")


class _S5SbsAutoLearningConfigMaxMacs_Type(Integer32):
    """Custom type s5SbsAutoLearningConfigMaxMacs based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_S5SbsAutoLearningConfigMaxMacs_Type.__name__ = "Integer32"
_S5SbsAutoLearningConfigMaxMacs_Object = MibTableColumn
s5SbsAutoLearningConfigMaxMacs = _S5SbsAutoLearningConfigMaxMacs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 22, 1, 4),
    _S5SbsAutoLearningConfigMaxMacs_Type()
)
s5SbsAutoLearningConfigMaxMacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsAutoLearningConfigMaxMacs.setStatus("current")
_S5SbsAutoLearningPorts_Type = PortSet
_S5SbsAutoLearningPorts_Object = MibScalar
s5SbsAutoLearningPorts = _S5SbsAutoLearningPorts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 23),
    _S5SbsAutoLearningPorts_Type()
)
s5SbsAutoLearningPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsAutoLearningPorts.setStatus("current")
_S5SbsAutoLearningSticky_Type = TruthValue
_S5SbsAutoLearningSticky_Object = MibScalar
s5SbsAutoLearningSticky = _S5SbsAutoLearningSticky_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 24),
    _S5SbsAutoLearningSticky_Type()
)
s5SbsAutoLearningSticky.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsAutoLearningSticky.setStatus("current")
_S5SbsSecurityLockoutPortList_Type = PortSet
_S5SbsSecurityLockoutPortList_Object = MibScalar
s5SbsSecurityLockoutPortList = _S5SbsSecurityLockoutPortList_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 25),
    _S5SbsSecurityLockoutPortList_Type()
)
s5SbsSecurityLockoutPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5SbsSecurityLockoutPortList.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S5-SWITCH-BAYSECURE-MIB",
    **{"PortSet": PortSet,
       "s5SbsAuth": s5SbsAuth,
       "s5SbsAuthSecurityLock": s5SbsAuthSecurityLock,
       "s5SbsAuthCtlPartTime": s5SbsAuthCtlPartTime,
       "s5SbsSecurityStatus": s5SbsSecurityStatus,
       "s5SbsSecurityMode": s5SbsSecurityMode,
       "s5SbsSecurityAction": s5SbsSecurityAction,
       "s5SbsCurrNodesAllowed": s5SbsCurrNodesAllowed,
       "s5SbsMaxNodesAllowed": s5SbsMaxNodesAllowed,
       "s5SbsCurrNodesBlocked": s5SbsCurrNodesBlocked,
       "s5SbsMaxNodesBlocked": s5SbsMaxNodesBlocked,
       "s5SbsAuthCfgTable": s5SbsAuthCfgTable,
       "s5SbsAuthCfgEntry": s5SbsAuthCfgEntry,
       "s5SbsAuthCfgBrdIndx": s5SbsAuthCfgBrdIndx,
       "s5SbsAuthCfgPortIndx": s5SbsAuthCfgPortIndx,
       "s5SbsAuthCfgMACIndx": s5SbsAuthCfgMACIndx,
       "s5SbsAuthCfgAccessCtrlType": s5SbsAuthCfgAccessCtrlType,
       "s5SbsAuthCfgStatus": s5SbsAuthCfgStatus,
       "s5SbsAuthCfgSecureList": s5SbsAuthCfgSecureList,
       "s5SbsAuthCfgSource": s5SbsAuthCfgSource,
       "s5SbsAuthCfgLifetime": s5SbsAuthCfgLifetime,
       "s5SbsAuthCfgTrunk": s5SbsAuthCfgTrunk,
       "s5SbsAuthStatusTable": s5SbsAuthStatusTable,
       "s5SbsAuthStatusEntry": s5SbsAuthStatusEntry,
       "s5SbsAuthStatusBrdIndx": s5SbsAuthStatusBrdIndx,
       "s5SbsAuthStatusPortIndx": s5SbsAuthStatusPortIndx,
       "s5SbsAuthStatusMACIndx": s5SbsAuthStatusMACIndx,
       "s5SbsCurrentAccessCtrlType": s5SbsCurrentAccessCtrlType,
       "s5SbsCurrentActionMode": s5SbsCurrentActionMode,
       "s5SbsCurrentPortSecurStatus": s5SbsCurrentPortSecurStatus,
       "s5SbsViolationStatusTable": s5SbsViolationStatusTable,
       "s5SbsViolationStatusEntry": s5SbsViolationStatusEntry,
       "s5SbsViolationStatusBrdIndx": s5SbsViolationStatusBrdIndx,
       "s5SbsViolationStatusPortIndx": s5SbsViolationStatusPortIndx,
       "s5SbsViolationStatusMACAddress": s5SbsViolationStatusMACAddress,
       "s5SbsMgmViolationType": s5SbsMgmViolationType,
       "s5SbsMgmViolationIpAddress": s5SbsMgmViolationIpAddress,
       "s5SbsPortSecurityStatus": s5SbsPortSecurityStatus,
       "s5SbsPortLearnStatus": s5SbsPortLearnStatus,
       "s5SbsCurrSecurityLists": s5SbsCurrSecurityLists,
       "s5SbsMaxSecurityLists": s5SbsMaxSecurityLists,
       "s5SbsSecurityListTable": s5SbsSecurityListTable,
       "s5SbsSecurityListEntry": s5SbsSecurityListEntry,
       "s5SbsSecurityListIndx": s5SbsSecurityListIndx,
       "s5SbsSecurityListMembers": s5SbsSecurityListMembers,
       "s5SbsSecurityListStatus": s5SbsSecurityListStatus,
       "s5SbsMacViolation": s5SbsMacViolation,
       "s5SbsMacViolationClear": s5SbsMacViolationClear,
       "s5SbsMacViolationTable": s5SbsMacViolationTable,
       "s5SbsMacViolationEntry": s5SbsMacViolationEntry,
       "s5SbsMacViolationAddress": s5SbsMacViolationAddress,
       "s5SbsMacViolationBrd": s5SbsMacViolationBrd,
       "s5SbsMacViolationPort": s5SbsMacViolationPort,
       "s5SbsAutoLearningAgingTime": s5SbsAutoLearningAgingTime,
       "s5SbsAutoLearningConfigTable": s5SbsAutoLearningConfigTable,
       "s5SbsAutoLearningConfigEntry": s5SbsAutoLearningConfigEntry,
       "s5SbsAutoLearningConfigBrd": s5SbsAutoLearningConfigBrd,
       "s5SbsAutoLearningConfigPort": s5SbsAutoLearningConfigPort,
       "s5SbsAutoLearningConfigEnabled": s5SbsAutoLearningConfigEnabled,
       "s5SbsAutoLearningConfigMaxMacs": s5SbsAutoLearningConfigMaxMacs,
       "s5SbsAutoLearningPorts": s5SbsAutoLearningPorts,
       "s5SbsAutoLearningSticky": s5SbsAutoLearningSticky,
       "s5SbsSecurityLockoutPortList": s5SbsSecurityLockoutPortList}
)
