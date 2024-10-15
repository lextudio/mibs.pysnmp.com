# SNMP MIB module (UMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:14 2024
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


# Types definitions



class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )





class Uint8(Integer32):
    """Custom type Uint8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class Sint8(Integer32):
    """Custom type Sint8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )





class Uint16(Integer32):
    """Custom type Uint16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class Sint16(Integer32):
    """Custom type Sint16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32766),
    )





class Uint32(Integer32):
    """Custom type Uint32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )





class Sint32(Integer32):
    """Custom type Sint32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483646),
    )





class Uint64(Integer32):
    """Custom type Uint64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )





class Sint64(Integer32):
    """Custom type Sint64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )





class Real32(Integer32):
    """Custom type Real32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )





class Real64(Integer32):
    """Custom type Real64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )





class String(OctetString):
    """Custom type String based on OctetString"""




class Datetime(OctetString):
    """Custom type Datetime based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Umservices_ObjectIdentity = ObjectIdentity
umservices = _Umservices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159)
)
_Cimv2_ObjectIdentity = ObjectIdentity
cimv2 = _Cimv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1)
)
_Ibmpsg_ObjectIdentity = ObjectIdentity
ibmpsg = _Ibmpsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1)
)
_IbmpsgEvent_ObjectIdentity = ObjectIdentity
ibmpsgEvent = _IbmpsgEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 0)
)
_IbmpsgAgent_ObjectIdentity = ObjectIdentity
ibmpsgAgent = _IbmpsgAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 10)
)
_IbmpsgEventSubsystem_ObjectIdentity = ObjectIdentity
ibmpsgEventSubsystem = _IbmpsgEventSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 20)
)
_IbmpsgHealth_ObjectIdentity = ObjectIdentity
ibmpsgHealth = _IbmpsgHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 30)
)
_IbmpsgVitalProductData_ObjectIdentity = ObjectIdentity
ibmpsgVitalProductData = _IbmpsgVitalProductData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 40)
)
_IbmpsgSMART_ObjectIdentity = ObjectIdentity
ibmpsgSMART = _IbmpsgSMART_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 50)
)
_IbmpsgAssetID_ObjectIdentity = ObjectIdentity
ibmpsgAssetID = _IbmpsgAssetID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60)
)
_IbmpsgAlertOnLAN_ObjectIdentity = ObjectIdentity
ibmpsgAlertOnLAN = _IbmpsgAlertOnLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70)
)
_IbmpsgLMSensor_ObjectIdentity = ObjectIdentity
ibmpsgLMSensor = _IbmpsgLMSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80)
)
_IbmpsgITDirector_ObjectIdentity = ObjectIdentity
ibmpsgITDirector = _IbmpsgITDirector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 90)
)
_Win32_ObjectIdentity = ObjectIdentity
win32 = _Win32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2)
)
_Win32Event_ObjectIdentity = ObjectIdentity
win32Event = _Win32Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 0)
)
_Win32WMI_ObjectIdentity = ObjectIdentity
win32WMI = _Win32WMI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10)
)
_Win32SMBIOS_ObjectIdentity = ObjectIdentity
win32SMBIOS = _Win32SMBIOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 20)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UMS-MIB",
    **{"Boolean": Boolean,
       "Uint8": Uint8,
       "Sint8": Sint8,
       "Uint16": Uint16,
       "Sint16": Sint16,
       "Uint32": Uint32,
       "Sint32": Sint32,
       "Uint64": Uint64,
       "Sint64": Sint64,
       "Real32": Real32,
       "Real64": Real64,
       "String": String,
       "Datetime": Datetime,
       "ibm": ibm,
       "ibmProd": ibmProd,
       "umservices": umservices,
       "cimv2": cimv2,
       "ibmpsg": ibmpsg,
       "ibmpsgEvent": ibmpsgEvent,
       "ibmpsgAgent": ibmpsgAgent,
       "ibmpsgEventSubsystem": ibmpsgEventSubsystem,
       "ibmpsgHealth": ibmpsgHealth,
       "ibmpsgVitalProductData": ibmpsgVitalProductData,
       "ibmpsgSMART": ibmpsgSMART,
       "ibmpsgAssetID": ibmpsgAssetID,
       "ibmpsgAlertOnLAN": ibmpsgAlertOnLAN,
       "ibmpsgLMSensor": ibmpsgLMSensor,
       "ibmpsgITDirector": ibmpsgITDirector,
       "win32": win32,
       "win32Event": win32Event,
       "win32WMI": win32WMI,
       "win32SMBIOS": win32SMBIOS}
)
