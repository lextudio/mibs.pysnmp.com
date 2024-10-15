# SNMP MIB module (NMS-EPON-ONU-REMOTE-SERVER-INFO) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-EPON-ONU-REMOTE-SERVER-INFO
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:49 2024
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

(nmsEPONGroup,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsEPONGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsEponOnuRemoteServer_ObjectIdentity = ObjectIdentity
nmsEponOnuRemoteServer = _NmsEponOnuRemoteServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 28)
)
_NmsEponOnuRemoteServerTable_Object = MibTable
nmsEponOnuRemoteServerTable = _NmsEponOnuRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 28, 1)
)
if mibBuilder.loadTexts:
    nmsEponOnuRemoteServerTable.setStatus("mandatory")
_NmsEponOnuRemoteServerEntry_Object = MibTableRow
nmsEponOnuRemoteServerEntry = _NmsEponOnuRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 28, 1, 1)
)
nmsEponOnuRemoteServerEntry.setIndexNames(
    (0, "NMS-EPON-ONU-REMOTE-SERVER-INFO", "onuRemoteServerIndex"),
)
if mibBuilder.loadTexts:
    nmsEponOnuRemoteServerEntry.setStatus("mandatory")


class _OnuRemoteServerIndex_Type(Integer32):
    """Custom type onuRemoteServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_OnuRemoteServerIndex_Type.__name__ = "Integer32"
_OnuRemoteServerIndex_Object = MibTableColumn
onuRemoteServerIndex = _OnuRemoteServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 28, 1, 1, 1),
    _OnuRemoteServerIndex_Type()
)
onuRemoteServerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuRemoteServerIndex.setStatus("mandatory")
_OnuRemoteServerIpAddr_Type = IpAddress
_OnuRemoteServerIpAddr_Object = MibTableColumn
onuRemoteServerIpAddr = _OnuRemoteServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 28, 1, 1, 2),
    _OnuRemoteServerIpAddr_Type()
)
onuRemoteServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuRemoteServerIpAddr.setStatus("mandatory")
_OnuRemoteServerRowStatus_Type = RowStatus
_OnuRemoteServerRowStatus_Object = MibTableColumn
onuRemoteServerRowStatus = _OnuRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 28, 1, 1, 3),
    _OnuRemoteServerRowStatus_Type()
)
onuRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuRemoteServerRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-EPON-ONU-REMOTE-SERVER-INFO",
    **{"nmsEponOnuRemoteServer": nmsEponOnuRemoteServer,
       "nmsEponOnuRemoteServerTable": nmsEponOnuRemoteServerTable,
       "nmsEponOnuRemoteServerEntry": nmsEponOnuRemoteServerEntry,
       "onuRemoteServerIndex": onuRemoteServerIndex,
       "onuRemoteServerIpAddr": onuRemoteServerIpAddr,
       "onuRemoteServerRowStatus": onuRemoteServerRowStatus}
)
