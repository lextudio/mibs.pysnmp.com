# SNMP MIB module (CXDHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXDHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:18 2024
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

(cxCfgIp,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxCfgIp")

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

_CxCfgDhcpRATable_Object = MibTable
cxCfgDhcpRATable = _CxCfgDhcpRATable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 4)
)
if mibBuilder.loadTexts:
    cxCfgDhcpRATable.setStatus("mandatory")
_CxCfgDhcpRAEntry_Object = MibTableRow
cxCfgDhcpRAEntry = _CxCfgDhcpRAEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 4, 1)
)
cxCfgDhcpRAEntry.setIndexNames(
    (0, "CXDHCP-MIB", "cxCfgDhcpRAIndex"),
)
if mibBuilder.loadTexts:
    cxCfgDhcpRAEntry.setStatus("mandatory")


class _CxCfgDhcpRAIndex_Type(Integer32):
    """Custom type cxCfgDhcpRAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CxCfgDhcpRAIndex_Type.__name__ = "Integer32"
_CxCfgDhcpRAIndex_Object = MibTableColumn
cxCfgDhcpRAIndex = _CxCfgDhcpRAIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 4, 1, 1),
    _CxCfgDhcpRAIndex_Type()
)
cxCfgDhcpRAIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgDhcpRAIndex.setStatus("mandatory")
_CxCfgDhcpRASrvAddr_Type = IpAddress
_CxCfgDhcpRASrvAddr_Object = MibTableColumn
cxCfgDhcpRASrvAddr = _CxCfgDhcpRASrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 4, 1, 2),
    _CxCfgDhcpRASrvAddr_Type()
)
cxCfgDhcpRASrvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgDhcpRASrvAddr.setStatus("mandatory")


class _CxCfgDhcpRARowStatus_Type(Integer32):
    """Custom type cxCfgDhcpRARowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxCfgDhcpRARowStatus_Type.__name__ = "Integer32"
_CxCfgDhcpRARowStatus_Object = MibTableColumn
cxCfgDhcpRARowStatus = _CxCfgDhcpRARowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 4, 1, 10),
    _CxCfgDhcpRARowStatus_Type()
)
cxCfgDhcpRARowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgDhcpRARowStatus.setStatus("mandatory")
_CxCfgDhcpRAStatTx_Type = Counter32
_CxCfgDhcpRAStatTx_Object = MibTableColumn
cxCfgDhcpRAStatTx = _CxCfgDhcpRAStatTx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 4, 1, 20),
    _CxCfgDhcpRAStatTx_Type()
)
cxCfgDhcpRAStatTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgDhcpRAStatTx.setStatus("mandatory")
_CxCfgDhcpRAStatRx_Type = Counter32
_CxCfgDhcpRAStatRx_Object = MibTableColumn
cxCfgDhcpRAStatRx = _CxCfgDhcpRAStatRx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 4, 1, 21),
    _CxCfgDhcpRAStatRx_Type()
)
cxCfgDhcpRAStatRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgDhcpRAStatRx.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXDHCP-MIB",
    **{"cxCfgDhcpRATable": cxCfgDhcpRATable,
       "cxCfgDhcpRAEntry": cxCfgDhcpRAEntry,
       "cxCfgDhcpRAIndex": cxCfgDhcpRAIndex,
       "cxCfgDhcpRASrvAddr": cxCfgDhcpRASrvAddr,
       "cxCfgDhcpRARowStatus": cxCfgDhcpRARowStatus,
       "cxCfgDhcpRAStatTx": cxCfgDhcpRAStatTx,
       "cxCfgDhcpRAStatRx": cxCfgDhcpRAStatRx}
)
