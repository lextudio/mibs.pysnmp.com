# SNMP MIB module (CENTILLION-SOURCE-ROUTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-SOURCE-ROUTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:14 2024
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

(cndot1dSr,) = mibBuilder.importSymbols(
    "CENTILLION-BRIDGE-MIB",
    "cndot1dSr")

(EnableIndicator,) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "EnableIndicator")

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

_Cndot1dSrPortTable_Object = MibTable
cndot1dSrPortTable = _Cndot1dSrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 3, 1)
)
if mibBuilder.loadTexts:
    cndot1dSrPortTable.setStatus("mandatory")
_Cndot1dSrPortEntry_Object = MibTableRow
cndot1dSrPortEntry = _Cndot1dSrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 3, 1, 1)
)
cndot1dSrPortEntry.setIndexNames(
    (0, "CENTILLION-SOURCE-ROUTING-MIB", "cndot1dSrPort"),
)
if mibBuilder.loadTexts:
    cndot1dSrPortEntry.setStatus("mandatory")


class _Cndot1dSrPort_Type(Integer32):
    """Custom type cndot1dSrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cndot1dSrPort_Type.__name__ = "Integer32"
_Cndot1dSrPort_Object = MibTableColumn
cndot1dSrPort = _Cndot1dSrPort_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 3, 1, 1, 1),
    _Cndot1dSrPort_Type()
)
cndot1dSrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dSrPort.setStatus("mandatory")
_Cndot1dSrPortAREHopCount_Type = Integer32
_Cndot1dSrPortAREHopCount_Object = MibTableColumn
cndot1dSrPortAREHopCount = _Cndot1dSrPortAREHopCount_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 3, 1, 1, 2),
    _Cndot1dSrPortAREHopCount_Type()
)
cndot1dSrPortAREHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cndot1dSrPortAREHopCount.setStatus("mandatory")
_Cndot1dSrPortSTEHopCount_Type = Integer32
_Cndot1dSrPortSTEHopCount_Object = MibTableColumn
cndot1dSrPortSTEHopCount = _Cndot1dSrPortSTEHopCount_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 3, 1, 1, 3),
    _Cndot1dSrPortSTEHopCount_Type()
)
cndot1dSrPortSTEHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cndot1dSrPortSTEHopCount.setStatus("mandatory")
_Cndot1dSrExplorerProxy_Type = EnableIndicator
_Cndot1dSrExplorerProxy_Object = MibScalar
cndot1dSrExplorerProxy = _Cndot1dSrExplorerProxy_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 3, 3),
    _Cndot1dSrExplorerProxy_Type()
)
cndot1dSrExplorerProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cndot1dSrExplorerProxy.setStatus("mandatory")
_Cndot1dSrBridgeNum_Type = Integer32
_Cndot1dSrBridgeNum_Object = MibScalar
cndot1dSrBridgeNum = _Cndot1dSrBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 3, 4),
    _Cndot1dSrBridgeNum_Type()
)
cndot1dSrBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cndot1dSrBridgeNum.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-SOURCE-ROUTING-MIB",
    **{"cndot1dSrPortTable": cndot1dSrPortTable,
       "cndot1dSrPortEntry": cndot1dSrPortEntry,
       "cndot1dSrPort": cndot1dSrPort,
       "cndot1dSrPortAREHopCount": cndot1dSrPortAREHopCount,
       "cndot1dSrPortSTEHopCount": cndot1dSrPortSTEHopCount,
       "cndot1dSrExplorerProxy": cndot1dSrExplorerProxy,
       "cndot1dSrBridgeNum": cndot1dSrBridgeNum}
)
