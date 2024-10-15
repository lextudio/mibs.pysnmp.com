# SNMP MIB module (MITEL-RIP2EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-RIP2EXTENSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:28 2024
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

(rip2IfConfAddress,) = mibBuilder.importSymbols(
    "RIPv2-MIB",
    "rip2IfConfAddress")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mitelRouterRipExtensionGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6)
)
mitelRouterRipExtensionGroup.setRevisions(
        ("2003-03-24 10:36",
         "1999-03-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mitel_ObjectIdentity = ObjectIdentity
mitel = _Mitel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027)
)
_MitelProprietary_ObjectIdentity = ObjectIdentity
mitelProprietary = _MitelProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4)
)
_MitelPropIpNetworking_ObjectIdentity = ObjectIdentity
mitelPropIpNetworking = _MitelPropIpNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8)
)
_MitelIpNetRouter_ObjectIdentity = ObjectIdentity
mitelIpNetRouter = _MitelIpNetRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1)
)
_MitelRipExtGrpIfConfTable_Object = MibTable
mitelRipExtGrpIfConfTable = _MitelRipExtGrpIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6, 1)
)
if mibBuilder.loadTexts:
    mitelRipExtGrpIfConfTable.setStatus("current")
_MitelRipExtGrpIfConfEntry_Object = MibTableRow
mitelRipExtGrpIfConfEntry = _MitelRipExtGrpIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6, 1, 1)
)
mitelRipExtGrpIfConfEntry.setIndexNames(
    (0, "RIPv2-MIB", "rip2IfConfAddress"),
)
if mibBuilder.loadTexts:
    mitelRipExtGrpIfConfEntry.setStatus("current")


class _MitelIfConfTblSendDefaultRoutes_Type(Integer32):
    """Custom type mitelIfConfTblSendDefaultRoutes based on Integer32"""
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


_MitelIfConfTblSendDefaultRoutes_Type.__name__ = "Integer32"
_MitelIfConfTblSendDefaultRoutes_Object = MibTableColumn
mitelIfConfTblSendDefaultRoutes = _MitelIfConfTblSendDefaultRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6, 1, 1, 1),
    _MitelIfConfTblSendDefaultRoutes_Type()
)
mitelIfConfTblSendDefaultRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIfConfTblSendDefaultRoutes.setStatus("current")


class _MitelIfConfTblRipType_Type(Integer32):
    """Custom type mitelIfConfTblRipType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rip", 1),
          ("triggerRip", 2))
    )


_MitelIfConfTblRipType_Type.__name__ = "Integer32"
_MitelIfConfTblRipType_Object = MibTableColumn
mitelIfConfTblRipType = _MitelIfConfTblRipType_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6, 1, 1, 2),
    _MitelIfConfTblRipType_Type()
)
mitelIfConfTblRipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelIfConfTblRipType.setStatus("current")
_MitelIfConfTblRowStatus_Type = RowStatus
_MitelIfConfTblRowStatus_Object = MibTableColumn
mitelIfConfTblRowStatus = _MitelIfConfTblRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6, 1, 1, 3),
    _MitelIfConfTblRowStatus_Type()
)
mitelIfConfTblRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelIfConfTblRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-RIP2EXTENSION-MIB",
    **{"mitel": mitel,
       "mitelProprietary": mitelProprietary,
       "mitelPropIpNetworking": mitelPropIpNetworking,
       "mitelIpNetRouter": mitelIpNetRouter,
       "mitelRouterRipExtensionGroup": mitelRouterRipExtensionGroup,
       "mitelRipExtGrpIfConfTable": mitelRipExtGrpIfConfTable,
       "mitelRipExtGrpIfConfEntry": mitelRipExtGrpIfConfEntry,
       "mitelIfConfTblSendDefaultRoutes": mitelIfConfTblSendDefaultRoutes,
       "mitelIfConfTblRipType": mitelIfConfTblRipType,
       "mitelIfConfTblRowStatus": mitelIfConfTblRowStatus}
)
