# SNMP MIB module (ASCEND-MIBSTACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSTACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:16 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibstackingProfile_ObjectIdentity = ObjectIdentity
mibstackingProfile = _MibstackingProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 122)
)
_MibstackingProfileTable_Object = MibTable
mibstackingProfileTable = _MibstackingProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 122, 1)
)
if mibBuilder.loadTexts:
    mibstackingProfileTable.setStatus("mandatory")
_MibstackingProfileEntry_Object = MibTableRow
mibstackingProfileEntry = _MibstackingProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1)
)
mibstackingProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSTACK-MIB", "stackingProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibstackingProfileEntry.setStatus("mandatory")
_StackingProfile_Index_o_Type = Integer32
_StackingProfile_Index_o_Object = MibScalar
stackingProfile_Index_o = _StackingProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1, 1),
    _StackingProfile_Index_o_Type()
)
stackingProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackingProfile_Index_o.setStatus("mandatory")


class _StackingProfile_Enabled_Type(Integer32):
    """Custom type stackingProfile_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_StackingProfile_Enabled_Type.__name__ = "Integer32"
_StackingProfile_Enabled_Object = MibScalar
stackingProfile_Enabled = _StackingProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1, 2),
    _StackingProfile_Enabled_Type()
)
stackingProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackingProfile_Enabled.setStatus("mandatory")
_StackingProfile_Name_Type = DisplayString
_StackingProfile_Name_Object = MibScalar
stackingProfile_Name = _StackingProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1, 3),
    _StackingProfile_Name_Type()
)
stackingProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackingProfile_Name.setStatus("mandatory")
_StackingProfile_UdpPort_Type = Integer32
_StackingProfile_UdpPort_Object = MibScalar
stackingProfile_UdpPort = _StackingProfile_UdpPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1, 4),
    _StackingProfile_UdpPort_Type()
)
stackingProfile_UdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackingProfile_UdpPort.setStatus("mandatory")
_StackingProfile_MulticastAddress_Type = IpAddress
_StackingProfile_MulticastAddress_Object = MibScalar
stackingProfile_MulticastAddress = _StackingProfile_MulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1, 5),
    _StackingProfile_MulticastAddress_Type()
)
stackingProfile_MulticastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackingProfile_MulticastAddress.setStatus("mandatory")
_StackingProfile_MulticastInterfaceIpAddress_Type = IpAddress
_StackingProfile_MulticastInterfaceIpAddress_Object = MibScalar
stackingProfile_MulticastInterfaceIpAddress = _StackingProfile_MulticastInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1, 6),
    _StackingProfile_MulticastInterfaceIpAddress_Type()
)
stackingProfile_MulticastInterfaceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackingProfile_MulticastInterfaceIpAddress.setStatus("mandatory")
_StackingProfile_DataIpAddress_Type = IpAddress
_StackingProfile_DataIpAddress_Object = MibScalar
stackingProfile_DataIpAddress = _StackingProfile_DataIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1, 7),
    _StackingProfile_DataIpAddress_Type()
)
stackingProfile_DataIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackingProfile_DataIpAddress.setStatus("mandatory")


class _StackingProfile_Action_o_Type(Integer32):
    """Custom type stackingProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_StackingProfile_Action_o_Type.__name__ = "Integer32"
_StackingProfile_Action_o_Object = MibScalar
stackingProfile_Action_o = _StackingProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1, 8),
    _StackingProfile_Action_o_Type()
)
stackingProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackingProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSTACK-MIB",
    **{"DisplayString": DisplayString,
       "mibstackingProfile": mibstackingProfile,
       "mibstackingProfileTable": mibstackingProfileTable,
       "mibstackingProfileEntry": mibstackingProfileEntry,
       "stackingProfile-Index-o": stackingProfile_Index_o,
       "stackingProfile-Enabled": stackingProfile_Enabled,
       "stackingProfile-Name": stackingProfile_Name,
       "stackingProfile-UdpPort": stackingProfile_UdpPort,
       "stackingProfile-MulticastAddress": stackingProfile_MulticastAddress,
       "stackingProfile-MulticastInterfaceIpAddress": stackingProfile_MulticastInterfaceIpAddress,
       "stackingProfile-DataIpAddress": stackingProfile_DataIpAddress,
       "stackingProfile-Action-o": stackingProfile_Action_o}
)
