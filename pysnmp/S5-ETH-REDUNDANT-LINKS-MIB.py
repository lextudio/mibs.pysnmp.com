# SNMP MIB module (S5-ETH-REDUNDANT-LINKS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/S5-ETH-REDUNDANT-LINKS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:05 2024
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

(s5EnCfg,) = mibBuilder.importSymbols(
    "S5-ETHERNET-MIB",
    "s5EnCfg")

(TimeIntervalSec,) = mibBuilder.importSymbols(
    "S5-TCS-MIB",
    "TimeIntervalSec")

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

s5EthRedundantLinksMib2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 99)
)
s5EthRedundantLinksMib2.setRevisions(
        ("2004-11-03 00:00",
         "2004-07-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S5EnRedun_ObjectIdentity = ObjectIdentity
s5EnRedun = _S5EnRedun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2)
)
_S5EnRedPortTable_Object = MibTable
s5EnRedPortTable = _S5EnRedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    s5EnRedPortTable.setStatus("current")
_S5EnRedPortEntry_Object = MibTableRow
s5EnRedPortEntry = _S5EnRedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 1, 1)
)
s5EnRedPortEntry.setIndexNames(
    (0, "S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortBrdIndx"),
    (0, "S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortPortIndx"),
)
if mibBuilder.loadTexts:
    s5EnRedPortEntry.setStatus("current")


class _S5EnRedPortBrdIndx_Type(Integer32):
    """Custom type s5EnRedPortBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5EnRedPortBrdIndx_Type.__name__ = "Integer32"
_S5EnRedPortBrdIndx_Object = MibTableColumn
s5EnRedPortBrdIndx = _S5EnRedPortBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 1, 1, 1),
    _S5EnRedPortBrdIndx_Type()
)
s5EnRedPortBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnRedPortBrdIndx.setStatus("current")


class _S5EnRedPortPortIndx_Type(Integer32):
    """Custom type s5EnRedPortPortIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5EnRedPortPortIndx_Type.__name__ = "Integer32"
_S5EnRedPortPortIndx_Object = MibTableColumn
s5EnRedPortPortIndx = _S5EnRedPortPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 1, 1, 2),
    _S5EnRedPortPortIndx_Type()
)
s5EnRedPortPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnRedPortPortIndx.setStatus("current")


class _S5EnRedPortCapability_Type(Integer32):
    """Custom type s5EnRedPortCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hwAndSwRed", 3),
          ("hwRedOnly", 1),
          ("swRedOnly", 2))
    )


_S5EnRedPortCapability_Type.__name__ = "Integer32"
_S5EnRedPortCapability_Object = MibTableColumn
s5EnRedPortCapability = _S5EnRedPortCapability_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 1, 1, 3),
    _S5EnRedPortCapability_Type()
)
s5EnRedPortCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnRedPortCapability.setStatus("current")


class _S5EnRedPortRedundMode_Type(Integer32):
    """Custom type s5EnRedPortRedundMode based on Integer32"""
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
        *(("hwActive", 2),
          ("hwStandby", 3),
          ("standAlone", 1),
          ("swActive", 4),
          ("swStandby", 5))
    )


_S5EnRedPortRedundMode_Type.__name__ = "Integer32"
_S5EnRedPortRedundMode_Object = MibTableColumn
s5EnRedPortRedundMode = _S5EnRedPortRedundMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 1, 1, 4),
    _S5EnRedPortRedundMode_Type()
)
s5EnRedPortRedundMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnRedPortRedundMode.setStatus("current")


class _S5EnRedPortOperStatus_Type(Integer32):
    """Custom type s5EnRedPortOperStatus based on Integer32"""
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
        *(("localFault", 3),
          ("ok", 2),
          ("other", 1),
          ("remoteFault", 4))
    )


_S5EnRedPortOperStatus_Type.__name__ = "Integer32"
_S5EnRedPortOperStatus_Object = MibTableColumn
s5EnRedPortOperStatus = _S5EnRedPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 1, 1, 5),
    _S5EnRedPortOperStatus_Type()
)
s5EnRedPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnRedPortOperStatus.setStatus("current")


class _S5EnRedPortRemoteOperStatus_Type(Integer32):
    """Custom type s5EnRedPortRemoteOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("snpxFLFBRemFltCpblPortUp", 2),
          ("snpxFLRemFltCpblPortUp", 1),
          ("snpxRemFltCpblPortFault", 5),
          ("tenBaseFBPortFault", 6),
          ("tenBaseFBPortUp", 4),
          ("tenBaseTFLPortUp", 3),
          ("unknown", 7))
    )


_S5EnRedPortRemoteOperStatus_Type.__name__ = "Integer32"
_S5EnRedPortRemoteOperStatus_Object = MibTableColumn
s5EnRedPortRemoteOperStatus = _S5EnRedPortRemoteOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 1, 1, 6),
    _S5EnRedPortRemoteOperStatus_Type()
)
s5EnRedPortRemoteOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnRedPortRemoteOperStatus.setStatus("current")


