# SNMP MIB module (ChrComIfifTable-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ChrComIfifTable-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:49 2024
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

(AdminStatus,
 OperStatus) = mibBuilder.importSymbols(
    "ChrTyp-MIB",
    "AdminStatus",
    "OperStatus")

(chrComIf,) = mibBuilder.importSymbols(
    "Chromatis-MIB",
    "chrComIf")

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

_ChrComIfifTableTable_Object = MibTable
chrComIfifTableTable = _ChrComIfifTableTable_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 10)
)
if mibBuilder.loadTexts:
    chrComIfifTableTable.setStatus("current")
_ChrComIfifTableEntry_Object = MibTableRow
chrComIfifTableEntry = _ChrComIfifTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 10, 1)
)
chrComIfifTableEntry.setIndexNames(
    (0, "ChrComIfifTable-MIB", "chrComIfifIndex"),
)
if mibBuilder.loadTexts:
    chrComIfifTableEntry.setStatus("current")


class _ChrComIfifIndex_Type(Unsigned32):
    """Custom type chrComIfifIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComIfifIndex_Type.__name__ = "Unsigned32"
_ChrComIfifIndex_Object = MibTableColumn
chrComIfifIndex = _ChrComIfifIndex_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 10, 1, 1),
    _ChrComIfifIndex_Type()
)
chrComIfifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComIfifIndex.setStatus("current")


class _ChrComIfifName_Type(DisplayString):
    """Custom type chrComIfifName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChrComIfifName_Type.__name__ = "DisplayString"
_ChrComIfifName_Object = MibTableColumn
chrComIfifName = _ChrComIfifName_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 10, 1, 2),
    _ChrComIfifName_Type()
)
chrComIfifName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComIfifName.setStatus("current")
_ChrComIfifAdminStatus_Type = AdminStatus
_ChrComIfifAdminStatus_Object = MibTableColumn
chrComIfifAdminStatus = _ChrComIfifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 10, 1, 3),
    _ChrComIfifAdminStatus_Type()
)
chrComIfifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComIfifAdminStatus.setStatus("current")
_ChrComIfifOperStatus_Type = OperStatus
_ChrComIfifOperStatus_Object = MibTableColumn
chrComIfifOperStatus = _ChrComIfifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 10, 1, 4),
    _ChrComIfifOperStatus_Type()
)
chrComIfifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComIfifOperStatus.setStatus("current")


class _ChrComIfvirtualIfIndex_Type(Unsigned32):
    """Custom type chrComIfvirtualIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComIfvirtualIfIndex_Type.__name__ = "Unsigned32"
_ChrComIfvirtualIfIndex_Object = MibTableColumn
chrComIfvirtualIfIndex = _ChrComIfvirtualIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 10, 1, 5),
    _ChrComIfvirtualIfIndex_Type()
)
chrComIfvirtualIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComIfvirtualIfIndex.setStatus("current")


class _ChrComIfreal1IfIndex_Type(Unsigned32):
    """Custom type chrComIfreal1IfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComIfreal1IfIndex_Type.__name__ = "Unsigned32"
_ChrComIfreal1IfIndex_Object = MibTableColumn
chrComIfreal1IfIndex = _ChrComIfreal1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 10, 1, 6),
    _ChrComIfreal1IfIndex_Type()
)
chrComIfreal1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComIfreal1IfIndex.setStatus("current")


class _ChrComIfreal2IfIndex_Type(Unsigned32):
    """Custom type chrComIfreal2IfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComIfreal2IfIndex_Type.__name__ = "Unsigned32"
_ChrComIfreal2IfIndex_Object = MibTableColumn
chrComIfreal2IfIndex = _ChrComIfreal2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 10, 1, 7),
    _ChrComIfreal2IfIndex_Type()
)
chrComIfreal2IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComIfreal2IfIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ChrComIfifTable-MIB",
    **{"chrComIfifTableTable": chrComIfifTableTable,
       "chrComIfifTableEntry": chrComIfifTableEntry,
       "chrComIfifIndex": chrComIfifIndex,
       "chrComIfifName": chrComIfifName,
       "chrComIfifAdminStatus": chrComIfifAdminStatus,
       "chrComIfifOperStatus": chrComIfifOperStatus,
       "chrComIfvirtualIfIndex": chrComIfvirtualIfIndex,
       "chrComIfreal1IfIndex": chrComIfreal1IfIndex,
       "chrComIfreal2IfIndex": chrComIfreal2IfIndex}
)
