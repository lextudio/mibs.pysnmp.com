# SNMP MIB module (AIHUBPORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AIHUBPORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:09 2024
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

(PositiveInteger,) = mibBuilder.importSymbols(
    "AISYSTEM-MIB",
    "PositiveInteger")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

aiHubport = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 27)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSystemOID_ObjectIdentity = ObjectIdentity
aiSystemOID = _AiSystemOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2)
)
_AiHubCnf_ObjectIdentity = ObjectIdentity
aiHubCnf = _AiHubCnf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 27, 1)
)
_HubPortCnfTable_Object = MibTable
hubPortCnfTable = _HubPortCnfTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 27, 1, 1)
)
if mibBuilder.loadTexts:
    hubPortCnfTable.setStatus("current")
_HubPortCnfEntry_Object = MibTableRow
hubPortCnfEntry = _HubPortCnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 27, 1, 1, 1)
)
hubPortCnfEntry.setIndexNames(
    (0, "AIHUBPORT-MIB", "hubPortIndex"),
)
if mibBuilder.loadTexts:
    hubPortCnfEntry.setStatus("current")


class _HubPortIndex_Type(Integer32):
    """Custom type hubPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HubPortIndex_Type.__name__ = "Integer32"
_HubPortIndex_Object = MibTableColumn
hubPortIndex = _HubPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 27, 1, 1, 1, 1),
    _HubPortIndex_Type()
)
hubPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubPortIndex.setStatus("current")


class _HubPortIfIndex_Type(Integer32):
    """Custom type hubPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HubPortIfIndex_Type.__name__ = "Integer32"
_HubPortIfIndex_Object = MibTableColumn
hubPortIfIndex = _HubPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 27, 1, 1, 1, 2),
    _HubPortIfIndex_Type()
)
hubPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubPortIfIndex.setStatus("current")


class _HubPortSpeedCtrl_Type(Integer32):
    """Custom type hubPortSpeedCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("t10", 1),
          ("tx100", 3))
    )


_HubPortSpeedCtrl_Type.__name__ = "Integer32"
_HubPortSpeedCtrl_Object = MibTableColumn
hubPortSpeedCtrl = _HubPortSpeedCtrl_Object(
    (1, 3, 6, 1, 4, 1, 539, 27, 1, 1, 1, 3),
    _HubPortSpeedCtrl_Type()
)
hubPortSpeedCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubPortSpeedCtrl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIHUBPORT-MIB",
    **{"aii": aii,
       "aiSystemOID": aiSystemOID,
       "aiHubport": aiHubport,
       "aiHubCnf": aiHubCnf,
       "hubPortCnfTable": hubPortCnfTable,
       "hubPortCnfEntry": hubPortCnfEntry,
       "hubPortIndex": hubPortIndex,
       "hubPortIfIndex": hubPortIfIndex,
       "hubPortSpeedCtrl": hubPortSpeedCtrl}
)