class _S5EnRedPortRemFltSelectMode_Type(Integer32):
    """Custom type s5EnRedPortRemFltSelectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 2),
          ("synoptics", 1))
    )


_S5EnRedPortRemFltSelectMode_Type.__name__ = "Integer32"
_S5EnRedPortRemFltSelectMode_Object = MibTableColumn
s5EnRedPortRemFltSelectMode = _S5EnRedPortRemFltSelectMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 1, 1, 7),
    _S5EnRedPortRemFltSelectMode_Type()
)
s5EnRedPortRemFltSelectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnRedPortRemFltSelectMode.setStatus("current")


class _S5EnRedPortTxMode_Type(Integer32):
    """Custom type s5EnRedPortTxMode based on Integer32"""
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
        *(("autoCfg", 1),
          ("fb", 3),
          ("fl", 2),
          ("other", 4))
    )


_S5EnRedPortTxMode_Type.__name__ = "Integer32"
_S5EnRedPortTxMode_Object = MibTableColumn
s5EnRedPortTxMode = _S5EnRedPortTxMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 1, 1, 8),
    _S5EnRedPortTxMode_Type()
)
s5EnRedPortTxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnRedPortTxMode.setStatus("current")
_S5EnRedPortFaults_Type = Counter32
_S5EnRedPortFaults_Object = MibTableColumn
s5EnRedPortFaults = _S5EnRedPortFaults_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 1, 1, 9),
    _S5EnRedPortFaults_Type()
)
s5EnRedPortFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnRedPortFaults.setStatus("current")
_S5EnRedPortModeChanges_Type = Counter32
_S5EnRedPortModeChanges_Object = MibTableColumn
s5EnRedPortModeChanges = _S5EnRedPortModeChanges_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 1, 1, 10),
    _S5EnRedPortModeChanges_Type()
)
s5EnRedPortModeChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnRedPortModeChanges.setStatus("current")


class _S5EnRedPortCompanionBrdNum_Type(Integer32):
    """Custom type s5EnRedPortCompanionBrdNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5EnRedPortCompanionBrdNum_Type.__name__ = "Integer32"
_S5EnRedPortCompanionBrdNum_Object = MibTableColumn
s5EnRedPortCompanionBrdNum = _S5EnRedPortCompanionBrdNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 1, 1, 11),
    _S5EnRedPortCompanionBrdNum_Type()
)
s5EnRedPortCompanionBrdNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnRedPortCompanionBrdNum.setStatus("current")


class _S5EnRedPortCompanionPortNum_Type(Integer32):
    """Custom type s5EnRedPortCompanionPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5EnRedPortCompanionPortNum_Type.__name__ = "Integer32"
_S5EnRedPortCompanionPortNum_Object = MibTableColumn
s5EnRedPortCompanionPortNum = _S5EnRedPortCompanionPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 1, 1, 12),
    _S5EnRedPortCompanionPortNum_Type()
)
s5EnRedPortCompanionPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnRedPortCompanionPortNum.setStatus("current")


class _S5EnRedPortSwitchoverStatus_Type(Integer32):
    """Custom type s5EnRedPortSwitchoverStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("timedSwitchover", 2))
    )


_S5EnRedPortSwitchoverStatus_Type.__name__ = "Integer32"
_S5EnRedPortSwitchoverStatus_Object = MibTableColumn
s5EnRedPortSwitchoverStatus = _S5EnRedPortSwitchoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 1, 1, 13),
    _S5EnRedPortSwitchoverStatus_Type()
)
s5EnRedPortSwitchoverStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnRedPortSwitchoverStatus.setStatus("current")


class _S5EnRedPortSwitchoverTime_Type(TimeIntervalSec):
    """Custom type s5EnRedPortSwitchoverTime based on TimeIntervalSec"""
    subtypeSpec = TimeIntervalSec.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5EnRedPortSwitchoverTime_Type.__name__ = "TimeIntervalSec"
_S5EnRedPortSwitchoverTime_Object = MibTableColumn
s5EnRedPortSwitchoverTime = _S5EnRedPortSwitchoverTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 1, 1, 14),
    _S5EnRedPortSwitchoverTime_Type()
)
s5EnRedPortSwitchoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnRedPortSwitchoverTime.setStatus("current")
_S5EnRedLastChg_Type = TimeTicks
_S5EnRedLastChg_Object = MibScalar
s5EnRedLastChg = _S5EnRedLastChg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 2, 2),
    _S5EnRedLastChg_Type()
)
s5EnRedLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnRedLastChg.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S5-ETH-REDUNDANT-LINKS-MIB",
    **{"s5EnRedun": s5EnRedun,
       "s5EnRedPortTable": s5EnRedPortTable,
       "s5EnRedPortEntry": s5EnRedPortEntry,
       "s5EnRedPortBrdIndx": s5EnRedPortBrdIndx,
       "s5EnRedPortPortIndx": s5EnRedPortPortIndx,
       "s5EnRedPortCapability": s5EnRedPortCapability,
       "s5EnRedPortRedundMode": s5EnRedPortRedundMode,
       "s5EnRedPortOperStatus": s5EnRedPortOperStatus,
       "s5EnRedPortRemoteOperStatus": s5EnRedPortRemoteOperStatus,
       "s5EnRedPortRemFltSelectMode": s5EnRedPortRemFltSelectMode,
       "s5EnRedPortTxMode": s5EnRedPortTxMode,
       "s5EnRedPortFaults": s5EnRedPortFaults,
       "s5EnRedPortModeChanges": s5EnRedPortModeChanges,
       "s5EnRedPortCompanionBrdNum": s5EnRedPortCompanionBrdNum,
       "s5EnRedPortCompanionPortNum": s5EnRedPortCompanionPortNum,
       "s5EnRedPortSwitchoverStatus": s5EnRedPortSwitchoverStatus,
       "s5EnRedPortSwitchoverTime": s5EnRedPortSwitchoverTime,
       "s5EnRedLastChg": s5EnRedLastChg,
       "s5EthRedundantLinksMib2": s5EthRedundantLinksMib2}
)
