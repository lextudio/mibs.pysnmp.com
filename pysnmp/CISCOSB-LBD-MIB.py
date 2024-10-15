# SNMP MIB module (CISCOSB-LBD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-LBD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:30 2024
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlLbd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127)
)
rlLbd.setRevisions(
        ("2007-11-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlLbdEnable_Type = TruthValue
_RlLbdEnable_Object = MibScalar
rlLbdEnable = _RlLbdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 1),
    _RlLbdEnable_Type()
)
rlLbdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLbdEnable.setStatus("current")


class _RlLbdDetectionInterval_Type(Integer32):
    """Custom type rlLbdDetectionInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 60),
    )


_RlLbdDetectionInterval_Type.__name__ = "Integer32"
_RlLbdDetectionInterval_Object = MibScalar
rlLbdDetectionInterval = _RlLbdDetectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 2),
    _RlLbdDetectionInterval_Type()
)
rlLbdDetectionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLbdDetectionInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlLbdDetectionInterval.setUnits("seconds")


class _RlLbdMode_Type(Integer32):
    """Custom type rlLbdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("base-mac-addr", 2),
          ("source-mac-addr", 1))
    )


_RlLbdMode_Type.__name__ = "Integer32"
_RlLbdMode_Object = MibScalar
rlLbdMode = _RlLbdMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 3),
    _RlLbdMode_Type()
)
rlLbdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLbdMode.setStatus("current")
_RlLbdIfAdminStatus_Type = PortList
_RlLbdIfAdminStatus_Object = MibScalar
rlLbdIfAdminStatus = _RlLbdIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 4),
    _RlLbdIfAdminStatus_Type()
)
rlLbdIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLbdIfAdminStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-LBD-MIB",
    **{"rlLbd": rlLbd,
       "rlLbdEnable": rlLbdEnable,
       "rlLbdDetectionInterval": rlLbdDetectionInterval,
       "rlLbdMode": rlLbdMode,
       "rlLbdIfAdminStatus": rlLbdIfAdminStatus}
)
