# SNMP MIB module (CXMLPPP-IP-NCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXMLPPP-IP-NCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:41 2024
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

(SapIndex,
 cxMLPPP) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "SapIndex",
    "cxMLPPP")

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

_MlpppIpNsTable_Object = MibTable
mlpppIpNsTable = _MlpppIpNsTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 52)
)
if mibBuilder.loadTexts:
    mlpppIpNsTable.setStatus("mandatory")
_MlpppIpNsEntry_Object = MibTableRow
mlpppIpNsEntry = _MlpppIpNsEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 52, 1)
)
mlpppIpNsEntry.setIndexNames(
    (0, "CXMLPPP-IP-NCP-MIB", "mlpppIpNsLSapNumber"),
    (0, "CXMLPPP-IP-NCP-MIB", "mlpppIpNsNumber"),
)
if mibBuilder.loadTexts:
    mlpppIpNsEntry.setStatus("mandatory")
_MlpppIpNsLSapNumber_Type = SapIndex
_MlpppIpNsLSapNumber_Object = MibTableColumn
mlpppIpNsLSapNumber = _MlpppIpNsLSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 52, 1, 1),
    _MlpppIpNsLSapNumber_Type()
)
mlpppIpNsLSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppIpNsLSapNumber.setStatus("mandatory")
_MlpppIpNsNumber_Type = Integer32
_MlpppIpNsNumber_Object = MibTableColumn
mlpppIpNsNumber = _MlpppIpNsNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 52, 1, 2),
    _MlpppIpNsNumber_Type()
)
mlpppIpNsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppIpNsNumber.setStatus("mandatory")


class _MlpppIpNsLocalToRemoteComp_Type(Integer32):
    """Custom type mlpppIpNsLocalToRemoteComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vj-tcp", 2))
    )


_MlpppIpNsLocalToRemoteComp_Type.__name__ = "Integer32"
_MlpppIpNsLocalToRemoteComp_Object = MibTableColumn
mlpppIpNsLocalToRemoteComp = _MlpppIpNsLocalToRemoteComp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 52, 1, 40),
    _MlpppIpNsLocalToRemoteComp_Type()
)
mlpppIpNsLocalToRemoteComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppIpNsLocalToRemoteComp.setStatus("mandatory")


class _MlpppIpNsRemoteToLocalComp_Type(Integer32):
    """Custom type mlpppIpNsRemoteToLocalComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vj-tcp", 2))
    )


_MlpppIpNsRemoteToLocalComp_Type.__name__ = "Integer32"
_MlpppIpNsRemoteToLocalComp_Object = MibTableColumn
mlpppIpNsRemoteToLocalComp = _MlpppIpNsRemoteToLocalComp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 52, 1, 41),
    _MlpppIpNsRemoteToLocalComp_Type()
)
mlpppIpNsRemoteToLocalComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppIpNsRemoteToLocalComp.setStatus("mandatory")
_MlpppIpNcTable_Object = MibTable
mlpppIpNcTable = _MlpppIpNcTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 53)
)
if mibBuilder.loadTexts:
    mlpppIpNcTable.setStatus("mandatory")
_MlpppIpNcEntry_Object = MibTableRow
mlpppIpNcEntry = _MlpppIpNcEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 53, 1)
)
mlpppIpNcEntry.setIndexNames(
    (0, "CXMLPPP-IP-NCP-MIB", "mlpppIpNcUSapNumber"),
    (0, "CXMLPPP-IP-NCP-MIB", "mlpppIpNcNumber"),
)
if mibBuilder.loadTexts:
    mlpppIpNcEntry.setStatus("mandatory")
_MlpppIpNcUSapNumber_Type = SapIndex
_MlpppIpNcUSapNumber_Object = MibTableColumn
mlpppIpNcUSapNumber = _MlpppIpNcUSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 53, 1, 1),
    _MlpppIpNcUSapNumber_Type()
)
mlpppIpNcUSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppIpNcUSapNumber.setStatus("mandatory")
_MlpppIpNcNumber_Type = Integer32
_MlpppIpNcNumber_Object = MibTableColumn
mlpppIpNcNumber = _MlpppIpNcNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 53, 1, 2),
    _MlpppIpNcNumber_Type()
)
mlpppIpNcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpppIpNcNumber.setStatus("mandatory")


class _MlpppIpNcComp_Type(Integer32):
    """Custom type mlpppIpNcComp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vj-tcp", 2))
    )


_MlpppIpNcComp_Type.__name__ = "Integer32"
_MlpppIpNcComp_Object = MibTableColumn
mlpppIpNcComp = _MlpppIpNcComp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 53, 1, 10),
    _MlpppIpNcComp_Type()
)
mlpppIpNcComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlpppIpNcComp.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXMLPPP-IP-NCP-MIB",
    **{"mlpppIpNsTable": mlpppIpNsTable,
       "mlpppIpNsEntry": mlpppIpNsEntry,
       "mlpppIpNsLSapNumber": mlpppIpNsLSapNumber,
       "mlpppIpNsNumber": mlpppIpNsNumber,
       "mlpppIpNsLocalToRemoteComp": mlpppIpNsLocalToRemoteComp,
       "mlpppIpNsRemoteToLocalComp": mlpppIpNsRemoteToLocalComp,
       "mlpppIpNcTable": mlpppIpNcTable,
       "mlpppIpNcEntry": mlpppIpNcEntry,
       "mlpppIpNcUSapNumber": mlpppIpNcUSapNumber,
       "mlpppIpNcNumber": mlpppIpNcNumber,
       "mlpppIpNcComp": mlpppIpNcComp}
)
