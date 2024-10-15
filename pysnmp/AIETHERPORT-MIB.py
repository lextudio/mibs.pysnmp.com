# SNMP MIB module (AIETHERPORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AIETHERPORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:08 2024
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

aiEtherport = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiEtherCnf_ObjectIdentity = ObjectIdentity
aiEtherCnf = _AiEtherCnf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 31, 1)
)
_EtherPortCnfTable_Object = MibTable
etherPortCnfTable = _EtherPortCnfTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 31, 1, 1)
)
if mibBuilder.loadTexts:
    etherPortCnfTable.setStatus("current")
_EtherPortCnfEntry_Object = MibTableRow
etherPortCnfEntry = _EtherPortCnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 31, 1, 1, 1)
)
etherPortCnfEntry.setIndexNames(
    (0, "AIETHERPORT-MIB", "etherPortIndex"),
)
if mibBuilder.loadTexts:
    etherPortCnfEntry.setStatus("current")


class _EtherPortIndex_Type(Integer32):
    """Custom type etherPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_EtherPortIndex_Type.__name__ = "Integer32"
_EtherPortIndex_Object = MibTableColumn
etherPortIndex = _EtherPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 31, 1, 1, 1, 1),
    _EtherPortIndex_Type()
)
etherPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortIndex.setStatus("current")


class _EtherPortName_Type(DisplayString):
    """Custom type etherPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_EtherPortName_Type.__name__ = "DisplayString"
_EtherPortName_Object = MibTableColumn
etherPortName = _EtherPortName_Object(
    (1, 3, 6, 1, 4, 1, 539, 31, 1, 1, 1, 2),
    _EtherPortName_Type()
)
etherPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherPortName.setStatus("current")


class _EtherPortAdminStatus_Type(Integer32):
    """Custom type etherPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_EtherPortAdminStatus_Type.__name__ = "Integer32"
_EtherPortAdminStatus_Object = MibTableColumn
etherPortAdminStatus = _EtherPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 31, 1, 1, 1, 3),
    _EtherPortAdminStatus_Type()
)
etherPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPortAdminStatus.setStatus("current")


class _EtherPortSpeedCtrl_Type(Integer32):
    """Custom type etherPortSpeedCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("t10Full", 3),
          ("t10Half", 2),
          ("tx100Full", 5),
          ("tx100Half", 4))
    )


_EtherPortSpeedCtrl_Type.__name__ = "Integer32"
_EtherPortSpeedCtrl_Object = MibTableColumn
etherPortSpeedCtrl = _EtherPortSpeedCtrl_Object(
    (1, 3, 6, 1, 4, 1, 539, 31, 1, 1, 1, 4),
    _EtherPortSpeedCtrl_Type()
)
etherPortSpeedCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherPortSpeedCtrl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIETHERPORT-MIB",
    **{"aii": aii,
       "aiEtherport": aiEtherport,
       "aiEtherCnf": aiEtherCnf,
       "etherPortCnfTable": etherPortCnfTable,
       "etherPortCnfEntry": etherPortCnfEntry,
       "etherPortIndex": etherPortIndex,
       "etherPortName": etherPortName,
       "etherPortAdminStatus": etherPortAdminStatus,
       "etherPortSpeedCtrl": etherPortSpeedCtrl}
)
