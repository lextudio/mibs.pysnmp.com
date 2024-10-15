# SNMP MIB module (CAIOPSMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAIOPSMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:19 2024
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

(caiSysMgt,) = mibBuilder.importSymbols(
    "CAIMIB",
    "caiSysMgt")

(cai,) = mibBuilder.importSymbols(
    "CAISECMIB",
    "cai")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CaiOps_ObjectIdentity = ObjectIdentity
caiOps = _CaiOps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 4)
)


class _CaiOpsLstMsg_Type(DisplayString):
    """Custom type caiOpsLstMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CaiOpsLstMsg_Type.__name__ = "DisplayString"
_CaiOpsLstMsg_Object = MibScalar
caiOpsLstMsg = _CaiOpsLstMsg_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 4, 2),
    _CaiOpsLstMsg_Type()
)
caiOpsLstMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caiOpsLstMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

caiOpsT1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 2000)
)
caiOpsT1.setObjects(
    ("CAIOPSMIB", "caiOpsLstMsg")
)
if mibBuilder.loadTexts:
    caiOpsT1.setStatus(
        ""
    )

caiOpsT2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 2001)
)
caiOpsT2.setObjects(
    ("CAIOPSMIB", "caiOpsLstMsg")
)
if mibBuilder.loadTexts:
    caiOpsT2.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAIOPSMIB",
    **{"caiOpsT1": caiOpsT1,
       "caiOpsT2": caiOpsT2,
       "caiOps": caiOps,
       "caiOpsLstMsg": caiOpsLstMsg}
)
