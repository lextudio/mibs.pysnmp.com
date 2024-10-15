# SNMP MIB module (Dot1xMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Dot1xMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:35:58 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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

swdot1xMGMTMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 30)
)


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot1xGuestVlan_ObjectIdentity = ObjectIdentity
dot1xGuestVlan = _Dot1xGuestVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 30, 1)
)


class _Dot1xGuestVlanName_Type(DisplayString):
    """Custom type dot1xGuestVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Dot1xGuestVlanName_Type.__name__ = "DisplayString"
_Dot1xGuestVlanName_Object = MibScalar
dot1xGuestVlanName = _Dot1xGuestVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 30, 1, 1),
    _Dot1xGuestVlanName_Type()
)
dot1xGuestVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xGuestVlanName.setStatus("current")
_Dot1xGuestVlanPort_Type = PortList
_Dot1xGuestVlanPort_Object = MibScalar
dot1xGuestVlanPort = _Dot1xGuestVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 30, 1, 2),
    _Dot1xGuestVlanPort_Type()
)
dot1xGuestVlanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xGuestVlanPort.setStatus("current")


class _Dot1xGuestVlanDelState_Type(Integer32):
    """Custom type dot1xGuestVlanDelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_Dot1xGuestVlanDelState_Type.__name__ = "Integer32"
_Dot1xGuestVlanDelState_Object = MibScalar
dot1xGuestVlanDelState = _Dot1xGuestVlanDelState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 30, 1, 3),
    _Dot1xGuestVlanDelState_Type()
)
dot1xGuestVlanDelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xGuestVlanDelState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Dot1xMGMT-MIB",
    **{"PortList": PortList,
       "swdot1xMGMTMIB": swdot1xMGMTMIB,
       "dot1xGuestVlan": dot1xGuestVlan,
       "dot1xGuestVlanName": dot1xGuestVlanName,
       "dot1xGuestVlanPort": dot1xGuestVlanPort,
       "dot1xGuestVlanDelState": dot1xGuestVlanDelState}
)
