# SNMP MIB module (PDN-SCMEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-SCMEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:05 2024
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

(pdnAtm,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdnAtm")

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

_DevAtmScm_ObjectIdentity = ObjectIdentity
devAtmScm = _DevAtmScm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4)
)
_DevAtmMaxVciVpiConfig_ObjectIdentity = ObjectIdentity
devAtmMaxVciVpiConfig = _DevAtmMaxVciVpiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 1)
)
_DevAtmMaxVciVpiConfigTable_Object = MibTable
devAtmMaxVciVpiConfigTable = _DevAtmMaxVciVpiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 1, 1)
)
if mibBuilder.loadTexts:
    devAtmMaxVciVpiConfigTable.setStatus("mandatory")
_DevAtmMaxVciVpiConfigEntry_Object = MibTableRow
devAtmMaxVciVpiConfigEntry = _DevAtmMaxVciVpiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 1, 1, 1)
)
devAtmMaxVciVpiConfigEntry.setIndexNames(
    (0, "PDN-SCMEXT-MIB", "devAtmMaxIfIndex"),
    (0, "PDN-SCMEXT-MIB", "devAtmMaxVpi"),
)
if mibBuilder.loadTexts:
    devAtmMaxVciVpiConfigEntry.setStatus("mandatory")
_DevAtmMaxIfIndex_Type = Integer32
_DevAtmMaxIfIndex_Object = MibTableColumn
devAtmMaxIfIndex = _DevAtmMaxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 1, 1, 1, 1),
    _DevAtmMaxIfIndex_Type()
)
devAtmMaxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devAtmMaxIfIndex.setStatus("mandatory")
_DevAtmMaxVpi_Type = Integer32
_DevAtmMaxVpi_Object = MibTableColumn
devAtmMaxVpi = _DevAtmMaxVpi_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 1, 1, 1, 2),
    _DevAtmMaxVpi_Type()
)
devAtmMaxVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devAtmMaxVpi.setStatus("mandatory")
_DevAtmMaxVci_Type = Integer32
_DevAtmMaxVci_Object = MibTableColumn
devAtmMaxVci = _DevAtmMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 1, 1, 1, 3),
    _DevAtmMaxVci_Type()
)
devAtmMaxVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devAtmMaxVci.setStatus("mandatory")
_DevAtmMaxVciVpiRowStatus_Type = RowStatus
_DevAtmMaxVciVpiRowStatus_Object = MibTableColumn
devAtmMaxVciVpiRowStatus = _DevAtmMaxVciVpiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 1, 1, 1, 4),
    _DevAtmMaxVciVpiRowStatus_Type()
)
devAtmMaxVciVpiRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devAtmMaxVciVpiRowStatus.setStatus("mandatory")
_DevAtmAutoConfigXcon_ObjectIdentity = ObjectIdentity
devAtmAutoConfigXcon = _DevAtmAutoConfigXcon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2)
)
_DevAtmAutoConfigXconTable_Object = MibTable
devAtmAutoConfigXconTable = _DevAtmAutoConfigXconTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2, 1)
)
if mibBuilder.loadTexts:
    devAtmAutoConfigXconTable.setStatus("mandatory")
_DevAtmAutoConfigXconEntry_Object = MibTableRow
devAtmAutoConfigXconEntry = _DevAtmAutoConfigXconEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2, 1, 1)
)
devAtmAutoConfigXconEntry.setIndexNames(
    (0, "PDN-SCMEXT-MIB", "devAtmAutoConfigXconChannel"),
)
if mibBuilder.loadTexts:
    devAtmAutoConfigXconEntry.setStatus("mandatory")
_DevAtmAutoConfigXconChannel_Type = Integer32
_DevAtmAutoConfigXconChannel_Object = MibTableColumn
devAtmAutoConfigXconChannel = _DevAtmAutoConfigXconChannel_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2, 1, 1, 1),
    _DevAtmAutoConfigXconChannel_Type()
)
devAtmAutoConfigXconChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devAtmAutoConfigXconChannel.setStatus("mandatory")
_DevAtmAutoConfigXconIfIndex_Type = Integer32
_DevAtmAutoConfigXconIfIndex_Object = MibTableColumn
devAtmAutoConfigXconIfIndex = _DevAtmAutoConfigXconIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2, 1, 1, 2),
    _DevAtmAutoConfigXconIfIndex_Type()
)
devAtmAutoConfigXconIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devAtmAutoConfigXconIfIndex.setStatus("mandatory")
_DevAtmAutoConfigXconVpi_Type = Integer32
_DevAtmAutoConfigXconVpi_Object = MibTableColumn
devAtmAutoConfigXconVpi = _DevAtmAutoConfigXconVpi_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2, 1, 1, 3),
    _DevAtmAutoConfigXconVpi_Type()
)
devAtmAutoConfigXconVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devAtmAutoConfigXconVpi.setStatus("mandatory")
_DevAtmAutoConfigXconVci_Type = Integer32
_DevAtmAutoConfigXconVci_Object = MibTableColumn
devAtmAutoConfigXconVci = _DevAtmAutoConfigXconVci_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2, 1, 1, 4),
    _DevAtmAutoConfigXconVci_Type()
)
devAtmAutoConfigXconVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devAtmAutoConfigXconVci.setStatus("mandatory")
_DevAtmAutoConfigXconTraffic_Type = Integer32
_DevAtmAutoConfigXconTraffic_Object = MibTableColumn
devAtmAutoConfigXconTraffic = _DevAtmAutoConfigXconTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2, 1, 1, 5),
    _DevAtmAutoConfigXconTraffic_Type()
)
devAtmAutoConfigXconTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devAtmAutoConfigXconTraffic.setStatus("mandatory")
_DevAtmAutoConfigXconRowStatus_Type = RowStatus
_DevAtmAutoConfigXconRowStatus_Object = MibTableColumn
devAtmAutoConfigXconRowStatus = _DevAtmAutoConfigXconRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2, 1, 1, 6),
    _DevAtmAutoConfigXconRowStatus_Type()
)
devAtmAutoConfigXconRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devAtmAutoConfigXconRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-SCMEXT-MIB",
    **{"devAtmScm": devAtmScm,
       "devAtmMaxVciVpiConfig": devAtmMaxVciVpiConfig,
       "devAtmMaxVciVpiConfigTable": devAtmMaxVciVpiConfigTable,
       "devAtmMaxVciVpiConfigEntry": devAtmMaxVciVpiConfigEntry,
       "devAtmMaxIfIndex": devAtmMaxIfIndex,
       "devAtmMaxVpi": devAtmMaxVpi,
       "devAtmMaxVci": devAtmMaxVci,
       "devAtmMaxVciVpiRowStatus": devAtmMaxVciVpiRowStatus,
       "devAtmAutoConfigXcon": devAtmAutoConfigXcon,
       "devAtmAutoConfigXconTable": devAtmAutoConfigXconTable,
       "devAtmAutoConfigXconEntry": devAtmAutoConfigXconEntry,
       "devAtmAutoConfigXconChannel": devAtmAutoConfigXconChannel,
       "devAtmAutoConfigXconIfIndex": devAtmAutoConfigXconIfIndex,
       "devAtmAutoConfigXconVpi": devAtmAutoConfigXconVpi,
       "devAtmAutoConfigXconVci": devAtmAutoConfigXconVci,
       "devAtmAutoConfigXconTraffic": devAtmAutoConfigXconTraffic,
       "devAtmAutoConfigXconRowStatus": devAtmAutoConfigXconRowStatus}
)
