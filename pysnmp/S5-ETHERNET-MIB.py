# SNMP MIB module (S5-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/S5-ETHERNET-MIB
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

(s5Eth,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "s5Eth")

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

s5EthernetMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 0)
)
s5EthernetMib.setRevisions(
        ("2004-07-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S5EnCfg_ObjectIdentity = ObjectIdentity
s5EnCfg = _S5EnCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1)
)
_S5EnStat_ObjectIdentity = ObjectIdentity
s5EnStat = _S5EnStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2)
)
_S5EnMisc_ObjectIdentity = ObjectIdentity
s5EnMisc = _S5EnMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 3)
)
_S5EnPIntconTable_Object = MibTable
s5EnPIntconTable = _S5EnPIntconTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 3, 1)
)
if mibBuilder.loadTexts:
    s5EnPIntconTable.setStatus("current")
_S5EnPIntconEntry_Object = MibTableRow
s5EnPIntconEntry = _S5EnPIntconEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 3, 1, 1)
)
s5EnPIntconEntry.setIndexNames(
    (0, "S5-ETHERNET-MIB", "s5EnPIntconIfIndx"),
    (0, "S5-ETHERNET-MIB", "s5EnPIntconBrdIndx"),
    (0, "S5-ETHERNET-MIB", "s5EnPIntconPortIndx"),
)
if mibBuilder.loadTexts:
    s5EnPIntconEntry.setStatus("current")


class _S5EnPIntconIfIndx_Type(Integer32):
    """Custom type s5EnPIntconIfIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_S5EnPIntconIfIndx_Type.__name__ = "Integer32"
_S5EnPIntconIfIndx_Object = MibTableColumn
s5EnPIntconIfIndx = _S5EnPIntconIfIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 3, 1, 1, 1),
    _S5EnPIntconIfIndx_Type()
)
s5EnPIntconIfIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPIntconIfIndx.setStatus("current")


class _S5EnPIntconBrdIndx_Type(Integer32):
    """Custom type s5EnPIntconBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5EnPIntconBrdIndx_Type.__name__ = "Integer32"
_S5EnPIntconBrdIndx_Object = MibTableColumn
s5EnPIntconBrdIndx = _S5EnPIntconBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 3, 1, 1, 2),
    _S5EnPIntconBrdIndx_Type()
)
s5EnPIntconBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPIntconBrdIndx.setStatus("current")


class _S5EnPIntconPortIndx_Type(Integer32):
    """Custom type s5EnPIntconPortIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5EnPIntconPortIndx_Type.__name__ = "Integer32"
_S5EnPIntconPortIndx_Object = MibTableColumn
s5EnPIntconPortIndx = _S5EnPIntconPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 3, 1, 1, 3),
    _S5EnPIntconPortIndx_Type()
)
s5EnPIntconPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPIntconPortIndx.setStatus("current")


class _S5EnPIntconIntconStatus_Type(Integer32):
    """Custom type s5EnPIntconIntconStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interconnect", 2),
          ("other", 1))
    )


_S5EnPIntconIntconStatus_Type.__name__ = "Integer32"
_S5EnPIntconIntconStatus_Object = MibTableColumn
s5EnPIntconIntconStatus = _S5EnPIntconIntconStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 3, 1, 1, 4),
    _S5EnPIntconIntconStatus_Type()
)
s5EnPIntconIntconStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPIntconIntconStatus.setStatus("current")


class _S5EnPIntconAddrCollect_Type(Integer32):
    """Custom type s5EnPIntconAddrCollect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysCollect", 3),
          ("default", 1),
          ("neverCollect", 2))
    )


_S5EnPIntconAddrCollect_Type.__name__ = "Integer32"
_S5EnPIntconAddrCollect_Object = MibTableColumn
s5EnPIntconAddrCollect = _S5EnPIntconAddrCollect_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 3, 1, 1, 5),
    _S5EnPIntconAddrCollect_Type()
)
s5EnPIntconAddrCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnPIntconAddrCollect.setStatus("current")


class _S5EnNodeInactInterval_Type(TimeIntervalSec):
    """Custom type s5EnNodeInactInterval based on TimeIntervalSec"""
    defaultValue = 5

    subtypeSpec = TimeIntervalSec.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_S5EnNodeInactInterval_Type.__name__ = "TimeIntervalSec"
_S5EnNodeInactInterval_Object = MibScalar
s5EnNodeInactInterval = _S5EnNodeInactInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 3, 2),
    _S5EnNodeInactInterval_Type()
)
s5EnNodeInactInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnNodeInactInterval.setStatus("current")


class _S5EnNodeAgeInterval_Type(TimeIntervalSec):
    """Custom type s5EnNodeAgeInterval based on TimeIntervalSec"""
    defaultValue = 300

    subtypeSpec = TimeIntervalSec.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_S5EnNodeAgeInterval_Type.__name__ = "TimeIntervalSec"
_S5EnNodeAgeInterval_Object = MibScalar
s5EnNodeAgeInterval = _S5EnNodeAgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 3, 3),
    _S5EnNodeAgeInterval_Type()
)
s5EnNodeAgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnNodeAgeInterval.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S5-ETHERNET-MIB",
    **{"s5EthernetMib": s5EthernetMib,
       "s5EnCfg": s5EnCfg,
       "s5EnStat": s5EnStat,
       "s5EnMisc": s5EnMisc,
       "s5EnPIntconTable": s5EnPIntconTable,
       "s5EnPIntconEntry": s5EnPIntconEntry,
       "s5EnPIntconIfIndx": s5EnPIntconIfIndx,
       "s5EnPIntconBrdIndx": s5EnPIntconBrdIndx,
       "s5EnPIntconPortIndx": s5EnPIntconPortIndx,
       "s5EnPIntconIntconStatus": s5EnPIntconIntconStatus,
       "s5EnPIntconAddrCollect": s5EnPIntconAddrCollect,
       "s5EnNodeInactInterval": s5EnNodeInactInterval,
       "s5EnNodeAgeInterval": s5EnNodeAgeInterval}
)
