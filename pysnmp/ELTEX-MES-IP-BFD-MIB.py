# SNMP MIB module (ELTEX-MES-IP-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-IP-BFD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:45 2024
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesIpBfd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6)
)
eltMesIpBfd.setRevisions(
        ("2014-03-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _EltIpBfdOspfEnable_Type(Integer32):
    """Custom type eltIpBfdOspfEnable based on Integer32"""
    defaultValue = 2

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


_EltIpBfdOspfEnable_Type.__name__ = "Integer32"
_EltIpBfdOspfEnable_Object = MibScalar
eltIpBfdOspfEnable = _EltIpBfdOspfEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 1),
    _EltIpBfdOspfEnable_Type()
)
eltIpBfdOspfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpBfdOspfEnable.setStatus("current")
_EltIpBfdIfTable_Object = MibTable
eltIpBfdIfTable = _EltIpBfdIfTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 2)
)
if mibBuilder.loadTexts:
    eltIpBfdIfTable.setStatus("current")
_EltIpBfdIfEntry_Object = MibTableRow
eltIpBfdIfEntry = _EltIpBfdIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 2, 1)
)
eltIpBfdIfEntry.setIndexNames(
    (0, "ELTEX-MES-IP-BFD-MIB", "eltIpBfdAddr"),
)
if mibBuilder.loadTexts:
    eltIpBfdIfEntry.setStatus("current")
_EltIpBfdAddr_Type = IpAddress
_EltIpBfdAddr_Object = MibTableColumn
eltIpBfdAddr = _EltIpBfdAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 2, 1, 1),
    _EltIpBfdAddr_Type()
)
eltIpBfdAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpBfdAddr.setStatus("current")
_EltIpBfdDesiredMinTxInterval_Type = Unsigned32
_EltIpBfdDesiredMinTxInterval_Object = MibTableColumn
eltIpBfdDesiredMinTxInterval = _EltIpBfdDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 2, 1, 2),
    _EltIpBfdDesiredMinTxInterval_Type()
)
eltIpBfdDesiredMinTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpBfdDesiredMinTxInterval.setStatus("current")
_EltIpBfdReqMinRxInterval_Type = Unsigned32
_EltIpBfdReqMinRxInterval_Object = MibTableColumn
eltIpBfdReqMinRxInterval = _EltIpBfdReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 2, 1, 3),
    _EltIpBfdReqMinRxInterval_Type()
)
eltIpBfdReqMinRxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpBfdReqMinRxInterval.setStatus("current")
_EltIpBfdDetectMult_Type = Unsigned32
_EltIpBfdDetectMult_Object = MibTableColumn
eltIpBfdDetectMult = _EltIpBfdDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 2, 1, 4),
    _EltIpBfdDetectMult_Type()
)
eltIpBfdDetectMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpBfdDetectMult.setStatus("current")
_EltIpBfdOspfDisable_Type = TruthValue
_EltIpBfdOspfDisable_Object = MibTableColumn
eltIpBfdOspfDisable = _EltIpBfdOspfDisable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 2, 1, 5),
    _EltIpBfdOspfDisable_Type()
)
eltIpBfdOspfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpBfdOspfDisable.setStatus("current")
_EltIpBfdRipDisable_Type = TruthValue
_EltIpBfdRipDisable_Object = MibTableColumn
eltIpBfdRipDisable = _EltIpBfdRipDisable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 2, 1, 6),
    _EltIpBfdRipDisable_Type()
)
eltIpBfdRipDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpBfdRipDisable.setStatus("current")
_EltIpBfdRowStatus_Type = RowStatus
_EltIpBfdRowStatus_Object = MibTableColumn
eltIpBfdRowStatus = _EltIpBfdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6, 2, 1, 7),
    _EltIpBfdRowStatus_Type()
)
eltIpBfdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltIpBfdRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-IP-BFD-MIB",
    **{"eltMesIpBfd": eltMesIpBfd,
       "eltIpBfdOspfEnable": eltIpBfdOspfEnable,
       "eltIpBfdIfTable": eltIpBfdIfTable,
       "eltIpBfdIfEntry": eltIpBfdIfEntry,
       "eltIpBfdAddr": eltIpBfdAddr,
       "eltIpBfdDesiredMinTxInterval": eltIpBfdDesiredMinTxInterval,
       "eltIpBfdReqMinRxInterval": eltIpBfdReqMinRxInterval,
       "eltIpBfdDetectMult": eltIpBfdDetectMult,
       "eltIpBfdOspfDisable": eltIpBfdOspfDisable,
       "eltIpBfdRipDisable": eltIpBfdRipDisable,
       "eltIpBfdRowStatus": eltIpBfdRowStatus}
)
